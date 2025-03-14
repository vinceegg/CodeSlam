class SemanticError:
    def __init__(self, error_message, line_number, column):
        self.error_message = error_message
        self.line_number = line_number
        self.column = column

    def __str__(self):
        return f"Semantic Error at line {self.line_number}, column {self.column}: {self.error_message}"

    def as_tuple(self):
        return (self.error_message, self.line_number, self.column)

def create_semantic_error(message, node):
    """Helper function to create a semantic error from an AST node"""
    # Extract line and column info from node if available
    line = node.get('line', 0)
    column = node.get('column', 0)
    return SemanticError(message, line, column)

class UndeclaredVariableError(SemanticError):
    """Error raised when a variable is used but not declared"""
    def __init__(self, var_name, line_number, column):
        super().__init__(f"Variable '{var_name}' is not declared", line_number, column)
        self.var_name = var_name

class TypeMismatchError(SemanticError):
    """Error raised when there's a type mismatch in an operation"""
    def __init__(self, expected_type, actual_type, line_number, column):
        super().__init__(f"Type mismatch: Expected {expected_type}, got {actual_type}", line_number, column)
        self.expected_type = expected_type
        self.actual_type = actual_type

class RedeclarationError(SemanticError):
    """Error raised when a variable is declared more than once in the same scope"""
    def __init__(self, var_name, line_number, column):
        super().__init__(f"Variable '{var_name}' is already declared in this scope", line_number, column)
        self.var_name = var_name

class UninitializedVariableError(SemanticError):
    """Error raised when a variable is used before initialization"""
    def __init__(self, var_name, line_number, column):
        super().__init__(f"Variable '{var_name}' is used before initialization", line_number, column)
        self.var_name = var_name 