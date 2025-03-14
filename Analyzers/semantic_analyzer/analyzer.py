from Analyzers.lexical_analyzer.tokens import TokenType
from .errors import (
    SemanticError, 
    UndeclaredVariableError, 
    TypeMismatchError, 
    RedeclarationError,
    UninitializedVariableError
)

class SymbolTable:
    """Symbol table to track variables and their types"""
    def __init__(self, parent=None):
        self.symbols = {}  # Maps variable names to their info (type, initialized, etc.)
        self.parent = parent  # Parent scope for nested scopes
        
    def declare(self, name, data_type, initialized=False, is_global=False):
        """Declare a variable in the current scope"""
        if name in self.symbols:
            return False  # Already declared in this scope
        
        self.symbols[name] = {
            'type': data_type,
            'initialized': initialized,
            'is_global': is_global
        }
        return True
        
    def lookup(self, name):
        """Look up a variable in the current scope or parent scopes"""
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.lookup(name)
        return None
        
    def update(self, name, initialized=True):
        """Update a variable's initialization status"""
        if name in self.symbols:
            self.symbols[name]['initialized'] = initialized
            return True
        if self.parent:
            return self.parent.update(name)
        return False
        
    def get_type(self, name):
        """Get the type of a variable"""
        symbol = self.lookup(name)
        return symbol['type'] if symbol else None
        
    def is_initialized(self, name):
        """Check if a variable is initialized"""
        symbol = self.lookup(name)
        return symbol['initialized'] if symbol else False

class SemanticAnalyzer:
    """Analyzes the AST for semantic errors"""
    def __init__(self, ast):
        self.ast = ast
        self.errors = []
        self.global_scope = SymbolTable()  # Global scope
        self.current_scope = self.global_scope  # Current scope (starts at global)
        
        # Type compatibility for operations
        self.type_compatibility = {
            'FEINT': ['FEINT', 'FLOATER'],
            'FLOATER': ['FEINT', 'FLOATER'],
            'CHANT': ['CHANT'],
            'STAT': ['STAT']
        }
        
        # Valid types for operations
        self.valid_types = {
            'arithmetic': ['FEINT', 'FLOATER'],
            'logical': ['STAT'],
            'relational': ['FEINT', 'FLOATER', 'CHANT', 'STAT'],
            'concatenation': ['CHANT']
        }
        
    def analyze(self):
        """Analyze the AST for semantic errors"""
        if not self.ast:
            return []
            
        # Start analysis from the root node
        self.visit(self.ast)
        return self.errors
        
    def visit(self, node):
        """Visit a node in the AST"""
        if not node or not isinstance(node, dict):
            return None
            
        # Dispatch to the appropriate visitor method based on node type
        method_name = f"visit_{node.get('type', '')}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
        
    def generic_visit(self, node):
        """Generic visitor for nodes without specific visitors"""
        # Visit all children of the node
        for key, value in node.items():
            if isinstance(value, dict):
                self.visit(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.visit(item)
        return None
        
    def visit_program(self, node):
        """Visit the program node (root of the AST)"""
        # Visit global declarations
        for decl in node.get('global_declarations', []):
            self.visit(decl)
            
        # Visit function declarations
        for func_decl in node.get('function_declarations', []):
            self.visit(func_decl)
            
        # Visit function definitions
        for func_def in node.get('function_definitions', []):
            self.visit(func_def)
            
        # Visit the team block
        team_block = node.get('team_block')
        if team_block:
            self.visit(team_block)
            
        return None
        
    def visit_team_block(self, node):
        """Visit the team (main) block"""
        # Visit local declarations first
        for decl in node.get('local_declarations', []):
            self.visit(decl)
            
        # Then visit statements
        for statement in node.get('statements', []):
            self.visit(statement)
        return None
        
    def visit_variable_declaration(self, node):
        """Visit a variable declaration"""
        data_type = node.get('data_type')
        is_global = node.get('is_global', False)
        
        for decl in node.get('declarations', []):
            var_name = decl.get('name')
            value = decl.get('value')
            
            # Check if variable is already declared in current scope
            if not self.current_scope.declare(var_name, data_type, value is not None, is_global):
                self.errors.append(RedeclarationError(
                    var_name, 
                    node.get('line', 0), 
                    node.get('column', 0)
                ))
                
            # If there's an initialization value, check type compatibility
            if value:
                value_type = self.get_expression_type(value)
                if value_type and not self.is_type_compatible(data_type, value_type):
                    self.errors.append(TypeMismatchError(
                        data_type, 
                        value_type, 
                        node.get('line', 0), 
                        node.get('column', 0)
                    ))
        return None
        
    def visit_announce(self, node):
        """Visit an announce statement"""
        for arg in node.get('arguments', []):
            # If it's a concatenation, check the value
            if isinstance(arg, dict) and arg.get('type') == 'concatenation':
                self.check_announce_arg(arg.get('value'), node)
            else:
                self.check_announce_arg(arg, node)
        return None
        
    def check_announce_arg(self, arg, node):
        """Check an announce argument for semantic errors"""
        if isinstance(arg, dict):
            # If it's a variable reference, check if it's declared and initialized
            if arg.get('type') == 'variable':
                var_name = arg.get('name')
                if not self.current_scope.lookup(var_name):
                    self.errors.append(UndeclaredVariableError(
                        var_name, 
                        node.get('line', 0), 
                        node.get('column', 0)
                    ))
                elif not self.current_scope.is_initialized(var_name):
                    self.errors.append(UninitializedVariableError(
                        var_name, 
                        node.get('line', 0), 
                        node.get('column', 0)
                    ))
            # Recursively check other expression types
            else:
                self.visit(arg)
        return None
        
    def get_expression_type(self, expr):
        """Get the type of an expression"""
        if not expr or not isinstance(expr, dict):
            return None
            
        expr_type = expr.get('type')
        
        # Literal values
        if expr_type == 'literal':
            literal_type = expr.get('literal_type')
            if literal_type == 'FEINTLIT':
                return 'FEINT'
            elif literal_type == 'FLOATERLIT':
                return 'FLOATER'
            elif literal_type == 'CHANT_LIT':
                return 'CHANT'
            elif literal_type in ['WIN', 'LOSS']:
                return 'STAT'
                
        # Variable references
        elif expr_type == 'variable':
            var_name = expr.get('name')
            symbol = self.current_scope.lookup(var_name)
            if symbol:
                return symbol['type']
                
        # Binary operations
        elif expr_type == 'binary_operation':
            left_type = self.get_expression_type(expr.get('left'))
            right_type = self.get_expression_type(expr.get('right'))
            operator = expr.get('operator')
            
            # Arithmetic operations
            if operator in ['+', '-', '*', '/', '%']:
                if left_type in ['FEINT', 'FLOATER'] and right_type in ['FEINT', 'FLOATER']:
                    return 'FLOATER' if 'FLOATER' in [left_type, right_type] else 'FEINT'
                    
            # Relational operations
            elif operator in ['==', '!=', '<', '>', '<=', '>=']:
                return 'STAT'
                
            # Logical operations
            elif operator in ['&&', '||']:
                if left_type == 'STAT' and right_type == 'STAT':
                    return 'STAT'
                    
        # Unary operations
        elif expr_type == 'unary_operation':
            operand_type = self.get_expression_type(expr.get('operand'))
            operator = expr.get('operator')
            
            # Negation
            if operator == '-' and operand_type in ['FEINT', 'FLOATER']:
                return operand_type
                
            # Logical not
            elif operator == '!' and operand_type == 'STAT':
                return 'STAT'
                
        return None
        
    def is_type_compatible(self, expected_type, actual_type):
        """Check if two types are compatible"""
        if expected_type == actual_type:
            return True
            
        # Check compatibility based on the type_compatibility map
        if expected_type in self.type_compatibility:
            return actual_type in self.type_compatibility[expected_type]
            
        return False
        
    def visit_assignment(self, node):
        """Visit an assignment statement"""
        # Handle direct assignment structure from parser
        if 'name' in node and 'target' not in node:
            var_name = node.get('name')
            value = node.get('value')
            
            # Check if variable exists
            symbol = self.current_scope.lookup(var_name)
            
            if not symbol:
                self.errors.append(UndeclaredVariableError(
                    var_name, 
                    node.get('line', 0), 
                    node.get('column', 0)
                ))
                return None
                
            # Check type compatibility
            target_type = symbol['type']
            value_type = self.get_expression_type(value)
            
            if value_type and not self.is_type_compatible(target_type, value_type):
                self.errors.append(TypeMismatchError(
                    target_type, 
                    value_type, 
                    node.get('line', 0), 
                    node.get('column', 0)
                ))
                
            # Mark variable as initialized
            self.current_scope.update(var_name, True)
            return None
        
        # Handle nested target structure
        target = node.get('target')
        value = node.get('value')
        
        # Check if target is None
        if target is None:
            self.errors.append(SemanticError(
                "Invalid assignment target",
                node.get('line', 0),
                node.get('column', 0)
            ))
            return None
        
        # Check if target variable exists
        if target.get('type') == 'variable':
            var_name = target.get('name')
            symbol = self.current_scope.lookup(var_name)
            
            if not symbol:
                self.errors.append(UndeclaredVariableError(
                    var_name, 
                    node.get('line', 0), 
                    node.get('column', 0)
                ))
                return None
                
            # Check type compatibility
            target_type = symbol['type']
            value_type = self.get_expression_type(value)
            
            if value_type and not self.is_type_compatible(target_type, value_type):
                self.errors.append(TypeMismatchError(
                    target_type, 
                    value_type, 
                    node.get('line', 0), 
                    node.get('column', 0)
                ))
                
            # Mark variable as initialized
            self.current_scope.update(var_name, True)
            
        return None
        
    def visit_binary_operation(self, node):
        """Visit a binary operation"""
        left = node.get('left')
        right = node.get('right')
        operator = node.get('operator')
        
        # Get types of operands
        left_type = self.get_expression_type(left)
        right_type = self.get_expression_type(right)
        
        # Check if operands are valid for the operation
        if operator in ['+', '-', '*', '/', '%']:
            # Arithmetic operations require numeric types
            if left_type not in ['FEINT', 'FLOATER'] or right_type not in ['FEINT', 'FLOATER']:
                self.errors.append(SemanticError(
                    f"Arithmetic operation '{operator}' requires numeric operands, got {left_type} and {right_type}",
                    node.get('line', 0),
                    node.get('column', 0)
                ))
                
        elif operator in ['&&', '||']:
            # Logical operations require boolean types
            if left_type != 'STAT' or right_type != 'STAT':
                self.errors.append(SemanticError(
                    f"Logical operation '{operator}' requires STAT operands, got {left_type} and {right_type}",
                    node.get('line', 0),
                    node.get('column', 0)
                ))
                
        elif operator in ['==', '!=', '<', '>', '<=', '>=']:
            # Relational operations require compatible types
            if not self.is_type_compatible(left_type, right_type):
                self.errors.append(SemanticError(
                    f"Relational operation '{operator}' requires compatible operands, got {left_type} and {right_type}",
                    node.get('line', 0),
                    node.get('column', 0)
                ))
                
        return None
        
    def visit_unary_operation(self, node):
        """Visit a unary operation"""
        operand = node.get('operand')
        operator = node.get('operator')
        
        # Get type of operand
        operand_type = self.get_expression_type(operand)
        
        # Check if operand is valid for the operation
        if operator == '-':
            # Negation requires numeric type
            if operand_type not in ['FEINT', 'FLOATER']:
                self.errors.append(SemanticError(
                    f"Unary operation '{operator}' requires numeric operand, got {operand_type}",
                    node.get('line', 0),
                    node.get('column', 0)
                ))
                
        elif operator == '!':
            # Logical not requires boolean type
            if operand_type != 'STAT':
                self.errors.append(SemanticError(
                    f"Unary operation '{operator}' requires STAT operand, got {operand_type}",
                    node.get('line', 0),
                    node.get('column', 0)
                ))
                
        return None
        
    def visit_variable(self, node):
        """Visit a variable reference"""
        var_name = node.get('name')
        symbol = self.current_scope.lookup(var_name)
        
        if not symbol:
            self.errors.append(UndeclaredVariableError(
                var_name, 
                node.get('line', 0), 
                node.get('column', 0)
            ))
        elif not symbol['initialized']:
            self.errors.append(UninitializedVariableError(
                var_name, 
                node.get('line', 0), 
                node.get('column', 0)
            ))
            
        return None
        
    def visit_code_block(self, node):
        """Visit a code block and create a new scope"""
        # Create a new scope for the block
        previous_scope = self.current_scope
        self.current_scope = SymbolTable(previous_scope)
        
        # Visit all statements in the block
        for statement in node.get('statements', []):
            self.visit(statement)
            
        # Restore the previous scope
        self.current_scope = previous_scope
        return None
        
    def visit_function_declaration(self, node):
        """Visit a function declaration"""
        func_name = node.get('name')
        return_type = node.get('return_type')
        parameters = node.get('parameters', [])
        
        # Create a new scope for the function
        previous_scope = self.current_scope
        self.current_scope = SymbolTable(previous_scope)
        
        # Add parameters to the function scope
        for param in parameters:
            param_name = param.get('name')
            param_type = param.get('type')
            self.current_scope.declare(param_name, param_type, True)
            
        # Visit the function body
        body = node.get('body')
        if body:
            self.visit(body)
            
        # Restore the previous scope
        self.current_scope = previous_scope
        return None
        
    def visit_function_call(self, node):
        """Visit a function call"""
        func_name = node.get('name')
        arguments = node.get('arguments', [])
        
        # Check if function exists (simplified for now)
        # In a real implementation, you would check against declared functions
        
        # Check argument types (simplified for now)
        for arg in arguments:
            self.visit(arg)
            
        return None
        
    def visit_if_statement(self, node):
        """Visit an if statement"""
        condition = node.get('condition')
        then_branch = node.get('then_branch')
        else_branch = node.get('else_branch')
        
        # Check if condition is a boolean expression
        condition_type = self.get_expression_type(condition)
        if condition_type != 'STAT':
            self.errors.append(SemanticError(
                f"If condition must be a STAT expression, got {condition_type}",
                node.get('line', 0),
                node.get('column', 0)
            ))
            
        # Visit then branch
        if then_branch:
            self.visit(then_branch)
            
        # Visit else branch if present
        if else_branch:
            self.visit(else_branch)
            
        return None
        
    def visit_while_statement(self, node):
        """Visit a while statement"""
        condition = node.get('condition')
        body = node.get('body')
        
        # Check if condition is a boolean expression
        condition_type = self.get_expression_type(condition)
        if condition_type != 'STAT':
            self.errors.append(SemanticError(
                f"While condition must be a STAT expression, got {condition_type}",
                node.get('line', 0),
                node.get('column', 0)
            ))
            
        # Visit body
        if body:
            self.visit(body)
            
        return None
        
    def visit_for_statement(self, node):
        """Visit a for statement"""
        initialization = node.get('initialization')
        condition = node.get('condition')
        update = node.get('update')
        body = node.get('body')
        
        # Create a new scope for the for loop
        previous_scope = self.current_scope
        self.current_scope = SymbolTable(previous_scope)
        
        # Visit initialization
        if initialization:
            self.visit(initialization)
            
        # Check if condition is a boolean expression
        if condition:
            condition_type = self.get_expression_type(condition)
            if condition_type != 'STAT':
                self.errors.append(SemanticError(
                    f"For condition must be a STAT expression, got {condition_type}",
                    node.get('line', 0),
                    node.get('column', 0)
                ))
                
        # Visit update
        if update:
            self.visit(update)
            
        # Visit body
        if body:
            self.visit(body)
            
        # Restore the previous scope
        self.current_scope = previous_scope
        return None

def analyze(ast):
    """Analyze the AST for semantic errors"""
    analyzer = SemanticAnalyzer(ast)
    errors = analyzer.analyze()
    return errors if errors else None 