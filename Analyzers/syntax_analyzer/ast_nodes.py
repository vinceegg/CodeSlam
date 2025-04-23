from typing import List, Optional, Union

class Node:
    """Base class for all AST nodes"""
    pass

class Program(Node):
    def __init__(self, global_decl: 'GlobalDecl', function_def: 'FunctionDef', team_block: 'TeamBlock'):
        self.global_decl = global_decl
        self.function_def = function_def
        self.team_block = team_block

class GlobalDecl(Node):
    def __init__(self, declarations: List['GlobalDeclaration']):
        self.declarations = declarations

class GlobalDeclaration(Node):
    def __init__(self, declaration: Union['VariableDec', 'ConstDec', 'ArrayDec']):
        self.declaration = declaration

class VariableDec(Node):
    def __init__(self, var_type: str, identifier: str, init_value: Optional['Expression'] = None):
        self.var_type = var_type  # Feint, Floater, Chant, or Stat
        self.identifier = identifier
        self.init_value = init_value

class ConstDec(Node):
    def __init__(self, const_type: str, identifier: str, value: 'Expression'):
        self.const_type = const_type
        self.identifier = identifier
        self.value = value

class ArrayDec(Node):
    def __init__(self, array_type: str, identifier: str, dimensions: List['Expression'], init_values: Optional[List['Expression']] = None):
        self.array_type = array_type
        self.identifier = identifier
        self.dimensions = dimensions
        self.init_values = init_values

class FunctionDef(Node):
    def __init__(self, functions: List['Function']):
        self.functions = functions

class Function(Node):
    def __init__(self, func_type: str, identifier: str, parameters: List[str], body: 'Block'):
        self.func_type = func_type  # Wilt or Dunk
        self.identifier = identifier
        self.parameters = parameters
        self.body = body

class TeamBlock(Node):
    def __init__(self, local_decl: 'LocalDecl', statements: List['Statement']):
        self.local_decl = local_decl
        self.statements = statements

class LocalDecl(Node):
    def __init__(self, declarations: List['LocalDeclaration']):
        self.declarations = declarations

class LocalDeclaration(Node):
    def __init__(self, declaration: Union['VariableDec', 'ArrayDec']):
        self.declaration = declaration

class Statement(Node):
    def __init__(self, stmt: Union['AnnounceStatement', 'InboundStatement', 'DribbleStatement', 
                                 'SwitchStatement', 'ForwardStatement', 'PlayStatement', 
                                 'RunPlayStatement', 'AssignmentStatement']):
        self.statement = stmt

class AnnounceStatement(Node):
    def __init__(self, expression: 'Expression'):
        self.expression = expression

class InboundStatement(Node):
    def __init__(self, message: str, variable: str):
        self.message = message
        self.variable = variable

class DribbleStatement(Node):
    def __init__(self, condition: 'Expression', body: 'Block', else_block: Optional['Block'] = None):
        self.condition = condition
        self.body = body
        self.else_block = else_block

class SwitchStatement(Node):
    def __init__(self, expression: 'Expression', cases: List['Case'], default: Optional['Block'] = None):
        self.expression = expression
        self.cases = cases
        self.default = default

class Case(Node):
    def __init__(self, value: 'Expression', body: 'Block'):
        self.value = value
        self.body = body

class ForwardStatement(Node):
    def __init__(self, init: 'AssignmentStatement', condition: 'Expression', 
                 update: 'AssignmentStatement', body: 'Block'):
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body

class PlayStatement(Node):
    def __init__(self, condition: 'Expression', body: 'Block'):
        self.condition = condition
        self.body = body

class RunPlayStatement(Node):
    def __init__(self, body: 'Block', condition: 'Expression'):
        self.body = body
        self.condition = condition

class AssignmentStatement(Node):
    def __init__(self, identifier: str, operator: str, value: 'Expression'):
        self.identifier = identifier
        self.operator = operator
        self.value = value

class Block(Node):
    def __init__(self, statements: List['Statement']):
        self.statements = statements

class Expression(Node):
    def __init__(self, expr: Union['BinaryOp', 'UnaryOp', 'Literal', 'Identifier', 'FunctionCall']):
        self.expression = expr

class BinaryOp(Node):
    def __init__(self, left: 'Expression', operator: str, right: 'Expression'):
        self.left = left
        self.operator = operator
        self.right = right

class UnaryOp(Node):
    def __init__(self, operator: str, operand: 'Expression'):
        self.operator = operator
        self.operand = operand

class Literal(Node):
    def __init__(self, value: Union[int, float, str, bool], type: str):
        self.value = value
        self.type = type

class Identifier(Node):
    def __init__(self, name: str):
        self.name = name

class FunctionCall(Node):
    def __init__(self, name: str, arguments: List['Expression']):
        self.name = name
        self.arguments = arguments 
        
class ArrayAccess(Node):
    def __init__(self, array: 'Expression', indices: List['Expression']):
        self.array = array
        self.indices = indices

class ArrayDeclaration(Node):
    def __init__(self, var_type: str, identifier: str, dimensions: List['Expression'], initial_values: Optional[List['Expression']] = None):
        self.var_type = var_type
        self.identifier = identifier
        self.dimensions = dimensions
        self.initial_values = initial_values

