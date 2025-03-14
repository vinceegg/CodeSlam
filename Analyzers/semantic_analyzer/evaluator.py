import re
from .errors import SemanticError

class Environment:
    """Environment for tracking variables during evaluation"""
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent
        
    def define(self, name, value):
        """Define a variable in the current environment"""
        self.variables[name] = value
        return value
        
    def lookup(self, name):
        """Look up a variable in the environment"""
        if name in self.variables:
            return self.variables[name]
            
        if self.parent:
            return self.parent.lookup(name)
            
        return None
        
    def assign(self, name, value):
        """Assign a value to an existing variable"""
        if name in self.variables:
            self.variables[name] = value
            return value
            
        if self.parent:
            return self.parent.assign(name, value)
            
        return None

class Evaluator:
    """Evaluator for expressions and statements"""
    def __init__(self, source_code=None):
        self.global_env = Environment()
        self.current_env = self.global_env
        self.source_code = source_code
        self.lines = source_code.split('\n') if source_code else []
        self.debug_output = []
        
    def get_line(self, line_number):
        """Get a specific line from the source code"""
        if 0 < line_number <= len(self.lines):
            return self.lines[line_number-1]
        return ""
        
    def enter_scope(self):
        """Enter a new scope"""
        self.current_env = Environment(self.current_env)
        return self.current_env
        
    def exit_scope(self):
        """Exit the current scope"""
        if self.current_env.parent:
            self.current_env = self.current_env.parent
        return self.current_env
        
    def evaluate(self, node):
        """Evaluate an AST node"""
        if not node:
            return None
            
        node_type = node.get('type')
        
        # Add debug info
        self.debug_output.append(f"Evaluating node type: {node_type}")
        
        # Handle different node types
        if node_type == 'literal':
            return self.evaluate_literal(node)
        elif node_type == 'variable':
            return self.evaluate_variable(node)
        elif node_type == 'binary_operation':
            return self.evaluate_binary_operation(node)
        elif node_type == 'arithmetic_operation':
            return self.evaluate_arithmetic_operation(node)
        elif node_type == 'unary_operation':
            return self.evaluate_unary_operation(node)
        elif node_type == 'assignment':
            return self.evaluate_assignment(node)
        elif node_type == 'function_call':
            return self.evaluate_function_call(node)
        elif node_type == 'array_element':
            return self.evaluate_array_element(node)
        elif node_type == 'announce':
            return self.evaluate_announce(node)
        elif node_type == 'concatenation':
            return self.evaluate_concatenation(node)
        elif node_type == 'numeric_literal':
            return self.evaluate_numeric_literal(node)
        elif node_type == 'string_literal':
            return self.evaluate_string_literal(node)
        
        # If no specific handler, return placeholder
        return f"[unhandled node type: {node_type}]"
        
    def evaluate_literal(self, node):
        """Evaluate a literal value"""
        value = node.get('value')
        value_type = node.get('value_type')
        
        if value_type == 'FEINTLIT':
            return int(value)
        elif value_type == 'FLOATERLIT':
            return float(value)
        elif value_type == 'CHANTLIT':
            # Remove quotes and handle escape sequences
            return str(value).strip('"')
        elif value_type in ['WIN', 'LOSS']:
            return value == 'WIN'
            
        return value
    
    def evaluate_numeric_literal(self, node):
        """Evaluate a numeric literal"""
        value = node.get('value')
        try:
            # Try to convert to int first
            return int(value)
        except (ValueError, TypeError):
            try:
                # If not int, try float
                return float(value)
            except (ValueError, TypeError):
                # If all fails, return as string
                return str(value)
                
    def evaluate_string_literal(self, node):
        """Evaluate a string literal"""
        value = node.get('value')
        # Remove quotes if present
        if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        return value
        
    def evaluate_variable(self, node):
        """Evaluate a variable reference"""
        var_name = node.get('name')
        line_number = node.get('line_number', node.get('line', 0))
        
        print(f"DEBUG Evaluator: Evaluating variable {var_name} at line {line_number}")
        
        # Look up the variable in the environment
        value = self.current_env.lookup(var_name)
        
        if value is None:
            # Check if this is a built-in variable
            if var_name == '@true':
                return True
            elif var_name == '@false':
                return False
            
            # Debug info for variable lookup failure
            print(f"DEBUG Evaluator: Variable {var_name} not found in environment")
            print(f"DEBUG Evaluator: Current environment variables: {self.current_env.variables}")
            
            # For undefined variables, return a placeholder with the name
            return f"[undefined:{var_name}]"
            
        print(f"DEBUG Evaluator: Found variable {var_name} = {value}")
        return value
        
    def evaluate_binary_operation(self, node):
        """Evaluate a binary operation"""
        left = self.evaluate(node.get('left'))
        right = self.evaluate(node.get('right'))
        operator = node.get('operator')
        
        # Handle arithmetic operations
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:  # Prevent division by zero
                return float('inf')
            return left / right
        elif operator == '%':
            return left % right
            
        # Handle string concatenation
        elif operator == '&':
            return str(left) + str(right)
            
        # Handle comparison operations
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        elif operator == '<':
            return left < right
        elif operator == '>':
            return left > right
        elif operator == '<=':
            return left <= right
        elif operator == '>=':
            return left >= right
            
        # Handle logical operations
        elif operator == '&&':
            return left and right
        elif operator == '||':
            return left or right
            
        return f"[unknown operator: {operator}]"
    
    def evaluate_arithmetic_operation(self, node):
        """Evaluate an arithmetic operation"""
        left = self.evaluate(node.get('left'))
        right = self.evaluate(node.get('right'))
        operator = node.get('operator')
        
        # Handle arithmetic operations
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:  # Prevent division by zero
                return float('inf')
            return left / right
        elif operator == '%':
            return left % right
            
        return f"[unknown arithmetic operator: {operator}]"
    
    def evaluate_concatenation(self, node):
        """Evaluate a string concatenation"""
        left = self.evaluate(node.get('left'))
        right = self.evaluate(node.get('right'))
        
        # Convert both to strings and concatenate
        return str(left) + str(right)
        
    def evaluate_unary_operation(self, node):
        """Evaluate a unary operation"""
        operand = self.evaluate(node.get('operand'))
        operator = node.get('operator')
        
        if operator == '-':
            return -operand
        elif operator == '!':
            return not operand
            
        return operand
        
    def evaluate_assignment(self, node):
        """Evaluate an assignment operation"""
        # Get target and value
        target_name = node.get('name')
        value_node = node.get('value')
        value = self.evaluate(value_node)
        
        # Define or update the variable in the environment
        if self.current_env.lookup(target_name) is None:
            self.current_env.define(target_name, value)
        else:
            self.current_env.assign(target_name, value)
            
        return value
        
    def evaluate_function_call(self, node):
        """Evaluate a function call"""
        # For demonstration, return a placeholder
        name = node.get('name')
        args = [self.evaluate(arg) for arg in node.get('arguments', [])]
        
        # Built-in functions could be implemented here
        
        return f"[function:{name}({', '.join(map(str, args))})]"
        
    def evaluate_array_element(self, node):
        """Evaluate an array element access"""
        # For demonstration, return a placeholder
        array_name = node.get('array_name')
        indices = [self.evaluate(idx) for idx in node.get('indices', [])]
        
        return f"[array:{array_name}[{', '.join(map(str, indices))}]]"
        
    def evaluate_announce(self, node):
        """Evaluate an announce statement"""
        args = node.get('arguments', [])
        result = []
        
        for arg in args:
            value = self.evaluate(arg)
            result.append(str(value))
            
        return ''.join(result)
        
    def populate_variables_from_ast(self, ast):
        """Populate the environment with variables from the AST"""
        if not ast:
            return
            
        # Process variable declarations in the AST
        self._extract_variables(ast)
            
    def _extract_variables(self, node):
        """Extract variables from AST nodes and populate the environment"""
        if not node or not isinstance(node, dict):
            return
            
        node_type = node.get('type')
        line_number = node.get('line_number', node.get('line', 0))
        
        print(f"DEBUG Evaluator: Extracting variables from {node_type} node at line {line_number}")
        
        if node_type == 'variable_declaration':
            var_type = node.get('data_type')
            print(f"DEBUG Evaluator: Found variable declaration of type {var_type}")
            
            # Try direct access to name field first
            var_name = node.get('name')
            if var_name and var_name.startswith('@'):
                value_node = node.get('value')
                
                # Default values based on type
                default_value = 0 if var_type == 'FEINT' else \
                               0.0 if var_type == 'FLOATER' else \
                               "" if var_type == 'CHANT' else \
                               False if var_type == 'STAT' else None
                               
                # If there's an initializer, evaluate it
                if value_node:
                    value = self.evaluate(value_node)
                else:
                    value = default_value
                    
                # Store in environment
                self.current_env.define(var_name, value)
                print(f"DEBUG Evaluator: Defined variable {var_name} = {value}")
                return
                
            # Process declarations list
            declarations = node.get('declarations', [])
            if isinstance(declarations, list):
                for decl in declarations:
                    if decl.get('type') == 'unknown':
                        var_name = decl.get('name')
                        value_node = decl.get('value')
                        
                        if var_name and var_name.startswith('@'):
                            # Default values based on type
                            default_value = 0 if var_type == 'FEINT' else \
                                        0.0 if var_type == 'FLOATER' else \
                                        "" if var_type == 'CHANT' else \
                                        False if var_type == 'STAT' else None
                                        
                            # If there's an initializer, evaluate it
                            if value_node:
                                value = self.evaluate(value_node)
                            else:
                                value = default_value
                                
                            # Store in environment
                            self.current_env.define(var_name, value)
                            print(f"DEBUG Evaluator: Defined variable {var_name} = {value} from declaration list")
            elif isinstance(declarations, dict):
                # Handle a single declaration
                decl = declarations
                if decl.get('type') == 'unknown':
                    var_name = decl.get('name')
                    value_node = decl.get('value')
                    
                    if var_name and var_name.startswith('@'):
                        # Default values based on type
                        default_value = 0 if var_type == 'FEINT' else \
                                    0.0 if var_type == 'FLOATER' else \
                                    "" if var_type == 'CHANT' else \
                                    False if var_type == 'STAT' else None
                                    
                        # If there's an initializer, evaluate it
                        if value_node:
                            value = self.evaluate(value_node)
                        else:
                            value = default_value
                            
                        # Store in environment
                        self.current_env.define(var_name, value)
                        print(f"DEBUG Evaluator: Defined variable {var_name} = {value} from single declaration")
                        
        elif node_type == 'assignment':
            target_name = node.get('name')
            value_node = node.get('value')
            
            if target_name and value_node:
                value = self.evaluate(value_node)
                
                # Define or update the variable in the environment
                if self.current_env.lookup(target_name) is None:
                    self.current_env.define(target_name, value)
                    print(f"DEBUG Evaluator: Defined variable through assignment {target_name} = {value}")
                else:
                    self.current_env.assign(target_name, value)
                    print(f"DEBUG Evaluator: Updated variable through assignment {target_name} = {value}")
                    
        # Try to handle other patterns that might contain variable declarations
        elif node_type in ['team_block', 'program']:
            # First check for local_declarations
            if 'local_declarations' in node:
                local_decls = node.get('local_declarations', [])
                if isinstance(local_decls, list):
                    for decl in local_decls:
                        self._extract_variables(decl)
                else:
                    self._extract_variables(local_decls)
        
        # Recursively process nested nodes (in order by line number if possible)
        # Collect all child nodes with line numbers
        child_nodes = []
        for key, value in node.items():
            if key == 'type':
                continue
                
            if isinstance(value, dict):
                line_num = value.get('line_number', value.get('line', 0))
                child_nodes.append((value, line_num))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        line_num = item.get('line_number', item.get('line', 0))
                        child_nodes.append((item, line_num))
        
        # Sort by line number and process in order
        child_nodes.sort(key=lambda x: x[1])
        for child_node, _ in child_nodes:
            self._extract_variables(child_node)

def evaluate_ast(ast_nodes, source_code=None):
    """Evaluate a list of AST nodes"""
    evaluator = Evaluator(source_code)
    results = []
    
    print(f"DEBUG Evaluator: Processing AST nodes type: {type(ast_nodes)}")
    if isinstance(ast_nodes, dict):
        print(f"DEBUG Evaluator: AST node keys: {list(ast_nodes.keys())}")
    
    # First, extract all variable declarations to populate the environment
    # This processes the entire AST recursively to find all variables
    if isinstance(ast_nodes, dict):
        print("DEBUG Evaluator: Extracting variables from full AST")
        evaluator._extract_all_variables(ast_nodes)
    elif isinstance(ast_nodes, list):
        for node in ast_nodes:
            evaluator._extract_all_variables(node)
    
    # Now evaluate Announce statements to get results
    # Start by handling program node (most likely case)
    if isinstance(ast_nodes, dict) and ast_nodes.get('type') == 'program':
        team_block = ast_nodes.get('team_block', {})
        print(f"DEBUG Evaluator: Found program node with team_block keys: {list(team_block.keys())}")
        
        statements = team_block.get('statements', [])
        if isinstance(statements, list):
            for stmt in statements:
                if stmt and stmt.get('type') == 'announce':
                    try:
                        result = evaluator.evaluate(stmt)
                        results.append(result)
                        print(f"DEBUG Evaluator: Evaluated announce statement, result: {result}")
                    except Exception as e:
                        print(f"DEBUG Evaluator: Error evaluating announce: {e}")
        elif statements and statements.get('type') == 'announce':
            try:
                result = evaluator.evaluate(statements)
                results.append(result)
                print(f"DEBUG Evaluator: Evaluated single announce statement, result: {result}")
            except Exception as e:
                print(f"DEBUG Evaluator: Error evaluating single announce: {e}")
    
    # Alternative case: direct list of nodes (for individual Announce statements)
    elif isinstance(ast_nodes, list):
        for node in ast_nodes:
            if node and node.get('type') == 'announce':
                try:
                    result = evaluator.evaluate(node)
                    results.append(result)
                    print(f"DEBUG Evaluator: Evaluated announce from list, result: {result}")
                except Exception as e:
                    print(f"DEBUG Evaluator: Error evaluating announce from list: {e}")
                    
    # Handle direct announce node
    elif ast_nodes and isinstance(ast_nodes, dict) and ast_nodes.get('type') == 'announce':
        try:
            result = evaluator.evaluate(ast_nodes)
            results.append(result)
            print(f"DEBUG Evaluator: Evaluated direct announce, result: {result}")
        except Exception as e:
            print(f"DEBUG Evaluator: Error evaluating direct announce: {e}")
    
    # Debug the variables found
    print(f"DEBUG Evaluator: Variables in environment: {evaluator.current_env.variables}")
    
    return results

def _extract_all_variables(self, node):
    """Extract all variables from the AST structure, regardless of node type"""
    if not node or not isinstance(node, dict):
        return
    
    node_type = node.get('type')
    print(f"DEBUG Evaluator: Extracting variables from node type: {node_type}")
    
    # Process variable declarations
    if node_type == 'variable_declaration':
        self._extract_variables_from_declaration(node)
    # Process assignments
    elif node_type == 'assignment':
        self._extract_variables_from_assignment(node)
    
    # Process all fields recursively
    for key, value in node.items():
        if key == 'type':
            continue
            
        if isinstance(value, dict):
            self._extract_all_variables(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    self._extract_all_variables(item)

def _extract_variables_from_declaration(self, node):
    """Extract variables from a declaration node"""
    var_type = node.get('data_type')
    print(f"DEBUG Evaluator: Found variable declaration of type {var_type}")
    
    # Try direct variable name
    var_name = node.get('name')
    if var_name and var_name.startswith('@'):
        value_node = node.get('value')
        default_value = self._get_default_value(var_type)
        
        if value_node:
            value = self.evaluate(value_node)
        else:
            value = default_value
            
        self.current_env.define(var_name, value)
        print(f"DEBUG Evaluator: Defined variable {var_name} = {value}")
        return
    
    # Try declarations list
    declarations = node.get('declarations', [])
    if declarations:
        if isinstance(declarations, list):
            for decl in declarations:
                self._process_declaration_item(decl, var_type)
        else:
            self._process_declaration_item(declarations, var_type)
    
    # Try nested fields
    for key, value in node.items():
        if key not in ['type', 'data_type']:
            if isinstance(value, dict):
                var_name = value.get('name')
                if var_name and var_name.startswith('@'):
                    value_node = value.get('value')
                    default_value = self._get_default_value(var_type)
                    
                    if value_node:
                        val = self.evaluate(value_node)
                    else:
                        val = default_value
                        
                    self.current_env.define(var_name, val)
                    print(f"DEBUG Evaluator: Defined variable from nested field {var_name} = {val}")

def _process_declaration_item(self, decl, var_type):
    """Process a single declaration item"""
    if not isinstance(decl, dict):
        return
        
    var_name = decl.get('name')
    if var_name and var_name.startswith('@'):
        value_node = decl.get('value')
        default_value = self._get_default_value(var_type)
        
        if value_node:
            value = self.evaluate(value_node)
        else:
            value = default_value
            
        self.current_env.define(var_name, value)
        print(f"DEBUG Evaluator: Defined variable from declaration item {var_name} = {value}")

def _extract_variables_from_assignment(self, node):
    """Extract variables from an assignment node"""
    target_name = node.get('name')
    value_node = node.get('value')
    
    if target_name and target_name.startswith('@') and value_node:
        value = self.evaluate(value_node)
        
        if self.current_env.lookup(target_name) is None:
            self.current_env.define(target_name, value)
            print(f"DEBUG Evaluator: Defined variable through assignment {target_name} = {value}")
        else:
            self.current_env.assign(target_name, value)
            print(f"DEBUG Evaluator: Updated variable through assignment {target_name} = {value}")

def _get_default_value(self, var_type):
    """Get the default value for a variable type"""
    if var_type == 'FEINT':
        return 0
    elif var_type == 'FLOATER':
        return 0.0
    elif var_type == 'CHANT':
        return ""
    elif var_type == 'STAT':
        return False
    return None

# Add the methods to the Evaluator class
Evaluator._extract_all_variables = _extract_all_variables
Evaluator._extract_variables_from_declaration = _extract_variables_from_declaration
Evaluator._process_declaration_item = _process_declaration_item  
Evaluator._extract_variables_from_assignment = _extract_variables_from_assignment
Evaluator._get_default_value = _get_default_value