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
    # Extract line and column from the node
    if isinstance(node, dict):
        line = node.get('line', 1)  # Default to line 1 instead of 0
        column = node.get('column', 0)
        
        # If node has a name attribute, adjust column to point to the identifier
        if 'name' in node:
            column = node.get('name_column', column)
    else:
        line = 1
        column = 0
    
    return SemanticError(message, line, column) 