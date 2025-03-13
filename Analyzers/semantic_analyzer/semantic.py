from dataclasses import dataclass
from typing import Dict, Any, List, Optional, Union, Tuple
from ..lexical_analyzer.lexical import Token
from .errors import SemanticError, create_semantic_error
import re

@dataclass
class SemanticError:
    message: str
    line_number: int
    column: int

class SymbolTable:
    def __init__(self):
        self.symbols: Dict[str, Dict[str, Any]] = {}
        # Compile regex pattern for identifier validation
        self.identifier_pattern = re.compile(r'^@[a-z][a-zA-Z0-9_]*$')
    
    def is_valid_identifier(self, name: str) -> bool:
        """Check if identifier follows the pattern: @lowercase[A-Za-z0-9_]*"""
        return bool(self.identifier_pattern.match(name))
    
    def declare(self, name: str, type_: str, value: Any = None, is_constant: bool = False, node: dict = None) -> Optional[SemanticError]:
        # Validate identifier format
        if not self.is_valid_identifier(name):
            return create_semantic_error(
                f"Invalid identifier '{name}'. Identifiers must start with @ followed by lowercase letter",
                node
            )
        
        if name in self.symbols:
            return create_semantic_error(
                f"Variable '{name}' already declared",
                node
            )
        
        self.symbols[name] = {
            'type': type_,
            'value': value,
            'is_constant': is_constant
        }
        return None
    
    def get(self, name: str) -> Optional[Dict[str, Any]]:
        return self.symbols.get(name)
    
    def update(self, name: str, value: Any, line: int = None, column: int = None) -> Optional[SemanticError]:
        if not self.is_valid_identifier(name):
            return SemanticError(
                f"Invalid identifier '{name}'. Identifiers must start with @ followed by lowercase letter, then letters/numbers/underscore",
                line,
                column
            )
        
        if name not in self.symbols:
            return SemanticError(
                f"Variable '{name}' not declared",
                line,
                column
            )
        
        if self.symbols[name]['is_constant']:
            return SemanticError(
                f"Cannot modify constant '{name}'",
                line,
                column
            )
            
        self.symbols[name]['value'] = value
        return None

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors: List[SemanticError] = []
        self.output: List[str] = []  # Add output list to store results
        
        # Define valid types
        self.valid_types = {
            'Feint': int,      # Integer type
            'Floater': float,  # Float type
            'Chant': str,      # String type
            'Stat': bool       # Boolean type
        }
    
    def analyze(self, ast) -> Tuple[List[SemanticError], List[str]]:
        """Return both errors and output"""
        self.errors = []
        self.output = []  # Clear previous output
        
        if ast and ast.get('type') == 'program':
            # Analyze global declarations
            for decl in ast.get('global_declarations', []):
                self._analyze_node(decl)
                
            # Analyze function declarations
            for func_decl in ast.get('function_declarations', []):
                self._analyze_node(func_decl)
                
            # Analyze function definitions
            for func_def in ast.get('function_definitions', []):
                self._analyze_node(func_def)
                
            # Analyze team block
            if 'team_block' in ast:
                self._analyze_node(ast['team_block'])
                
        return self.errors, self.output
    
    def _analyze_node(self, node):
        if not node:
            return None
            
        node_type = node.get('type')
        
        if node_type == 'variable_declaration':
            return self._analyze_variable_declaration(node)
        elif node_type == 'constant_declaration':
            return self._analyze_constant_declaration(node)
        elif node_type == 'assignment':
            return self._analyze_assignment(node)
        elif node_type == 'announce':
            return self._analyze_announce(node)
        elif node_type == 'team_block':
            return self._analyze_team_block(node)
        elif node_type == 'arithmetic_operation':
            return self._analyze_arithmetic_operation(node)
        elif node_type == 'comparison':
            return self._analyze_comparison(node)
        elif node_type == 'function_call_statement':
            return self._analyze_function_call(node)
            
        # Recursively analyze child nodes if present
        if 'children' in node:
            for child in node['children']:
                self._analyze_node(child)
        if 'body' in node:
            for stmt in node['body']:
                self._analyze_node(stmt)
        if 'statements' in node:
            for stmt in node['statements']:
                self._analyze_node(stmt)
    
    def _analyze_variable_declaration(self, node):
        data_type = node['data_type']
        
        if data_type not in self.valid_types:
            self.errors.append(SemanticError(
                f"Invalid type '{data_type}'",
                node['line'],
                node['column']
            ))
            return
            
        for decl in node['declarations']:
            var_name = decl['name']
            init_value = None
            
            if decl.get('value'):
                init_value = self._evaluate_expression(decl['value'])
                if init_value is not None:
                    if not self._check_type_compatibility(data_type, init_value):
                        self.errors.append(SemanticError(
                            f"Type mismatch: Cannot initialize '{data_type}' with value of type '{type(init_value).__name__}'",
                            node['line'],
                            node['column']
                        ))
                        continue
            
            error = self.symbol_table.declare(
                var_name,
                data_type,
                init_value,
                False,
                node
            )
            
            if error:
                self.errors.append(error)
    
    def _analyze_constant_declaration(self, node):
        data_type = node['data_type']
        const_name = node['name']
        
        if data_type not in self.valid_types:
            self.errors.append(SemanticError(
                f"Invalid type '{data_type}'",
                node['line'],
                node['column']
            ))
            return
            
        value = self._evaluate_expression(node['value'])
        if value is not None:
            if not self._check_type_compatibility(data_type, value):
                self.errors.append(SemanticError(
                    f"Type mismatch: Cannot initialize constant '{data_type}' with value of type '{type(value).__name__}'",
                    node['line'],
                    node['column']
                ))
                return
                
        error = self.symbol_table.declare(
            const_name,
            data_type,
            value,
            True,  # is_constant=True
            node
        )
        
        if error:
            self.errors.append(error)
    
    def _analyze_assignment(self, node):
        var_name = node['name']
        value = self._evaluate_expression(node['value'])
        
        var_info = self.symbol_table.get(var_name)
        if not var_info:
            self.errors.append(SemanticError(
                f"Variable '{var_name}' used before declaration",
                node['line'],
                node['column']
            ))
            return
            
        if value is not None:
            if not self._check_type_compatibility(var_info['type'], value):
                self.errors.append(SemanticError(
                    f"Type mismatch: Cannot assign value of type '{type(value).__name__}' to variable of type '{var_info['type']}'",
                    node['line'],
                    node['column']
                ))
                return
                
        error = self.symbol_table.update(
            var_name,
            value,
            node['line'],
            node['column']
        )
        
        if error:
            self.errors.append(error)
    
    def _analyze_team_block(self, node):
        """Analyze the team block and its statements"""
        # Process local declarations if any
        if 'local_declarations' in node:
            for decl in node['local_declarations']:
                self._analyze_node(decl)
        
        # Process statements
        if 'statements' in node:
            for stmt in node['statements']:
                self._analyze_node(stmt)
    
    def _analyze_announce(self, node):
        """Analyze announce statement and collect output"""
        results = []
        
        if 'arguments' not in node:
            self.errors.append(create_semantic_error(
                "Missing arguments in Announce statement",
                node
            ))
            return
        
        for arg in node['arguments']:
            if isinstance(arg, dict):
                if arg.get('type') == 'string_literal':
                    value = arg['value']
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    results.append(value)
                elif arg.get('type') == 'variable':
                    var_name = arg['name']
                    var_info = self.symbol_table.get(var_name)
                    if not var_info:
                        self.errors.append(create_semantic_error(
                            f"Variable '{var_name}' used before declaration",
                            arg  # Pass the argument node for accurate position
                        ))
                    else:
                        results.append(str(var_info['value']))
                else:
                    value = self._evaluate_expression(arg)
                    if value is not None:
                        results.append(str(value))
                    else:
                        self.errors.append(create_semantic_error(
                            "Invalid expression in Announce statement",
                            arg
                        ))
        
        # Add the evaluated result to output
        if results and not self.errors:
            self.output.append(''.join(map(str, results)))
    
    def _evaluate_expression(self, node) -> Any:
        if not node:
            return None
            
        if isinstance(node, dict):
            node_type = node.get('type')
            
            if node_type == 'numeric_literal':
                return float(node['value']) if '.' in str(node['value']) else int(node['value'])
            elif node_type == 'string_literal':
                # Remove quotes from string literals
                value = node['value']
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                return str(value)
            elif node_type == 'boolean_literal':
                return node['value'].lower() == 'win'
            elif node_type == 'variable':
                var_name = node['name']
                var_info = self.symbol_table.get(var_name)
                if not var_info:
                    self.errors.append(create_semantic_error(
                        f"Variable '{var_name}' used before declaration",
                        node
                    ))
                    return None
                return var_info['value']
            elif node_type in ['arithmetic_operation', 'comparison']:
                return self._evaluate_operation(node)
        
        return node  # Return the node itself if it's a direct value
    
    def _evaluate_operation(self, node):
        left = self._evaluate_expression(node['left'])
        right = self._evaluate_expression(node['right'])
        
        if left is None or right is None:
            return None
            
        if node['type'] == 'arithmetic_operation':
            if not (isinstance(left, (int, float)) and isinstance(right, (int, float))):
                self.errors.append(SemanticError(
                    f"Invalid operands for arithmetic operation: {type(left).__name__} {node['operator']} {type(right).__name__}",
                    node.get('line', 0),
                    node.get('column', 0)
                ))
                return None
                
            try:
                if node['operator'] == '+': return left + right
                elif node['operator'] == '-': return left - right
                elif node['operator'] == '*': return left * right
                elif node['operator'] == '/': 
                    if right == 0:
                        self.errors.append(SemanticError(
                            "Division by zero",
                            node.get('line', 0),
                            node.get('column', 0)
                        ))
                        return None
                    return left / right
            except Exception as e:
                self.errors.append(SemanticError(
                    str(e),
                    node.get('line', 0),
                    node.get('column', 0)
                ))
                return None
                
        return None
    
    def _check_type_compatibility(self, expected_type: str, value: Any) -> bool:
        if value is None:
            return True
            
        expected_python_type = self.valid_types.get(expected_type)
        if not expected_python_type:
            return False
            
        # Handle numeric type compatibility
        if expected_type == 'Feint' and isinstance(value, int):
            return True
        if expected_type == 'Floater' and isinstance(value, (int, float)):
            return True
        if expected_type == 'Chant' and isinstance(value, str):
            return True
        if expected_type == 'Stat' and isinstance(value, bool):
            return True
            
        return False 