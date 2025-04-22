from typing import Any, Dict, List, Optional
from .ast_visitor import ASTVisitor
from .ast_builder import (
    ASTNode, Program, Team, Player, Statement, Expression,
    Literal, Identifier, BinaryOperation, UnaryOperation, FunctionCall,
    VariableDeclaration, Assignment, IfStatement, WhileLoop, ForLoop,
    ReturnStatement, Block
)

class ASTPrettyPrinter(ASTVisitor):
    """
    Visitor class for pretty printing the AST.
    """
    
    def __init__(self, indent_size: int = 2):
        """
        Initialize the pretty printer.
        
        Args:
            indent_size: The number of spaces to use for indentation
        """
        self.indent_size = indent_size
        self.indent_level = 0
        self.output = []
    
    def indent(self) -> None:
        """Increase the indentation level."""
        self.indent_level += 1
    
    def dedent(self) -> None:
        """Decrease the indentation level."""
        self.indent_level -= 1
    
    def write(self, text: str) -> None:
        """
        Write text to the output with proper indentation.
        
        Args:
            text: The text to write
        """
        if text.strip():
            self.output.append(" " * (self.indent_level * self.indent_size) + text)
        else:
            self.output.append("")
    
    def get_output(self) -> str:
        """
        Get the pretty-printed output.
        
        Returns:
            The pretty-printed output as a string
        """
        return "\n".join(self.output)
    
    def visit_program(self, node: Program) -> str:
        """
        Visit a Program node.
        
        Args:
            node: The Program node to visit
            
        Returns:
            The pretty-printed Program node
        """
        self.write("Program:")
        self.indent()
        for statement in node.statements:
            self.visit(statement)
        self.dedent()
        return self.get_output()
    
    def visit_team(self, node: Team) -> str:
        """
        Visit a Team node.
        
        Args:
            node: The Team node to visit
            
        Returns:
            The pretty-printed Team node
        """
        self.write(f"Team: {node.name}")
        self.indent()
        for player in node.players:
            self.visit(player)
        self.dedent()
        return self.get_output()
    
    def visit_player(self, node: Player) -> str:
        """
        Visit a Player node.
        
        Args:
            node: The Player node to visit
            
        Returns:
            The pretty-printed Player node
        """
        self.write(f"Player: {node.name}")
        self.indent()
        for stat_name, stat_value in node.stats.items():
            self.write(f"{stat_name}:")
            self.indent()
            self.visit(stat_value)
            self.dedent()
        self.dedent()
        return self.get_output()
    
    def visit_literal(self, node: Literal) -> str:
        """
        Visit a Literal node.
        
        Args:
            node: The Literal node to visit
            
        Returns:
            The pretty-printed Literal node
        """
        self.write(f"Literal({node.literal_type}): {node.value}")
        return self.get_output()
    
    def visit_identifier(self, node: Identifier) -> str:
        """
        Visit an Identifier node.
        
        Args:
            node: The Identifier node to visit
            
        Returns:
            The pretty-printed Identifier node
        """
        self.write(f"Identifier: {node.name}")
        return self.get_output()
    
    def visit_binaryoperation(self, node: BinaryOperation) -> str:
        """
        Visit a BinaryOperation node.
        
        Args:
            node: The BinaryOperation node to visit
            
        Returns:
            The pretty-printed BinaryOperation node
        """
        self.write(f"BinaryOperation: {node.operator}")
        self.indent()
        self.write("Left:")
        self.indent()
        self.visit(node.left)
        self.dedent()
        self.write("Right:")
        self.indent()
        self.visit(node.right)
        self.dedent()
        self.dedent()
        return self.get_output()
    
    def visit_unaryoperation(self, node: UnaryOperation) -> str:
        """
        Visit a UnaryOperation node.
        
        Args:
            node: The UnaryOperation node to visit
            
        Returns:
            The pretty-printed UnaryOperation node
        """
        self.write(f"UnaryOperation: {node.operator}")
        self.indent()
        self.write("Operand:")
        self.indent()
        self.visit(node.operand)
        self.dedent()
        self.dedent()
        return self.get_output()
    
    def visit_functioncall(self, node: FunctionCall) -> str:
        """
        Visit a FunctionCall node.
        
        Args:
            node: The FunctionCall node to visit
            
        Returns:
            The pretty-printed FunctionCall node
        """
        self.write(f"FunctionCall: {node.function_name}")
        self.indent()
        self.write("Arguments:")
        self.indent()
        for arg in node.arguments:
            self.visit(arg)
        self.dedent()
        self.dedent()
        return self.get_output()
    
    def visit_variabledeclaration(self, node: VariableDeclaration) -> str:
        """
        Visit a VariableDeclaration node.
        
        Args:
            node: The VariableDeclaration node to visit
            
        Returns:
            The pretty-printed VariableDeclaration node
        """
        type_str = f": {node.variable_type}" if node.variable_type else ""
        self.write(f"VariableDeclaration: {node.variable_name}{type_str}")
        if node.initial_value:
            self.indent()
            self.write("Initial Value:")
            self.indent()
            self.visit(node.initial_value)
            self.dedent()
            self.dedent()
        return self.get_output()
    
    def visit_assignment(self, node: Assignment) -> str:
        """
        Visit an Assignment node.
        
        Args:
            node: The Assignment node to visit
            
        Returns:
            The pretty-printed Assignment node
        """
        self.write(f"Assignment: {node.variable_name} =")
        self.indent()
        self.visit(node.value)
        self.dedent()
        return self.get_output()
    
    def visit_ifstatement(self, node: IfStatement) -> str:
        """
        Visit an IfStatement node.
        
        Args:
            node: The IfStatement node to visit
            
        Returns:
            The pretty-printed IfStatement node
        """
        self.write("IfStatement:")
        self.indent()
        self.write("Condition:")
        self.indent()
        self.visit(node.condition)
        self.dedent()
        self.write("Then Branch:")
        self.indent()
        self.visit(node.then_branch)
        self.dedent()
        if node.else_branch:
            self.write("Else Branch:")
            self.indent()
            self.visit(node.else_branch)
            self.dedent()
        self.dedent()
        return self.get_output()
    
    def visit_whileloop(self, node: WhileLoop) -> str:
        """
        Visit a WhileLoop node.
        
        Args:
            node: The WhileLoop node to visit
            
        Returns:
            The pretty-printed WhileLoop node
        """
        self.write("WhileLoop:")
        self.indent()
        self.write("Condition:")
        self.indent()
        self.visit(node.condition)
        self.dedent()
        self.write("Body:")
        self.indent()
        self.visit(node.body)
        self.dedent()
        self.dedent()
        return self.get_output()
    
    def visit_forloop(self, node: ForLoop) -> str:
        """
        Visit a ForLoop node.
        
        Args:
            node: The ForLoop node to visit
            
        Returns:
            The pretty-printed ForLoop node
        """
        self.write("ForLoop:")
        self.indent()
        self.write("Initializer:")
        self.indent()
        self.visit(node.initializer)
        self.dedent()
        self.write("Condition:")
        self.indent()
        self.visit(node.condition)
        self.dedent()
        self.write("Increment:")
        self.indent()
        self.visit(node.increment)
        self.dedent()
        self.write("Body:")
        self.indent()
        self.visit(node.body)
        self.dedent()
        self.dedent()
        return self.get_output()
    
    def visit_returnstatement(self, node: ReturnStatement) -> str:
        """
        Visit a ReturnStatement node.
        
        Args:
            node: The ReturnStatement node to visit
            
        Returns:
            The pretty-printed ReturnStatement node
        """
        self.write("ReturnStatement:")
        if node.value:
            self.indent()
            self.visit(node.value)
            self.dedent()
        return self.get_output()
    
    def visit_block(self, node: Block) -> str:
        """
        Visit a Block node.
        
        Args:
            node: The Block node to visit
            
        Returns:
            The pretty-printed Block node
        """
        self.write("Block:")
        self.indent()
        for statement in node.statements:
            self.visit(statement)
        self.dedent()
        return self.get_output() 