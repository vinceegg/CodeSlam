#errors.py
class Error:
    '''
    Represents an error that occurred during tokenization.

    Properties:
    • pos_start: The position where the error starts (a Position object).
    • pos_end: The position where the error ends (a Position object).
    • error_name: A string representing the type of error (e.g., "Illegal Character").
    • details: A string providing details about the error.

    Methods:
    • as_string(): Generates a formatted error message as a string.
    '''

    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        '''
        Generates a formatted error message as a string.
        '''
        result = f"{self.error_name}: {self.details}\n"
        result += f"File {self.pos_start.fn}, line {self.pos_start.ln + 1}"
        return result


class IllegalCharError(Error):
    """
    Raised when an illegal character is encountered.
    """
    # Triggered when: An invalid or unrecognized character appears in the source code.

    # Example Code:
    # Feint Main() { Announce("Hello$World"); }

    # Error Message:
    # LexerError: Illegal character '$' at line 1, column 24

    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, "Lexical error: Illegal character/s", details)


class UnterminatedStringError(Error):
    """
    Raised when a string literal is not properly terminated.
    """

    # Triggered when: A string literal starts with a double quote but does not have a closing double quote.

    # Example Code:
    # Feint Main() { Announce("Hello World; }

    # Error Message:
    # LexerError: Unterminated string literal at line 1, column 24
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, "Lexical error: Unterminated string error", details)


class UnterminatedCommentError(Error):
    """
    Raised when a comment is not properly terminated.
    """
    # Triggered when: A multi-line comment is started but not closed.

    # Example Code:
    # || This is an unterminated comment
    # Feint Main() { Announce("Hello World"); }

    # Error Message:
    # LexerError: Unterminated comment at line 1, column 1
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, "Lexical error: Unterminated comment error", details)


class OverflowError(Error):
    """
    Raised when a number exceeds allowable limits.
    """
    # Triggered when: A number exceeds the allowable range for numeric literals.
        
    # Example Code:
    # Feint Main() { Announce(99999999999999999999); }

    # Error Message:
    # LexerError: Overflow error with number '99999999999999999999' at line 1, column 23
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, "Lexical error: Overflow error", details)


class InvalidIdentifierError(Error):
    """
    Raised when an identifier is invalid.
    """
    # Triggered when: An identifier does not follow the rules for naming variables (e.g., it must start with @).
        
    # Example Code:
    # Feint Main() { Feint = 5; }

    # Error Message:
    # LexerError: Invalid identifier 'Feint' at line 1, column 13
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, "Lexical error: Invalid identifier error", details)