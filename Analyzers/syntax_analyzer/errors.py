class SyntaxError(Exception):
    """Exception raised for syntax errors during parsing."""
    def __init__(self, message: str, line_number: int = 0, column: int = 0):
        super().__init__(message)
        self.line_number = line_number
        self.column = column
        
    def __str__(self):
        return f"{super().__str__()} at line {self.line_number}, column {self.column}"

    def as_tuple(self):
        return (str(self), self.line_number, self.column)