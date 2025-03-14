class Symbol:
    """Base class for all symbols in the symbol table"""
    def __init__(self, name, symbol_type, line_number=None):
        self.name = name
        self.type = symbol_type
        self.line_number = line_number  # Where the symbol was defined

class VariableSymbol(Symbol):
    """Symbol representing a variable"""
    def __init__(self, name, var_type, is_constant=False, dimensions=None, line_number=None, column=None):
        super().__init__(name, "variable", line_number)
        self.var_type = var_type  # FEINT, FLOATER, CHANT, STAT
        self.is_constant = is_constant
        self.dimensions = dimensions or []  # For arrays, list of dimensions
        self.column = column
        self.initialized = False  # Track if the variable has been initialized

class FunctionSymbol(Symbol):
    """Symbol representing a function"""
    def __init__(self, name, return_type, parameters=None, line_number=None, column=None):
        super().__init__(name, "function", line_number)
        self.return_type = return_type  # FEINT, FLOATER, CHANT, STAT, DUNK (void)
        self.parameters = parameters or []  # List of VariableSymbol for parameters
        self.column = column
        self.is_defined = False  # Track if the function is declared or defined

class SymbolTable:
    """Symbol table for managing variable and function symbols"""
    def __init__(self, parent=None):
        self.symbols = {}  # Maps names to Symbol objects
        self.parent = parent  # Parent scope for nested scopes
        
    def define(self, symbol):
        """Add a symbol to the table"""
        self.symbols[symbol.name] = symbol
        return symbol
        
    def lookup(self, name, current_scope_only=False):
        """Look up a symbol by name, optionally searching parent scopes"""
        if name in self.symbols:
            return self.symbols[name]
            
        if not current_scope_only and self.parent:
            return self.parent.lookup(name)
            
        return None
        
    def is_defined(self, name, current_scope_only=False):
        """Check if a symbol is defined, optionally in the current scope only"""
        return self.lookup(name, current_scope_only) is not None

class SemanticAnalyzer:
    """Helper class to track current scope and manage symbol tables"""
    def __init__(self):
        # Global scope
        self.global_scope = SymbolTable()
        self.current_scope = self.global_scope
        self.scopes_stack = [self.global_scope]
        
    def enter_scope(self):
        """Enter a new scope"""
        new_scope = SymbolTable(self.current_scope)
        self.scopes_stack.append(new_scope)
        self.current_scope = new_scope
        return new_scope
        
    def exit_scope(self):
        """Exit the current scope"""
        if len(self.scopes_stack) > 1:
            self.scopes_stack.pop()
            self.current_scope = self.scopes_stack[-1]
        return self.current_scope
            
    def define_symbol(self, symbol):
        """Define a symbol in the current scope"""
        return self.current_scope.define(symbol)
        
    def lookup_symbol(self, name, current_scope_only=False):
        """Look up a symbol by name"""
        return self.current_scope.lookup(name, current_scope_only)
        
    def is_symbol_defined(self, name, current_scope_only=False):
        """Check if a symbol is defined"""
        return self.current_scope.is_defined(name, current_scope_only)

    # Helper methods for type checking
    @staticmethod
    def is_numeric_type(type_name):
        """Check if a type is numeric"""
        if not type_name:
            return False
        
        type_upper = type_name.upper()
        return type_upper in ['FEINT', 'FLOATER']
        
    @staticmethod
    def is_string_type(type_name):
        """Check if a type is a string"""
        if not type_name:
            return False
            
        type_upper = type_name.upper()
        return type_upper == 'CHANT'
        
    @staticmethod
    def is_boolean_type(type_name):
        """Check if a type is a boolean"""
        if not type_name:
            return False
            
        type_upper = type_name.upper()
        return type_upper == 'STAT'
        
    @staticmethod
    def get_result_type(left_type, right_type, operator):
        """Get the result type of a binary operation"""
        # Handle null types
        if not left_type or not right_type:
            return None
            
        # Convert types to uppercase for consistent comparison
        left_upper = left_type.upper()
        right_upper = right_type.upper()
            
        # Arithmetic operations
        if operator in ['+', '-', '*', '/', '%']:
            if left_upper in ['FEINT', 'FLOATER'] and right_upper in ['FEINT', 'FLOATER']:
                # If either is FLOATER, result is FLOATER
                if 'FLOATER' in [left_upper, right_upper]:
                    return 'Floater'
                # Otherwise both are FEINT, result is FEINT
                return 'Feint'
            return None
            
        # String concatenation
        if operator == '&':
            if 'CHANT' in [left_upper, right_upper]:
                return 'Chant'
            return None
            
        # Comparison operations
        if operator in ['==', '!=', '<', '>', '<=', '>=']:
            # Numeric types can be compared
            if left_upper in ['FEINT', 'FLOATER'] and right_upper in ['FEINT', 'FLOATER']:
                return 'Stat'
            # Strings can be compared
            if left_upper == 'CHANT' and right_upper == 'CHANT':
                return 'Stat'
            # Booleans can be compared
            if left_upper == 'STAT' and right_upper == 'STAT':
                return 'Stat'
            return None
            
        # Logical operations
        if operator in ['&&', '||']:
            if left_upper == 'STAT' and right_upper == 'STAT':
                return 'Stat'
            return None
            
        return None 