from Analyzers.lexical_analyzer.tokens import TokenType
from .errors import (
    SemanticError, undefined_variable_error, type_mismatch_error, 
    already_defined_error, invalid_operation_error, undefined_function_error,
    argument_count_error, invalid_array_index_error, array_dimension_error,
    non_array_error, constant_assignment_error, invalid_return_error,
    missing_return_error
)
from .symbol_table import (
    SemanticAnalyzer, SymbolTable, Symbol, VariableSymbol, FunctionSymbol
)

class AstVisitor:
    """Base visitor class for traversing the AST"""
    def __init__(self, semantic_analyzer=None):
        self.semantic_analyzer = semantic_analyzer or SemanticAnalyzer()
        self.errors = []
        # Track current function for return type checking
        self.current_function = None
        # Track if we've seen a return statement
        self.has_return = False
        
    def add_error(self, error):
        """Add an error to the list"""
        self.errors.append(error)
        
    def visit(self, node):
        """Visit a node in the AST"""
        if not node:
            return None
            
        method_name = f"visit_{node.get('type', '')}"
        visitor = getattr(self, method_name, None)
        
        if visitor:
            return visitor(node)
        else:
            # If no specific visitor method exists, use generic_visit
            return self.generic_visit(node)
        
    def generic_visit(self, node):
        """Default visitor method"""
        # Process children recursively
        if isinstance(node, dict):
            for key, value in node.items():
                if key == 'type':
                    continue
                    
                if isinstance(value, dict):
                    self.visit(value)
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            self.visit(item)
        return None
        
    def visit_program(self, node):
        """Visit the program node (top-level node in the AST)"""
        print(f"DEBUG: Visiting program node with keys: {node.keys()}")
        
        # The team block is the main part of the program
        if 'team_block' in node:
            self.visit(node['team_block'])
        
        return None
        
    def visit_team_block(self, node):
        """Visit the main team block - handles all declarations and statements"""
        print(f"DEBUG: Visiting team_block with keys: {node.keys()}")
        print(f"DEBUG: Full team_block node: {node}")
        
        # Process all variable declarations first
        if 'local_declarations' in node:
            if isinstance(node['local_declarations'], list):
                for decl in node['local_declarations']:
                    print(f"DEBUG: Processing local declaration: {decl}")
                    self.visit(decl)
            else:
                print(f"DEBUG: Processing single local declaration: {node['local_declarations']}")
                self.visit(node['local_declarations'])
        
        # Then process statements which might reference those variables
        if 'statements' in node:
            if isinstance(node['statements'], list):
                for stmt in node['statements']:
                    print(f"DEBUG: Processing statement: {stmt}")
                    self.visit(stmt)
            else:
                print(f"DEBUG: Processing single statement: {node['statements']}")
                self.visit(node['statements'])
        
        # Handle any remaining sections
        for key, value in node.items():
            if key not in ['type', 'local_declarations', 'statements']:
                if isinstance(value, list):
                    for item in value:
                        self.visit(item)
                elif isinstance(value, dict):
                    self.visit(value)
                    
        return None
        
    def visit_unknown(self, node):
        """Visit an unknown node type (handles special syntax structure)"""
        # Extract variable name and value
        var_name = node.get('name')
        value = node.get('value')
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # If this is a variable declaration part
        if var_name and var_name.startswith('@'):
            # Handle initializer if present
            if value is not None:
                self.visit(value)
                
        return None
        
    def visit_variable_declaration(self, node):
        """Visit a variable declaration"""
        print(f"DEBUG: Visiting variable declaration: {node}")
        
        # Get the data type
        var_type = node.get('data_type')
        
        # Get line info
        line_number = node.get('line_number', node.get('line', 0))
        column = node.get('column', 0)
        is_constant = node.get('is_constant', False)
        
        # Try direct variable name in the node
        var_name = node.get('name')
        if var_name and var_name.startswith('@'):
            print(f"DEBUG: Found variable name directly: {var_name}")
            
            # Create and register the variable
            dimensions = []
            var_symbol = VariableSymbol(var_name, var_type, is_constant, dimensions, line_number, column)
            self.semantic_analyzer.define_symbol(var_symbol)
            print(f"DEBUG: Defined symbol: {var_name} of type {var_type}")
            
            # Process initializer if present
            value = node.get('value')
            if value is not None:
                # Check type compatibility
                initializer_type = self.get_expression_type(value)
                print(f"DEBUG: Variable type: {var_type}, Initializer type: {initializer_type}")
                
                # Case-insensitive comparison
                if initializer_type and var_type.upper() != initializer_type.upper():
                    self.add_error(type_mismatch_error(var_type, initializer_type, line_number, column))
                
                self.visit(value)
            
            return None
        
        # Try 'declarations' field
        declarations = node.get('declarations', [])
        if declarations:
            if isinstance(declarations, list):
                for decl in declarations:
                    self.process_declaration_item(decl, var_type, line_number, column, is_constant)
            else:
                self.process_declaration_item(declarations, var_type, line_number, column, is_constant)
            return None
        
        # Try looking at each field for possible nested variable declarations
        for key, value in node.items():
            if key not in ['type', 'data_type', 'line_number', 'line', 'column', 'is_constant']:
                if isinstance(value, dict):
                    var_name = value.get('name')
                    if var_name and var_name.startswith('@'):
                        print(f"DEBUG: Found variable in nested field {key}: {var_name}")
                        dimensions = []
                        var_symbol = VariableSymbol(var_name, var_type, is_constant, dimensions, line_number, column)
                        self.semantic_analyzer.define_symbol(var_symbol)
                        print(f"DEBUG: Defined symbol from nested field: {var_name} of type {var_type}")
                        
                        # Process initializer if present
                        init_value = value.get('value')
                        if init_value is not None:
                            # Check type compatibility with case-insensitivity
                            initializer_type = self.get_expression_type(init_value)
                            if initializer_type and var_type.upper() != initializer_type.upper():
                                self.add_error(type_mismatch_error(var_type, initializer_type, line_number, column))
                                
                            self.visit(init_value)
        
        return None
        
    def process_declaration_item(self, decl, var_type, line_number, column, is_constant):
        """Process a single declaration item (helper for visit_variable_declaration)"""
        print(f"DEBUG: Processing declaration item: {decl}")
        
        # Handle 'unknown' type nodes
        if isinstance(decl, dict):
            var_name = decl.get('name')
            if var_name and var_name.startswith('@'):
                print(f"DEBUG: Found variable in declaration item: {var_name}")
                dimensions = []
                var_symbol = VariableSymbol(var_name, var_type, is_constant, dimensions, line_number, column)
                self.semantic_analyzer.define_symbol(var_symbol)
                print(f"DEBUG: Defined symbol from declaration: {var_name} of type {var_type}")
                
                # Process initializer if present
                value = decl.get('value')
                if value is not None:
                    # Check type compatibility with case-insensitivity
                    initializer_type = self.get_expression_type(value)
                    print(f"DEBUG: Variable type: {var_type}, Initializer type: {initializer_type}")
                    
                    if initializer_type and var_type.upper() != initializer_type.upper():
                        self.add_error(type_mismatch_error(var_type, initializer_type, line_number, column))
                    
                    self.visit(value)
            elif decl.get('type'):
                # Recursive for nested structures
                self.visit(decl)
        
    def visit_function_declaration(self, node):
        """Visit a function declaration"""
        func_name = node.get('name')
        return_type = node.get('return_type')
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # Check if function is already defined
        if self.semantic_analyzer.is_symbol_defined(func_name, current_scope_only=True):
            self.add_error(already_defined_error(func_name, line_number, column))
            return None
            
        # Process parameters
        parameters = []
        for param in node.get('parameters', []):
            param_name = param.get('name')
            param_type = param.get('param_type')
            param_line = param.get('line_number', line_number)
            param_col = param.get('column', column)
            
            param_symbol = VariableSymbol(param_name, param_type, False, [], param_line, param_col)
            parameters.append(param_symbol)
            
        # Create a function symbol
        func_symbol = FunctionSymbol(func_name, return_type, parameters, line_number, column)
        
        # Add to symbol table
        self.semantic_analyzer.define_symbol(func_symbol)
        
        return None
        
    def visit_function_definition(self, node):
        """Visit a function definition"""
        func_name = node.get('name')
        return_type = node.get('return_type')
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # Look up the function
        func_symbol = self.semantic_analyzer.lookup_symbol(func_name)
        
        if not func_symbol:
            # If not declared, create a new function symbol
            parameters = []
            for param in node.get('parameters', []):
                param_name = param.get('name')
                param_type = param.get('param_type')
                param_line = param.get('line_number', line_number)
                param_col = param.get('column', column)
                
                param_symbol = VariableSymbol(param_name, param_type, False, [], param_line, param_col)
                parameters.append(param_symbol)
                
            func_symbol = FunctionSymbol(func_name, return_type, parameters, line_number, column)
            self.semantic_analyzer.define_symbol(func_symbol)
        else:
            # Check if return types match for function declaration and definition
            if func_symbol.return_type != return_type:
                self.add_error(type_mismatch_error(func_symbol.return_type, return_type, line_number, column))
                
            # Check if parameters match
            func_params = func_symbol.parameters
            def_params = node.get('parameters', [])
            
            if len(func_params) != len(def_params):
                self.add_error(argument_count_error(
                    func_name, len(func_params), len(def_params), line_number, column
                ))
            else:
                for i, (func_param, def_param) in enumerate(zip(func_params, def_params)):
                    if func_param.var_type != def_param.get('param_type'):
                        self.add_error(type_mismatch_error(
                            func_param.var_type, def_param.get('param_type'), 
                            def_param.get('line_number', line_number), 
                            def_param.get('column', column)
                        ))
        
        # Mark the function as defined
        func_symbol.is_defined = True
        
        # Enter a new scope for the function body
        self.semantic_analyzer.enter_scope()
        
        # Add parameters to the function scope
        for param in node.get('parameters', []):
            param_name = param.get('name')
            param_type = param.get('param_type')
            param_line = param.get('line_number', line_number)
            param_col = param.get('column', column)
            
            param_symbol = VariableSymbol(param_name, param_type, False, [], param_line, param_col)
            self.semantic_analyzer.define_symbol(param_symbol)
            
        # Store current function for return type checking
        prev_function = self.current_function
        self.current_function = func_symbol
        
        # Reset return flag
        prev_has_return = self.has_return
        self.has_return = False
        
        # Visit the function body
        if 'body' in node:
            if isinstance(node['body'], list):
                for stmt in node['body']:
                    self.visit(stmt)
            else:
                self.visit(node['body'])
            
        # Check if function has a return statement if needed
        if func_symbol.return_type != "DUNK" and not self.has_return:
            self.add_error(missing_return_error(func_name, line_number))
            
        # Restore previous function and return flag
        self.current_function = prev_function
        self.has_return = prev_has_return
        
        # Exit the function scope
        self.semantic_analyzer.exit_scope()
        
        return None
        
    def visit_rebound(self, node):
        """Visit a return statement"""
        # Set the return flag
        self.has_return = True
        
        # Check if expression matches function return type
        if 'expression' in node and self.current_function:
            expr = node['expression']
            expr_type = self.get_expression_type(expr)
            expected_type = self.current_function.return_type
            line_number = node.get('line_number', 0)
            column = node.get('column', 0)
            
            if expr_type and expr_type != expected_type:
                self.add_error(invalid_return_error(expected_type, expr_type, line_number, column))
                
            # Visit the expression
            self.visit(expr)
            
        return None
        
    def visit_assignment(self, node):
        """Visit an assignment statement"""
        target_name = node.get('name')
        value = node.get('value')
        operator = node.get('operator', '=')
        line_number = node.get('line_number', 0)
        if not line_number:
            line_number = node.get('line', 0)
        column = node.get('column', 0)
        
        print(f"DEBUG: Assignment: {target_name} = {value} at line {line_number}")
        
        # Look up the target variable
        var_symbol = self.semantic_analyzer.lookup_symbol(target_name)
        
        if not var_symbol:
            self.add_error(undefined_variable_error(target_name, line_number, column))
        else:
            # Check if variable is constant
            if var_symbol.is_constant:
                self.add_error(constant_assignment_error(target_name, line_number, column))
                
            # Get expression type
            expr_type = self.get_expression_type(value)
            print(f"DEBUG: Variable type: {var_symbol.var_type}, Expression type: {expr_type}")
            
            # Make case-insensitive comparison
            if expr_type and var_symbol.var_type.upper() != expr_type.upper():
                self.add_error(type_mismatch_error(var_symbol.var_type, expr_type, line_number, column))
                
            # Mark the variable as initialized
            var_symbol.initialized = True
            
        # Visit the value
        self.visit(value)
        
        return None
        
    def visit_binary_operation(self, node):
        """Visit a binary operation"""
        left = node.get('left')
        right = node.get('right')
        operator = node.get('operator')
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # Get operand types
        left_type = self.get_expression_type(left)
        right_type = self.get_expression_type(right)
        
        # Skip if types couldn't be determined
        if not left_type or not right_type:
            # Visit children
            self.visit(left)
            self.visit(right)
            return None
            
        # Check type compatibility for the operation
        result_type = SemanticAnalyzer.get_result_type(left_type, right_type, operator)
        
        if not result_type:
            self.add_error(invalid_operation_error(operator, left_type, right_type, line_number, column))
            
        # Visit children
        self.visit(left)
        self.visit(right)
        
        return None
        
    def visit_unary_operation(self, node):
        """Visit a unary operation"""
        operand = node.get('operand')
        operator = node.get('operator')
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # Get operand type
        operand_type = self.get_expression_type(operand)
        
        # Skip if type couldn't be determined
        if not operand_type:
            self.visit(operand)
            return None
            
        # Check type compatibility for the operation
        if operator == '-' and not SemanticAnalyzer.is_numeric_type(operand_type):
            self.add_error(invalid_operation_error(operator, operand_type, None, line_number, column))
        elif operator == '!' and not SemanticAnalyzer.is_boolean_type(operand_type):
            self.add_error(invalid_operation_error(operator, operand_type, None, line_number, column))
            
        # Visit children
        self.visit(operand)
        
        return None
        
    def visit_function_call(self, node):
        """Visit a function call"""
        func_name = node.get('name')
        arguments = node.get('arguments', [])
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # Look up the function
        func_symbol = self.semantic_analyzer.lookup_symbol(func_name)
        
        if not func_symbol:
            self.add_error(undefined_function_error(func_name, line_number, column))
            
            # Still visit arguments
            for arg in arguments:
                self.visit(arg)
                
            return None
            
        # Check argument count
        if len(arguments) != len(func_symbol.parameters):
            self.add_error(argument_count_error(
                func_name, len(func_symbol.parameters), len(arguments), line_number, column
            ))
        else:
            # Check argument types
            for i, (param, arg) in enumerate(zip(func_symbol.parameters, arguments)):
                arg_type = self.get_expression_type(arg)
                
                if arg_type and arg_type != param.var_type:
                    self.add_error(type_mismatch_error(
                        param.var_type, arg_type, node.get('line_number', line_number), column
                    ))
                    
        # Visit arguments
        for arg in arguments:
            self.visit(arg)
            
        return None
        
    def visit_variable(self, node):
        """Visit a variable reference"""
        var_name = node.get('name')
        
        # Normalize line number detection
        line_number = node.get('line_number', node.get('line', 0))
        column = node.get('column', 0)
        
        # Print debug info
        print(f"DEBUG: Visiting variable: {var_name} at line {line_number}, column {column}")
        
        # Look up the variable
        var_symbol = self.semantic_analyzer.lookup_symbol(var_name)
        
        if not var_symbol:
            print(f"DEBUG: Symbol not found: {var_name}")
            self.add_error(undefined_variable_error(var_name, line_number, column))
        else:
            print(f"DEBUG: Symbol found: {var_name}, type: {var_symbol.var_type}")
            
        return None
        
    def visit_array_element(self, node):
        """Visit an array element access"""
        array_name = node.get('array_name')
        indices = node.get('indices', [])
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # Look up the array
        array_symbol = self.semantic_analyzer.lookup_symbol(array_name)
        
        if not array_symbol:
            self.add_error(undefined_variable_error(array_name, line_number, column))
        else:
            # Check if variable is an array
            if not array_symbol.dimensions:
                self.add_error(non_array_error(array_name, line_number, column))
                
            # Check dimensions
            if len(indices) != len(array_symbol.dimensions):
                self.add_error(array_dimension_error(
                    len(array_symbol.dimensions), len(indices), line_number, column
                ))
                
            # Verify indices are integers
            for idx in indices:
                idx_type = self.get_expression_type(idx)
                if idx_type != "FEINT":
                    self.add_error(invalid_array_index_error(line_number, column))
                    
        # Visit indices
        for idx in indices:
            self.visit(idx)
            
        return None
        
    def visit_dribble(self, node):
        """Visit an if statement"""
        condition = node.get('condition')
        condition_type = self.get_expression_type(condition)
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # Check condition type
        if condition_type and condition_type != "STAT":
            self.add_error(type_mismatch_error("STAT", condition_type, line_number, column))
            
        # Visit condition
        self.visit(condition)
        
        # Enter then scope
        self.semantic_analyzer.enter_scope()
        # Visit then body
        if 'then_body' in node:
            if isinstance(node['then_body'], list):
                for stmt in node['then_body']:
                    self.visit(stmt)
            else:
                self.visit(node['then_body'])
        # Exit then scope
        self.semantic_analyzer.exit_scope()
        
        # Enter else scope if present
        if 'else_body' in node:
            self.semantic_analyzer.enter_scope()
            # Visit else body
            if isinstance(node['else_body'], list):
                for stmt in node['else_body']:
                    self.visit(stmt)
            else:
                self.visit(node['else_body'])
            # Exit else scope
            self.semantic_analyzer.exit_scope()
            
        return None
        
    def visit_play(self, node):
        """Visit a while loop"""
        condition = node.get('condition')
        condition_type = self.get_expression_type(condition)
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # Check condition type
        if condition_type and condition_type != "STAT":
            self.add_error(type_mismatch_error("STAT", condition_type, line_number, column))
            
        # Visit condition
        self.visit(condition)
        
        # Enter loop scope
        self.semantic_analyzer.enter_scope()
        # Visit loop body
        if 'body' in node:
            if isinstance(node['body'], list):
                for stmt in node['body']:
                    self.visit(stmt)
            else:
                self.visit(node['body'])
        # Exit loop scope
        self.semantic_analyzer.exit_scope()
        
        return None
        
    def visit_forward(self, node):
        """Visit a for loop"""
        # Visit initialization
        init = node.get('init')
        if init:
            self.visit(init)
            
        # Check condition type
        condition = node.get('condition')
        condition_type = self.get_expression_type(condition)
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        if condition_type and condition_type != "STAT":
            self.add_error(type_mismatch_error("STAT", condition_type, line_number, column))
            
        # Visit condition
        self.visit(condition)
        
        # Visit update
        update = node.get('update')
        if update:
            self.visit(update)
            
        # Enter loop scope
        self.semantic_analyzer.enter_scope()
        # Visit loop body
        if 'body' in node:
            if isinstance(node['body'], list):
                for stmt in node['body']:
                    self.visit(stmt)
            else:
                self.visit(node['body'])
        # Exit loop scope
        self.semantic_analyzer.exit_scope()
        
        return None
        
    def visit_announce(self, node):
        """Visit an announce statement"""
        arguments = node.get('arguments', [])
        
        # Visit all arguments
        for arg in arguments:
            self.visit(arg)
            
        return None
        
    def visit_inbound(self, node):
        """Visit an inbound statement"""
        prompt = node.get('prompt')
        variable = node.get('variable')
        line_number = node.get('line_number', 0)
        column = node.get('column', 0)
        
        # Check prompt type
        if prompt:
            prompt_type = self.get_expression_type(prompt)
            if prompt_type and prompt_type != "CHANT":
                self.add_error(type_mismatch_error("CHANT", prompt_type, line_number, column))
                
            # Visit prompt
            self.visit(prompt)
            
        # Check variable
        if variable:
            if variable.get('type') == 'variable':
                var_name = variable.get('name')
                var_symbol = self.semantic_analyzer.lookup_symbol(var_name)
                
                if not var_symbol:
                    self.add_error(undefined_variable_error(var_name, line_number, column))
                    
                # Mark the variable as initialized
                if var_symbol:
                    var_symbol.initialized = True
                    
            # Visit variable
            self.visit(variable)
            
        return None
        
    def visit_numeric_literal(self, node):
        """Visit a numeric literal node"""
        # Nothing to check here
        return None
        
    def visit_string_literal(self, node):
        """Visit a string literal node"""
        # Nothing to check here
        return None
        
    def visit_concatenation(self, node):
        """Visit a string concatenation operation"""
        left = node.get('left')
        right = node.get('right')
        line_number = node.get('line_number', 0)
        if not line_number:
            line_number = node.get('line', 0)
        column = node.get('column', 0)
        
        # Visit the operands
        self.visit(left)
        self.visit(right)
        
        # Check types for concatenation
        left_type = self.get_expression_type(left)
        right_type = self.get_expression_type(right)
        
        # String concatenation should have at least one operand as a string
        if left_type and right_type:
            if not (SemanticAnalyzer.is_string_type(left_type) or SemanticAnalyzer.is_string_type(right_type)):
                self.add_error(invalid_operation_error('&', left_type, right_type, line_number, column))
        
        return None
        
    def visit_arithmetic_operation(self, node):
        """Visit an arithmetic operation"""
        left = node.get('left')
        right = node.get('right')
        operator = node.get('operator')
        line_number = node.get('line_number', 0)
        if not line_number:
            line_number = node.get('line', 0)
        column = node.get('column', 0)
        
        # Visit the operands
        self.visit(left)
        self.visit(right)
        
        # Check types for arithmetic operation
        left_type = self.get_expression_type(left)
        right_type = self.get_expression_type(right)
        
        if left_type and right_type:
            if not (SemanticAnalyzer.is_numeric_type(left_type) and SemanticAnalyzer.is_numeric_type(right_type)):
                self.add_error(invalid_operation_error(operator, left_type, right_type, line_number, column))
        
        return None
        
    def get_expression_type(self, node):
        """Get the type of an expression"""
        if not node:
            return None
            
        node_type = node.get('type')
        
        if node_type == 'literal':
            value_type = node.get('value_type')
            
            if value_type == 'FEINTLIT':
                return 'Feint'
            elif value_type == 'FLOATERLIT':
                return 'Floater'
            elif value_type == 'CHANTLIT':
                return 'Chant'
            elif value_type in ['WIN', 'LOSS']:
                return 'Stat'
                
            return None
            
        elif node_type == 'variable':
            var_name = node.get('name')
            var_symbol = self.semantic_analyzer.lookup_symbol(var_name)
            
            if var_symbol:
                return var_symbol.var_type
                
            return None
            
        elif node_type == 'numeric_literal':
            # Check if it's an integer or float
            value = node.get('value')
            try:
                int(value)
                return 'Feint'
            except (ValueError, TypeError):
                try:
                    float(value)
                    return 'Floater'
                except (ValueError, TypeError):
                    return None
            
        elif node_type == 'string_literal':
            return 'Chant'
            
        elif node_type == 'binary_operation' or node_type == 'arithmetic_operation':
            left_type = self.get_expression_type(node.get('left'))
            right_type = self.get_expression_type(node.get('right'))
            operator = node.get('operator')
            
            # For consistency, standardize types before passing to get_result_type
            if left_type:
                left_type = self._standardize_type(left_type)
            if right_type:
                right_type = self._standardize_type(right_type)
                
            # Let the analyzer determine the result type
            return SemanticAnalyzer.get_result_type(left_type, right_type, operator)
            
        elif node_type == 'concatenation':
            # Concatenation always results in a string
            return 'Chant'
            
        elif node_type == 'unary_operation':
            operand_type = self.get_expression_type(node.get('operand'))
            operator = node.get('operator')
            
            if operator == '-' and operand_type and SemanticAnalyzer.is_numeric_type(operand_type):
                return operand_type
            elif operator == '!' and operand_type and SemanticAnalyzer.is_boolean_type(operand_type):
                return 'Stat'
                
            return None
            
        elif node_type == 'function_call':
            func_name = node.get('name')
            func_symbol = self.semantic_analyzer.lookup_symbol(func_name)
            
            if func_symbol:
                return func_symbol.return_type
                
            return None
            
        elif node_type == 'array_element':
            array_name = node.get('array_name')
            array_symbol = self.semantic_analyzer.lookup_symbol(array_name)
            
            if array_symbol:
                return array_symbol.var_type
                
            return None
            
        return None
        
    def _standardize_type(self, type_name):
        """Standardize type names to match language specification"""
        if not type_name:
            return None
            
        type_upper = type_name.upper()
        if type_upper == 'FEINT':
            return 'Feint'
        elif type_upper == 'FLOATER':
            return 'Floater'
        elif type_upper == 'CHANT':
            return 'Chant'
        elif type_upper == 'STAT':
            return 'Stat'
        return type_name

def analyze(ast):
    """Analyze the AST for semantic errors"""
    # Create a semantic analyzer
    semantic_analyzer = SemanticAnalyzer()
    
    # Create an AST visitor
    visitor = AstVisitor(semantic_analyzer)
    
    # Visit the AST
    try:
        visitor.visit(ast)
    except Exception as e:
        # If there's an error during traversal, add it to the errors list
        import traceback
        error_info = str(e) + "\n" + traceback.format_exc()
        visitor.add_error(SemanticError(f"Error during semantic analysis: {error_info}", 0, 0))
    
    # Return any errors found
    return visitor.errors 