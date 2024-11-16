#errors.py
class LexerError(Exception):
    """
    Base class for lexer-related errors.
    """
    def __init__(self, message, line, column):
        super().__init__(f"LexerError: {message} at line {line}, column {column}")
        self.message = message
        self.line = line
        self.column = column


class IllegalCharError(LexerError):
    """
    Raised when an illegal character is encountered.
    """
    def __init__(self, char, line, column):
        message = f"Illegal character '{char}'"
        super().__init__(message, line, column)


class UnterminatedStringError(LexerError):
    """
    Raised when a string literal is not properly terminated.
    """
    def __init__(self, line, column):
        message = "Unterminated string literal"
        super().__init__(message, line, column)


class InvalidNumberError(LexerError):
    """
    Raised when a number literal is invalid.
    """
    def __init__(self, number, line, column):
        message = f"Invalid number '{number}'"
        super().__init__(message, line, column)


class UnterminatedCommentError(LexerError):
    """
    Raised when a comment is not properly terminated.
    """
    def __init__(self, line, column):
        message = "Unterminated comment"
        super().__init__(message, line, column)


class OverflowError(LexerError):
    """
    Raised when a number exceeds allowable limits.
    """
    def __init__(self, number, line, column):
        message = f"Overflow error with number '{number}'"
        super().__init__(message, line, column)


class InvalidIdentifierError(LexerError):
    """
    Raised when an identifier is invalid.
    """
    def __init__(self, identifier, line, column):
        message = f"Invalid identifier '{identifier}'"
        super().__init__(message, line, column)