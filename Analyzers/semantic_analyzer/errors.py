class SemanticError:
    def __init__(self, error_message, line_number, column=0):
        self.error_message = error_message
        self.line_number = line_number
        self.column = column

    def __str__(self):
        return f"Semantic Error at line {self.line_number}, column {self.column}: {self.error_message}"

    def as_tuple(self):
        return (self.error_message, self.line_number, self.column)

def create_semantic_error(message, line_number, column=0):
    """Helper function to create a semantic error"""
    return SemanticError(message, line_number, column)

# Common semantic error types
def undefined_variable_error(variable_name, line_number, column=0):
    return SemanticError(f"Undefined variable '{variable_name}'", line_number, column)

def type_mismatch_error(expected_type, actual_type, line_number, column=0):
    return SemanticError(f"Type mismatch: Expected '{expected_type}', got '{actual_type}'", line_number, column)

def already_defined_error(name, line_number, column=0):
    return SemanticError(f"Identifier '{name}' is already defined in this scope", line_number, column)

def invalid_operation_error(operation, type1, type2, line_number, column=0):
    return SemanticError(f"Invalid operation '{operation}' between types '{type1}' and '{type2}'", line_number, column)

def undefined_function_error(function_name, line_number, column=0):
    return SemanticError(f"Undefined function '{function_name}'", line_number, column)

def argument_count_error(function_name, expected, actual, line_number, column=0):
    return SemanticError(f"Function '{function_name}' expects {expected} arguments but got {actual}", line_number, column)

def invalid_array_index_error(line_number, column=0):
    return SemanticError(f"Array index must be an integer", line_number, column)

def array_dimension_error(expected, actual, line_number, column=0):
    return SemanticError(f"Array access with wrong number of dimensions: Expected {expected}, got {actual}", line_number, column)

def non_array_error(name, line_number, column=0):
    return SemanticError(f"Variable '{name}' is not an array", line_number, column)

def constant_assignment_error(name, line_number, column=0):
    return SemanticError(f"Cannot reassign constant '{name}'", line_number, column)

def invalid_return_error(expected_type, actual_type, line_number, column=0):
    return SemanticError(f"Invalid return type: Expected '{expected_type}', got '{actual_type}'", line_number, column)

def missing_return_error(function_name, line_number, column=0):
    return SemanticError(f"Function '{function_name}' must return a value", line_number, column) 