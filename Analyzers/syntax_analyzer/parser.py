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
                self.current_column += len(str(self.current_token.value)) if hasattr(self.current_token, 'value') else 0
                
            # Skip spaces and tabs
            if self.current_token.type in [TokenType.SPACE.value, TokenType.TAB.value]:
                self.current_token_index += 1
                continue
                
            return self.current_token
            
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
        """Entry point for parsing using predictive parsing"""
        try:
            self.skip_whitespace_and_comments()
            
            # Parse global declarations first
            global_declarations = self.parse_global_declarations()
            if isinstance(global_declarations, SyntaxError):
                return global_declarations
            
            self.skip_whitespace_and_comments()
            
            # Parse function declarations
            function_declarations = self.parse_function_decls()
            if isinstance(function_declarations, SyntaxError):
                return function_declarations
            
            self.skip_whitespace_and_comments()
            
            # Parse function definitions
            function_definitions = self.parse_function_definitions()
            if isinstance(function_definitions, SyntaxError):
                return function_definitions
            
            self.skip_whitespace_and_comments()
            
            # Parse Team block
            if not self.current_token or self.current_token.type != TokenType.TEAM.value:
                return self.error("Expected 'Team' block")
            
            team_block = self.parse_team_block()
            if isinstance(team_block, SyntaxError):
                return team_block
            
            return {
                'type': 'program',
                'global_declarations': global_declarations,
                'function_declarations': function_declarations,
                'function_definitions': function_definitions,
                'team_block': team_block
            }
            
        except Exception as e:
            return self.error(str(e))

    def skip_whitespace_and_comments(self):
        """Helper method to skip whitespace, newlines and comments"""
        while self.current_token and self.current_token.type in [
            TokenType.SPACE.value,
            TokenType.TAB.value,
            TokenType.NEWLINE.value,
            TokenType.COMMENT.value
        ]:
            self.advance()

    def parse_team_block(self):
        """Parse Team block including local declarations"""
        start_line = self.current_line
        start_column = self.current_column
        
        self.advance()  # Move past Team

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after 'Team'")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after 'Team('")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after 'Team()'")
        self.advance()

        # Parse local declarations first
        local_declarations = self.parse_local_declarations()
        if isinstance(local_declarations, SyntaxError):
            return local_declarations

        # Parse statements
        statements = self.parse_statements()
        if isinstance(statements, SyntaxError):
            return statements

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' at end of Team block")
        self.advance()

        return {
            'type': 'team_block',
            'local_declarations': local_declarations,
            'statements': statements,
            'line': start_line,
            'column': start_column
        }

    def parse_statements(self):
        """Parse multiple statements"""
        statements = []
        
        while self.current_token and self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            # Skip whitespace, newlines, and comments between statements
            self.skip_whitespace_and_comments()
            
            if self.current_token and self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
                statement = self.parse_statement()
                if isinstance(statement, SyntaxError):
                    return statement
                if statement:  # Skip None results from empty statements
                    statements.append(statement)
                
        return statements

    def skip_whitespace_and_newlines(self):
        """Helper method to skip whitespace and newlines"""
        while self.current_token and self.current_token.type in [
            TokenType.SPACE.value, 
            TokenType.TAB.value,
            TokenType.NEWLINE.value
        ]:
            self.advance()

    def parse_global_declarations(self):
        """Parse global declarations according to rules 2-6"""
        declarations = []
        
        while self.current_token and (self.is_data_type(self.current_token.type) or 
                                    self.current_token.type == TokenType.CONST.value):
            # Skip if we hit Team block
            next_token = self.peek()
            if next_token and next_token.type == TokenType.WILT.value:
                break
            if next_token and next_token.type == TokenType.TEAM.value:
                break
            
            # Parse global declaration based on type
            declaration = self.parse_global_declared()
            if isinstance(declaration, SyntaxError):
                return declaration
            declarations.append(declaration)
            
            self.skip_whitespace_and_comments()
            
        return declarations

    def parse_global_declared(self):
        """Parse individual global declaration according to rules 4-6"""
        if self.current_token.type == TokenType.CONST.value:
            return self.parse_constant_declaration()
        elif self.peek() and self.peek().type == TokenType.LEFT_BRACKET.value:
            return self.parse_array_declaration(is_global=True)
        else:
            return self.parse_variable_declaration(is_global=True)

    def parse_local_declarations(self):
        """Parse local declarations according to rules 46-49"""
        declarations = []
        
        while self.current_token and self.is_data_type(self.current_token.type):
            # Check if this is the start of a statement
            next_token = self.peek()
            if next_token and next_token.type in [
                TokenType.ANNOUNCE.value,
                TokenType.INBOUND.value,
                TokenType.FORWARD.value,
                TokenType.PLAY.value,
                TokenType.RUN.value,
                TokenType.SWITCH.value
            ]:
                break
            
            # Parse local declaration
            declaration = self.parse_local_declared()
            if isinstance(declaration, SyntaxError):
                return declaration
            declarations.append(declaration)
            
            self.skip_whitespace_and_comments()
            
        return declarations

    def parse_local_declared(self):
        """Parse individual local declaration according to rules 48-49"""
        if self.peek() and self.peek().type == TokenType.LEFT_BRACKET.value:
            return self.parse_array_declaration(is_global=False)
        else:
            return self.parse_variable_declaration(is_global=False)

    def parse_function_decls(self):
        """Parse function declarations"""
        declarations = []
        
        while self.current_token and self.current_token.type == TokenType.WILT.value:
            # Peek ahead to check if this is a declaration (has return type) or definition
            next_token = self.peek()
            if not next_token or not self.is_data_type(next_token.type):
                break  # This is a definition, not a declaration
            
            # Parse function declaration
            declaration = self.parse_function_declaration()
            if isinstance(declaration, SyntaxError):
                return declaration
            declarations.append(declaration)
            
            self.skip_whitespace_and_comments()
            
        return declarations

    def parse_function_declaration(self):
        """Parse function declaration"""
        start_line = self.current_line
        start_column = self.current_column
        
        # Check for Wilt keyword
        if not self.current_token or self.current_token.type != TokenType.WILT.value:
            return self.error("Expected 'Wilt' keyword for function declaration")
        self.advance()
        
        # Parse return type
        if not self.is_data_type(self.current_token.type):
            return self.error("Expected return type for function declaration")
        return_type = self.current_token.value
        self.advance()

        # Parse function name (must be VAR_INIT with @ prefix)
        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected function name with @ prefix")
        function_name = self.current_token.value
        self.advance()

        # Parse parameter list
        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after function name")
        self.advance()

        parameters = self.parse_parameters()
        if isinstance(parameters, SyntaxError):
            return parameters

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after parameters")
        self.advance()

        # Function declarations must end with semicolon
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
        
        while self.current_token and self.current_token.type == TokenType.WILT.value:
            # Peek ahead to check if this is a definition (no return type)
            next_token = self.peek()
            if next_token and self.is_data_type(next_token.type):
                break  # This is a declaration, not a definition
            
            defn = self.parse_function_definition()
            if isinstance(defn, SyntaxError):
                return defn
            definitions.append(defn)
            
        return definitions

    def parse_function_definition(self):
        """Parse function definition"""
        start_line = self.current_line
        start_column = self.current_column
        
        # Check for Wilt keyword
        if not self.current_token or self.current_token.type != TokenType.WILT.value:
            return self.error("Expected 'Wilt' keyword for function definition")
        self.advance()
        
        # Parse function name (must be VAR_INIT with @ prefix)
        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected function name with @ prefix")
        function_name = self.current_token.value
        self.advance()

        # Parse parameter list
        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after function name")
        self.advance()

        # Parse simplified parameters (just variable names)
        parameters = self.parse_simple_parameters()
        if isinstance(parameters, SyntaxError):
            return parameters

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after parameters")
        self.advance()

        # Parse function body
        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after function header")
        self.advance()

        # Parse statements
        statements = []
        rebound_statement = None
        
        self.skip_whitespace_and_comments()
        
        while self.current_token and self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            # Check for Rebound statement
            if self.current_token.type == TokenType.REBOUND.value:
                if rebound_statement:
                    return self.error("Multiple Rebound statements not allowed")
                rebound_statement = self.parse_rebound()
                if isinstance(rebound_statement, SyntaxError):
                    return rebound_statement
                break  # Rebound must be the last statement
            
            statement = self.parse_statement()
            if isinstance(statement, SyntaxError):
                return statement
            if statement:  # Skip None results from empty statements
                statements.append(statement)
            
            self.skip_whitespace_and_comments()
        
        self.skip_whitespace_and_comments()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' at end of function")
        self.advance()

        return {
            'type': 'function_definition',
            'name': function_name,
            'parameters': parameters,
            'body': statements,
            'rebound': rebound_statement,
            'line': start_line,
            'column': start_column
        }

    def parse_simple_parameters(self):
        """Parse function parameters without types"""
        parameters = []
        
        while self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
            # Parse parameter name (must be VAR_INIT with @ prefix)
            if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
                return self.error("Expected parameter name with @ prefix")
            param_name = self.current_token.value
            self.advance()

            parameters.append({
                'name': param_name
            })

            # Check for more parameters
            if self.current_token and self.current_token.type == TokenType.COMMA.value:
                self.advance()
                continue
            break

        return parameters

    def parse_parameters(self):
        """Parse function parameters"""
        parameters = []
        
        while self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
            # Parse parameter type
            if not self.is_data_type(self.current_token.type):
                return self.error("Expected parameter type")
            param_type = self.current_token.value
            self.advance()

            # Parse parameter name (must be VAR_INIT with @ prefix)
            if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
                return self.error("Expected parameter name with @ prefix")
            param_name = self.current_token.value
            self.advance()

            parameters.append({
                'type': param_type,
                'name': param_name
            })

            # Check for more parameters
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

    def parse_statement(self):
        """Parse individual statements according to rules 56-65"""
        if not self.current_token:
            return self.error("Unexpected end of file")

        token_type = self.current_token.type
        
        if self.is_data_type(token_type):
            return self.parse_variable_declaration()
        elif token_type == TokenType.ANNOUNCE.value:
            return self.parse_announce()
        elif token_type == TokenType.INBOUND.value:
            return self.parse_inbound()
        elif token_type == TokenType.FORWARD.value:
            return self.parse_forward()
        elif token_type == TokenType.PLAY.value:
            return self.parse_play()
        elif token_type == TokenType.RUN.value:
            return self.parse_run_play()
        elif token_type == TokenType.DRIBBLE.value:  # Add Dribble statement support
            return self.parse_dribble()
        elif token_type == TokenType.VAR_INIT.value:
            # Check next token to determine if it's a function call or assignment
            next_token = self.peek()
            if next_token and next_token.type == TokenType.LEFT_PAREN.value:
                return self.parse_function_call()
            return self.parse_assignment()
        elif token_type == TokenType.SWITCH.value:
            return self.parse_switch()
        elif token_type == TokenType.COMMENT.value:
            self.advance()
            return None
        else:
            return self.error(f"Unexpected token: {self.current_token.value}")

    def parse_variable_declaration(self, is_global=False):
        """Parse variable declarations according to rules 11-14 and 82"""
        start_line = self.current_line
        start_column = self.current_column
        
        data_type = self.current_token.value
        self.advance()

        declarations = []
        
        # Parse first variable
        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error(f"Expected variable name after {data_type}")
        
        while True:
            var_name = self.current_token.value
            self.advance()

            # Handle initialization if present
            value = None
            if self.current_token and self.current_token.type == TokenType.ASSIGN.value:
                self.advance()
                
                # Parse the initialization value - can be an expression, function call, etc.
                value = self.parse_expression()
                if isinstance(value, SyntaxError):
                    return value

            declarations.append({
                'name': var_name,
                'value': value
            })

            # Check for more variables (,)
            if self.current_token and self.current_token.type == TokenType.COMMA.value:
                self.advance()
                if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
                    return self.error("Expected variable name after comma")
                continue
            break

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after variable declaration")
        self.advance()

        return {
            'type': 'variable_declaration',
            'data_type': data_type,
            'declarations': declarations,
            'is_global': is_global,
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

    """Inbound Syntax : Inbound("String", @id);"""
    def parse_inbound(self):
        """Parse Inbound statement"""
        start_line = self.current_line
        start_column = self.current_column
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after 'Inbound'")
        self.advance()

        args = self.parse_inbound_args()
        if isinstance(args, SyntaxError):
            return args

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after Inbound arguments")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after Inbound statement")
        self.advance()

        return {
            'type': 'inbound',
            'arguments': args,
            'line': start_line,
            'column': start_column
        }
    
    def parse_inbound_args(self):
        """Parse Inbound statement arguments"""
        args = []

        while self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
            expr = self.parse_expression()
            if isinstance(expr, SyntaxError):
                return expr
            args.append(expr)
            
            if self.current_token and self.current_token.type == TokenType.COMMA.value:
                self.advance()
                continue
            break

        return args
        
    def parse_expression(self):
        """Parse expressions including string concatenation"""
        left = self.parse_logical()
        if isinstance(left, SyntaxError):
            return left
        
        # Handle string concatenation with &
        while self.current_token and self.current_token.type == TokenType.AMPERSAND.value:
            operator = self.current_token.value
            self.advance()
            
            right = self.parse_logical()
            if isinstance(right, SyntaxError):
                return right
            
            left = {
                'type': 'concatenation',
                'operator': operator,
                'left': left,
                'right': right,
                'line': self.current_line,
                'column': self.current_column
            }
        
        return left

    def parse_logical(self):
        """Parse logical operations (AND, OR)"""
        left = self.parse_relational()
        if isinstance(left, SyntaxError):
            return left
        
        while self.current_token and self.current_token.type in [
            TokenType.AND.value,
            TokenType.OR.value
        ]:
            operator = self.current_token.value
            self.advance()
            
            right = self.parse_relational()
            if isinstance(right, SyntaxError):
                return right
            
            left = {
                'type': 'logical_operation',
                'operator': operator,
                'left': left,
                'right': right
            }
        
        return left

    def parse_relational(self):
        """Parse relational operations (>, <, >=, <=, ==, !=)"""
        left = self.parse_arithmetic()
        if isinstance(left, SyntaxError):
            return left
        
        while self.current_token and self.current_token.type in [
            TokenType.GREATER_THAN.value,
            TokenType.LESS_THAN.value,
            TokenType.GREATER_EQUAL.value,
            TokenType.LESS_EQUAL.value,
            TokenType.EQUAL.value,
            TokenType.NOT_EQUAL.value
        ]:
            operator = self.current_token.value
            self.advance()
            
            right = self.parse_arithmetic()
            if isinstance(right, SyntaxError):
                return right
            
            left = {
                'type': 'comparison',
                'operator': operator,
                'left': left,
                'right': right
            }
        
        return left

    def parse_arithmetic(self):
        """Parse arithmetic operations (+, -, *, /, %)"""
        left = self.parse_term()
        if isinstance(left, SyntaxError):
            return left
        
        while self.current_token and self.current_token.type in [
            TokenType.ADD.value,
            TokenType.SUB.value
        ]:
            operator = self.current_token.value
            self.advance()
            
            right = self.parse_term()
            if isinstance(right, SyntaxError):
                return right
            
            left = {
                'type': 'arithmetic_operation',
                'operator': operator,
                'left': left,
                'right': right
            }
        
        return left

    def parse_term(self):
        """Parse term operations (*, /, %)"""
        left = self.parse_factor()
        if isinstance(left, SyntaxError):
            return left
        
        while self.current_token and self.current_token.type in [
            TokenType.MUL.value,
            TokenType.DIV.value,
            TokenType.MOD.value
        ]:
            operator = self.current_token.value
            self.advance()
            
            right = self.parse_factor()
            if isinstance(right, SyntaxError):
                return right
            
            left = {
                'type': 'arithmetic_operation',
                'operator': operator,
                'left': left,
                'right': right
            }
        
        return left

    def parse_factor(self):
        """Parse factors (primary expressions, unary operations, and type casting)"""
        if not self.current_token:
            return self.error("Expected expression")
        
        # Handle type casting
        if self.current_token.type in [TokenType.FEINT.value, TokenType.FLOATER.value, 
                                      TokenType.CHANT.value, TokenType.STAT.value]:
            return self.parse_type_cast()
        
        # Handle unary operations
        if self.current_token.type in [TokenType.ADD.value, TokenType.SUB.value, TokenType.NOT.value]:
            operator = self.current_token.value
            self.advance()
            
            operand = self.parse_factor()
            if isinstance(operand, SyntaxError):
                return operand
            
            return {
                'type': 'unary_operation',
                'operator': operator,
                'operand': operand
            }
        
        return self.parse_primary()

    def parse_type_cast(self):
        """Parse type casting expressions"""
        cast_type = self.current_token.value
        start_line = self.current_line
        start_column = self.current_column
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error(f"Expected '(' after {cast_type} for type casting")
        self.advance()

        value = self.parse_expression()
        if isinstance(value, SyntaxError):
            return value

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error(f"Expected ')' after value in {cast_type} type cast")
        self.advance()

        return {
            'type': 'type_cast',
            'cast_type': cast_type,
            'value': value,
            'line': start_line,
            'column': start_column
        }

    def parse_primary(self):
        """Parse primary expressions (variables, literals, parenthesized expressions, function calls)"""
        if not self.current_token:
            return self.error("Expected expression")

        token = self.current_token
        
        # Handle variables with @ prefix and function calls
        if token.type == TokenType.VAR_INIT.value:
            var_name = token.value
            self.advance()
            
            # Check if this is a function call
            if self.current_token and self.current_token.type == TokenType.LEFT_PAREN.value:
                self.advance()  # Move past (
                
                # Parse arguments
                arguments = []
                while self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
                    argument = self.parse_expression()
                    if isinstance(argument, SyntaxError):
                        return argument
                    arguments.append(argument)
                    
                    # Check for more arguments
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
                    'name': var_name,
                    'arguments': arguments
                }
            
            return {
                'type': 'variable',
                'name': var_name
            }
        
        # Handle numeric literals
        elif token.type in [TokenType.FEINTLIT.value, TokenType.FLOATERLIT.value]:
            value = token.value
            self.advance()
            return {
                'type': 'numeric_literal',
                'value': value
            }
        
        # Handle string literals
        elif token.type == TokenType.CHANTLIT.value:
            value = token.value
            self.advance()
            return {
                'type': 'string_literal',
                'value': value
            }
        
        # Handle boolean literals
        elif token.type in [TokenType.WIN.value, TokenType.LOSS.value]:
            value = token.value
            self.advance()
            return {
                'type': 'boolean_literal',
                'value': value
            }
        
        # Handle parenthesized expressions
        elif token.type == TokenType.LEFT_PAREN.value:
            self.advance()
            expr = self.parse_expression()
            if isinstance(expr, SyntaxError):
                return expr
            
            if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
                return self.error("Expected ')'")
            self.advance()
            return expr
        
        else:
            return self.error(f"Unexpected token in expression: {token.value}")

    def parse_function_call(self):
        """Parse function call as a statement according to rule 228"""
        start_line = self.current_line
        start_column = self.current_column
        
        # Get function name
        function_name = self.current_token.value
        self.advance()

        # Parse argument list
        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after function name")
        self.advance()

        arguments = []
        while self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
            # Parse argument according to rules 233-237
            if self.current_token.type in [TokenType.FEINTLIT.value, TokenType.FLOATERLIT.value, TokenType.CHANTLIT.value, TokenType.WIN.value, TokenType.LOSS.value]:
                # Literal argument
                arguments.append({
                    'type': 'literal',
                    'value': self.current_token.value
                })
                self.advance()
            elif self.current_token.type == TokenType.VAR_INIT.value:
                # Variable or array element argument
                var_name = self.current_token.value
                self.advance()
                
                # Check for array access
                if self.current_token and self.current_token.type == TokenType.LEFT_BRACKET.value:
                    self.advance()
                    index = self.parse_expression()
                    if isinstance(index, SyntaxError):
                        return index
                        
                    if not self.current_token or self.current_token.type != TokenType.RIGHT_BRACKET.value:
                        return self.error("Expected ']' after array index")
                    self.advance()
                    
                    arguments.append({
                        'type': 'array_element',
                        'name': var_name,
                        'index': index
                    })
                else:
                    arguments.append({
                        'type': 'variable',
                        'name': var_name
                    })
            else:
                # Expression argument
                argument = self.parse_expression()
                if isinstance(argument, SyntaxError):
                    return argument
                arguments.append(argument)

            # Check for more arguments
            if self.current_token and self.current_token.type == TokenType.COMMA.value:
                self.advance()
                continue
            elif self.current_token and self.current_token.type != TokenType.RIGHT_PAREN.value:
                return self.error("Expected ',' or ')' in function arguments")

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after function arguments")
        self.advance()

        # Function calls in statements must end with semicolon
        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after function call")
        self.advance()

        return {
            'type': 'function_call_statement',
            'name': function_name,
            'arguments': arguments,
            'line': start_line,
            'column': start_column
        }

    def parse_assignment(self):
        """Parse variable assignment"""
        start_line = self.current_line
        start_column = self.current_column
        
        var_name = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type not in [
            TokenType.ASSIGN.value,
            TokenType.ADD_ASSIGN.value,
            TokenType.SUB_ASSIGN.value,
            TokenType.MUL_ASSIGN.value,
            TokenType.DIV_ASSIGN.value,
            TokenType.MOD_ASSIGN.value
        ]:
            return self.error(f"Expected '=', '+=', '-=', '*=', '/=', or '%=' after variable name {var_name}")
        operator = self.current_token.value
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
            'operator': operator,
            'value': value,
            'line': start_line,
            'column': start_column
        }

    def parse_constant_declaration(self):
        """Parse constant declaration"""
        start_line = self.current_line
        start_column = self.current_column
        
        # Skip 'Const' keyword
        self.advance()
        
        if not self.current_token or not self.is_data_type(self.current_token.type):
            return self.error("Expected data type after 'Const'")
        data_type = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected variable name after data type")
        const_name = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.ASSIGN.value:
            return self.error("Expected '=' after constant name")
        self.advance()

        value = self.parse_expression()
        if isinstance(value, SyntaxError):
            return value

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after constant declaration")
        self.advance()

        return {
            'type': 'constant_declaration',
            'data_type': data_type,
            'name': const_name,
            'value': value,
            'is_global': True,
            'line': start_line,
            'column': start_column
        }

    def parse_array_declaration(self, is_global=False):
        """Parse array declaration according to CFG rules 21-36"""
        start_line = self.current_line
        start_column = self.current_column
        
        data_type = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected array name")
        array_name = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_BRACKET.value:
            return self.error("Expected '[' after array name")
        self.advance()

        # Parse array size
        size = self.parse_array_size()
        if isinstance(size, SyntaxError):
            return size

        if not self.current_token or self.current_token.type != TokenType.RIGHT_BRACKET.value:
            return self.error("Expected ']' after array size")
        self.advance()

        # Check for optional second dimension
        dimensions = [size]
        if self.current_token and self.current_token.type == TokenType.LEFT_BRACKET.value:
            self.advance()
            size2 = self.parse_array_size()
            if isinstance(size2, SyntaxError):
                return size2
            dimensions.append(size2)
            
            if not self.current_token or self.current_token.type != TokenType.RIGHT_BRACKET.value:
                return self.error("Expected ']' after second dimension size")
            self.advance()

        # Parse optional initialization
        initialization = None
        if self.current_token and self.current_token.type == TokenType.ASSIGN.value:
            self.advance()
            initialization = self.parse_array_initialization(len(dimensions))
            if isinstance(initialization, SyntaxError):
                return initialization

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after array declaration")
        self.advance()

        return {
            'type': 'array_declaration',
            'data_type': data_type,
            'name': array_name,
            'dimensions': dimensions,
            'initialization': initialization,
            'is_global': is_global,
            'line': start_line,
            'column': start_column
        }

    def parse_array_size(self):
        """Parse array size expression"""
        if not self.current_token:
            return self.error("Expected array size")
        
        if self.current_token.type != TokenType.FEINTLIT.value:
            return self.error("Array size must be a Feint literal")
        
        size = int(self.current_token.value)
        self.advance()
        return size

    def parse_array_initialization(self, dimensions):
        """Parse array initialization values"""
        if not self.current_token or self.current_token.type != TokenType.LEFT_BRACE.value:
            return self.error("Expected '{' for array initialization")
        self.advance()

        values = []
        while self.current_token and self.current_token.type != TokenType.RIGHT_BRACE.value:
            if dimensions == 2:
                # Parse nested array for 2D
                if not self.current_token or self.current_token.type != TokenType.LEFT_BRACE.value:
                    return self.error("Expected '{' for nested array")
                self.advance()
                
                row = []
                while self.current_token and self.current_token.type != TokenType.RIGHT_BRACE.value:
                    value = self.parse_array_element()
                    if isinstance(value, SyntaxError):
                        return value
                    row.append(value)
                    
                values.append(row)
                
                if not self.current_token or self.current_token.type != TokenType.RIGHT_BRACE.value:
                    return self.error("Expected '}' after nested array")
                self.advance()
                
            else:
                # Parse 1D array elements
                value = self.parse_array_element()
                if isinstance(value, SyntaxError):
                    return value
                values.append(value)
                
            if self.current_token and self.current_token.type == TokenType.COMMA.value:
                self.advance()
                
        if not self.current_token or self.current_token.type != TokenType.RIGHT_BRACE.value:
            return self.error("Expected '}' after array initialization")
        self.advance()
        
        return values

    def parse_array_element(self):
        """Parse single array element according to CFG rules 32-34"""
        if not self.current_token:
            return self.error("Expected array element")
        
        if self.current_token.type in [TokenType.FEINTLIT.value, TokenType.FLOATERLIT.value, TokenType.CHANTLIT.value]:
            value = self.current_token.value
            self.advance()
            return value
        
        return self.error("Invalid array element type")

    def data_type(self):
        """
        <data_type> → Feint
        <data_type> → Floater
        <data_type> → Chant
        <data_type> → Stat
        """
        if self.current_token.type in ['Feint', 'Floater', 'Chant', 'Stat']:
            self.advance()
        else:
            raise SyntaxError(
                f"Expected data type (Feint, Floater, Chant, Stat), got {self.current_token.type}",
                self.current_token.line,
                self.current_token.column
            )

    def initialize_end(self):
        """
        <initialize_end> → = <global_value> <decls_end>
        <initialize_end> → λ
        """
        if self.current_token.type == 'EQUALS':
            self.advance()  # consume '='
            self.global_value()
            self.decls_end()

    def decls_end(self):
        """
        <decls_end> → , identifier <initialize_end> <decls_end>
        <decls_end> → λ
        """
        if self.current_token.type == 'COMMA':
            self.advance()  # consume ','
            self.match('IDENTIFIER')
            self.initialize_end()
            self.decls_end()

    def parse_switch(self):
        """Parse Switch statement according to rules 71-81"""
        start_line = self.current_line
        start_column = self.current_column
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after Switch")
        self.advance()

        # Parse switch expression (rules 72-74)
        switch_expr = None
        if self.current_token.type == TokenType.VAR_INIT.value:
            switch_expr = {'type': 'identifier', 'value': self.current_token.value}
        elif self.current_token.type == TokenType.FEINTLIT.value:
            switch_expr = {'type': 'feint_literal', 'value': self.current_token.value}
        elif self.current_token.type == TokenType.CHANTLIT.value:
            switch_expr = {'type': 'chant_literal', 'value': self.current_token.value}
        else:
            return self.error("Invalid switch expression")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after switch expression")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after switch header")
        self.advance()

        # Parse case list (rules 75-80)
        cases = []
        while self.current_token and self.current_token.type == TokenType.GET.value:
            self.advance()
            
            # Parse case value
            if not self.current_token:
                return self.error("Expected case value")
            
            if self.current_token.type in [TokenType.ARITH_OP.value, TokenType.ALPHABET.value,
                                         TokenType.FEINTLIT.value, TokenType.FLOATERLIT.value]:
                case_value = self.current_token.value
                self.advance()
            else:
                return self.error("Invalid case value")

            if not self.current_token or self.current_token.type != TokenType.COLON.value:
                return self.error("Expected ':' after case value")
            self.advance()

            # Parse case statements
            case_statements = self.parse_statements()
            if isinstance(case_statements, SyntaxError):
                return case_statements

            cases.append({
                'value': case_value,
                'statements': case_statements
            })

        # Parse default case (rule 81)
        default_case = None
        if self.current_token and self.current_token.type == TokenType.DEFAULT.value:
            self.advance()
            
            if not self.current_token or self.current_token.type != TokenType.COLON.value:
                return self.error("Expected ':' after Default")
            self.advance()

            default_statements = self.parse_statements()
            if isinstance(default_statements, SyntaxError):
                return default_statements
            default_case = default_statements

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' at end of switch")
        self.advance()

        return {
            'type': 'switch',
            'expression': switch_expr,
            'cases': cases,
            'default': default_case,
            'line': start_line,
            'column': start_column
        }

    def parse_binary_operation(self):
        """Parse binary operations like addition, comparison, etc."""
        left = self.parse_expression()
        if isinstance(left, SyntaxError):
            return left
        
        while self.current_token and self.current_token.type in [
            TokenType.ADD.value,
            TokenType.SUB.value,
            TokenType.MUL.value,
            TokenType.DIV.value,
            TokenType.MOD.value,
            TokenType.GREATER_THAN.value,
            TokenType.LESS_THAN.value,
            TokenType.GREATER_EQUAL.value,
            TokenType.LESS_EQUAL.value,
            TokenType.EQUAL.value,
            TokenType.NOT_EQUAL.value
        ]:
            operator = self.current_token.value
            self.advance()
            
            right = self.parse_expression()
            if isinstance(right, SyntaxError):
                return right
            
            left = {
                'type': 'binary_operation',
                'operator': operator,
                'left': left,
                'right': right,
                'line': self.current_line,
                'column': self.current_column
            }
        
        return left

    def parse_forward(self):
        """Parse Forward statement according to rules 201-213"""
        start_line = self.current_line
        start_column = self.current_column
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after Forward")
        self.advance()

        # Parse initialization (rules 202-205)
        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected variable name in Forward initialization")
        var_name = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.ASSIGN.value:
            return self.error("Expected '=' in Forward initialization")
        self.advance()

        initial_value = self.parse_expression()
        if isinstance(initial_value, SyntaxError):
            return initial_value

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after Forward initialization")
        self.advance()

        # Parse condition (rules 206-210)
        condition = self.parse_binary_operation()
        if isinstance(condition, SyntaxError):
            return condition

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after Forward condition")
        self.advance()

        # Parse increment/decrement (rules 211-213)
        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected variable in Forward increment/decrement")
        inc_var = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type not in [
            TokenType.ADD_ASSIGN.value,
            TokenType.SUB_ASSIGN.value,
            TokenType.MUL_ASSIGN.value,
            TokenType.DIV_ASSIGN.value,
            TokenType.MOD_ASSIGN.value
        ]:
            return self.error("Expected '+=', '-=', '*=', '/=', or '%=' in Forward increment/decrement")
        inc_op = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.FEINTLIT.value:
            return self.error("Expected numeric literal in Forward increment/decrement")
        inc_value = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after Forward increment/decrement")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after Forward header")
        self.advance()

        # Parse loop body
        body = self.parse_statements()
        if isinstance(body, SyntaxError):
            return body

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' at end of Forward block")
        self.advance()

        return {
            'type': 'forward',
            'initialization': {
                'name': var_name,
                'value': initial_value
            },
            'condition': condition,
            'update': {
                'variable': inc_var,
                'operator': inc_op,
                'value': inc_value
            },
            'body': body,
            'line': start_line,
            'column': start_column
        }

    def parse_play(self):
        """Parse Play statement according to rule 226"""
        start_line = self.current_line
        start_column = self.current_column
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after Play")
        self.advance()

        condition = self.parse_expression()
        if isinstance(condition, SyntaxError):
            return condition

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after Play condition")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after Play condition")
        self.advance()

        body = self.parse_statements()
        if isinstance(body, SyntaxError):
            return body

        # Parse increment/decrement
        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected variable for Play increment/decrement")
        inc_var = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type not in [
            TokenType.ADD_ASSIGN.value,
            TokenType.SUB_ASSIGN.value,
            TokenType.MUL_ASSIGN.value,
            TokenType.DIV_ASSIGN.value,
            TokenType.MOD_ASSIGN.value
        ]:
            return self.error("Expected '+=', '-=', '*=', '/=', or '%=' in Play increment/decrement")
        inc_op = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.FEINTLIT.value:
            return self.error("Expected numeric literal in Play increment/decrement")
        inc_value = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' at end of Play block")
        self.advance()

        return {
            'type': 'play',
            'condition': condition,
            'body': body,
            'update': {
                'variable': inc_var,
                'operator': inc_op,
                'value': inc_value
            },
            'line': start_line,
            'column': start_column
        }

    def parse_run_play(self):
        """Parse Run-Play statement according to rule 227"""
        start_line = self.current_line
        start_column = self.current_column
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after Run")
        self.advance()

        body = self.parse_statements()
        if isinstance(body, SyntaxError):
            return body

        # Parse increment/decrement
        if not self.current_token or self.current_token.type != TokenType.VAR_INIT.value:
            return self.error("Expected variable for Run-Play increment/decrement")
        inc_var = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type not in [
            TokenType.ADD_ASSIGN.value,
            TokenType.SUB_ASSIGN.value,
            TokenType.MUL_ASSIGN.value,
            TokenType.DIV_ASSIGN.value,
            TokenType.MOD_ASSIGN.value
        ]:
            return self.error("Expected '+=', '-=', '*=', '/=', or '%=' in Run-Play increment/decrement")
        inc_op = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.FEINTLIT.value:
            return self.error("Expected numeric literal in Run-Play increment/decrement")
        inc_value = self.current_token.value
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' after Run block")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.PLAY.value:
            return self.error("Expected 'Play' after Run block")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after Play")
        self.advance()

        condition = self.parse_expression()
        if isinstance(condition, SyntaxError):
            return condition

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after Play condition")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            return self.error("Expected ';' after Run-Play statement")
        self.advance()

        return {
            'type': 'run_play',
            'body': body,
            'update': {
                'variable': inc_var,
                'operator': inc_op,
                'value': inc_value
            },
            'condition': condition,
            'line': start_line,
            'column': start_column
        }

    def parse_dribble(self):
        """Parse Dribble-Pass-Shoot (if-elseif-else) statement"""
        start_line = self.current_line
        start_column = self.current_column
        self.advance()  # Move past 'Dribble'

        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            return self.error("Expected '(' after Dribble")
        self.advance()

        # Parse condition
        condition = self.parse_expression()
        if isinstance(condition, SyntaxError):
            return condition

        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            return self.error("Expected ')' after condition")
        self.advance()

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            return self.error("Expected '{' after Dribble condition")
        self.advance()

        # Parse if block statements
        if_statements = self.parse_statements()
        if isinstance(if_statements, SyntaxError):
            return if_statements

        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            return self.error("Expected '}' after Dribble block")
        self.advance()

        # Parse Pass (else if) blocks
        pass_blocks = []
        while self.current_token and self.current_token.type == TokenType.PASS.value:
            self.advance()  # Move past 'Pass'

            if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
                return self.error("Expected '(' after Pass")
            self.advance()

            pass_condition = self.parse_expression()
            if isinstance(pass_condition, SyntaxError):
                return pass_condition

            if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
                return self.error("Expected ')' after Pass condition")
            self.advance()

            if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
                return self.error("Expected '{' after Pass condition")
            self.advance()

            pass_statements = self.parse_statements()
            if isinstance(pass_statements, SyntaxError):
                return pass_statements

            if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
                return self.error("Expected '}' after Pass block")
            self.advance()

            pass_blocks.append({
                'condition': pass_condition,
                'statements': pass_statements
            })

        # Parse optional Shoot (else) block
        shoot_statements = None
        if self.current_token and self.current_token.type == TokenType.SHOOT.value:
            self.advance()  # Move past 'Shoot'

            if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
                return self.error("Expected '{' after Shoot")
            self.advance()

            shoot_statements = self.parse_statements()
            if isinstance(shoot_statements, SyntaxError):
                return shoot_statements

            if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
                return self.error("Expected '}' after Shoot block")
            self.advance()

        return {
            'type': 'dribble',
            'condition': condition,
            'if_statements': if_statements,
            'pass_blocks': pass_blocks,
            'shoot_statements': shoot_statements,
            'line': start_line,
            'column': start_column
        }

    def is_in_first_set(self, token_type, non_terminal):
        """Check if token is in FIRST set of given non-terminal"""
        first_sets = {
            'program': {TokenType.FEINT.value, TokenType.FLOATER.value, TokenType.CHANT.value, 
                       TokenType.STAT.value, TokenType.CONST.value, TokenType.TEAM.value},
            'global_decl': {TokenType.FEINT.value, TokenType.FLOATER.value, TokenType.CHANT.value, 
                           TokenType.STAT.value, TokenType.CONST.value},
            'function_decls': {TokenType.FEINT.value, TokenType.FLOATER.value, TokenType.CHANT.value, 
                              TokenType.STAT.value},
            'team_statements': {TokenType.FEINT.value, TokenType.FLOATER.value, TokenType.CHANT.value,
                              TokenType.STAT.value, TokenType.ANNOUNCE.value, TokenType.INBOUND.value,
                              TokenType.FORWARD.value, TokenType.PLAY.value, TokenType.RUN.value,
                              TokenType.SWITCH.value, TokenType.VAR_INIT.value},
            'expression': {TokenType.VAR_INIT.value, TokenType.FEINTLIT.value, TokenType.FLOATERLIT.value,
                          TokenType.CHANTLIT.value, TokenType.WIN.value, TokenType.LOSS.value,
                          TokenType.LEFT_PAREN.value}
        }
        return token_type in first_sets.get(non_terminal, set())

    def is_in_follow_set(self, token_type, non_terminal):
        """Check if token is in FOLLOW set of given non-terminal"""
        follow_sets = {
            'global_decl': {TokenType.TEAM.value, TokenType.FEINT.value, TokenType.FLOATER.value,
                           TokenType.CHANT.value, TokenType.STAT.value},
            'function_decls': {TokenType.TEAM.value},
            'team_statements': {TokenType.CODE_BLOCK_RIGHT.value, TokenType.REBOUND.value},
            'expression': {TokenType.SEMICOLON.value, TokenType.RIGHT_PAREN.value, TokenType.COMMA.value,
                          TokenType.AMPERSAND.value}
        }
        return token_type in follow_sets.get(non_terminal, set())

    def predict(self, productions):
        """Use predict sets to determine which production to use"""
        if not self.current_token:
            return None
        
        token_type = self.current_token.type
        
        predict_sets = {
            'variable_declaration': {TokenType.FEINT.value, TokenType.FLOATER.value, 
                                   TokenType.CHANT.value, TokenType.STAT.value},
            'constant_declaration': {TokenType.CONST.value},
            'array_declaration': {TokenType.FEINT.value, TokenType.FLOATER.value, 
                                TokenType.CHANT.value, TokenType.STAT.value},
            'function_declaration': {TokenType.FEINT.value, TokenType.FLOATER.value, 
                                   TokenType.CHANT.value, TokenType.STAT.value},
            'team_block': {TokenType.TEAM.value}
        }
        
        for production, predict_set in predict_sets.items():
            if token_type in predict_set:
                return production
            
        return None

    def sync(self, sync_set):
        """Synchronize parser after error by skipping tokens until sync point"""
        while self.current_token and self.current_token.type not in sync_set:
            self.advance()

def parse(tokens):
    """Main entry point for parsing"""
    parser = Parser(tokens)
    return parser.parse()