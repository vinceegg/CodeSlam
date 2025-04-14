class SyntaxError(Exception):
    """Custom exception for syntax errors"""
    def __init__(self, message, line_number=None, column=None, expected=None, token=None, nonterminal=None, production_rule=None):
        super().__init__(message)
        self.line_number = line_number
        self.column = column
        self.expected = expected
        self.token = token
        self.nonterminal = nonterminal
        self.production_rule = production_rule

    def __str__(self):
        return self.args[0]  # Return the formatted error message

    def as_tuple(self):
        return (self.error_message, self.line_number, self.column)