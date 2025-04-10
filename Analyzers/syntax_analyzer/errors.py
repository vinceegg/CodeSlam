
class SyntaxError(Exception):
    """Exception raised for syntax errors during parsing."""
    
    def __init__(self, message, line_number, column, expected=None, token=None, nonterminal=None, production_rule=None):
        self.message = message
        self.line_number = line_number
        self.column = column
        self.expected = expected
        self.token = token
        self.nonterminal = nonterminal
        self.production_rule = production_rule
        super().__init__(self.message)
    
    def __str__(self):
        return self.message