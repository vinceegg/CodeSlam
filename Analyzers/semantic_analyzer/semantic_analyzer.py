from typing import Any, Dict, List, Optional, Set, Union
from ..syntax_analyzer.ast_builder import (
    ASTNode, Program, Team, Player, Statement, Expression,
    Literal, Identifier, BinaryOperation, UnaryOperation, FunctionCall,
    ArrayAccess, VariableDeclaration, Assignment, IfStatement, ElseStatement,
    ElseIfStatement, SwitchStatement, CaseStatement, DefaultStatement,
    WhileLoop, ForLoop, DoWhileLoop, BreakStatement, ContinueStatement,
    ReturnStatement, Block, FunctionDeclaration, ArrayDeclaration
)
from ..lexical_analyzer.tokens import TokenType

class Symbol:
    """Represents a symbol in the symbol table."""
    
    def __init__(self, name: str, type: str, scope: str, is_constant: bool = False):
        self.name = name
        self.type = type
        self.scope = scope
        self.is_constant = is_constant
        self.value = None
        self.is_array = False
        self.array_size = None
        self.is_function = False
        self.parameters = []
        self.return_type = None

class SymbolTable:
    """Manages the symbol table for the semantic analyzer."""
    
    def __init__(self):
        self.symbols: Dict[str, Symbol] = {}
        self.scopes: List[str] = ["global"]
        self.current_scope = "global"
    
    def enter_scope(self, scope_name: str) -> None:
        """Enter a new scope."""
        self.scopes.append(scope_name)
        self.current_scope = scope_name
    
    def exit_scope(self) -> None:
        """Exit the current scope."""
        if len(self.scopes) > 1:
            self.scopes.pop()
            self.current_scope = self.scopes[-1]
    
    def define(self, name: str, type: str, is_constant: bool = False) -> Symbol:
        """Define a new symbol in the current scope."""
        symbol = Symbol(name, type, self.current_scope, is_constant)
        self.symbols[name] = symbol
        return symbol
    
    def lookup(self, name: str) -> Optional[Symbol]:
        """Look up a symbol by name, starting from the current scope."""
        for scope in reversed(self.scopes):
            if name in self.symbols and self.symbols[name].scope == scope:
                return self.symbols[name]
        return None
    
    def update(self, name: str, value: Any) -> None:
        """Update the value of a symbol."""
        symbol = self.lookup(name)
        if symbol:
            symbol.value = value

class SemanticAnalyzer:
    """Performs semantic analysis on the AST."""
    
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.current_function: Optional[str] = None
        self.in_loop = False
        self.in_switch = False
    
    def analyze(self, node: ASTNode) -> bool:
        """
        Analyze the AST starting from the given node.
        
        Args:
            node: The root node of the AST
            
        Returns:
            True if the analysis was successful, False otherwise
        """
        try:
            self.visit(node)
            return len(self.errors) == 0
        except Exception as e:
            self.errors.append(f"Internal error during semantic analysis: {str(e)}")
            return False
    
    def visit(self, node: ASTNode) -> Any:
        """
        Visit a node in the AST.
        
        Args:
            node: The AST node to visit
            
        Returns:
            The result of visiting the node
        """
        method_name = f"visit_{node.__class__.__name__.lower()}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node: ASTNode) -> Any:
        """
        Default visitor method for nodes without a specific visit method.
        
        Args:
            node: The AST node to visit
            
        Returns:
            None
        """
        return None
    
    def visit_program(self, node: Program) -> Any:
        """
        Visit a Program node.
        
        Args:
            node: The Program node to visit
            
        Returns:
            The result of visiting the Program node
        """
        for statement in node.statements:
            self.visit(statement)
        return None
    
    def visit_team(self, node: Team) -> Any:
        """
        Visit a Team node (main function).
        
        Args:
            node: The Team node to visit
            
        Returns:
            The result of visiting the Team node
        """
        self.symbol_table.enter_scope(node.name)
        self.current_function = node.name
        
        # Define the team's parameters
        for param in node.parameters:
            self.symbol_table.define(param.name, param.type)
        
        # Visit the team's body
        self.visit(node.body)
        
        self.current_function = None
        self.symbol_table.exit_scope()
        return None
    
    def visit_player(self, node: Player) -> Any:
        """
        Visit a Player node.
        
        Args:
            node: The Player node to visit
            
        Returns:
            The result of visiting the Player node
        """
        # Define the player's stats
        for stat_name, stat_value in node.stats.items():
            stat_type = self.visit(stat_value)
            if stat_type:
                self.symbol_table.define(stat_name, stat_type)
        return None
    
    def visit_literal(self, node: Literal) -> str:
        """
        Visit a Literal node.
        
        Args:
            node: The Literal node to visit
            
        Returns:
            The type of the literal
        """
        if isinstance(node.value, bool):
            return "boolean"
        elif isinstance(node.value, int):
            return "integer"
        elif isinstance(node.value, float):
            return "float"
        elif isinstance(node.value, str):
            return "string"
        else:
            self.errors.append(f"Unknown literal type: {type(node.value)}")
            return "unknown"
    
    def visit_identifier(self, node: Identifier) -> str:
        """
        Visit an Identifier node.
        
        Args:
            node: The Identifier node to visit
            
        Returns:
            The type of the identifier
        """
        symbol = self.symbol_table.lookup(node.name)
        if symbol:
            return symbol.type
        else:
            self.errors.append(f"Undefined variable: {node.name}")
            return "unknown"
    
    def visit_binaryoperation(self, node: BinaryOperation) -> str:
        """
        Visit a BinaryOperation node.
        
        Args:
            node: The BinaryOperation node to visit
            
        Returns:
            The type of the binary operation result
        """
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        
        # Type checking for arithmetic operations
        if node.operator in [TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE]:
            if left_type in ["integer", "float"] and right_type in ["integer", "float"]:
                return "float" if "float" in [left_type, right_type] else "integer"
            else:
                self.errors.append(f"Invalid operands for arithmetic operation: {left_type} and {right_type}")
                return "unknown"
        
        # Type checking for comparison operations
        elif node.operator in [TokenType.EQUAL, TokenType.NOT_EQUAL, TokenType.LESS_THAN, 
                             TokenType.GREATER_THAN, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL]:
            if left_type == right_type:
                return "boolean"
            else:
                self.errors.append(f"Cannot compare {left_type} with {right_type}")
                return "unknown"
        
        # Type checking for logical operations
        elif node.operator in [TokenType.AND, TokenType.OR]:
            if left_type == "boolean" and right_type == "boolean":
                return "boolean"
            else:
                self.errors.append(f"Invalid operands for logical operation: {left_type} and {right_type}")
                return "unknown"
        
        return "unknown"
    
    def visit_unaryoperation(self, node: UnaryOperation) -> str:
        """
        Visit a UnaryOperation node.
        
        Args:
            node: The UnaryOperation node to visit
            
        Returns:
            The type of the unary operation result
        """
        operand_type = self.visit(node.operand)
        
        if node.operator == TokenType.NOT:
            if operand_type == "boolean":
                return "boolean"
            else:
                self.errors.append(f"Invalid operand for NOT operation: {operand_type}")
                return "unknown"
        
        elif node.operator == TokenType.MINUS:
            if operand_type in ["integer", "float"]:
                return operand_type
            else:
                self.errors.append(f"Invalid operand for negation: {operand_type}")
                return "unknown"
        
        return "unknown"
    
    def visit_functioncall(self, node: FunctionCall) -> str:
        """
        Visit a FunctionCall node.
        
        Args:
            node: The FunctionCall node to visit
            
        Returns:
            The return type of the function
        """
        symbol = self.symbol_table.lookup(node.name)
        if not symbol or not symbol.is_function:
            self.errors.append(f"Undefined function: {node.name}")
            return "unknown"
        
        # Check argument count
        if len(node.arguments) != len(symbol.parameters):
            self.errors.append(f"Function {node.name} expects {len(symbol.parameters)} arguments, but got {len(node.arguments)}")
            return "unknown"
        
        # Check argument types
        for arg, param in zip(node.arguments, symbol.parameters):
            arg_type = self.visit(arg)
            if arg_type != param.type:
                self.errors.append(f"Type mismatch in function {node.name}: expected {param.type}, got {arg_type}")
                return "unknown"
        
        return symbol.return_type
    
    def visit_arrayaccess(self, node: ArrayAccess) -> str:
        """
        Visit an ArrayAccess node.
        
        Args:
            node: The ArrayAccess node to visit
            
        Returns:
            The type of the array element
        """
        symbol = self.symbol_table.lookup(node.array_name)
        if not symbol or not symbol.is_array:
            self.errors.append(f"Undefined array: {node.array_name}")
            return "unknown"
        
        index_type = self.visit(node.index)
        if index_type != "integer":
            self.errors.append(f"Array index must be an integer, got {index_type}")
            return "unknown"
        
        return symbol.type
    
    def visit_variabledeclaration(self, node: VariableDeclaration) -> None:
        """
        Visit a VariableDeclaration node.
        
        Args:
            node: The VariableDeclaration node to visit
            
        Returns:
            None
        """
        # Check if variable is already defined in the current scope
        if self.symbol_table.lookup(node.name):
            self.errors.append(f"Variable {node.name} is already defined in the current scope")
            return
        
        # If there's an initial value, check its type
        if node.initial_value:
            value_type = self.visit(node.initial_value)
            if value_type != node.type:
                self.errors.append(f"Type mismatch in variable declaration: expected {node.type}, got {value_type}")
                return
        
        # Define the variable in the symbol table
        self.symbol_table.define(node.name, node.type)
    
    def visit_assignment(self, node: Assignment) -> None:
        """
        Visit an Assignment node.
        
        Args:
            node: The Assignment node to visit
            
        Returns:
            None
        """
        # Check if the variable exists
        symbol = self.symbol_table.lookup(node.name)
        if not symbol:
            self.errors.append(f"Undefined variable: {node.name}")
            return
        
        # Check if the variable is constant
        if symbol.is_constant:
            self.errors.append(f"Cannot assign to constant variable: {node.name}")
            return
        
        # Check the type of the value
        value_type = self.visit(node.value)
        if value_type != symbol.type:
            self.errors.append(f"Type mismatch in assignment: expected {symbol.type}, got {value_type}")
            return
        
        # Update the variable's value
        self.symbol_table.update(node.name, node.value)
    
    def visit_ifstatement(self, node: IfStatement) -> None:
        """
        Visit an IfStatement node (DRIBBLE).
        
        Args:
            node: The IfStatement node to visit
            
        Returns:
            None
        """
        # Check the condition type
        condition_type = self.visit(node.condition)
        if condition_type != "boolean":
            self.errors.append(f"If condition must be a boolean, got {condition_type}")
            return
        
        # Visit the then branch
        self.symbol_table.enter_scope("if")
        self.visit(node.then_branch)
        self.symbol_table.exit_scope()
        
        # Visit the else branch if it exists
        if node.else_branch:
            self.symbol_table.enter_scope("else")
            self.visit(node.else_branch)
            self.symbol_table.exit_scope()
    
    def visit_elsestatement(self, node: ElseStatement) -> None:
        """
        Visit an ElseStatement node (SHOOT).
        
        Args:
            node: The ElseStatement node to visit
            
        Returns:
            None
        """
        self.visit(node.body)
    
    def visit_elseifstatement(self, node: ElseIfStatement) -> None:
        """
        Visit an ElseIfStatement node (PASS).
        
        Args:
            node: The ElseIfStatement node to visit
            
        Returns:
            None
        """
        # Check the condition type
        condition_type = self.visit(node.condition)
        if condition_type != "boolean":
            self.errors.append(f"Else-if condition must be a boolean, got {condition_type}")
            return
        
        self.visit(node.body)
    
    def visit_switchstatement(self, node: SwitchStatement) -> None:
        """
        Visit a SwitchStatement node (SWITCH).
        
        Args:
            node: The SwitchStatement node to visit
            
        Returns:
            None
        """
        # Check the expression type
        expr_type = self.visit(node.expression)
        if expr_type not in ["integer", "string"]:
            self.errors.append(f"Switch expression must be an integer or string, got {expr_type}")
            return
        
        self.in_switch = True
        
        # Visit all cases
        for case in node.cases:
            self.visit(case)
        
        # Visit the default case if it exists
        if node.default_case:
            self.visit(node.default_case)
        
        self.in_switch = False
    
    def visit_casestatement(self, node: CaseStatement) -> None:
        """
        Visit a CaseStatement node (GET).
        
        Args:
            node: The CaseStatement node to visit
            
        Returns:
            None
        """
        if not self.in_switch:
            self.errors.append("Case statement must be inside a switch statement")
            return
        
        self.visit(node.value)
        self.visit(node.body)
    
    def visit_defaultstatement(self, node: DefaultStatement) -> None:
        """
        Visit a DefaultStatement node (DEFAULT).
        
        Args:
            node: The DefaultStatement node to visit
            
        Returns:
            None
        """
        if not self.in_switch:
            self.errors.append("Default statement must be inside a switch statement")
            return
        
        self.visit(node.body)
    
    def visit_whileloop(self, node: WhileLoop) -> None:
        """
        Visit a WhileLoop node (PLAY).
        
        Args:
            node: The WhileLoop node to visit
            
        Returns:
            None
        """
        # Check the condition type
        condition_type = self.visit(node.condition)
        if condition_type != "boolean":
            self.errors.append(f"While condition must be a boolean, got {condition_type}")
            return
        
        self.in_loop = True
        self.symbol_table.enter_scope("while")
        self.visit(node.body)
        self.symbol_table.exit_scope()
        self.in_loop = False
    
    def visit_forloop(self, node: ForLoop) -> None:
        """
        Visit a ForLoop node (FORWARD).
        
        Args:
            node: The ForLoop node to visit
            
        Returns:
            None
        """
        self.symbol_table.enter_scope("for")
        
        # Visit the initializer
        self.visit(node.initializer)
        
        # Check the condition type
        condition_type = self.visit(node.condition)
        if condition_type != "boolean":
            self.errors.append(f"For condition must be a boolean, got {condition_type}")
            return
        
        # Visit the increment
        self.visit(node.increment)
        
        self.in_loop = True
        self.visit(node.body)
        self.in_loop = False
        
        self.symbol_table.exit_scope()
    
    def visit_dowhileloop(self, node: DoWhileLoop) -> None:
        """
        Visit a DoWhileLoop node (RUN).
        
        Args:
            node: The DoWhileLoop node to visit
            
        Returns:
            None
        """
        self.in_loop = True
        self.symbol_table.enter_scope("do-while")
        self.visit(node.body)
        self.symbol_table.exit_scope()
        
        # Check the condition type
        condition_type = self.visit(node.condition)
        if condition_type != "boolean":
            self.errors.append(f"Do-while condition must be a boolean, got {condition_type}")
            return
        
        self.in_loop = False
    
    def visit_breakstatement(self, node: BreakStatement) -> None:
        """
        Visit a BreakStatement node (TIMEOUT).
        
        Args:
            node: The BreakStatement node to visit
            
        Returns:
            None
        """
        if not self.in_loop and not self.in_switch:
            self.errors.append("Break statement must be inside a loop or switch statement")
    
    def visit_continuestatement(self, node: ContinueStatement) -> None:
        """
        Visit a ContinueStatement node (RESUME).
        
        Args:
            node: The ContinueStatement node to visit
            
        Returns:
            None
        """
        if not self.in_loop:
            self.errors.append("Continue statement must be inside a loop")
    
    def visit_returnstatement(self, node: ReturnStatement) -> None:
        """
        Visit a ReturnStatement node (REBOUND).
        
        Args:
            node: The ReturnStatement node to visit
            
        Returns:
            None
        """
        if not self.current_function:
            self.errors.append("Return statement must be inside a function")
            return
        
        symbol = self.symbol_table.lookup(self.current_function)
        if not symbol or not symbol.is_function:
            self.errors.append(f"Undefined function: {self.current_function}")
            return
        
        if node.value:
            value_type = self.visit(node.value)
            if value_type != symbol.return_type:
                self.errors.append(f"Return type mismatch: expected {symbol.return_type}, got {value_type}")
        elif symbol.return_type != "void":
            self.errors.append(f"Function {self.current_function} must return a value of type {symbol.return_type}")
    
    def visit_functiondeclaration(self, node: FunctionDeclaration) -> None:
        """
        Visit a FunctionDeclaration node (WILT).
        
        Args:
            node: The FunctionDeclaration node to visit
            
        Returns:
            None
        """
        # Check if function is already defined
        if self.symbol_table.lookup(node.name):
            self.errors.append(f"Function {node.name} is already defined")
            return
        
        # Create a new symbol for the function
        symbol = self.symbol_table.define(node.name, node.return_type)
        symbol.is_function = True
        symbol.parameters = node.parameters
        symbol.return_type = node.return_type
        
        # Enter the function's scope
        self.symbol_table.enter_scope(node.name)
        self.current_function = node.name
        
        # Define the parameters in the function's scope
        for param in node.parameters:
            self.symbol_table.define(param.name, param.type)
        
        # Visit the function's body
        self.visit(node.body)
        
        self.current_function = None
        self.symbol_table.exit_scope()
    
    def visit_arraydeclaration(self, node: ArrayDeclaration) -> None:
        """
        Visit an ArrayDeclaration node (ZONE).
        
        Args:
            node: The ArrayDeclaration node to visit
            
        Returns:
            None
        """
        # Check if array is already defined
        if self.symbol_table.lookup(node.name):
            self.errors.append(f"Array {node.name} is already defined")
            return
        
        # Check the size type
        size_type = self.visit(node.size)
        if size_type != "integer":
            self.errors.append(f"Array size must be an integer, got {size_type}")
            return
        
        # Check initial values if provided
        if node.initial_values:
            for value in node.initial_values:
                value_type = self.visit(value)
                if value_type != node.type:
                    self.errors.append(f"Array element type mismatch: expected {node.type}, got {value_type}")
                    return
        
        # Create a new symbol for the array
        symbol = self.symbol_table.define(node.name, node.type)
        symbol.is_array = True
        symbol.array_size = node.size
    
    def visit_block(self, node: Block) -> None:
        """
        Visit a Block node.
        
        Args:
            node: The Block node to visit
            
        Returns:
            None
        """
        self.symbol_table.enter_scope("block")
        for statement in node.statements:
            self.visit(statement)
        self.symbol_table.exit_scope() 