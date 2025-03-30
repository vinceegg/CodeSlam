class SyntaxError:
    def __init__(self, error_message, line_number, column):
        self.error_message = error_message
        self.line_number = line_number
        self.column = column

    def __str__(self):
        return f"Syntax Error at line {self.line_number}, column {self.column}: {self.error_message}"

    def as_tuple(self):
        return (self.error_message, self.line_number, self.column)

def create_syntax_error(message, token):
    """Helper function to create a syntax error from a token"""
    # Extract line and column info from token position if available
    line = getattr(token, 'line', 0)
    column = getattr(token, 'column', 0)
    return SyntaxError(message, line, column) 