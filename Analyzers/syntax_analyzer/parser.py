from Analyzers.lexical_analyzer.tokens import TokenType, Token
from typing import List, Optional, Set
from Analyzers.syntax_analyzer.errors import SyntaxError 
from Analyzers.syntax_analyzer.first_sets import FIRST_SETS
from Analyzers.syntax_analyzer.predict_sets import PREDICT_SETS

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.current_token = self.tokens[0] if tokens else None
        self.line_number = 1
        self.column = 0
        self.expected_tokens = set()
        self.line_starts = {1: 0}  # Track the starting position of each line
        self.current_line_content = ""  # Track content of current line
        self.current_nonterminal = None  # Track current nonterminal being parsed

    def get_expected_tokens(self, nonterminal: str) -> Set[TokenType]:
        """Get all expected tokens for a nonterminal based on FIRST sets"""
        if nonterminal in FIRST_SETS:
            return FIRST_SETS[nonterminal]
        return set()

    def get_production_rule(self, nonterminal: str, token_type: TokenType) -> Optional[int]:
        """Get the production rule number based on PREDICT sets"""
        if (nonterminal, token_type) in PREDICT_SETS:
            return PREDICT_SETS[(nonterminal, token_type)]
        return None

    def error_handler(self, nonterminal: str, expected_tokens: Set[TokenType] = None) -> None:
        """Enhanced error handler that uses PREDICT sets and FIRST sets"""
        if expected_tokens is None:
            expected_tokens = self.get_expected_tokens(nonterminal)

        if self.current_token:
            token_type = self.current_token.type
            token_value = self.current_token.value
            production_rule = self.get_production_rule(nonterminal, token_type)
            
            # Build detailed error message
            error_msg = f"Syntax Error at line {self.line_number}, column {self.column}:\n"
            error_msg += f"While parsing {nonterminal}, "
            
            if production_rule:
                error_msg += f"expected production rule {production_rule} "
            else:
                error_msg += "unexpected "
            
            error_msg += f"token '{token_value}' of type {token_type}.\n"
            error_msg += f"Expected one of: {', '.join(str(t.value) for t in expected_tokens)}"
            
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected=', '.join(str(t.value) for t in expected_tokens),
                token=token_value,
                nonterminal=nonterminal,
                production_rule=production_rule
            )
        else:
            error_msg = f"Syntax Error at line {self.line_number}, column {self.column}:\n"
            error_msg += f"Unexpected end of file while parsing {nonterminal}.\n"
            error_msg += f"Expected one of: {', '.join(str(t.value) for t in expected_tokens)}"
            
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected=', '.join(str(t.value) for t in expected_tokens),
                token="EOF",
                nonterminal=nonterminal
            )

    def skip_whitespace_and_comments(self):
        """Helper method to skip whitespace, newlines and comments"""
        while self.current_token and self.current_token.type in [
            TokenType.SPACE,
            TokenType.TAB,
            TokenType.NEWLINE,
            TokenType.SINGLE_COMMENT,
            TokenType.MULTI_COMMENT
        ]:
            # Update position tracking for whitespace/comments
            if self.current_token.type == TokenType.NEWLINE:
                self.line_number += 1
                self.column = 0
                self.line_starts[self.line_number] = 0
                self.current_line_content = ""
            elif self.current_token.type in [TokenType.SPACE, TokenType.TAB]:
                # Add spaces to line content
                self.current_line_content += " " * (1 if self.current_token.type == TokenType.TAB else 1)
                
            self.current += 1
            if self.current < len(self.tokens):
                self.current_token = self.tokens[self.current]
            else:
                self.current_token = None
                break

    def update_position(self, token):
        """Update line and column position based on token content"""
        if token.type == TokenType.NEWLINE:
            self.line_number += 1
            self.column = 0
            self.line_starts[self.line_number] = 0
            self.current_line_content = ""
        else:
            # Only update column for non-whitespace tokens
            if token.type not in [TokenType.SPACE, TokenType.TAB]:
                token_value = token.value if hasattr(token, 'value') and token.value else ""
                self.column = len(self.current_line_content)
                self.current_line_content += token_value

    def advance(self) -> None:
        """Advance to next token and update position tracking"""
        if self.current_token:
            self.update_position(self.current_token)
            
        self.current += 1
        if self.current < len(self.tokens):
            self.current_token = self.tokens[self.current]
            # Skip any whitespace or comments after advancing
            self.skip_whitespace_and_comments()
        else:
            self.current_token = None

    def peek(self) -> Optional[Token]:
        """Look at next token without advancing"""
        if self.current + 1 >= len(self.tokens):
            return None
        return self.tokens[self.current + 1]

    def get_token_type(self, token_value: str) -> TokenType:
        """Convert a token value to its corresponding TokenType"""
        try:
            return TokenType[token_value.upper()]
        except KeyError:
            # If not found, return the original token type
            return None

    def match_token_type(self, token: Token, expected_type: TokenType) -> bool:
        """Match a token against an expected token type, considering both type and value"""
        if not token:
            return False
        
        # Get the TokenType for the token's value
        value_type = self.get_token_type(token.value) if token.value else None
        
        # Check if either the token's type matches or its value converts to the expected type
        return token.type == expected_type or value_type == expected_type

    def expect(self, token_type: TokenType) -> None:
        """Expect a specific token type, raise error if not found"""
        if self.current_token and self.match_token_type(self.current_token, token_type):
            self.advance()
        else:
            expected_tokens = {token_type}
            self.error_handler(self.current_nonterminal, expected_tokens)

    def match(self, expected_type: TokenType) -> bool:
        """Check if current token matches expected type"""
        if self.current_token and self.match_token_type(self.current_token, expected_type):
            self.advance()
            return True
        return False
    
    def parse(self) -> None:
        """Start parsing the program"""
        try:
            self.parse_program()
        except SyntaxError as e:
            print(f"Syntax Error: {str(e)}")
            raise
    
    def parse_program(self) -> None:
        """Parse the root production of the grammar - a program"""
        self.current_nonterminal = "program"
        self.skip_whitespace_and_comments()
        
        # Parse declarations until end of file
        while self.current_token:
            if self.current_token.type == TokenType.TEAM:
                self.parse_team_declaration()
            elif self.current_token.type == TokenType.DUNK:
                self.parse_function_declaration()
            else:
                expected_tokens = {TokenType.TEAM, TokenType.DUNK}
                self.error_handler("program", expected_tokens)
        
        # No need to check for remaining tokens as we process them all above
    
    def parse_team_declaration(self) -> None:
        """Parse a team declaration (equivalent to main function)"""
        self.current_nonterminal = "team_declaration"
        
        # Match TEAM keyword
        self.expect(TokenType.TEAM)
        
        # Match left parenthesis
        self.expect(TokenType.LEFT_PAREN)
        
        # Match right parenthesis
        self.expect(TokenType.RIGHT_PAREN)
        
        # Match opening brace
        self.expect(TokenType.CODE_BLOCK_LEFT)
        
        # Parse statements inside the team block
        self.parse_statement_list()
        
        # Match closing brace
        self.expect(TokenType.CODE_BLOCK_RIGHT)
    
    def parse_statement_list(self) -> None:
        """Parse a list of statements"""
        self.current_nonterminal = "statement_list"
        
        # Parse statements until we hit a closing brace
        while self.current_token and self.current_token.type != TokenType.CODE_BLOCK_RIGHT:
            self.parse_statement()
    
    def parse_statement(self) -> None:
        """Parse a single statement"""
        self.current_nonterminal = "statement"
        
        if not self.current_token:
            self.error_handler("statement", {
                TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT,
                TokenType.ANNOUNCE, TokenType.VAR_INIT, TokenType.DRIBBLE, TokenType.FORWARD,
                TokenType.SWITCH, TokenType.TIMEOUT, TokenType.INBOUND
            })
                
        # Check statement type based on first token
        if self.current_token.type in [TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT]:
            # Variable declaration (for any data type)
            self.parse_variable_declaration()
        elif self.current_token.type == TokenType.ANNOUNCE:
            # Announce (print) statement
            self.parse_announce_statement()
        elif self.current_token.type == TokenType.INBOUND:
            # Inbound (input) statement
            self.parse_inbound_statement()
        elif self.current_token.type == TokenType.VAR_INIT:
            # Check if this is a standalone function call or variable assignment
            next_token = self.peek()
            
            if next_token and next_token.type == TokenType.LEFT_PAREN:
                # This is a function call statement
                self.parse_function_call_statement()
            else:
                # This is a variable assignment
                self.parse_variable_assignment()
        elif self.current_token.type == TokenType.DRIBBLE:
            # Conditional statement (if-else)
            self.parse_conditional_statement()
        elif self.current_token.type == TokenType.FORWARD:
            # For loop statement
            self.parse_for_loop_statement()
        elif self.current_token.type == TokenType.SWITCH:
            # Switch statement
            self.parse_switch_statement()
        elif self.current_token.type == TokenType.TIMEOUT:
            # Timeout (break) statement
            self.parse_timeout_statement()
        else:
            # Other statement types would go here
            self.error_handler("statement", {
                TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT,
                TokenType.ANNOUNCE, TokenType.VAR_INIT, TokenType.DRIBBLE, TokenType.FORWARD,
                TokenType.SWITCH, TokenType.TIMEOUT, TokenType.INBOUND
            })

    def parse_inbound_statement(self) -> None:
        """Parse an inbound (input) statement"""
        self.current_nonterminal = "inbound_statement"
        
        # Match INBOUND keyword
        self.expect(TokenType.INBOUND)
        
        # Match opening parenthesis
        self.expect(TokenType.LEFT_PAREN)
        
        # Parse prompt string
        self.parse_expression()
        
        # Expect comma
        self.expect(TokenType.COMMA)
        
        # Expect variable to store input
        self.expect(TokenType.VAR_INIT)
        
        # Match closing parenthesis
        self.expect(TokenType.RIGHT_PAREN)
        
        # Match semicolon
        self.expect(TokenType.SEMICOLON)

    def parse_switch_statement(self) -> None:
        """Parse a switch statement"""
        self.current_nonterminal = "switch_statement"
        
        # Match SWITCH keyword
        self.expect(TokenType.SWITCH)
        
        # Match left parenthesis
        self.expect(TokenType.LEFT_PAREN)
        
        # Parse switch expression
        self.parse_expression()
        
        # Match right parenthesis
        self.expect(TokenType.RIGHT_PAREN)
        
        # Match opening brace
        self.expect(TokenType.CODE_BLOCK_LEFT)
        
        # Parse case statements
        while self.current_token and self.current_token.type != TokenType.CODE_BLOCK_RIGHT:
            if self.current_token.type == TokenType.GET:
                self.parse_case_statement()
            elif self.current_token.type == TokenType.DEFAULT:
                self.parse_default_statement()
                break  # Default should be the last statement in switch
            else:
                self.error_handler("switch_statement", {TokenType.GET, TokenType.DEFAULT, TokenType.CODE_BLOCK_RIGHT})
        
        # Match closing brace
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_case_statement(self) -> None:
        """Parse a case statement within a switch"""
        self.current_nonterminal = "case_statement"
        
        # Match GET keyword (case)
        self.expect(TokenType.GET)
        
        # Parse case value
        self.parse_expression()
        
        # Match colon
        self.expect(TokenType.COLON)
        
        # Parse statements until timeout/next case/default/end of switch
        while self.current_token and self.current_token.type not in [
            TokenType.GET, TokenType.DEFAULT, TokenType.CODE_BLOCK_RIGHT, TokenType.TIMEOUT
        ]:
            self.parse_statement()
        
        # Handle TIMEOUT statement if present (optional)
        if self.current_token and self.current_token.type == TokenType.TIMEOUT:
            self.parse_timeout_statement()

    def parse_default_statement(self) -> None:
        """Parse a default statement within a switch"""
        self.current_nonterminal = "default_statement"
        
        # Match DEFAULT keyword
        self.expect(TokenType.DEFAULT)
        
        # Match colon
        self.expect(TokenType.COLON)
        
        # Parse statements until timeout/end of switch
        while self.current_token and self.current_token.type not in [
            TokenType.CODE_BLOCK_RIGHT, TokenType.TIMEOUT
        ]:
            self.parse_statement()
        
        # Handle TIMEOUT statement if present (optional)
        if self.current_token and self.current_token.type == TokenType.TIMEOUT:
            self.parse_timeout_statement()

    def parse_timeout_statement(self) -> None:
        """Parse a timeout (break) statement"""
        self.current_nonterminal = "timeout_statement"
        
        # Match TIMEOUT keyword
        self.expect(TokenType.TIMEOUT)
        
        # Match semicolon
        self.expect(TokenType.SEMICOLON)

    def parse_for_loop_statement(self) -> None:
        """Parse a for loop statement"""
        self.current_nonterminal = "for_loop_statement"
        
        # Match FORWARD keyword (for)
        self.expect(TokenType.FORWARD)
        
        # Match left parenthesis
        self.expect(TokenType.LEFT_PAREN)
        
        # Parse initialization part (can be variable declaration or assignment)
        if self.current_token and self.current_token.type in [TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT]:
            # Variable declaration
            self.parse_variable_declaration()
        elif self.current_token and self.current_token.type == TokenType.VAR_INIT:
            # Variable assignment
            self.parse_variable_assignment()
        else:
            self.error_handler("for_loop_initialization", {
                TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT, TokenType.VAR_INIT
            })
        
        # Parse condition part (but without semicolon at the end)
        self.parse_conditional_expression()
        self.expect(TokenType.SEMICOLON)
        
        # Parse update part (increment/decrement or assignment)
        if self.current_token and self.current_token.type == TokenType.VAR_INIT:
            variable_name = self.current_token.value
            self.advance()
            
            # Check for increment/decrement
            if self.current_token and self.current_token.type in [TokenType.INCREMENT, TokenType.DECREMENT]:
                # Increment/decrement operators
                self.advance()
            else:
                # Assume it's an assignment, go back to variable
                self.current -= 1
                self.current_token = self.tokens[self.current]
                self.skip_whitespace_and_comments()
                self.parse_variable_assignment_without_semicolon()
        else:
            self.error_handler("for_loop_update", {TokenType.VAR_INIT})
        
        # Match right parenthesis
        self.expect(TokenType.RIGHT_PAREN)
        
        # Match opening brace
        self.expect(TokenType.CODE_BLOCK_LEFT)
        
        # Parse statements inside the loop block
        self.parse_statement_list()
        
        # Match closing brace
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_variable_assignment_without_semicolon(self) -> None:
        """Parse a variable assignment without expecting a semicolon"""
        self.current_nonterminal = "variable_assignment_without_semicolon"
        
        # Match variable identifier (starting with @)
        self.expect(TokenType.VAR_INIT)
        
        # Match assignment operator
        self.expect(TokenType.ASSIGN)
        
        # Parse expression
        self.parse_expression()
        
        # No semicolon expected

    def parse_function_call_statement(self) -> None:
        """Parse a function call as a standalone statement"""
        self.current_nonterminal = "function_call_statement"
        
        # Match variable identifier (function name with @)
        self.expect(TokenType.VAR_INIT)
        
        # Parse the function call
        self.parse_function_call()
        
        # The semicolon is already handled in parse_function_call

    def parse_conditional_statement(self) -> None:
        """Parse a conditional (if/else-if/else) statement"""
        self.current_nonterminal = "conditional_statement"
        
        # Match DRIBBLE keyword (if)
        self.expect(TokenType.DRIBBLE)
        
        # Match left parenthesis
        self.expect(TokenType.LEFT_PAREN)
        
        # Parse conditional expression
        self.parse_conditional_expression()
        
        # Match right parenthesis
        self.expect(TokenType.RIGHT_PAREN)
        
        # Match opening brace
        self.expect(TokenType.CODE_BLOCK_LEFT)
        
        # Parse statements inside the if block
        self.parse_statement_list()
        
        # Match closing brace
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        
        # Check for else-if blocks (PASS)
        while self.current_token and self.current_token.type == TokenType.PASS:
            # Match PASS keyword (else-if)
            self.expect(TokenType.PASS)
            
            # Match left parenthesis
            self.expect(TokenType.LEFT_PAREN)
            
            # Parse conditional expression
            self.parse_conditional_expression()
            
            # Match right parenthesis
            self.expect(TokenType.RIGHT_PAREN)
            
            # Match opening brace
            self.expect(TokenType.CODE_BLOCK_LEFT)
            
            # Parse statements inside the else-if block
            self.parse_statement_list()
            
            # Match closing brace
            self.expect(TokenType.CODE_BLOCK_RIGHT)
        
        # Check if there's an else block (SHOOT)
        if self.current_token and self.current_token.type == TokenType.SHOOT:
            # Match SHOOT keyword (else)
            self.expect(TokenType.SHOOT)
            
            # Match opening brace
            self.expect(TokenType.CODE_BLOCK_LEFT)
            
            # Parse statements inside the else block
            self.parse_statement_list()
            
            # Match closing brace
            self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_conditional_expression(self) -> None:
        """Parse a conditional expression (potentially with logical operators and nested parentheses)"""
        self.current_nonterminal = "conditional_expression"
        
        # Check for opening parenthesis for grouped condition
        if self.current_token and self.current_token.type == TokenType.LEFT_PAREN:
            self.advance()  # Skip opening parenthesis
            self.parse_conditional_expression()  # Parse the inner condition
            self.expect(TokenType.RIGHT_PAREN)  # Expect closing parenthesis
        else:
            # Parse relational expression as normal
            self.parse_relational_expression()
        
        # Check for logical operators like AND_OP, OR_OP
        while self.current_token and self.current_token.type in [TokenType.AND_OP, TokenType.OR_OP]:
            # Match logical operator
            operator_type = self.current_token.type
            self.advance()
            
            # Check for opening parenthesis for the right operand
            if self.current_token and self.current_token.type == TokenType.LEFT_PAREN:
                self.advance()  # Skip opening parenthesis
                self.parse_conditional_expression()  # Parse the inner condition
                self.expect(TokenType.RIGHT_PAREN)  # Expect closing parenthesis
            else:
                # Parse relational expression as normal
                self.parse_relational_expression()

    def parse_relational_expression(self) -> None:
        """Parse a relational expression with operators like ==, !=, <, >, etc."""
        self.current_nonterminal = "relational_expression"
        
        # Parse first expression
        self.parse_expression()
        
        # Check for relational operators
        if self.current_token and self.current_token.type in [
            TokenType.EQUAL, TokenType.NOT_EQUAL, 
            TokenType.LESS_THAN, TokenType.GREATER_THAN,
            TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL
        ]:
            # Match relational operator
            self.advance()
            
            # Parse second expression
            self.parse_expression()
    
    # MARK AS
    
    def parse_variable_declaration(self) -> None:
        """Parse a variable declaration and initialization, potentially with multiple variables"""
        self.current_nonterminal = "variable_declaration"
        
        # Match data type (FEINT, CHANT, FLOATER, STAT)
        if self.current_token.type in [TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT]:
            data_type = self.current_token.type
            self.advance()
        else:
            self.error_handler("variable_declaration", {
                TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT
            })
        
        # Process one or more variable declarations
        while True:
            # Match variable identifier (starting with @)
            self.expect(TokenType.VAR_INIT)
            
            # Check if this variable has an initialization
            if self.current_token and self.current_token.type == TokenType.ASSIGN:
                # Match assignment operator
                self.expect(TokenType.ASSIGN)
                
                # Parse expression
                self.parse_expression()
            
            # Check if there are more variables (separated by comma)
            if self.current_token and self.current_token.type == TokenType.COMMA:
                self.advance()  # Skip the comma
            else:
                break  # No more variables in this declaration
        
        # Match semicolon
        self.expect(TokenType.SEMICOLON)
    
    def parse_variable_assignment(self) -> None:
        """Parse a variable assignment"""
        self.current_nonterminal = "variable_assignment"
        
        # Match variable identifier (starting with @)
        self.expect(TokenType.VAR_INIT)
        
        # Variable name is now handled correctly - no additional check needed
        # Note: Variables can be assigned without prior declaration
        # The semantic analyzer will handle type inference and checking
        
        # Match assignment operator
        self.expect(TokenType.ASSIGN)
        
        # Parse expression
        self.parse_expression()
        
        # Match semicolon
        self.expect(TokenType.SEMICOLON)
    
    def parse_announce_statement(self) -> None:
        """Parse an announce (print) statement with format specifiers"""
        self.current_nonterminal = "announce_statement"
        
        # Match ANNOUNCE keyword
        self.expect(TokenType.ANNOUNCE)
        
        # Match opening parenthesis
        self.expect(TokenType.LEFT_PAREN)
        
        # Parse expression (format string or other expression)
        self.parse_expression()
        
        # Check for additional format arguments
        while self.current_token and self.current_token.type == TokenType.COMMA:
            # Skip comma
            self.advance()
            
            # Parse format argument
            self.parse_expression()
        
        # Match closing parenthesis
        self.expect(TokenType.RIGHT_PAREN)
        
        # Match semicolon
        self.expect(TokenType.SEMICOLON)
    
    def parse_expression(self) -> None:
        """Parse an expression"""
        self.current_nonterminal = "expression"
        
        # Parse simple expression (term)
        self.parse_term()
        
        # Check for operators like +, -, &, etc.
        while self.current_token and self.current_token.type in [
            TokenType.ADD, TokenType.SUB, TokenType.CHANT_CONCAT
        ]:
            # Match operator
            self.advance()
            
            # Parse next term
            self.parse_term()

    def parse_function_declaration(self) -> None:
        """Parse a function declaration"""
        self.current_nonterminal = "function_declaration"
        
        # Match DUNK keyword (void function)
        self.expect(TokenType.DUNK)
        
        # Match function name (@identifier)
        self.expect(TokenType.VAR_INIT)
        
        # Match left parenthesis for parameters
        self.expect(TokenType.LEFT_PAREN)
        
        # Parse parameters if any
        if self.current_token and self.current_token.type != TokenType.RIGHT_PAREN:
            self.parse_parameter_list()
        
        # Match right parenthesis
        self.expect(TokenType.RIGHT_PAREN)
        
        # Match opening brace
        self.expect(TokenType.CODE_BLOCK_LEFT)
        
        # Parse statements inside the function body
        self.parse_statement_list()
        
        # Match closing brace
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_parameter_list(self) -> None:
        """Parse a comma-separated list of function parameters"""
        self.current_nonterminal = "parameter_list"
        
        # Parse at least one parameter
        self.expect(TokenType.VAR_INIT)
        
        # Parse additional parameters if any
        while self.current_token and self.current_token.type == TokenType.COMMA:
            self.advance()  # Skip comma
            self.expect(TokenType.VAR_INIT)  # Expect parameter
    
    def parse_term(self) -> None:
        """Parse a term in an expression"""
        self.current_nonterminal = "term"
        
        # Parse factor
        self.parse_factor()
        
        # Check for operators like *, /, etc.
        while self.current_token and self.current_token.type in [
            TokenType.MUL, TokenType.DIV, TokenType.MOD
        ]:
            # Match operator
            self.advance()
            
            # Parse next factor
            self.parse_factor()
    
    def parse_factor(self) -> None:
        """Parse a factor in a term"""
        self.current_nonterminal = "factor"
        
        if not self.current_token:
            self.error_handler("factor", {
                TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
                TokenType.LEFT_PAREN, TokenType.VAR_INIT
            })
        
        # Check what kind of factor we're dealing with
        if self.current_token.type == TokenType.LEFT_PAREN:
            # Parenthesized expression
            self.advance()
            
            # For nested expressions in conditions, this could be a conditional expression
            if self.current_token and self.current_token.type == TokenType.LEFT_PAREN:
                self.parse_conditional_expression()
            else:
                self.parse_expression()
                
            self.expect(TokenType.RIGHT_PAREN)
        elif self.current_token.type in [TokenType.FEINTLIT, TokenType.FLOATERLIT]:
            # Numeric literal
            self.advance()
        elif self.current_token.type == TokenType.CHANTLIT:
            # String literal
            self.advance()
        elif self.current_token.type == TokenType.VAR_INIT:
            # Variable reference or function call
            variable_name = self.current_token.value
            self.advance()
            
            # Check if this is a function call (has parentheses after the variable)
            if self.current_token and self.current_token.type == TokenType.LEFT_PAREN:
                self.parse_function_call()
        else:
            self.error_handler("factor", {
                TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
                TokenType.LEFT_PAREN, TokenType.VAR_INIT
            })

    def parse_function_call(self) -> None:
        """Parse a function call with arguments"""
        self.current_nonterminal = "function_call"
        
        # Opening parenthesis already matched in parse_factor
        self.expect(TokenType.LEFT_PAREN)
        
        # Parse arguments if any
        if self.current_token and self.current_token.type != TokenType.RIGHT_PAREN:
            self.parse_argument_list()
        
        # Match closing parenthesis
        self.expect(TokenType.RIGHT_PAREN)
        
        # Match semicolon if this is a standalone statement
        if self.current_token and self.current_token.type == TokenType.SEMICOLON:
            self.expect(TokenType.SEMICOLON)

    def parse_argument_list(self) -> None:
        """Parse a comma-separated list of function arguments"""
        self.current_nonterminal = "argument_list"
        
        # Parse first argument
        self.parse_expression()
        
        # Parse additional arguments if any
        while self.current_token and self.current_token.type == TokenType.COMMA:
            self.advance()  # Skip comma
            self.parse_expression()  # Parse next argument

def parse(tokens: List[Token]) -> bool:
    """
    Main parsing function that creates a Parser instance and runs the parsing process.
    
    Args:
        tokens: List of tokens from the lexical analyzer
    
    Returns:
        bool: True if parsing successful, False if syntax errors found
    """
    try:
        parser = Parser(tokens)
        parser.parse()
        return True
    except SyntaxError as e:
        # Instead of printing to console, re-raise the error so it can be caught by the editor
        raise