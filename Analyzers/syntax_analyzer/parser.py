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
        parser.parse_program()
        return True
    except SyntaxError as e:
        # Instead of printing to console, re-raise the error so it can be caught by the editor
        raise