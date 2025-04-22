from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum, auto
from ..lexical_analyzer.tokens import TokenType, Token

# AST Node Types
class NodeType(Enum):
    PROGRAM = auto()
    TEAM = auto()  # Main function
    STATEMENT = auto()
    EXPRESSION = auto()
    LITERAL = auto()
    IDENTIFIER = auto()
    BINARY_OP = auto()
    UNARY_OP = auto()
    FUNCTION_CALL = auto()
    VARIABLE_DECLARATION = auto()
    ASSIGNMENT = auto()
    IF_STATEMENT = auto()  # DRIBBLE
    ELSE_STATEMENT = auto()  # SHOOT
    ELSE_IF_STATEMENT = auto()  # PASS
    SWITCH_STATEMENT = auto()  # SWITCH
    CASE_STATEMENT = auto()  # GET
    DEFAULT_STATEMENT = auto()  # DEFAULT
    WHILE_LOOP = auto()  # PLAY
    FOR_LOOP = auto()  # FORWARD
    DO_WHILE_LOOP = auto()  # RUN
    BREAK_STATEMENT = auto()  # TIMEOUT
    CONTINUE_STATEMENT = auto()  # RESUME
    RETURN_STATEMENT = auto()  # REBOUND
    BLOCK = auto()
    FUNCTION_DECLARATION = auto()  # WILT
    ARRAY_DECLARATION = auto()  # ZONE

# Base AST Node class
@dataclass
class ASTNode:
    node_type: NodeType
    line_number: int
    column: int

# Expression nodes
@dataclass
class Expression(ASTNode):
    pass

@dataclass
class Literal(Expression):
    value: Any
    literal_type: str  # 'FEINTLIT', 'FLOATERLIT', 'CHANTLIT', 'WIN', 'LOSS'

@dataclass
class Identifier(Expression):
    name: str

@dataclass
class BinaryOperation(Expression):
    left: Expression
    operator: str  # ADD, SUB, MUL, DIV, MOD, etc.
    right: Expression

@dataclass
class UnaryOperation(Expression):
    operator: str  # NEG, NOT_OP
    operand: Expression

@dataclass
class FunctionCall(Expression):
    function_name: str
    arguments: List[Expression]

@dataclass
class ArrayAccess(Expression):
    array_name: str
    index: Expression

# Statement nodes
@dataclass
class Statement(ASTNode):
    pass

@dataclass
class VariableDeclaration(Statement):
    variable_name: str
    variable_type: Optional[str]  # FEINT, CHANT, FLOATER, STAT, CONST
    initial_value: Optional[Expression]

@dataclass
class Assignment(Statement):
    variable_name: str
    operator: str  # ASSIGN, ADD_ASSIGN, SUB_ASSIGN, etc.
    value: Expression

@dataclass
class IfStatement(Statement):
    condition: Expression
    then_branch: 'Block'
    else_branch: Optional['Block']

@dataclass
class ElseStatement(Statement):
    body: 'Block'

@dataclass
class ElseIfStatement(Statement):
    condition: Expression
    body: 'Block'

@dataclass
class SwitchStatement(Statement):
    expression: Expression
    cases: List['CaseStatement']
    default_case: Optional['DefaultStatement']

@dataclass
class CaseStatement(Statement):
    value: Expression
    body: 'Block'

@dataclass
class DefaultStatement(Statement):
    body: 'Block'

@dataclass
class WhileLoop(Statement):
    condition: Expression
    body: 'Block'

@dataclass
class ForLoop(Statement):
    initializer: Statement
    condition: Expression
    increment: Statement
    body: 'Block'

@dataclass
class DoWhileLoop(Statement):
    body: 'Block'
    condition: Expression

@dataclass
class BreakStatement(Statement):
    pass

@dataclass
class ContinueStatement(Statement):
    pass

@dataclass
class ReturnStatement(Statement):
    value: Optional[Expression]

@dataclass
class Block(Statement):
    statements: List[Statement]

@dataclass
class FunctionDeclaration(Statement):
    function_name: str
    return_type: str  # DUNK, FEINT, CHANT, FLOATER, STAT
    parameters: List[Dict[str, str]]  # List of {name, type} dictionaries
    body: 'Block'

@dataclass
class ArrayDeclaration(Statement):
    array_name: str
    element_type: str  # FEINT, CHANT, FLOATER, STAT
    size: Expression
    initial_values: Optional[List[Expression]]

# Program structure nodes
@dataclass
class Program(ASTNode):
    statements: List[Statement]

@dataclass
class Team(ASTNode):
    name: str
    players: List['Player']

@dataclass
class Player(ASTNode):
    name: str
    stats: Dict[str, Expression]

class ASTBuilder:
    def __init__(self):
        self.current_line = 0
        self.current_column = 0
        self.tokens = []
        self.current_token_index = 0

    def build(self, tokens: List[Token]) -> Program:
        """
        Build an AST from a list of tokens.
        
        Args:
            tokens: List of tokens from the lexical analyzer
            
        Returns:
            Program node representing the root of the AST
        """
        self.tokens = tokens
        self.current_token_index = 0
        statements = []
        
        while self.current_token_index < len(self.tokens):
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
        
        return Program(
            node_type=NodeType.PROGRAM,
            line_number=1,
            column=1,
            statements=statements
        )

    def parse_statement(self) -> Optional[Statement]:
        """Parse a statement from the current token position."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        token = self.tokens[self.current_token_index]
        self.current_line = token.line_number
        self.current_column = token.column
        
        # Handle different statement types based on token type
        if token.type == TokenType.TEAM:
            return self.parse_team_declaration()
        elif token.type == TokenType.DRIBBLE:
            return self.parse_if_statement()
        elif token.type == TokenType.SHOOT:
            return self.parse_else_statement()
        elif token.type == TokenType.PASS:
            return self.parse_else_if_statement()
        elif token.type == TokenType.SWITCH:
            return self.parse_switch_statement()
        elif token.type == TokenType.FORWARD:
            return self.parse_for_loop()
        elif token.type == TokenType.PLAY:
            return self.parse_while_loop()
        elif token.type == TokenType.RUN:
            return self.parse_do_while_loop()
        elif token.type == TokenType.TIMEOUT:
            return self.parse_break_statement()
        elif token.type == TokenType.RESUME:
            return self.parse_continue_statement()
        elif token.type == TokenType.REBOUND:
            return self.parse_return_statement()
        elif token.type == TokenType.WILT:
            return self.parse_function_declaration()
        elif token.type == TokenType.ZONE:
            return self.parse_array_declaration()
        elif token.type in [TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT, TokenType.CONST]:
            return self.parse_variable_declaration()
        elif token.type == TokenType.VAR_INIT:
            return self.parse_assignment()
        else:
            # Skip tokens that don't start a statement
            self.current_token_index += 1
            return None

    def parse_expression(self) -> Optional[Expression]:
        """Parse an expression from the current token position."""
        return self.parse_binary_expression()

    def parse_binary_expression(self, precedence: int = 0) -> Optional[Expression]:
        """Parse a binary expression with operator precedence."""
        left = self.parse_primary_expression()
        if not left:
            return None

        while self.current_token_index < len(self.tokens):
            token = self.tokens[self.current_token_index]
            current_precedence = self.get_operator_precedence(token.type)
            
            if current_precedence <= precedence:
                break
                
            self.current_token_index += 1
            right = self.parse_binary_expression(current_precedence)
            if not right:
                return None
                
            left = BinaryOperation(
                node_type=NodeType.BINARY_OP,
                line_number=token.line_number,
                column=token.column,
                left=left,
                operator=token.type.name,
                right=right
            )
            
        return left

    def parse_primary_expression(self) -> Optional[Expression]:
        """Parse a primary expression (literal, identifier, parenthesized expression)."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        token = self.tokens[self.current_token_index]
        self.current_line = token.line_number
        self.current_column = token.column
        
        if token.type == TokenType.FEINTLIT or token.type == TokenType.FLOATERLIT:
            return self.parse_numeric_literal()
        elif token.type == TokenType.CHANTLIT:
            return self.parse_string_literal()
        elif token.type == TokenType.WIN or token.type == TokenType.LOSS:
            return self.parse_boolean_literal()
        elif token.type == TokenType.VAR_INIT:
            return self.parse_identifier()
        elif token.type == TokenType.LEFT_PAREN:
            return self.parse_parenthesized_expression()
        elif token.type == TokenType.NEGATIVE or token.type == TokenType.NOT_OP:
            return self.parse_unary_operation()
        else:
            return None

    def get_operator_precedence(self, token_type: TokenType) -> int:
        """Get the precedence level of an operator."""
        precedence_map = {
            TokenType.MUL: 5,
            TokenType.DIV: 5,
            TokenType.MOD: 5,
            TokenType.ADD: 4,
            TokenType.SUB: 4,
            TokenType.GREATER_THAN: 3,
            TokenType.LESS_THAN: 3,
            TokenType.GREATER_EQUAL: 3,
            TokenType.LESS_EQUAL: 3,
            TokenType.EQUAL: 2,
            TokenType.NOT_EQUAL: 2,
            TokenType.AND_OP: 1,
            TokenType.OR_OP: 1,
        }
        return precedence_map.get(token_type, 0)

    def parse_unary_operation(self) -> Optional[Expression]:
        """Parse a unary operation (NOT or negative)."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        
        operand = self.parse_primary_expression()
        if not operand:
            return None
            
        return UnaryOperation(
            node_type=NodeType.UNARY_OP,
            line_number=token.line_number,
            column=token.column,
            operator=token.type.name,
            operand=operand
        )

    def parse_parenthesized_expression(self) -> Optional[Expression]:
        """Parse a parenthesized expression."""
        if not self.expect(TokenType.LEFT_PAREN, "Expected '('"):
            return None
            
        expr = self.parse_expression()
        if not expr:
            return None
            
        if not self.expect(TokenType.RIGHT_PAREN, "Expected ')'"):
            return None
            
        return expr

    def parse_team_declaration(self) -> Optional[Statement]:
        """Parse a team declaration (main function)."""
        if not self.expect(TokenType.TEAM, "Expected 'TEAM'"):
            return None

        if not self.expect(TokenType.LEFT_PAREN, "Expected '('"):
            return None

        if not self.expect(TokenType.RIGHT_PAREN, "Expected ')'"):
            return None

        body = self.parse_block()
        if not body:
            return None

        return Team(
            node_type=NodeType.TEAM,
            line_number=self.current_line,
            column=self.current_column,
            body=body
        )

    def parse_if_statement(self) -> Optional[Statement]:
        """Parse an if statement (DRIBBLE)."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        start_token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        
        # Parse condition
        if not self.expect(TokenType.LEFT_PAREN, "Expected '(' after DRIBBLE"):
            return None
            
        # Parse condition expression
        left = self.parse_expression()
        if not left:
            return None
            
        if self.current_token_index >= len(self.tokens):
            return None
            
        op_token = self.tokens[self.current_token_index]
        if op_token.type not in [TokenType.GREATER_THAN, TokenType.LESS_THAN, TokenType.EQUAL, TokenType.NOT_EQUAL, TokenType.GREATER_EQUAL, TokenType.LESS_EQUAL]:
            return None
        self.current_token_index += 1
        
        right = self.parse_expression()
        if not right:
            return None
            
        condition = BinaryOperation(
            node_type=NodeType.BINARY_OP,
            line_number=op_token.line_number,
            column=op_token.column,
            left=left,
            operator=op_token.type.name,
            right=right
        )
        
        if not self.expect(TokenType.RIGHT_PAREN, "Expected ')' after condition"):
            return None
            
        # Parse then branch
        if not self.expect(TokenType.CODE_BLOCK_LEFT, "Expected '{' after if condition"):
            return None
            
        then_branch = Block(
            node_type=NodeType.BLOCK,
            line_number=start_token.line_number,
            column=start_token.column,
            statements=[]
        )
        
        # Parse else branch if present
        else_branch = None
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type == TokenType.SHOOT:
            self.current_token_index += 1
            if not self.expect(TokenType.CODE_BLOCK_LEFT, "Expected '{' after SHOOT"):
                return None
            else_branch = Block(
                node_type=NodeType.BLOCK,
                line_number=start_token.line_number,
                column=start_token.column,
                statements=[]
            )
            
        return IfStatement(
            node_type=NodeType.IF_STATEMENT,
            line_number=start_token.line_number,
            column=start_token.column,
            condition=condition,
            then_branch=then_branch,
            else_branch=else_branch
        )

    def parse_else_statement(self) -> Optional[Statement]:
        """Parse an else statement."""
        if not self.expect(TokenType.ELSE, "Expected 'ELSE'"):
            return None

        body = self.parse_block()
        if not body:
            return None

        return ElseStatement(
            node_type=NodeType.ELSE_STATEMENT,
            line_number=self.current_line,
            column=self.current_column,
            body=body
        )

    def parse_else_if_statement(self) -> Optional[Statement]:
        """Parse an else-if statement."""
        if not self.expect(TokenType.ELSE_IF, "Expected 'ELSE IF'"):
            return None

        if not self.expect(TokenType.LEFT_PAREN, "Expected '('"):
            return None

        condition = self.parse_expression()
        if not condition:
            return None

        if not self.expect(TokenType.RIGHT_PAREN, "Expected ')'"):
            return None

        body = self.parse_block()
        if not body:
            return None

        return ElseIfStatement(
            node_type=NodeType.ELSE_IF_STATEMENT,
            line_number=self.current_line,
            column=self.current_column,
            condition=condition,
            body=body
        )

    def parse_switch_statement(self) -> Optional[Statement]:
        """Parse a switch statement."""
        if not self.expect(TokenType.SWITCH, "Expected 'SWITCH'"):
            return None

        if not self.expect(TokenType.LEFT_PAREN, "Expected '('"):
            return None

        condition = self.parse_expression()
        if not condition:
            return None

        if not self.expect(TokenType.RIGHT_PAREN, "Expected ')'"):
            return None

        if not self.expect(TokenType.LEFT_BRACE, "Expected '{'"):
            return None

        cases = []
        default_case = None

        while self.current_token_index < len(self.tokens):
            token = self.tokens[self.current_token_index]
            
            if token.type == TokenType.RIGHT_BRACE:
                self.current_token_index += 1
                break
            elif token.type == TokenType.CASE:
                case = self.parse_case_statement()
                if case:
                    cases.append(case)
            elif token.type == TokenType.DEFAULT:
                default_case = self.parse_default_statement()
            else:
                self.current_token_index += 1

        return SwitchStatement(
            node_type=NodeType.SWITCH_STATEMENT,
            line_number=self.current_line,
            column=self.current_column,
            condition=condition,
            cases=cases,
            default_case=default_case
        )

    def parse_case_statement(self) -> Optional[Statement]:
        """Parse a case statement."""
        if not self.expect(TokenType.CASE, "Expected 'CASE'"):
            return None

        value = self.parse_expression()
        if not value:
            return None

        if not self.expect(TokenType.COLON, "Expected ':'"):
            return None

        body = self.parse_block()
        if not body:
            return None

        return CaseStatement(
            node_type=NodeType.CASE_STATEMENT,
            line_number=self.current_line,
            column=self.current_column,
            value=value,
            body=body
        )

    def parse_default_statement(self) -> Optional[Statement]:
        """Parse a default statement."""
        if not self.expect(TokenType.DEFAULT, "Expected 'DEFAULT'"):
            return None

        if not self.expect(TokenType.COLON, "Expected ':'"):
            return None

        body = self.parse_block()
        if not body:
            return None

        return DefaultStatement(
            node_type=NodeType.DEFAULT_STATEMENT,
            line_number=self.current_line,
            column=self.current_column,
            body=body
        )

    def parse_for_loop(self) -> Optional[Statement]:
        """Parse a for loop."""
        if not self.expect(TokenType.FOR, "Expected 'FOR'"):
            return None

        if not self.expect(TokenType.LEFT_PAREN, "Expected '('"):
            return None

        initialization = self.parse_statement()
        if not initialization:
            return None

        condition = self.parse_expression()
        if not condition:
            return None

        if not self.expect(TokenType.SEMICOLON, "Expected ';'"):
            return None

        increment = self.parse_statement()
        if not increment:
            return None

        if not self.expect(TokenType.RIGHT_PAREN, "Expected ')'"):
            return None

        body = self.parse_block()
        if not body:
            return None

        return ForLoop(
            node_type=NodeType.FOR_LOOP,
            line_number=self.current_line,
            column=self.current_column,
            initialization=initialization,
            condition=condition,
            increment=increment,
            body=body
        )

    def parse_while_loop(self) -> Optional[Statement]:
        """Parse a while loop."""
        if not self.expect(TokenType.WHILE, "Expected 'WHILE'"):
            return None

        if not self.expect(TokenType.LEFT_PAREN, "Expected '('"):
            return None

        condition = self.parse_expression()
        if not condition:
            return None

        if not self.expect(TokenType.RIGHT_PAREN, "Expected ')'"):
            return None

        body = self.parse_block()
        if not body:
            return None

        return WhileLoop(
            node_type=NodeType.WHILE_LOOP,
            line_number=self.current_line,
            column=self.current_column,
            condition=condition,
            body=body
        )

    def parse_do_while_loop(self) -> Optional[Statement]:
        """Parse a do-while loop."""
        if not self.expect(TokenType.DO, "Expected 'DO'"):
            return None

        body = self.parse_block()
        if not body:
            return None

        if not self.expect(TokenType.WHILE, "Expected 'WHILE'"):
            return None

        if not self.expect(TokenType.LEFT_PAREN, "Expected '('"):
            return None

        condition = self.parse_expression()
        if not condition:
            return None

        if not self.expect(TokenType.RIGHT_PAREN, "Expected ')'"):
            return None

        return DoWhileLoop(
            node_type=NodeType.DO_WHILE_LOOP,
            line_number=self.current_line,
            column=self.current_column,
            condition=condition,
            body=body
        )

    def parse_break_statement(self) -> Optional[Statement]:
        """Parse a break statement (TIMEOUT)."""
        if not self.expect(TokenType.BREAK, "Expected 'BREAK'"):
            return None

        if not self.expect(TokenType.SEMICOLON, "Expected ';'"):
            return None

        return BreakStatement(
            node_type=NodeType.BREAK_STATEMENT,
            line_number=self.current_line,
            column=self.current_column
        )

    def parse_continue_statement(self) -> Optional[Statement]:
        """Parse a continue statement (FASTBREAK)."""
        if not self.expect(TokenType.CONTINUE, "Expected 'CONTINUE'"):
            return None

        if not self.expect(TokenType.SEMICOLON, "Expected ';'"):
            return None

        return ContinueStatement(
            node_type=NodeType.CONTINUE_STATEMENT,
            line_number=self.current_line,
            column=self.current_column
        )

    def parse_return_statement(self) -> Optional[Statement]:
        """Parse a return statement (REBOUND)."""
        if not self.expect(TokenType.REBOUND, "Expected 'REBOUND'"):
            return None

        # Parse return value if present
        value = None
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type != TokenType.SEMICOLON:
            value = self.parse_expression()
            if not value:
                return None

        if not self.expect(TokenType.SEMICOLON, "Expected ';'"):
            return None

        return ReturnStatement(
            node_type=NodeType.RETURN_STATEMENT,
            line_number=self.current_line,
            column=self.current_column,
            value=value
        )

    def parse_function_declaration(self) -> Optional[Statement]:
        """Parse a function declaration (WILT)."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        start_token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        
        # Parse function name
        if self.current_token_index >= len(self.tokens):
            return None
        name_token = self.tokens[self.current_token_index]
        if name_token.type != TokenType.VAR_INIT:
            return None
        self.current_token_index += 1
        
        # Parse parameters
        if not self.expect(TokenType.LEFT_PAREN, "Expected '(' after function name"):
            return None
            
        parameters = []
        while self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type != TokenType.RIGHT_PAREN:
            # Parse parameter type
            if self.current_token_index >= len(self.tokens):
                return None
            param_type = self.tokens[self.current_token_index]
            if param_type.type not in [TokenType.FEINT, TokenType.CHANT, TokenType.FLOATER, TokenType.STAT]:
                return None
            self.current_token_index += 1
            
            # Parse parameter name
            if self.current_token_index >= len(self.tokens):
                return None
            param_name = self.tokens[self.current_token_index]
            if param_name.type != TokenType.VAR_INIT:
                return None
            self.current_token_index += 1
            
            parameters.append({"name": param_name.value, "type": param_type.type.name})
            
            # Check for comma
            if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type == TokenType.COMMA:
                self.current_token_index += 1
                
        if not self.expect(TokenType.RIGHT_PAREN, "Expected ')' after parameters"):
            return None
            
        # Parse return type
        if self.current_token_index >= len(self.tokens):
            return None
        return_type = self.tokens[self.current_token_index]
        if return_type.type != TokenType.DUNK:
            return None
        self.current_token_index += 1
        
        # Parse function body
        if not self.expect(TokenType.CODE_BLOCK_LEFT, "Expected '{' after function declaration"):
            return None
            
        body = self.parse_block()
        if not body:
            return None
            
        return FunctionDeclaration(
            node_type=NodeType.FUNCTION_DECLARATION,
            line_number=start_token.line_number,
            column=start_token.column,
            function_name=name_token.value,
            return_type=return_type.type.name,
            parameters=parameters,
            body=body
        )

    def parse_array_declaration(self) -> Optional[Statement]:
        """Parse an array declaration."""
        if not self.expect_type():
            return None

        identifier = self.parse_identifier()
        if not identifier:
            return None

        if not self.expect(TokenType.ZONE, "Expected 'ZONE'"):
            return None

        if not self.expect(TokenType.LEFT_BRACKET, "Expected '['"):
            return None

        size = self.parse_expression()
        if not size:
            return None

        if not self.expect(TokenType.RIGHT_BRACKET, "Expected ']'"):
            return None

        if not self.expect_type():
            return None

        # Check for initialization
        initial_values = None
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type == TokenType.ASSIGN:
            self.current_token_index += 1  # Skip ASSIGN token
            
            if not self.expect(TokenType.LEFT_BRACE, "Expected '{'"):
                return None
                
            initial_values = []
            while self.current_token_index < len(self.tokens):
                if self.tokens[self.current_token_index].type == TokenType.RIGHT_BRACE:
                    self.current_token_index += 1
                    break
                    
                value = self.parse_expression()
                if not value:
                    return None
                    
                initial_values.append(value)
                
                # Skip comma if present
                if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type == TokenType.COMMA:
                    self.current_token_index += 1

        if not self.expect(TokenType.SEMICOLON, "Expected ';'"):
            return None

        return ArrayDeclaration(
            node_type=NodeType.ARRAY_DECLARATION,
            line_number=self.current_line,
            column=self.current_column,
            array_name=identifier.name,
            element_type=type_token.type.name,
            size=size,
            initial_values=initial_values
        )

    def parse_variable_declaration(self) -> Optional[Statement]:
        """Parse a variable declaration."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        # Get the type token (FEINT, CHANT, FLOATER, STAT, CONST)
        type_token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        
        # Get the variable name
        if self.current_token_index >= len(self.tokens):
            return None
        name_token = self.tokens[self.current_token_index]
        if name_token.type != TokenType.VAR_INIT:
            return None
        self.current_token_index += 1
        
        # Check for initialization
        initial_value = None
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type == TokenType.ASSIGN:
            self.current_token_index += 1
            initial_value = self.parse_expression()
            
        # Expect semicolon
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type == TokenType.SEMICOLON:
            self.current_token_index += 1
            
        return VariableDeclaration(
            node_type=NodeType.VARIABLE_DECLARATION,
            line_number=type_token.line_number,
            column=type_token.column,
            variable_name=name_token.value,
            variable_type=type_token.type.name,
            initial_value=initial_value
        )

    def parse_assignment(self) -> Optional[Statement]:
        """Parse an assignment statement."""
        # Parse the left-hand side (variable name or array access)
        left = self.parse_identifier()
        if not left:
            return None
            
        # Check if this is an array access
        array_access = None
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type == TokenType.LEFT_BRACKET:
            self.current_token_index += 1  # Skip '['
            index = self.parse_expression()
            if not index:
                return None
                
            if not self.expect(TokenType.RIGHT_BRACKET, "Expected ']'"):
                return None
                
            array_access = ArrayAccess(
                node_type=NodeType.ARRAY_ACCESS,
                line_number=left.line_number,
                column=left.column,
                array_name=left.name,
                index=index
            )

        # Get the assignment operator
        if self.current_token_index >= len(self.tokens):
            return None
            
        op_token = self.tokens[self.current_token_index]
        if op_token.type not in [TokenType.ASSIGN, TokenType.ADD_ASSIGN, TokenType.SUB_ASSIGN, 
                                TokenType.MUL_ASSIGN, TokenType.DIV_ASSIGN, TokenType.MOD_ASSIGN]:
            return None
            
        self.current_token_index += 1
        
        # Parse the right-hand side expression
        value = self.parse_expression()
        if not value:
            return None
            
        if not self.expect(TokenType.SEMICOLON, "Expected ';'"):
            return None

        return Assignment(
            node_type=NodeType.ASSIGNMENT,
            line_number=left.line_number,
            column=left.column,
            variable_name=array_access.array_name if array_access else left.name,
            operator=op_token.type.name,
            value=value
        )

    def parse_block(self) -> Optional[Block]:
        """Parse a block of statements."""
        if not self.expect(TokenType.CODE_BLOCK_LEFT, "Expected '{'"):
            return None

        statements = []
        while self.current_token_index < len(self.tokens):
            if self.tokens[self.current_token_index].type == TokenType.CODE_BLOCK_RIGHT:
                self.current_token_index += 1
                return Block(
                    node_type=NodeType.BLOCK,
                    line_number=self.current_line,
                    column=self.current_column,
                    statements=statements
                )

            statement = self.parse_statement()
            if statement:
                statements.append(statement)
            else:
                # Skip invalid statements to continue parsing
                self.current_token_index += 1

        return None  # Missing closing brace

    def parse_numeric_literal(self) -> Optional[Expression]:
        """Parse a numeric literal (FEINTLIT, FLOATERLIT)."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        
        try:
            value = float(token.value) if token.type == TokenType.FLOATERLIT else int(token.value)
            return Literal(
                node_type=NodeType.LITERAL,
                line_number=token.line_number,
                column=token.column,
                value=value,
                literal_type=token.type.name
            )
        except ValueError:
            return None

    def parse_string_literal(self) -> Optional[Expression]:
        """Parse a string literal (CHANTLIT)."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        
        return Literal(
            node_type=NodeType.LITERAL,
            line_number=token.line_number,
            column=token.column,
            value=token.value,
            literal_type=token.type.name
        )

    def parse_boolean_literal(self) -> Optional[Expression]:
        """Parse a boolean literal (WIN, LOSS)."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        
        value = token.type == TokenType.WIN
        return Literal(
            node_type=NodeType.LITERAL,
            line_number=token.line_number,
            column=token.column,
            value=value,
            literal_type=token.type.name
        )

    def parse_identifier(self) -> Optional[Expression]:
        """Parse an identifier."""
        if self.current_token_index >= len(self.tokens):
            return None
            
        token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        
        return Identifier(
            node_type=NodeType.IDENTIFIER,
            line_number=token.line_number,
            column=token.column,
            name=token.value
        )

    def expect(self, expected_type: TokenType, error_message: str) -> bool:
        """
        Check if the current token matches the expected type and advance.
        
        Args:
            expected_type: The expected token type
            error_message: Error message to log if the token doesn't match
            
        Returns:
            True if the token matches and was consumed, False otherwise
        """
        if self.current_token_index >= len(self.tokens):
            return False

        token = self.tokens[self.current_token_index]
        if token.type != expected_type:
            return False

        self.current_token_index += 1
        return True

    def peek(self) -> Optional[Token]:
        """Look at the next token without consuming it."""
        if self.current_token_index >= len(self.tokens):
            return None
        return self.tokens[self.current_token_index]

    def advance(self) -> Optional[Token]:
        """Consume and return the next token."""
        if self.current_token_index >= len(self.tokens):
            return None
        token = self.tokens[self.current_token_index]
        self.current_token_index += 1
        return token 