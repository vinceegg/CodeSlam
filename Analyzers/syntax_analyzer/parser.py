from Analyzers.lexical_analyzer.tokens import TokenType, Token
from .errors import create_syntax_error, SyntaxError

class Parser:
    def __init__(self, tokens):
        # Keep all tokens including newlines for accurate line tracking
        self.tokens = tokens
        self.current_token_index = -1
        self.current_token = None
        self.current_line = 1  # Track current line
        self.current_column = 0  # Track current column
        self.advance()

    def error(self, message):
        """Create a syntax error with current token's position"""
        if self.current_token:
            return SyntaxError(message, self.current_line, self.current_column)
        return SyntaxError(message, self.current_line, self.current_column)

    def advance(self):
        """Move to next token and track position"""
        self.current_token_index += 1
        while self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
            
            # Update position tracking
            if self.current_token.type == TokenType.NEWLINE.value:
                self.current_line += 1
                self.current_column = 0
            else:
                self.current_column += len(str(self.current_token.value))
                
            if self.current_token.type not in [TokenType.SPACE.value, TokenType.TAB.value]:
                return self.current_token
                
            self.current_token_index += 1
            
        self.current_token = None
        return None

    def peek(self):
        """Look ahead to next non-whitespace token"""
        index = self.current_token_index + 1
        while index < len(self.tokens):
            if self.tokens[index].type not in [TokenType.SPACE.value, TokenType.TAB.value]:
                return self.tokens[index]
            index += 1
        return None

    def parse(self):
        """Entry point for parsing according to CFG rule 1"""
        try:
            # Parse global declarations
            global_declarations = self.parse_global_declarations()
            if isinstance(global_declarations, SyntaxError):
                return global_declarations

            # Parse function declarations
            function_declarations = self.parse_function_declarations()
            if isinstance(function_declarations, SyntaxError):
                return function_declarations

            # Parse function definitions
            function_definitions = self.parse_function_definitions()
            if isinstance(function_definitions, SyntaxError):
                return function_definitions

            # Parse Team block
            team_block = self.parse_team_block()
            if isinstance(team_block, SyntaxError):
                return team_block

            return {
                'type': 'program',
                'global_declarations': global_declarations,
                'function_declarations': function_declarations,
                'function_definitions': function_definitions,
                'team_block': team_block,
                'line': 1,
                'column': 0
            }
        except Exception as e:
            return self.error(str(e))

    def parse_global_declarations(self):
        """Parse global variable declarations"""
        declarations = []
        
        while self.current_token and self.is_data_type(self.current_token.type):
            if self.peek() and self.peek().type == TokenType.LEFT_PAREN.value:
                break  # Stop if we hit a function declaration
                
            decl = self.parse_variable_declaration(is_global=True)
            if isinstance(decl, SyntaxError):
                return decl
            declarations.append(decl)
            
        return declarations

    def parse_function_declarations(self):
        """Parse function declarations"""
        declarations = []
        
        while self.current_token and self.is_data_type(self.current_token.type):
            if not (self.peek() and self.peek().type == TokenType.LEFT_PAREN.value):
                break
                
            decl = self.parse_function_declaration()
            if isinstance(decl, SyntaxError):
                return decl
            declarations.append(decl)
            
        return declarations

    def parse_function_declaration(self):
        """Parse a single function declaration"""
        start_line = self.current_line
        start_column = self.current_column
        
        return_type = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected function name")
        function_name = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after function name")
        self.advance()

        parameters = self.parse_parameters()
        if isinstance(parameters, SyntaxError):
            return parameters

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after parameters")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after function declaration")
        self.advance()

        return {
            'type': 'function_declaration',
            'return_type': return_type,
            'name': function_name,
            'parameters': parameters,
            'line': start_line,
            'column': start_column
        }

    def parse_function_definitions(self):
        """Parse function definitions"""
        definitions = []
        
        while self.current_token and self.is_data_type(self.current_token.type):
            if not (self.peek() and self.peek().type == TokenType.LEFT_PAREN.value):
                break
                
            defn = self.parse_function_definition()
            if isinstance(defn, SyntaxError):
                return defn
            definitions.append(defn)
            
        return definitions

    def parse_function_definition(self):
        """Parse a single function definition"""
        start_line = self.current_line
        start_column = self.current_column
        
        return_type = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected function name")
        function_name = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after function name")
        self.advance()

        parameters = self.parse_parameters()
        if isinstance(parameters, SyntaxError):
            return parameters

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after parameters")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after function header")
        self.advance()

        body = self.parse_function_body()
        if isinstance(body, SyntaxError):
            return body

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' at end of function")
        self.advance()

        return {
            'type': 'function_definition',
            'return_type': return_type,
            'name': function_name,
            'parameters': parameters,
            'body': body,
            'line': start_line,
            'column': start_column
        }

    def parse_parameters(self):
        """Parse function parameters"""
        parameters = []
        
        while self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
            if not self.is_data_type(self.current_token.type):
                return self.error("Expected parameter type")
                
            param_type = self.current_token.value
            self.advance()

            if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
                return self.error("Expected parameter name")
            param_name = self.current_token.value
            self.advance()

            parameters.append({
                'type': param_type,
                'name': param_name
            })

            if self.current_token and self.current_token.type == TokenType.COMMA.value:
                self.advance()
                continue
            break

        return parameters

    def parse_function_body(self):
        """Parse function body including Rebound statement"""
        statements = []
        
        while self.current_token and self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            if self.current_token.type == TokenType.REBOUND.value:
                rebound = self.parse_rebound()
                if isinstance(rebound, SyntaxError):
                    return rebound
                statements.append(rebound)
                break
                
            statement = self.parse_statement()
            if isinstance(statement, SyntaxError):
                return statement
            if statement:
                statements.append(statement)
                
        return statements

    def parse_rebound(self):
        """Parse Rebound statement"""
        start_line = self.current_line
        start_column = self.current_column
        self.advance()

        expression = self.parse_expression()
        if isinstance(expression, SyntaxError):
            return expression

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after Rebound statement")
        self.advance()

        return {
            'type': 'rebound',
            'value': expression,
            'line': start_line,
            'column': start_column
        }

    def is_data_type(self, token_type):
        """Check if token is a data type"""
        return token_type in [
            TokenType.FEINT.value,
            TokenType.FLOATER.value,
            TokenType.CHANT.value,
            TokenType.STAT.value
        ]

    def parse_team_block(self):
        """Parse Team() { statements }"""
        if not self.current_token or self.current_token.type != TokenType.TEAM.value:
            return self.error("Program must start with 'Team'")

        # Store initial position
        start_line = self.current_line
        start_column = self.current_column
        
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after 'Team'")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after 'Team('")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after 'Team()'")
        self.advance()

        statements = self.parse_statements()
        if isinstance(statements, SyntaxError):
            return statements

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' at end of program")
        self.advance()

        return {
            'type': 'program',
            'statements': statements,
            'line': start_line,
            'column': start_column
        }

    def parse_statements(self):
        """Parse multiple statements"""
        statements = []
        
        while self.current_token and self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            # Skip newlines between statements
            if self.current_token.type == TokenType.NEWLINE.value:
                self.advance()
                continue
                
            statement = self.parse_statement()
            if isinstance(statement, SyntaxError):
                return statement
            if statement:  # Skip None results from empty statements
                statements.append(statement)
                
        return statements

    def parse_statement(self):
        """Parse individual statements"""
        if not self.current_token:
            return self.error("Unexpected end of file")

        token_type = self.current_token.type
        
        if self.is_data_type(token_type):
            return self.parse_variable_declaration()
        elif token_type == TokenType.ANNOUNCE.value:
            return self.parse_announce()
        elif token_type == TokenType.DRIBBLE.value:
            return self.parse_dribble()
        elif token_type == TokenType.VAR_INIT.value:
            return self.parse_assignment()
        elif token_type == TokenType.COMMENT.value:
            self.advance()
            return None
        else:
            return self.error(f"Unexpected token: {self.current_token.value}")

    def parse_variable_declaration(self, is_global=False):
        """Parse variable declaration and initialization"""
        start_line = self.current_line
        start_column = self.current_column
        data_type = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error(f"Expected variable name after {data_type}")
        
        var_name = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.ASSIGN.value:
            return self.error(f"Expected '=' after variable name {var_name}")
        self.advance()

        value = self.parse_expression()
        if isinstance(value, SyntaxError):
            return value

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after variable declaration")
        self.advance()

        return {
            'type': 'variable_declaration',
            'data_type': data_type,
            'name': var_name,
            'value': value,
            'line': start_line,
            'column': start_column
        }

    def parse_announce(self):
        """Parse Announce statement"""
        start_line = self.current_line
        start_column = self.current_column
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after 'Announce'")
        self.advance()

        args = self.parse_announce_args()
        if isinstance(args, SyntaxError):
            return args

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after Announce arguments")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after Announce statement")
        self.advance()

        return {
            'type': 'announce',
            'arguments': args,
            'line': start_line,
            'column': start_column
        }

    def parse_announce_args(self):
        """Parse Announce statement arguments including string concatenation"""
        args = []
        
        while self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
            # Parse the first expression
            expr = self.parse_expression()
            if isinstance(expr, SyntaxError):
                return expr
            args.append(expr)
            
            # Check for string concatenation with &
            while self.current_token and self.current_token.type == TokenType.AMPERSAND.value:
                self.advance()  # Move past &
                
                # Parse the next expression after &
                next_expr = self.parse_expression()
                if isinstance(next_expr, SyntaxError):
                    return next_expr
                args.append({
                    'type': 'concatenation',
                    'operator': '&',
                    'value': next_expr
                })
            
            # Break if we hit the closing parenthesis
            if self.current_token and self.current_token.type == TokenType.RIGHT_PAREN.value:
                break
                
        return args

    def parse_expression(self):
        """Parse expressions including literals, variables, and string concatenation"""
        if not self.current_token:
            return self.error("Expected expression")

        start_line = self.current_line
        start_column = self.current_column
        token = self.current_token
        
        # Handle string literals
        if token.type == TokenType.CHANTLIT.value:
            self.advance()
            return {
                'type': 'string_literal',
                'value': token.value,
                'line': start_line,
                'column': start_column
            }
            
        # Handle numeric literals
        elif token.type in [TokenType.FEINTLIT.value, TokenType.FLOATERLIT.value]:
            self.advance()
            return {
                'type': 'numeric_literal',
                'value': token.value,
                'line': start_line,
                'column': start_column
            }
            
        # Handle variables
        elif token.type == TokenType.VAR_INIT.value:
            self.advance()
            return {
                'type': 'variable',
                'name': token.value,
                'line': start_line,
                'column': start_column
            }
            
        # Handle function calls
        elif token.type == TokenType.IDENTIFIER.value:
            return self.parse_function_call()
            
        else:
            return self.error(f"Unexpected token in expression: {token.value}")

    def parse_function_call(self):
        """Parse function call expression"""
        start_line = self.current_line
        start_column = self.current_column
        
        function_name = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error(f"Expected '(' after function name {function_name}")
        self.advance()

        # Parse arguments
        arguments = []
        while self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
            arg = self.parse_expression()
            if isinstance(arg, SyntaxError):
                return arg
            arguments.append(arg)

            if self.current_token and self.current_token.type == TokenType.COMMA.value:
                self.advance()
                continue
            elif self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
                return self.error("Expected ',' or ')' in function arguments")

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after function arguments")
        self.advance()

        return {
            'type': 'function_call',
            'name': function_name,
            'arguments': arguments,
            'line': start_line,
            'column': start_column
        }

    def parse_dribble(self):
        """Parse Dribble (if) statement"""
        start_line = self.current_line
        start_column = self.current_column
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after Dribble")
        self.advance()

        condition = self.parse_expression()
        if isinstance(condition, SyntaxError):
            return condition

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after condition")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after Dribble condition")
        self.advance()

        then_block = self.parse_statements()
        if isinstance(then_block, SyntaxError):
            return then_block

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' after Dribble block")
        self.advance()

        else_block = None
        if self.current_token and self.current_token.type == TokenType.SHOOT.value:
            self.advance()
            
            if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
                return self.error("Expected '{' after Shoot")
            self.advance()

            else_block = self.parse_statements()
            if isinstance(else_block, SyntaxError):
                return else_block

            if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
                return self.error("Expected '}' after Shoot block")
            self.advance()

        return {
            'type': 'dribble',
            'condition': condition,
            'then_block': then_block,
            'else_block': else_block,
            'line': start_line,
            'column': start_column
        }

    def parse_assignment(self):
        """Parse variable assignment"""
        start_line = self.current_line
        start_column = self.current_column
        
        var_name = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.ASSIGN.value:
            return self.error(f"Expected '=' after variable name {var_name}")
        self.advance()

        value = self.parse_expression()
        if isinstance(value, SyntaxError):
            return value

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after assignment")
        self.advance()

        return {
            'type': 'assignment',
            'name': var_name,
            'value': value,
            'line': start_line,
            'column': start_column
        }

def parse(tokens):
    """Main entry point for parsing"""
    parser = Parser(tokens)
    return parser.parse() 