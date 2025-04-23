from rply import ParserGenerator, Token as RPLYToken
from rply.token import Token, SourcePosition
from typing import List, Optional, Union
from .ast_nodes import *
from .tokens import TokenType
from .errors import SyntaxError

class ASTBuilder:
    def __init__(self):
        # Define the grammar
        pg = ParserGenerator(
            # List of all token names
            [t.name for t in TokenType],
            precedence=[
                ('left', ['OR_OP']),
                ('left', ['AND_OP']),
                ('left', ['EQUAL', 'NOT_EQUAL']),
                ('left', ['LESS_THAN', 'GREATER_THAN', 'LESS_EQUAL', 'GREATER_EQUAL']),
                ('left', ['ADD', 'SUB']),
                ('left', ['MUL', 'DIV', 'MOD']),
                ('right', ['NOT_OP']),
                ('right', ['INCREMENT', 'DECREMENT']),
            ]
        )

        # Program structure
        @pg.production('program : global_decl function_def team_block')
        def program(p):
            return Program(p[0], p[1], p[2])

        # Global declarations
        @pg.production('global_decl : global_declaration global_decl')
        @pg.production('global_decl : ')
        def global_decl(p):
            if len(p) == 0:
                return GlobalDecl([])
            return GlobalDecl([p[0]] + p[1].declarations)

        @pg.production('global_declaration : variable_dec')
        @pg.production('global_declaration : CONST const_dec')
        @pg.production('global_declaration : ZONE array_dec')
        def global_declaration(p):
            if len(p) == 1:
                return GlobalDeclaration(p[0])
            return GlobalDeclaration(p[1])

        # Variable declarations
        @pg.production('variable_dec : FEINT VAR_INIT more_feint SEMICOLON')
        @pg.production('variable_dec : FLOATER VAR_INIT more_floater SEMICOLON')
        @pg.production('variable_dec : CHANT VAR_INIT more_chant SEMICOLON')
        @pg.production('variable_dec : STAT VAR_INIT more_stat SEMICOLON')
        def variable_dec(p):
            var_type = p[0].getstr()
            identifier = p[1].getstr()
            init_value = p[2]
            return VariableDec(var_type, identifier, init_value)

        @pg.production('more_feint : ASSIGN expression')
        @pg.production('more_feint : ')
        def more_feint(p):
            if len(p) == 0:
                return None
            return p[1]

        @pg.production('more_floater : ASSIGN expression')
        @pg.production('more_floater : ')
        def more_floater(p):
            if len(p) == 0:
                return None
            return p[1]

        @pg.production('more_chant : ASSIGN expression')
        @pg.production('more_chant : ')
        def more_chant(p):
            if len(p) == 0:
                return None
            return p[1]

        @pg.production('more_stat : ASSIGN expression')
        @pg.production('more_stat : ')
        def more_stat(p):
            if len(p) == 0:
                return None
            return p[1]

        # Constant declarations
        @pg.production('const_dec : FEINT VAR_INIT ASSIGN expression SEMICOLON')
        @pg.production('const_dec : FLOATER VAR_INIT ASSIGN expression SEMICOLON')
        @pg.production('const_dec : CHANT VAR_INIT ASSIGN expression SEMICOLON')
        @pg.production('const_dec : STAT VAR_INIT ASSIGN expression SEMICOLON')
        def const_dec(p):
            const_type = p[0].getstr()
            identifier = p[1].getstr()
            value = p[3]
            return ConstDec(const_type, identifier, value)

        # Array declarations
        @pg.production('array_dec : FEINT VAR_INIT array_dimensions SEMICOLON')
        @pg.production('array_dec : FLOATER VAR_INIT array_dimensions SEMICOLON')
        @pg.production('array_dec : CHANT VAR_INIT array_dimensions SEMICOLON')
        @pg.production('array_dec : STAT VAR_INIT array_dimensions SEMICOLON')
        def array_dec(p):
            array_type = p[0].getstr()
            identifier = p[1].getstr()
            dimensions = p[2]
            return ArrayDec(array_type, identifier, dimensions)

        @pg.production('array_dimensions : ARRAY_INDEX_LEFT expression ARRAY_INDEX_RIGHT')
        @pg.production('array_dimensions : array_dimensions ARRAY_INDEX_LEFT expression ARRAY_INDEX_RIGHT')
        def array_dimensions(p):
            if len(p) == 3:
                return [p[1]]
            return p[0] + [p[2]]

        # Function definitions
        @pg.production('function_def : WILT function_declared function_def')
        @pg.production('function_def : DUNK dunk_func_declared function_def')
        @pg.production('function_def : ')
        def function_def(p):
            if len(p) == 0:
                return FunctionDef([])
            return FunctionDef([p[1]] + p[2].functions)

        @pg.production('function_declared : type_specifier VAR_INIT LEFT_PAREN func_parameters RIGHT_PAREN CODE_BLOCK_LEFT function_statement rebound_statement CODE_BLOCK_RIGHT')
        def function_declared(p):
            return Function(p[0].getstr(), p[1].getstr(), p[3], Block(p[6] + [p[7]]))

        @pg.production('dunk_func_declared : VAR_INIT LEFT_PAREN func_parameters RIGHT_PAREN CODE_BLOCK_LEFT function_statement CODE_BLOCK_RIGHT')
        def dunk_func_declared(p):
            return Function('dunk', p[0].getstr(), p[2], Block(p[5]))

        @pg.production('func_parameters : parameter_list')
        @pg.production('func_parameters : ')
        def func_parameters(p):
            if len(p) == 0:
                return []
            return p[0]

        @pg.production('parameter_list : VAR_INIT')
        @pg.production('parameter_list : VAR_INIT COMMA parameter_list')
        def parameter_list(p):
            param = p[0].getstr()
            if len(p) == 1:
                return [param]
            return [param] + p[2]

        @pg.production('type_specifier : FEINT')
        @pg.production('type_specifier : FLOATER')
        @pg.production('type_specifier : CHANT')
        @pg.production('type_specifier : STAT')
        def type_specifier(p):
            return p[0]

        # Team block
        @pg.production('team_block : TEAM LEFT_PAREN RIGHT_PAREN CODE_BLOCK_LEFT local_decl team_statement CODE_BLOCK_RIGHT')
        def team_block(p):
            return TeamBlock(p[4], p[5])

        @pg.production('local_decl : local_declaration local_decl')
        @pg.production('local_decl : ')
        def local_decl(p):
            if len(p) == 0:
                return LocalDecl([])
            return LocalDecl([p[0]] + p[1].declarations)

        @pg.production('local_declaration : variable_dec')
        @pg.production('local_declaration : ZONE array_dec')
        def local_declaration(p):
            if len(p) == 1:
                return LocalDeclaration(p[0])
            return LocalDeclaration(p[1])

        @pg.production('team_statement : statement team_statement')
        @pg.production('team_statement : ')
        def team_statement(p):
            if len(p) == 0:
                return []
            return [p[0]] + p[1]

        # Statements
        @pg.production('statement : announce_statement')
        @pg.production('statement : inbound_statement')
        @pg.production('statement : dribble_statement')
        @pg.production('statement : switch_statement')
        @pg.production('statement : forward_statement')
        @pg.production('statement : play_statement')
        @pg.production('statement : run_play_statement')
        @pg.production('statement : VAR_INIT follow_statement SEMICOLON')
        def statement(p):
            if len(p) == 1:
                return Statement(p[0])
            return Statement(AssignmentStatement(p[0].getstr(), p[1].operator, p[1].value))

        @pg.production('follow_statement : ASSIGN expression')
        @pg.production('follow_statement : ADD_ASSIGN expression')
        @pg.production('follow_statement : SUB_ASSIGN expression')
        @pg.production('follow_statement : MUL_ASSIGN expression')
        @pg.production('follow_statement : DIV_ASSIGN expression')
        @pg.production('follow_statement : MOD_ASSIGN expression')
        def follow_statement(p):
            return AssignmentStatement(None, p[0].getstr(), p[1])

        @pg.production('announce_statement : ANNOUNCE LEFT_PAREN expression RIGHT_PAREN SEMICOLON')
        def announce_statement(p):
            return AnnounceStatement(p[2])

        @pg.production('inbound_statement : INBOUND LEFT_PAREN expression COMMA VAR_INIT RIGHT_PAREN SEMICOLON')
        def inbound_statement(p):
            return InboundStatement(p[2], p[4].getstr())

        @pg.production('dribble_statement : DRIBBLE LEFT_PAREN expression RIGHT_PAREN CODE_BLOCK_LEFT function_statement CODE_BLOCK_RIGHT else_clause')
        def dribble_statement(p):
            return DribbleStatement(p[2], Block(p[5]), p[7])

        @pg.production('else_clause : SHOOT CODE_BLOCK_LEFT function_statement CODE_BLOCK_RIGHT')
        @pg.production('else_clause : ')
        def else_clause(p):
            if len(p) == 0:
                return None
            return Block(p[2])

        @pg.production('switch_statement : SWITCH LEFT_PAREN expression RIGHT_PAREN CODE_BLOCK_LEFT case_list default_case CODE_BLOCK_RIGHT')
        def switch_statement(p):
            return SwitchStatement(p[2], p[5], p[6])

        @pg.production('case_list : case case_list')
        @pg.production('case_list : ')
        def case_list(p):
            if len(p) == 0:
                return []
            return [p[0]] + p[1]

        @pg.production('case : GET expression COLON function_statement TIMEOUT SEMICOLON')
        def case(p):
            return Case(p[1], Block(p[3]))

        @pg.production('default_case : DEFAULT COLON function_statement')
        @pg.production('default_case : ')
        def default_case(p):
            if len(p) == 0:
                return None
            return Block(p[2])

        @pg.production('forward_statement : FORWARD LEFT_PAREN VAR_INIT ASSIGN expression SEMICOLON expression SEMICOLON update_expression RIGHT_PAREN CODE_BLOCK_LEFT function_statement CODE_BLOCK_RIGHT')
        def forward_statement(p):
            return ForwardStatement(
                AssignmentStatement(p[2].getstr(), 'assign', p[4]),
                p[6],
                p[8],
                Block(p[11])
            )

        @pg.production('update_expression : VAR_INIT INCREMENT')
        @pg.production('update_expression : VAR_INIT DECREMENT')
        @pg.production('update_expression : VAR_INIT ADD_ASSIGN expression')
        def update_expression(p):
            if len(p) == 2:
                return AssignmentStatement(p[0].getstr(), p[1].getstr(), None)
            return AssignmentStatement(p[0].getstr(), p[1].getstr(), p[2])

        @pg.production('play_statement : PLAY LEFT_PAREN expression RIGHT_PAREN CODE_BLOCK_LEFT function_statement CODE_BLOCK_RIGHT')
        def play_statement(p):
            return PlayStatement(p[2], Block(p[5]))

        @pg.production('run_play_statement : RUN CODE_BLOCK_LEFT function_statement CODE_BLOCK_RIGHT PLAY LEFT_PAREN expression RIGHT_PAREN SEMICOLON')
        def run_play_statement(p):
            return RunPlayStatement(Block(p[2]), p[6])

        # Function statements
        @pg.production('function_statement : statement function_statement')
        @pg.production('function_statement : ')
        def function_statement(p):
            if len(p) == 0:
                return []
            return [p[0]] + p[1]

        @pg.production('rebound_statement : REBOUND expression SEMICOLON')
        def rebound_statement(p):
            return p[1]

        # Expressions
        @pg.production('expression : logical_expression')
        def expression(p):
            return Expression(p[0])

        @pg.production('logical_expression : relational_expression more_logical')
        def logical_expression(p):
            if p[1] is None:
                return p[0]
            return BinaryOp(p[0], p[1].operator, p[1].right)

        @pg.production('more_logical : OR_OP relational_expression more_logical')
        @pg.production('more_logical : AND_OP relational_expression more_logical')
        @pg.production('more_logical : ')
        def more_logical(p):
            if len(p) == 0:
                return None
            return BinaryOp(None, p[0].getstr(), p[1])

        @pg.production('relational_expression : arithmetic_expression more_relational')
        def relational_expression(p):
            if p[1] is None:
                return p[0]
            return BinaryOp(p[0], p[1].operator, p[1].right)

        @pg.production('more_relational : EQUAL arithmetic_expression more_relational')
        @pg.production('more_relational : NOT_EQUAL arithmetic_expression more_relational')
        @pg.production('more_relational : LESS_THAN arithmetic_expression more_relational')
        @pg.production('more_relational : GREATER_THAN arithmetic_expression more_relational')
        @pg.production('more_relational : LESS_EQUAL arithmetic_expression more_relational')
        @pg.production('more_relational : GREATER_EQUAL arithmetic_expression more_relational')
        @pg.production('more_relational : ')
        def more_relational(p):
            if len(p) == 0:
                return None
            return BinaryOp(None, p[0].getstr(), p[1])

        @pg.production('arithmetic_expression : term more_term')
        def arithmetic_expression(p):
            if p[1] is None:
                return p[0]
            return BinaryOp(p[0], p[1].operator, p[1].right)

        @pg.production('more_term : ADD term more_term')
        @pg.production('more_term : SUB term more_term')
        @pg.production('more_term : ')
        def more_term(p):
            if len(p) == 0:
                return None
            return BinaryOp(None, p[0].getstr(), p[1])

        @pg.production('term : factor more_factor')
        def term(p):
            if p[1] is None:
                return p[0]
            return BinaryOp(p[0], p[1].operator, p[1].right)

        @pg.production('more_factor : MUL factor more_factor')
        @pg.production('more_factor : DIV factor more_factor')
        @pg.production('more_factor : MOD factor more_factor')
        @pg.production('more_factor : ')
        def more_factor(p):
            if len(p) == 0:
                return None
            return BinaryOp(None, p[0].getstr(), p[1])

        @pg.production('factor : LEFT_PAREN expression RIGHT_PAREN')
        @pg.production('factor : VAR_INIT')
        @pg.production('factor : literal')
        @pg.production('factor : array_access')
        @pg.production('factor : function_call')
        def factor(p):
            if len(p) == 3:  # Parenthesized expression
                return p[1]
            elif len(p) == 1:
                if isinstance(p[0], Token) and p[0].gettokentype() == 'VAR_INIT':
                    return Identifier(p[0].getstr())
                return p[0]

        @pg.production('array_access : VAR_INIT array_dimensions')
        def array_access(p):
            return ArrayAccess(p[0].getstr(), p[1])

        @pg.production('function_call : VAR_INIT LEFT_PAREN argument_list RIGHT_PAREN')
        def function_call(p):
            return FunctionCall(p[0].getstr(), p[2])

        @pg.production('argument_list : expression')
        @pg.production('argument_list : expression COMMA argument_list')
        def argument_list(p):
            if len(p) == 1:
                return [p[0]]
            return [p[0]] + p[2]

        # Literals
        @pg.production('literal : FEINTLIT')
        @pg.production('literal : FLOATERLIT')
        @pg.production('literal : CHANTLIT')
        @pg.production('literal : WIN')
        @pg.production('literal : LOSS')
        def literal(p):
            token = p[0]
            if token.gettokentype() == 'FEINTLIT':
                return Literal(int(token.getstr()), 'feint')
            elif token.gettokentype() == 'FLOATERLIT':
                return Literal(float(token.getstr()), 'floater')
            elif token.gettokentype() == 'CHANTLIT':
                return Literal(token.getstr(), 'chant')
            else:
                return Literal(token.getstr(), 'stat')

        # Error handling
        @pg.error
        def error_handler(token):
            """Handle parsing errors with proper error reporting"""
            if token is None:
                # End of input error
                raise SyntaxError("Unexpected end of input", line_number=0, column=0)
            
            try:
                token_str = token.getstr() if hasattr(token, 'getstr') else str(token)
                source_pos = token.getsourcepos()
                
                if source_pos is None:
                    # If no source position, use default values
                    line_number = 0
                    column = 0
                else:
                    line_number = source_pos.lineno
                    column = source_pos.colno
                    
                raise SyntaxError(
                    f"Unexpected token '{token_str}' at line {line_number}, column {column}",
                    line_number=line_number,
                    column=column
                )
            except Exception as e:
                # Fallback error with default position
                raise SyntaxError(
                    f"Syntax error: {str(e)}",
                    line_number=0,
                    column=0
                )

        self.parser = pg.build()

    def parse(self, tokens: List[Token]) -> Program:
        """Parse a list of tokens into an AST"""
        if not tokens:
            raise SyntaxError("No tokens to parse", line_number=0, column=0)

        # Convert our tokens to RPLY tokens with proper source position
        rply_tokens = []
        for token in tokens:
            try:
                # Create source position if available
                source_pos = None
                if hasattr(token, 'line_number') and hasattr(token, 'column'):
                    source_pos = SourcePosition(token.line_number, token.column, 0)
                elif hasattr(token, 'source_pos'):
                    source_pos = token.source_pos

                # Create RPLY token with source position
                rply_token = RPLYToken(
                    token.type,
                    token.value,
                    source_pos=source_pos
                )
                rply_tokens.append(rply_token)
            except Exception as e:
                raise SyntaxError(
                    f"Error converting token: {str(e)}",
                    line_number=getattr(token, 'line_number', 0),
                    column=getattr(token, 'column', 0)
                )
        
        # Convert list to iterator
        token_iterator = iter(rply_tokens)
        
        try:
            return self.parser.parse(token_iterator)
        except Exception as e:
            # Handle parsing errors
            if isinstance(e, SyntaxError):
                raise e
            # Get line and column from the error if possible
            line_number = 0
            column = 0
            if hasattr(e, 'source_pos'):
                line_number = e.source_pos.lineno
                column = e.source_pos.colno
            raise SyntaxError(
                f"Parsing error: {str(e)}",
                line_number=line_number,
                column=column
            ) 