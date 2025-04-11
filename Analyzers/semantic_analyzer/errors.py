class SemanticError(Exception):
    """Base class for all semantic analyzer errors"""
    
    def __init__(self, message, line_number=None, column=None):
        super().__init__(message)
        self.message = message
        self.line_number = line_number
        self.column = column
    
    def __str__(self):
        if self.line_number is not None and self.column is not None:
            return f"Semantic Error at line {self.line_number}, column {self.column}: {self.message}"
        return f"Semantic Error: {self.message}"

class UndeclaredVariableError(SemanticError):
    """Error raised when an undeclared variable is used"""
    
    def __init__(self, variable_name, line_number=None, column=None):
        super().__init__(f"Undeclared variable '{variable_name}'", line_number, column)
        self.variable_name = variable_name

class TypeMismatchError(SemanticError):
    """Error raised when there is a type mismatch in an operation"""
    
    def __init__(self, expected_type, actual_type, line_number=None, column=None):
        super().__init__(
            f"Type mismatch: Expected {expected_type}, got {actual_type}", 
            line_number, column
        )
        self.expected_type = expected_type
        self.actual_type = actual_type

class RedeclarationError(SemanticError):
    """Error raised when a variable is declared more than once"""
    
    def __init__(self, variable_name, line_number=None, column=None):
        super().__init__(f"Variable '{variable_name}' already declared", line_number, column)
        self.variable_name = variable_name

class OperationError(SemanticError):
    """Error raised when an invalid operation is performed"""
    
    def __init__(self, operation, types, line_number=None, column=None):
        super().__init__(
            f"Invalid operation '{operation}' for types {types}", 
            line_number, column
        )
        self.operation = operation
        self.types = types 