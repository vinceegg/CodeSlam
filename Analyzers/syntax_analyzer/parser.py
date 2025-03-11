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
    
    def skip_whitespace_and_comments(self):
        """Helper method to skip whitespace, newlines and comments"""
        while self.current_token and self.current_token.type in [
            TokenType.SPACE.value,
            TokenType.TAB.value,
            TokenType.NEWLINE.value,
            TokenType.COMMENT.value,
            TokenType.MULTI_COMMENT.value
        ]:
            self.advance()
            
    def parse(self):
        """Entry point for parsing"""
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
            