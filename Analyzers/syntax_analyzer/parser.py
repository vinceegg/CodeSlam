from Analyzers.lexical_analyzer.tokens import TokenType, Token

class Parser:
    def __init__(self, tokens):
        # Filter out whitespace tokens
        self.tokens = [token for token in tokens if token.type not in 
                      [TokenType.SPACE.value, TokenType.TAB.value, TokenType.NEWLINE.value]]
        self.current_token_index = -1
        self.current_token = None
        self.advance()

    def advance(self):
        """Move to the next token"""
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
        return self.current_token

    def peek(self):
        """Look at the next token without advancing"""
        peek_index = self.current_token_index + 1
        if peek_index < len(self.tokens):
            return self.tokens[peek_index]
        return None

    def parse(self):
        """Main parsing method"""
        try:
            return self.program()
        except Exception as e:
            return f"Syntax Error: {str(e)}"

    def program(self):
        """Program → Team() { statements }"""
        if not self.current_token or self.current_token.type != TokenType.TEAM.value:
            raise Exception("Program must start with 'Team'")
        
        self.advance()  # Move past 'Team'
        
        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            raise Exception("Expected '(' after 'Team'")
        
        self.advance()  # Move past '('
        
        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            raise Exception("Expected ')' after 'Team('")
        
        self.advance()  # Move past ')'
        
        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_LEFT.value:
            raise Exception("Expected '{' after 'Team()'")
        
        self.advance()  # Move past '{'
        
        # Parse statements
        statements = self.statements()
        
        if not self.current_token or self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            raise Exception("Expected '}' at end of program")
        
        return statements

    def statements(self):
        """statements → statement statements | ε"""
        statements = []
        
        while self.current_token and self.current_token.type != TokenType.CODE_BLOCK_RIGHT.value:
            statement = self.statement()
            if statement:
                statements.append(statement)
                
        return statements

    def statement(self):
        """Parse individual statements"""
        if not self.current_token:
            return None
            
        # Variable declaration
        if self.current_token.type == TokenType.VAR_INIT.value:
            return self.parse_variable_declaration()
            
        # Announce statement
        elif self.current_token.type == TokenType.ANNOUNCE.value:
            return self.parse_announce()
            
        # Dribble (if) statement
        elif self.current_token.type == TokenType.DRIBBLE.value:
            return self.parse_dribble()
            
        # Play (while) statement
        elif self.current_token.type == TokenType.PLAY.value:
            return self.parse_play()
            
        # Forward (for) statement
        elif self.current_token.type == TokenType.FORWARD.value:
            return self.parse_forward()
            
        else:
            raise Exception(f"Unexpected token: {self.current_token.type}")

    def parse_variable_declaration(self):
        """Parse variable declaration"""
        var_name = self.current_token.value
        self.advance()  # Move past variable name
        
        if not self.current_token or self.current_token.type != TokenType.ASSIGN.value:
            raise Exception("Expected '=' after variable name")
            
        self.advance()  # Move past '='
        
        value = self.parse_expression()
        
        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            raise Exception("Expected ';' after variable declaration")
            
        self.advance()  # Move past ';'
        
        return {
            'type': 'variable_declaration',
            'name': var_name,
            'value': value
        }

    def parse_announce(self):
        """Parse Announce statement"""
        self.advance()  # Move past 'Announce'
        
        if not self.current_token or self.current_token.type != TokenType.LEFT_PAREN.value:
            raise Exception("Expected '(' after 'Announce'")
            
        self.advance()  # Move past '('
        
        expression = self.parse_expression()
        
        if not self.current_token or self.current_token.type != TokenType.RIGHT_PAREN.value:
            raise Exception("Expected ')' after expression in Announce")
            
        self.advance()  # Move past ')'
        
        if not self.current_token or self.current_token.type != TokenType.SEMICOLON.value:
            raise Exception("Expected ';' after Announce statement")
            
        self.advance()  # Move past ';'
        
        return {
            'type': 'announce',
            'expression': expression
        }

    def parse_expression(self):
        """Parse expressions (basic implementation)"""
        if not self.current_token:
            raise Exception("Expected expression")
            
        # Handle literals
        if self.current_token.type in [TokenType.FEINTLIT.value, TokenType.FLOATERLIT.value, TokenType.CHANTLIT.value]:
            value = self.current_token.value
            self.advance()
            return {
                'type': 'literal',
                'value': value
            }
            
        # Handle variables
        elif self.current_token.type == TokenType.VAR_INIT.value:
            value = self.current_token.value
            self.advance()
            return {
                'type': 'variable',
                'name': value
            }
            
        else:
            raise Exception(f"Unexpected token in expression: {self.current_token.type}")

def parse(tokens):
    """Main function to start parsing"""
    parser = Parser(tokens)
    return parser.parse() 