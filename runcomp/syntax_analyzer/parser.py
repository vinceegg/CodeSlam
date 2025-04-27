from rply import ParserGenerator
from lexical_analyzer.tokens import TokenType
from syntax_analyzer.ast_nodes import ASTNode

pg = ParserGenerator([token.name for token in TokenType], 
                     precedence=[('left', ['ADD', 'SUB']), ('left', ['MUL', 'DIV', "MOD"])
    ])

@pg.error
def error_handler(token):
    raise ValueError(f"Syntax error at token: '{token.gettokentype()}' (value: {token.getstr()}) on line {token.source_pos.lineno}")

# Rule 1: program → global_decl function_def team_block
@pg.production("program : global_decl function_def team_block")
def program(p):
    return ASTNode("program", children=[p[0], p[1], p[2]])

# Rule 2: global_decl → global_declaration global_decl
@pg.production("global_decl : global_declaration global_decl")
def global_decl_recursive(p):
    return ASTNode("global_decl", children=[p[0]] + p[1].children)

# Rule 3: global_decl → λ
@pg.production("global_decl : ")
def global_decl_empty(p):
    return ASTNode("global_decl", children=[])

# Rule 4: global_declaration → variable_dec
@pg.production("global_declaration : variable_dec")
def global_declaration_var(p):
    return ASTNode("global_declaration", children=[p[0]])

# Rule 5: global_declaration → CONST const_dec
@pg.production("global_declaration : CONST const_dec")
def global_declaration_const(p):
    return ASTNode("global_declaration", children=[p[1]])

# Rule 6: global_declaration → ZONE array_dec
@pg.production("global_declaration : ZONE array_dec")
def global_declaration_array(p):
    return ASTNode("global_declaration", children=[p[1]])

# Rule 7: variable_dec → feint_dec
@pg.production("variable_dec : feint_dec")
def variable_dec_feint(p):
    return ASTNode("variable_dec", children=[p[0]])

# Rule 8: variable_dec → floater_dec
@pg.production("variable_dec : floater_dec")
def variable_dec_floater(p):
    return ASTNode("variable_dec", children=[p[0]])

# Rule 9: variable_dec → chant_dec
@pg.production("variable_dec : chant_dec")
def variable_dec_chant(p):
    return ASTNode("variable_dec", children=[p[0]])

# Rule 10: variable_dec → stat_dec
@pg.production("variable_dec : stat_dec")
def variable_dec_stat(p):
    return ASTNode("variable_dec", children=[p[0]])

# Rule 11: feint_dec → FEINT VAR_INIT more_feint SEMICOLON
@pg.production("feint_dec : FEINT VAR_INIT more_feint SEMICOLON")
def feint_dec(p):
    return ASTNode("feint_dec", children=[p[1], p[2]])

# Rule 12: more_feint → λ
@pg.production("more_feint : ")
def more_feint_empty(p):
    return ASTNode("more_feint", children=[])

# Rule 13: more_feint → feint_init feint_init_end
@pg.production("more_feint : feint_init feint_init_end")
def more_feint_full(p):
    return ASTNode("more_feint", children=[p[0], p[1]])

# Rule 14: feint_init → λ
@pg.production("feint_init : ")
def feint_init_empty(p):
    return ASTNode("feint_init", children=[])

# Rule 15: feint_init → ASSIGN feint_lits
@pg.production("feint_init : ASSIGN feint_lits")
def feint_init_assign(p):
    return ASTNode("feint_init", value=p[1].value)

# Rule 16: feint_lit → FEINTLIT
@pg.production("feint_lit : FEINTLIT")
def feint_lit(p):
    return ASTNode("feint_lit", value=p[0].value)

#ADDED
# Rule 16: feint_lits → FEINTLIT
@pg.production("feint_lits : FEINTLIT")
def feint_lit(p):
    return ASTNode("feint_lits", value=p[0].value)

# Rule 16: feint_lits → NEGAFEINT
@pg.production("feint_lits : NEGAFEINT")
def feint_lit(p):
    return ASTNode("feint_lits", value=p[0].value)

# Rule 17: feint_init_end → λ
@pg.production("feint_init_end : ")
def feint_init_end_empty(p):
    return ASTNode("feint_init_end", children=[])

# Rule 18: feint_init_end → COMMA VAR_INIT more_feint
@pg.production("feint_init_end : COMMA VAR_INIT more_feint")
def feint_init_end_comma(p):
    return ASTNode("feint_init_end", children=[p[1], p[2]])

# Rule 19: floater_dec → FLOATER VAR_INIT more_floater SEMICOLON
@pg.production("floater_dec : FLOATER VAR_INIT more_floater SEMICOLON")
def floater_dec(p):
    return ASTNode("floater_dec", children=[p[1], p[2]])

# Rule 20: more_floater → λ
@pg.production("more_floater : ")
def more_floater_empty(p):
    return ASTNode("more_floater", children=[])

# Rule 21: more_floater → floater_init floater_init_end
@pg.production("more_floater : floater_init floater_init_end")
def more_floater_full(p):
    return ASTNode("more_floater", children=[p[0], p[1]])

# Rule 22: floater_init → λ
@pg.production("floater_init : ")
def floater_init_empty(p):
    return ASTNode("floater_init", children=[])

# Rule 23: floater_init → ASSIGN floater_lits
@pg.production("floater_init : ASSIGN floater_lits")
def floater_init_assign(p):
    return ASTNode("floater_init", value=p[1].value)

# Rule 24: floater_lit → FLOATERLIT
@pg.production("floater_lit : FLOATERLIT")
def floater_lit(p):
    return ASTNode("floater_lit", value=p[0].value)

# ADDED
# Rule 24: floater_lits → FLOATERLIT
@pg.production("floater_lits : FLOATERLIT")
def floater_lit(p):
    return ASTNode("floater_lits", value=p[0].value)

# Rule 24: floater_lits → FLOATERLIT
@pg.production("floater_lits : NEGAFLOATER")
def floater_lit(p):
    return ASTNode("floater_lits", value=p[0].value)

# Rule 25: floater_init_end → λ
@pg.production("floater_init_end : ")
def floater_init_end_empty(p):
    return ASTNode("floater_init_end", children=[])

# Rule 26: floater_init_end → COMMA VAR_INIT more_floater
@pg.production("floater_init_end : COMMA VAR_INIT more_floater")
def floater_init_end_comma(p):
    return ASTNode("floater_init_end", children=[p[1], p[2]])

# Rule 27: chant_dec → CHANT VAR_INIT more_chant SEMICOLON
@pg.production("chant_dec : CHANT VAR_INIT more_chant SEMICOLON")
def chant_dec(p):
    return ASTNode("chant_dec", children=[p[1], p[2]])

# Rule 28: more_chant → λ
@pg.production("more_chant : ")
def more_chant_empty(p):
    return ASTNode("more_chant", children=[])

# Rule 29: more_chant → chant_init chant_init_end
@pg.production("more_chant : chant_init chant_init_end")
def more_chant_full(p):
    return ASTNode("more_chant", children=[p[0], p[1]])

# Rule 30: chant_init → λ
@pg.production("chant_init : ")
def chant_init_empty(p):
    return ASTNode("chant_init", children=[])

# Rule 31: chant_init → ASSIGN CHANTLIT
@pg.production("chant_init : ASSIGN chant_lit")
def chant_init_assign(p):
    return ASTNode("chant_init", value=p[1].value)

# Rule 32: chant_lit → CHANTLIT
@pg.production("chant_lit : CHANTLIT")
def chant_lit(p):
    return ASTNode("chant_lit", value=p[0].value)

# Rule 33: chant_init_end → λ
@pg.production("chant_init_end : ")
def chant_init_end_empty(p):
    return ASTNode("chant_init_end", children=[])

# Rule 34: chant_init_end → COMMA VAR_INIT more_chant
@pg.production("chant_init_end : COMMA VAR_INIT more_chant")
def chant_init_end_comma(p):
    return ASTNode("chant_init_end", children=[p[1], p[2]])

# Rule 35: stat_dec → STAT VAR_INIT more_stat SEMICOLON
@pg.production("stat_dec : STAT VAR_INIT more_stat SEMICOLON")
def stat_dec(p):
    return ASTNode("stat_dec", children=[p[1], p[2]])

# Rule 36: more_stat → λ
@pg.production("more_stat : ")
def more_stat_empty(p):
    return ASTNode("more_stat", children=[])

# Rule 37: more_stat → stat_init stat_init_end
@pg.production("more_stat : stat_init stat_init_end")
def more_stat_full(p):
    return ASTNode("more_stat", children=[p[0], p[1]])

# Rule 38: stat_init → λ
@pg.production("stat_init : ")
def stat_init_empty(p):
    return ASTNode("stat_init", children=[])

# Rule 39: stat_init → ASSIGN stat_value stat_init_end
@pg.production("stat_init : ASSIGN stat_value")
def stat_init_assign(p):
    return ASTNode("stat_init", value=p[1].value)

# Rule 40: stat_value → WIN
@pg.production("stat_value : WIN")
def stat_value_win(p):
    return ASTNode("stat_value", value="Win")

# Rule 41: stat_value → LOSS
@pg.production("stat_value : LOSS")
def stat_value_loss(p):
    return ASTNode("stat_value", value="Loss")

# Rule 42: stat_init_end → λ
@pg.production("stat_init_end : ")
def stat_init_end_empty(p):
    return ASTNode("stat_init_end", children=[])

# Rule 43: stat_init_end → COMMA VAR_INIT more_stat
@pg.production("stat_init_end : COMMA VAR_INIT more_stat")
def stat_init_end_comma(p):
    return ASTNode("stat_init_end", children=[p[1], p[2]])

# Rule 44-47: const_dec → const_x
@pg.production("const_dec : const_feint")
@pg.production("const_dec : const_floater")
@pg.production("const_dec : const_chant")
@pg.production("const_dec : const_stat")
def const_dec(p):
    return ASTNode("const_dec", children=[p[0]])

# Rule 48: const_feint → FEINT VAR_INIT feint_const_init SEMICOLON
@pg.production("const_feint : FEINT VAR_INIT feint_const_init SEMICOLON")
def const_feint(p):
    return ASTNode("const_feint", children=[p[1], p[2]])

# Rule 49: feint_const_init → feint_const feint_const_end
@pg.production("feint_const_init : feint_const feint_const_end")
def feint_const_init(p):
    return ASTNode("feint_const_init", children=[p[0], p[1]])

# Rule 50: feint_const → ASSIGN feint_lits
@pg.production("feint_const : ASSIGN feint_lits")
def feint_const(p):
    return ASTNode("feint_const", value=p[1].value)

# Rule 51: feint_const_end → "," VAR_INIT feint_const_init
@pg.production("feint_const_end : COMMA VAR_INIT feint_const_init")
def feint_const_end_recurse(p):
    return ASTNode("feint_const_end", children=[p[1], p[2]])

# Rule 52: feint_const_end → λ
@pg.production("feint_const_end : ")
def feint_const_end_empty(p):
    return ASTNode("feint_const_end", children=[])

# Rule 53: const_floater → FLOATER VAR_INIT floater_const_init ;
@pg.production("const_floater : FLOATER VAR_INIT floater_const_init SEMICOLON")
def const_floater(p):
    return ASTNode("const_floater", children=[p[1], p[2]])

# Rule 54: floater_const_init → floater_const floater_const_end
@pg.production("floater_const_init : floater_const floater_const_end")
def floater_const_init(p):
    return ASTNode("floater_const_init", children=[p[0], p[1]])

# Rule 55: floater_const → = floater_lit
@pg.production("floater_const : ASSIGN floater_lits")
def floater_const(p):
    return ASTNode("floater_const", value=p[1].value)

# Rule 56: floater_const_end → "," VAR_INIT floater_const_init
@pg.production("floater_const_end : COMMA VAR_INIT floater_const_init")
def floater_const_end_recurse(p):
    return ASTNode("floater_const_end", children=[p[1], p[2]])

# Rule 57: floater_const_end → λ
@pg.production("floater_const_end : ")
def floater_const_end_empty(p):
    return ASTNode("floater_const_end", children=[])

# Rule 58: const_chant → CHANT VAR_INIT chant_const_init ;
@pg.production("const_chant : CHANT VAR_INIT chant_const_init SEMICOLON")
def const_chant(p):
    return ASTNode("const_chant", children=[p[1], p[2]])

# Rule 59: chant_const_init → chant_const chant_const_end
@pg.production("chant_const_init : chant_const chant_const_end")
def chant_const_init(p):
    return ASTNode("chant_const_init", children=[p[0], p[1]])

# Rule 60: chant_const → = chant_lit
@pg.production("chant_const : ASSIGN chant_lit")
def chant_const(p):
    return ASTNode("chant_const", value=p[1].value)

# Rule 61: chant_const_end → "," VAR_INIT chant_const_init
@pg.production("chant_const_end : COMMA VAR_INIT chant_const_init")
def chant_const_end_recurse(p):
    return ASTNode("chant_const_end", children=[p[1], p[2]])

# Rule 62: chant_const_end → λ
@pg.production("chant_const_end : ")
def chant_const_end_empty(p):
    return ASTNode("chant_const_end", children=[])

# Rule 63: const_stat → STAT VAR_INIT stat_const_init ;
@pg.production("const_stat : STAT VAR_INIT stat_const_init SEMICOLON")
def const_stat(p):
    return ASTNode("const_stat", children=[p[1], p[2]])

# Rule 64: stat_const_init → stat_const stat_const_end
@pg.production("stat_const_init : stat_const stat_const_end")
def stat_const_init(p):
    return ASTNode("stat_const_init", children=[p[0], p[1]])

# Rule 65: stat_const → = WIN | = LOSS
@pg.production("stat_const : ASSIGN stat_value")
def stat_const(p):
    return ASTNode("stat_const", children=[p[1]])

# Rule 66: stat_const_end → "," VAR_INIT stat_const_init
@pg.production("stat_const_end : COMMA VAR_INIT stat_const_init")
def stat_const_end_recurse(p):
    return ASTNode("stat_const_end", children=[p[1], p[2]])

# Rule 67: stat_const_end → λ
@pg.production("stat_const_end : ")
def stat_const_end_empty(p):
    return ASTNode("stat_const_end", children=[])

# Rule 68: array_dec → feint_array
@pg.production("array_dec : feint_array")
def array_dec_feint(p):
    return ASTNode("array_dec", children=[p[0]])

# Rule 69: array_dec → floater_array
@pg.production("array_dec : floater_array")
def array_dec_floater(p):
    return ASTNode("array_dec", children=[p[0]])

# Rule 70: array_dec → chant_array
@pg.production("array_dec : chant_array")
def array_dec_chant(p):
    return ASTNode("array_dec", children=[p[0]])

# Rule 71: feint_array → FEINT VAR_INIT [ feint_lit ] 2D_array feint_array_init ;
@pg.production("feint_array : FEINT VAR_INIT ARRAY_INDEX_LEFT feint_lit ARRAY_INDEX_RIGHT 2D_array feint_array_init SEMICOLON")
def feint_array(p):
    return ASTNode("feint_array", children=[p[1], p[3], p[5], p[6]])

# Rule 72: 2D_array → λ
@pg.production("2D_array : ")
def two_d_array_empty(p):
    return ASTNode("2D_array", children=[])

# Rule 73: 2D_array → [ feint_lit ]
@pg.production("2D_array : ARRAY_INDEX_LEFT feint_lit ARRAY_INDEX_RIGHT")
def two_d_array(p):
    return ASTNode("2D_array", children=[p[1]])

# Rule 74: feint_array_init → λ
@pg.production("feint_array_init : ")
def feint_array_init_empty(p):
    return ASTNode("feint_array_init", children=[])

# Rule 75: feint_array_init → = { feint_row }
@pg.production("feint_array_init : ASSIGN CODE_BLOCK_LEFT feint_row CODE_BLOCK_RIGHT")
def feint_array_init(p):
    return ASTNode("feint_array_init", children=[p[2]])

# Rule 76: feint_row → feint_lits more_feint_lit
@pg.production("feint_row : feint_lits more_feint_lit")
def feint_row_inline(p):
    return ASTNode("feint_row", children=[p[0]] + p[1].children)

# Rule 77: feint_row → { feint_lits more_feint_lit } 2D_feint_row
@pg.production("feint_row : CODE_BLOCK_LEFT feint_lits more_feint_lit CODE_BLOCK_RIGHT 2D_feint_row")
def feint_row_nested(p):
    return ASTNode("feint_row", children=[p[1]] + p[2].children + p[4].children)

# Rule 78: 2D_feint_row → λ
@pg.production("2D_feint_row : ")
def two_d_feint_row_empty(p):
    return ASTNode("2D_feint_row", children=[])

# Rule 79: 2D_feint_row → , { feint_lits more_feint_lit } 2D_feint_row
@pg.production("2D_feint_row : COMMA CODE_BLOCK_LEFT feint_lits more_feint_lit CODE_BLOCK_RIGHT 2D_feint_row")
def two_d_feint_row_recursive(p):
    return ASTNode("2D_feint_row", children=[p[2]] + p[3].children + p[5].children)

# Rule 80: more_feint_lit → λ
@pg.production("more_feint_lit : ")
def more_feint_lit_empty(p):
    return ASTNode("more_feint_lit", children=[])

# Rule 81: more_feint_lit → , feint_lit more_feint_lit
@pg.production("more_feint_lit : COMMA feint_lits more_feint_lit")
def more_feint_lit_recursive(p):
    return ASTNode("more_feint_lit", children=[p[1]] + p[2].children)

# Rule 82: floater_array → FLOATER VAR_INIT [ feint_lit ] 2D_array floater_array_init ;
@pg.production("floater_array : FLOATER VAR_INIT ARRAY_INDEX_LEFT feint_lit ARRAY_INDEX_RIGHT 2D_array floater_array_init SEMICOLON")
def floater_array(p):
    return ASTNode("floater_array", children=[p[1], p[3], p[5], p[6]])

# Rule 83: floater_array_init → λ
@pg.production("floater_array_init : ")
def floater_array_init_empty(p):
    return ASTNode("floater_array_init", children=[])

# Rule 84: floater_array_init → = { floater_row }
@pg.production("floater_array_init : ASSIGN CODE_BLOCK_LEFT floater_row CODE_BLOCK_RIGHT")
def floater_array_init(p):
    return ASTNode("floater_array_init", children=[p[2]])

# Rule 85: floater_row → floater_lits more_floater_lit
@pg.production("floater_row : floater_lits more_floater_lit")
def floater_row_inline(p):
    return ASTNode("floater_row", children=[p[0]] + p[1].children)

# Rule 86: floater_row → { floater_lits more_floater_lit } 2D_floater_row
@pg.production("floater_row : CODE_BLOCK_LEFT floater_lits more_floater_lit CODE_BLOCK_RIGHT 2D_floater_row")
def floater_row_nested(p):
    return ASTNode("floater_row", children=[p[1]] + p[2].children + p[4].children)

# Rule 87: 2D_floater_row → λ
@pg.production("2D_floater_row : ")
def two_d_floater_row_empty(p):
    return ASTNode("2D_floater_row", children=[])

# Rule 88: 2D_floater_row → , { floater_lits more_floater_lit } 2D_floater_row
@pg.production("2D_floater_row : COMMA CODE_BLOCK_LEFT floater_lits more_floater_lit CODE_BLOCK_RIGHT 2D_floater_row")
def two_d_floater_row_recursive(p):
    return ASTNode("2D_floater_row", children=[p[2]] + p[3].children + p[5].children)

# Rule 89: more_floater_lit → λ
@pg.production("more_floater_lit : ")
def more_floater_lit_empty(p):
    return ASTNode("more_floater_lit", children=[])

# Rule 90: more_floater_lit → , floater_lits more_floater_lit
@pg.production("more_floater_lit : COMMA floater_lits more_floater_lit")
def more_floater_lit_recursive(p):
    return ASTNode("more_floater_lit", children=[p[1]] + p[2].children)

# Rule 91: chant_array → CHANT VAR_INIT [ feint_lit ] 2D_array chant_array_init ;
@pg.production("chant_array : CHANT VAR_INIT ARRAY_INDEX_LEFT feint_lit ARRAY_INDEX_RIGHT 2D_array chant_array_init SEMICOLON")
def chant_array(p):
    return ASTNode("chant_array", children=[p[1], p[3], p[5], p[6]])

# Rule 92: chant_array_init → λ
@pg.production("chant_array_init : ")
def chant_array_init_empty(p):
    return ASTNode("chant_array_init", children=[])

# Rule 93: chant_array_init → = { chant_row }
@pg.production("chant_array_init : ASSIGN CODE_BLOCK_LEFT chant_row CODE_BLOCK_RIGHT")
def chant_array_init(p):
    return ASTNode("chant_array_init", children=[p[2]])

# Rule 94: chant_row → chant_lit more_chant_lit
@pg.production("chant_row : chant_lit more_chant_lit")
def chant_row_inline(p):
    return ASTNode("chant_row", children=[p[0]] + p[1].children)

# Rule 95: chant_row → { chant_lit more_chant_lit } 2D_chant_row
@pg.production("chant_row : CODE_BLOCK_LEFT chant_lit more_chant_lit CODE_BLOCK_RIGHT 2D_chant_row")
def chant_row_nested(p):
    return ASTNode("chant_row", children=[p[1]] + p[2].children + p[4].children)

# Rule 96: 2D_chant_row → λ
@pg.production("2D_chant_row : ")
def two_d_chant_row_empty(p):
    return ASTNode("2D_chant_row", children=[])

# Rule 97: 2D_chant_row → , { chant_lit more_chant_lit } 2D_chant_row
@pg.production("2D_chant_row : COMMA CODE_BLOCK_LEFT chant_lit more_chant_lit CODE_BLOCK_RIGHT 2D_chant_row")
def two_d_chant_row_recursive(p):
    return ASTNode("2D_chant_row", children=[p[2]] + p[3].children + p[5].children)

# Rule 98: more_chant_lit → λ
@pg.production("more_chant_lit : ")
def more_chant_lit_empty(p):
    return ASTNode("more_chant_lit", children=[])

# Rule 99: more_chant_lit → , chant_lit more_chant_lit
@pg.production("more_chant_lit : COMMA chant_lit more_chant_lit")
def more_chant_lit_recursive(p):
    return ASTNode("more_chant_lit", children=[p[1]] + p[2].children)

# Rule 100: function_def → λ
@pg.production("function_def : ")
def function_def_empty(p):
    return ASTNode("function_def", children=[])

# Rule 101: function_def → WILT function_declared function_def
@pg.production("function_def : WILT function_declared function_def")
def function_def_wilt(p):
    return ASTNode("function_def", children=[p[1]] + p[2].children)

# Rule 102: function_def → DUNK dunk_func_declared function_def
@pg.production("function_def : DUNK dunk_func_declared function_def")
def function_def_dunk(p):
    return ASTNode("function_def", children=[p[1]] + p[2].children)

# Rule 103: function_declared → feint_function
@pg.production("function_declared : feint_function")
def function_declared_feint(p):
    return ASTNode("function_declared", children=[p[0]])

# Rule 104: function_declared → floater_function
@pg.production("function_declared : floater_function")
def function_declared_floater(p):
    return ASTNode("function_declared", children=[p[0]])

# Rule 105: function_declared → chant_function
@pg.production("function_declared : chant_function")
def function_declared_chant(p):
    return ASTNode("function_declared", children=[p[0]])

# Rule 106: function_declared → stat_function
@pg.production("function_declared : stat_function")
def function_declared_stat(p):
    return ASTNode("function_declared", children=[p[0]])

# Rule 107: dunk_func_declared → dunk_function
@pg.production("dunk_func_declared : dunk_function")
def dunk_func_declared(p):
    return ASTNode("dunk_func_declared", children=[p[0]])

# Rule 108: feint_function → FEINT VAR_INIT ( func_parameters ) { function_statement rebound_statement }
@pg.production("feint_function : FEINT VAR_INIT LEFT_PAREN func_parameters RIGHT_PAREN CODE_BLOCK_LEFT function_statement rebound_statement CODE_BLOCK_RIGHT")
def feint_function(p):
    return ASTNode("feint_function", children=[p[1], p[3], p[6], p[7]])

# Rule 109: floater_function → FLOATER VAR_INIT ( func_parameters ) { function_statement rebound_statement }
@pg.production("floater_function : FLOATER VAR_INIT LEFT_PAREN func_parameters RIGHT_PAREN CODE_BLOCK_LEFT function_statement rebound_statement CODE_BLOCK_RIGHT")
def floater_function(p):
    return ASTNode("floater_function", children=[p[1], p[3], p[6], p[7]])

# Rule 110: chant_function → CHANT VAR_INIT ( func_parameters ) { function_statement rebound_statement }
@pg.production("chant_function : CHANT VAR_INIT LEFT_PAREN func_parameters RIGHT_PAREN CODE_BLOCK_LEFT function_statement rebound_statement CODE_BLOCK_RIGHT")
def chant_function(p):
    return ASTNode("chant_function", children=[p[1], p[3], p[6], p[7]])

# Rule 111: stat_function → STAT VAR_INIT ( func_parameters ) { function_statement rebound_statement }
@pg.production("stat_function : STAT VAR_INIT LEFT_PAREN func_parameters RIGHT_PAREN CODE_BLOCK_LEFT function_statement rebound_statement CODE_BLOCK_RIGHT")
def stat_function(p):
    return ASTNode("stat_function", children=[p[1], p[3], p[6], p[7]])

# Rule 112: dunk_function → VAR_INIT ( func_parameters ) { function_statement }
@pg.production("dunk_function : VAR_INIT LEFT_PAREN func_parameters RIGHT_PAREN CODE_BLOCK_LEFT function_statement CODE_BLOCK_RIGHT")
def dunk_function(p):
    return ASTNode("dunk_function", children=[p[0], p[2], p[5]])

# Rule 113: func_parameters → λ
@pg.production("func_parameters : ")
def func_parameters_empty(p):
    return ASTNode("func_parameters", children=[])

# Rule 114: func_parameters → VAR_INIT param_end
@pg.production("func_parameters : VAR_INIT param_end")
def func_parameters(p):
    return ASTNode("func_parameters", children=[p[0]] + p[1].children)

# Rule 115: param_end → , VAR_INIT param_end
@pg.production("param_end : COMMA VAR_INIT param_end")
def param_end_recurse(p):
    return ASTNode("param_end", children=[p[1]] + p[2].children)

# Rule 116: param_end → λ
@pg.production("param_end : ")
def param_end_empty(p):
    return ASTNode("param_end", children=[])

# Rule 117: function_statement → statement function_statement
@pg.production("function_statement : statement function_statement")
def function_statement_recursive(p):
    return ASTNode("function_statement", children=[p[0]] + p[1].children)

# Rule 118: function_statement → λ
@pg.production("function_statement : ")
def function_statement_empty(p):
    return ASTNode("function_statement", children=[])

# Rule 119: team_statement → statement team_statement
@pg.production("team_statement : statement team_statement")
def team_statement_recursive(p):
    return ASTNode("team_statement", children=[p[0]] + p[1].children)

# Rule 120: team_statement → λ
@pg.production("team_statement : ")
def team_statement_empty(p):
    return ASTNode("team_statement", children=[])

# Rule 121: statement → variable_dec
@pg.production("statement : variable_dec")
def statement_variable(p):
    return ASTNode("statement", children=[p[0]])

# Rule 122: statement → announce_statement
@pg.production("statement : announce_statement")
def statement_announce(p):
    return ASTNode("statement", children=[p[0]])

# Rule 123: statement → inbound_statement
@pg.production("statement : inbound_statement")
def statement_inbound(p):
    return ASTNode("statement", children=[p[0]])

# Rule 124: statement → dribble_statement
@pg.production("statement : dribble_statement")
def statement_dribble(p):
    return ASTNode("statement", children=[p[0]])

# Rule 125: statement → switch_statement
@pg.production("statement : switch_statement")
def statement_switch(p):
    return ASTNode("statement", children=[p[0]])

# Rule 126: statement → forward_statement
@pg.production("statement : forward_statement")
def statement_forward(p):
    return ASTNode("statement", children=[p[0]])

# Rule 127: statement → play_statement
@pg.production("statement : play_statement")
def statement_play(p):
    return ASTNode("statement", children=[p[0]])

# Rule 128: statement → run_play_statement
@pg.production("statement : run_play_statement")
def statement_run(p):
    return ASTNode("statement", children=[p[0]])

# ADDED
@pg.production("statement : assignment_expression")
def statement_follow(p):
    return ASTNode("statement", children=[p[0]])

# Rule 129: statement → VAR_INIT follow_statement ;
@pg.production("statement : VAR_INIT follow_statement SEMICOLON")
def statement_follow(p):
    return ASTNode("statement", children=[p[0], p[1]])

# Rule 130: follow_statement → increment
@pg.production("follow_statement : increment")
def follow_statement_increment(p):
    return ASTNode("follow_statement", children=[p[0]])

# Rule 131: follow_statement → decrement
@pg.production("follow_statement : decrement")
def follow_statement_decrement(p):
    return ASTNode("follow_statement", children=[p[0]])

# Rule 132: follow_statement → function_call
@pg.production("follow_statement : function_call")
def follow_statement_call(p):
    return ASTNode("follow_statement", children=[p[0]])

# # Rule 134: follow_statement → array_manipulation
# @pg.production("follow_statement : array_manipulation")
# def follow_statement_array(p):
#     return ASTNode("follow_statement", children=[p[0]])

# # Rule 135: array_manipulation → [ element_index ] 2d_manipulation array_man
# @pg.production("array_manipulation : ARRAY_INDEX_LEFT element_index ARRAY_INDEX_RIGHT 2d_manipulation array_man")
# def array_manipulation(p):
#     return ASTNode("array_manipulation", children=[p[1], p[3], p[4]])

# Rule 136: element_index → feint_lit
@pg.production("element_index : feint_lit")
def element_index(p):
    return ASTNode("element_index", value=p[0].value)

# Rule 136: element_index → VAR_INIT
@pg.production("element_index : VAR_INIT")
def element_index(p):
    return ASTNode("element_index", value=p[0].value)

# # Rule 137: 2d_manipulation → [ element_index ]
# @pg.production("2d_manipulation : ARRAY_INDEX_LEFT element_index ARRAY_INDEX_RIGHT")
# def two_d_manipulation(p):
#     return ASTNode("2d_manipulation", children=[p[1]])

# # Rule 138: 2d_manipulation → λ
# @pg.production("2d_manipulation : ")
# def two_d_manipulation_empty(p):
#     return ASTNode("2d_manipulation", children=[])

# # Rule 139: array_man → = array_elem
# @pg.production("array_man : ASSIGN array_elem")
# def array_man(p):
#     return ASTNode("array_man", children=[p[1]])

# # Rule 140: array_man → λ
# @pg.production("array_man : ")
# def array_man_empty(p):
#     return ASTNode("array_man", children=[])

# # Rule 141: array_elem → feint_lit
# @pg.production("array_elem : expression")
# def array_elem_feint(p):
#     return ASTNode("array_elem", children=[p[0]])

# Rule 144: rebound_statement → REBOUND rebound_value ;
@pg.production("rebound_statement : REBOUND expression SEMICOLON")
def rebound_statement(p):
    return ASTNode("rebound_statement", children=[p[1]])

# # Rule 145: rebound_value → literal
# @pg.production("rebound_value : literal")
# def rebound_value_literal(p):
#     return ASTNode("rebound_value", children=[p[0]])

# # Rule 146: rebound_value → VAR_INIT
# @pg.production("rebound_value : VAR_INIT")
# def rebound_value_identifier(p):
#     return ASTNode("rebound_value", value=p[0].value)

# # Rule 147: rebound_value → expression
# @pg.production("rebound_value : expression")
# def rebound_value_expression(p):
#     return ASTNode("rebound_value", children=[p[0]])

# Rule 148: announce_statement → ANNOUNCE ( outputs ) ;
@pg.production("announce_statement : ANNOUNCE LEFT_PAREN outputs RIGHT_PAREN SEMICOLON")
def announce_statement(p):
    return ASTNode("announce_statement", children=[p[2]])

# Rule 149: outputs → output other_outputs
@pg.production("outputs : output other_outputs")
def outputs(p):
    return ASTNode("outputs", children=[p[0]] + p[1].children)

# Rule 151: output → expression
@pg.production("output : expression")
def output_expression(p):
    return ASTNode("output", children=[p[0]])

# Rule 156: other_outputs → λ
@pg.production("other_outputs : ")
def other_outputs_empty(p):
    return ASTNode("other_outputs", children=[])

# Rule 157: other_outputs → & outputs
@pg.production("other_outputs : CHANT_CONCAT outputs")
def other_outputs_concat(p):
    return ASTNode("other_outputs", children=p[1].children)

# Rule 158: literal → feint_lit
@pg.production("literal : feint_lit")
def literal_feint(p):
    return ASTNode("literal", value=p[0].value)

# Rule 159: literal → floater_lit
@pg.production("literal : floater_lit")
def literal_floater(p):
    return ASTNode("literal", value=p[0].value)

# Rule 160: literal → nega_feint_lit
@pg.production("literal : nega_feint_lit")
def literal_nega_feint(p):
    return ASTNode("literal", value=p[0].value)

# Rule 161: literal → nega_floater_lit
@pg.production("literal : nega_floater_lit")
def literal_nega_floater(p):
    return ASTNode("literal", value=p[0].value)

# Rule 162: literal → chant_lit
@pg.production("literal : chant_lit")
def literal_chant(p):
    return ASTNode("literal", value=p[0].value)

# Rule 163: literal → stat_value
@pg.production("literal : stat_value")
def literal_stat(p):
    return ASTNode("literal", children=[p[0]])

# Rule 164: nega_feint_lit → NEGAFEINT
@pg.production("nega_feint_lit : NEGAFEINT")
def nega_feint_lit(p):
    return ASTNode("nega_feint_lit", value=p[0].value)

# Rule 165: nega_floater_lit → NEGAFLOATER
@pg.production("nega_floater_lit : NEGAFLOATER")
def nega_floater_lit(p):
    return ASTNode("nega_floater_lit", value=p[0].value)

# ADDED
@pg.production("expression : logical_expression")
def expression_logical(p):
    return ASTNode("expression", children=[p[0]])

# Rule 169: logical_expression → relational_expression logical_expression_tail
@pg.production("logical_expression : relational_expression logical_expression_tail")
def logical_expression(p):
    return ASTNode("logical_expression", children=[p[0], p[1]])

# Rule 170: logical_expression_tail → AND_OP relational_expression logical_expression_tail
@pg.production("logical_expression_tail : AND_OP relational_expression logical_expression_tail")
def logical_expression_tail_and(p):
    return ASTNode("AND_OP", children=[p[1], p[2]])

# Rule 171: logical_expression_tail → OR_OP relational_expression logical_expression_tail
@pg.production("logical_expression_tail : OR_OP relational_expression logical_expression_tail")
def logical_expression_tail_or(p):
    return ASTNode("OR_OP", children=[p[1], p[2]])

# Rule 172: logical_expression_tail → (empty)
@pg.production("logical_expression_tail :")
def logical_expression_tail_empty(p):
    return ASTNode("logical_expression_tail")  # no children -> end of chain

# Rule 173: relational_expression → arithmetic_expression relational_expression_tail
@pg.production("relational_expression : arithmetic_expression relational_expression_tail")
def relational_expression(p):
    return ASTNode("relational_expression", children=[p[0], p[1]])

# Rule 174+: relational_expression_tail → EQUAL/NOT_EQUAL/etc

@pg.production("relational_expression_tail : EQUAL arithmetic_expression relational_expression_tail")
def relational_expression_tail_eq(p):
    return ASTNode("EQUAL", children=[p[1], p[2]])

@pg.production("relational_expression_tail : NOT_EQUAL arithmetic_expression relational_expression_tail")
def relational_expression_tail_neq(p):
    return ASTNode("NOT_EQUAL", children=[p[1], p[2]])

@pg.production("relational_expression_tail : LESS_THAN arithmetic_expression relational_expression_tail")
def relational_expression_tail_lt(p):
    return ASTNode("LESS_THAN", children=[p[1], p[2]])

@pg.production("relational_expression_tail : GREATER_THAN arithmetic_expression relational_expression_tail")
def relational_expression_tail_gt(p):
    return ASTNode("GREATER_THAN", children=[p[1], p[2]])

@pg.production("relational_expression_tail : LESS_EQUAL arithmetic_expression relational_expression_tail")
def relational_expression_tail_le(p):
    return ASTNode("LESS_EQUAL", children=[p[1], p[2]])

@pg.production("relational_expression_tail : GREATER_EQUAL arithmetic_expression relational_expression_tail")
def relational_expression_tail_ge(p):
    return ASTNode("GREATER_EQUAL", children=[p[1], p[2]])

# Rule: relational_expression_tail → (empty)
@pg.production("relational_expression_tail :")
def relational_expression_tail_empty(p):
    return ASTNode("relational_expression_tail")  # no children -> end

# Rule 180: arithmetic_expression → term arithmetic_expression_tail
@pg.production("arithmetic_expression : term arithmetic_expression_tail")
def arithmetic_expression(p):
    return ASTNode("arithmetic_expression", children=[p[0], p[1]])

# Rule 181+: arithmetic_expression_tail
@pg.production("arithmetic_expression_tail : ADD term arithmetic_expression_tail")
def arithmetic_expression_tail_add(p):
    return ASTNode("ADD", children=[p[1], p[2]])

@pg.production("arithmetic_expression_tail : SUB term arithmetic_expression_tail")
def arithmetic_expression_tail_sub(p):
    return ASTNode("SUB", children=[p[1], p[2]])

# Rule: arithmetic_expression_tail → (empty)
@pg.production("arithmetic_expression_tail :")
def arithmetic_expression_tail_empty(p):
    return ASTNode("arithmetic_expression_tail")  # no children -> end

# Rule 184: term → factor term_tail
@pg.production("term : factor term_tail")
def term(p):
    return ASTNode("term", children=[p[0], p[1]])

@pg.production("term_tail : MUL factor term_tail")
def term_tail_mul(p):
    return ASTNode("MUL", children=[p[1], p[2]])

@pg.production("term_tail : DIV factor term_tail")
def term_tail_div(p):
    return ASTNode("DIV", children=[p[1], p[2]])

@pg.production("term_tail : MOD factor term_tail")
def term_tail_mod(p):
    return ASTNode("MOD", children=[p[1], p[2]])

@pg.production("term_tail :")
def term_tail_empty(p):
    return ASTNode("term_tail")  # no children

@pg.production("factor : LEFT_PAREN expression RIGHT_PAREN")
def factor_group(p):
    return p[1]  # group expression directly

@pg.production("factor : NOT_OP factor")
def factor_not(p):
    return ASTNode("NOT_OP", children=[p[1]])

@pg.production("factor : literal")
def factor_literal(p):
    return p[0]

# VAR_INIT followed by a postfix (either array access or function call)
@pg.production("factor : VAR_INIT postfix")
def factor_var_with_postfix(p):
    var_token = p[0]         # The variable token (@something)
    postfix_node = p[1]       # array_access, function_call, or none

    if postfix_node.name == "no_postfix":
        return ASTNode("variable", value=var_token.value)
    elif postfix_node.name == "array_access" or postfix_node.name == "array_access_2d":
        return ASTNode(postfix_node.name, value=var_token.value, children=postfix_node.children)
    elif postfix_node.name == "function_call":
        return ASTNode("function_call", value=var_token.value, children=postfix_node.children)
    else:
        raise Exception(f"[ERROR] Unexpected postfix: {postfix_node.name}")

# postfix : array_access
@pg.production("postfix : array_access")
def postfix_array_access(p):
    return p[0]

# postfix : function_call
@pg.production("postfix : function_call")
def postfix_function_call(p):
    return p[0]

# postfix : (empty)
@pg.production("postfix :")
def postfix_empty(p):
    return ASTNode("no_postfix")  # means plain variable

# If NO array access (simple variable)
@pg.production("array_access :")
def array_access_empty(p):
    return ASTNode("no_array_access")

@pg.production("array_access : ARRAY_INDEX_LEFT element_index ARRAY_INDEX_RIGHT array_access_tail")
def array_access_1d_or_2d(p):
    first_index = p[1]
    tail = p[3]
    
    if tail.name == "array_access_tail_2d":
        second_index = tail.children[0]
        return ASTNode("array_access_2d", children=[first_index, second_index])
    else:
        return ASTNode("array_access", children=[first_index])

# If there is a second [ expr ]
@pg.production("array_access_tail : ARRAY_INDEX_LEFT element_index ARRAY_INDEX_RIGHT")
def array_access_tail_2d(p):
    return ASTNode("array_access_tail_2d", children=[p[1]])

# If no second [ expr ]
@pg.production("array_access_tail :")
def array_access_tail_empty(p):
    return ASTNode("array_access_tail_empty")


# # Rule 173: number → feint_lit
# @pg.production("number : feint_lit")
# def number_feint(p):
#     return ASTNode("number", value=p[0].value)

# # Rule 174: number → floater_lit
# @pg.production("number : floater_lit")
# def number_floater(p):
#     return ASTNode("number", value=p[0].value)

# # Rule 175: number → VAR_INIT
# @pg.production("number : VAR_INIT")
# def number_var(p):
#     return ASTNode("number", value=p[0].value)

# # Rule 176: number → nega_feint_lit
# @pg.production("number : NEGAFEINT")
# def number_nega_feint(p):
#     return ASTNode("number", value=p[0].value)

# # Rule 177: number → nega_floater_lit
# @pg.production("number : nega_floater_lit")
# def number_nega_floater(p):
#     return ASTNode("number", value=p[0].value)

# Rule 178: number_type_cast → feint_type_casting
@pg.production("number_type_cast : feint_type_casting")
def number_type_cast_feint(p):
    return ASTNode("number_type_cast", children=[p[0]])

# Rule 179: number_type_cast → floater_type_casting
@pg.production("number_type_cast : floater_type_casting")
def number_type_cast_floater(p):
    return ASTNode("number_type_cast", children=[p[0]])

# Rule 180: feint_type_casting → FEINT ( typecast_value )
@pg.production("feint_type_casting : FEINT LEFT_PAREN typecast_value RIGHT_PAREN")
def feint_type_casting(p):
    return ASTNode("feint_type_casting", children=[p[2]])

# Rule 181: floater_type_casting → FLOATER ( typecast_value )
@pg.production("floater_type_casting : FLOATER LEFT_PAREN typecast_value RIGHT_PAREN")
def floater_type_casting(p):
    return ASTNode("floater_type_casting", children=[p[2]])

# Rule 182: chant_type_casting → CHANT ( typecast_value )
@pg.production("chant_type_casting : CHANT LEFT_PAREN typecast_value RIGHT_PAREN")
def chant_type_casting(p):
    return ASTNode("chant_type_casting", children=[p[2]])

# Rule 183: stat_type_casting → STAT ( typecast_value )
@pg.production("stat_type_casting : STAT LEFT_PAREN typecast_value RIGHT_PAREN")
def stat_type_casting(p):
    return ASTNode("stat_type_casting", children=[p[2]])

# Rule 223: assignment_expression → assign_operator assign_operand ;
@pg.production("assignment_expression : VAR_INIT array_access assign_operator assign_operand SEMICOLON")
def assignment_expression(p):
    return ASTNode("assignment_expression", children=[p[0], p[1], p[2], p[3]])

# Rule 224–229: assign_operator → = | += | -= | *= | /= | %=
@pg.production("assign_operator : ASSIGN")
@pg.production("assign_operator : ADD_ASSIGN")
@pg.production("assign_operator : SUB_ASSIGN")
@pg.production("assign_operator : MUL_ASSIGN")
@pg.production("assign_operator : DIV_ASSIGN")
@pg.production("assign_operator : MOD_ASSIGN")
def assign_operator(p):
    return ASTNode("assign_operator", value=p[0].value)

# Rule 230: assign_operand → arithmetic_expression
@pg.production("assign_operand : expression")
def assign_operand_arith(p):
    return ASTNode("assign_operand", children=[p[0]])

# Rule 233: assign_operand → function_call
@pg.production("assign_operand : function_call")
def assign_operand_func(p):
    return ASTNode("assign_operand", children=[p[0]])

#ADDED
@pg.production("assign_operand : stat_value")
def assign_operand_arith(p):
    return ASTNode("assign_operand", children=[p[0]])

# Rule 234: function_call → ( arguments )
@pg.production("function_call : LEFT_PAREN arguments RIGHT_PAREN")
def function_call(p):
    return ASTNode("function_call", children=[p[1]])

# Rule 235: arguments → λ
@pg.production("arguments : ")
def arguments(p):
    return ASTNode("arguments",  children=[])

# Rule 235: arguments → arg more_args
@pg.production("arguments : arg more_args")
def arguments(p):
    return ASTNode("arguments", children=[p[0]] + p[1].children)

# Rule 236: arg → literal
@pg.production("arg : literal")
def arg_literal(p):
    return ASTNode("arg", children=[p[0]])

# Rule 237: arg → VAR_INIT
@pg.production("arg : VAR_INIT")
def arg_var(p):
    return ASTNode("arg", value=p[0].value)

# Rule 238: more_args → , arg more_args
@pg.production("more_args : COMMA arg more_args")
def more_args_recursive(p):
    return ASTNode("more_args", children=[p[1]] + p[2].children)

# Rule 239: more_args → λ
@pg.production("more_args : ")
def more_args_empty(p):
    return ASTNode("more_args", children=[])

# Rule 240: inbound_statement → INBOUND ( chant_lit , VAR_INIT ) ;
@pg.production("inbound_statement : INBOUND LEFT_PAREN chant_lit COMMA VAR_INIT RIGHT_PAREN SEMICOLON")
def inbound_statement(p):
    return ASTNode("inbound_statement", children=[p[2], p[4]])

# Rule 241: dribble_statement → DRIBBLE ( expression ) { loop_statements } add_condition
@pg.production("dribble_statement : DRIBBLE LEFT_PAREN expression RIGHT_PAREN CODE_BLOCK_LEFT loop_statements CODE_BLOCK_RIGHT add_condition")
def dribble_statement(p):
    return ASTNode("dribble_statement", children=[p[2], p[5], p[7]])

# Rule 242: add_condition → PASS ( expression ) { loop_statements } add_condition
@pg.production("add_condition : PASS LEFT_PAREN expression RIGHT_PAREN CODE_BLOCK_LEFT loop_statements CODE_BLOCK_RIGHT add_condition")
def add_condition_pass(p):
    return ASTNode("add_condition", children=[ASTNode("Pass"), p[2], p[5]] + p[7].children)

# Rule 243: add_condition → SHOOT { loop_statements }
@pg.production("add_condition : SHOOT CODE_BLOCK_LEFT loop_statements CODE_BLOCK_RIGHT")
def add_condition_shoot(p):
    return ASTNode("add_condition", children=[ASTNode("Shoot"), p[2]])

# Rule 244: add_condition → λ
@pg.production("add_condition : ")
def add_condition_empty(p):
    return ASTNode("add_condition", children=[])

# Rule 245: loop_statements → loop_statement loop_statements
@pg.production("loop_statements : loop_statement loop_statements")
def loop_statements_recursive(p):
    return ASTNode("loop_statements", children=[p[0]] + p[1].children)

# Rule 246: loop_statements → λ
@pg.production("loop_statements : ")
def loop_statements_empty(p):
    return ASTNode("loop_statements", children=[])

# Rule 248: loop_statement → resume_statement
@pg.production("loop_statement : resume_statement")
def loop_statement_resume(p):
    return ASTNode("loop_statement", children=[p[0]])

# Rule 249: switch_statement → SWITCH ( VAR_INIT ) { get_case get_default }
@pg.production("switch_statement : SWITCH LEFT_PAREN VAR_INIT RIGHT_PAREN CODE_BLOCK_LEFT get_case get_default CODE_BLOCK_RIGHT")
def switch_statement(p):
    return ASTNode("switch_statement", children=[p[2], p[5], p[6]])

# Rule 250: get_case → GET get_value : team_statement timeout_statement get_case_end
@pg.production("get_case : GET get_value COLON team_statement timeout_statement get_case_end")
def get_case(p):
    return ASTNode("get_case", children=[p[1], p[3], p[4], p[5]])

# Rule 251: get_value → feint_lit
@pg.production("get_value : feint_lit")
def get_value_feint(p):
    return ASTNode("get_value", value=p[0].value)

# Rule 252: get_value → chant_lit
@pg.production("get_value : chant_lit")
def get_value_chant(p):
    return ASTNode("get_value", value=p[0].value)

# Rule 253: timeout_statement → TIMEOUT ;
@pg.production("timeout_statement : TIMEOUT SEMICOLON")
def timeout_statement(p):
    return ASTNode("timeout_statement")

# Rule 254: get_case_end → λ
@pg.production("get_case_end : ")
def get_case_end_empty(p):
    return ASTNode("get_case_end", children=[])

# Rule 255: get_case_end → get_case
@pg.production("get_case_end : get_case")
def get_case_end_recursive(p):
    return ASTNode("get_case_end", children=[p[0]])

# Rule 256: get_default → DEFAULT : team_statement
@pg.production("get_default : DEFAULT COLON team_statement")
def get_default(p):
    return ASTNode("get_default", children=[p[2]])

# Rule 257: get_default → λ
@pg.production("get_default : ")
def get_default_empty(p):
    return ASTNode("get_default", children=[])

# Rule 258: forward_statement → FORWARD ( VAR_INIT = forward_lit ; expression ; VAR_INIT forward_inc_dec ) { team_statement
@pg.production("forward_statement : FORWARD LEFT_PAREN VAR_INIT ASSIGN forward_lit SEMICOLON expression SEMICOLON VAR_INIT forward_inc_dec RIGHT_PAREN CODE_BLOCK_LEFT loop_statements CODE_BLOCK_RIGHT")
def forward_statement(p):
    return ASTNode("forward_statement", children=[p[2], p[4], p[6], p[8], p[9], p[12]])

# Rule 259: forward_lit → feint_lit
@pg.production("forward_lit : feint_lit")
def forward_lit_feint(p):
    return ASTNode("forward_lit", value=p[0].value)

# Rule 260: forward_lit → VAR_INIT
@pg.production("forward_lit : VAR_INIT")
def forward_lit_var(p):
    return ASTNode("forward_lit", value=p[0].value)

# Rule 261: forward_inc_dec → increment
@pg.production("forward_inc_dec : increment")
def forward_inc_dec_inc(p):
    return ASTNode("forward_inc_dec", children=[p[0]])

# Rule 262: forward_inc_dec → decrement
@pg.production("forward_inc_dec : decrement")
def forward_inc_dec_dec(p):
    return ASTNode("forward_inc_dec", children=[p[0]])

# Rule 263: forward_inc_dec → forward_assign_operator forward_lit
@pg.production("forward_inc_dec : forward_assign_operator forward_lit")
def forward_inc_dec_assign(p):
    return ASTNode("forward_inc_dec", children=[p[0], p[1]])

# Rule 264: increment → INCREMENT
@pg.production("increment : INCREMENT")
def increment(p):
    return ASTNode("increment", value=p[0].value)

# Rule 265: decrement → DECREMENT
@pg.production("decrement : DECREMENT")
def decrement(p):
    return ASTNode("decrement", value=p[0].value)

# Rule 266–267: forward_assign_operator → += | -=
@pg.production("forward_assign_operator : ADD_ASSIGN")
@pg.production("forward_assign_operator : SUB_ASSIGN")
def forward_assign_operator(p):
    return ASTNode("forward_assign_operator", value=p[0].value)

# Rule 268: resume_statement → RESUME ;
@pg.production("resume_statement : RESUME SEMICOLON")
def resume_statement(p):
    return ASTNode("resume_statement")

# Rule 269: resume_statement → λ
@pg.production("resume_statement : ")
def resume_statement_empty(p):
    return ASTNode("resume_statement", children=[])

# Rule 270: play_statement → PLAY ( expression ) { team_statement }
@pg.production("play_statement : PLAY LEFT_PAREN expression RIGHT_PAREN CODE_BLOCK_LEFT team_statement CODE_BLOCK_RIGHT")
def play_statement(p):
    return ASTNode("play_statement", children=[p[2], p[5]])

# Rule 271: run_play_statement → RUN { team_statement } PLAY ( expression ) ;
@pg.production("run_play_statement : RUN CODE_BLOCK_LEFT team_statement CODE_BLOCK_RIGHT PLAY LEFT_PAREN expression RIGHT_PAREN SEMICOLON")
def run_play_statement(p):
    return ASTNode("run_play_statement", children=[p[2], p[6]])

# Rule 272: team_block → TEAM ( ) { local_decl team_statement }
@pg.production("team_block : TEAM LEFT_PAREN RIGHT_PAREN CODE_BLOCK_LEFT local_decl team_statement CODE_BLOCK_RIGHT")
def team_block(p):
    return ASTNode("team_block", children=[p[4], p[5]])

# Rule 273: local_decl → local_declaration local_decl
@pg.production("local_decl : local_declaration local_decl")
def local_decl_recursive(p):
    return ASTNode("local_decl", children=[p[0]] + p[1].children)

# Rule 274: local_decl → λ
@pg.production("local_decl : ")
def local_decl_empty(p):
    return ASTNode("local_decl", children=[])

# Rule 275: local_declaration → variable_dec
@pg.production("local_declaration : variable_dec")
def local_declaration_var(p):
    return ASTNode("local_declaration", children=[p[0]])

# Rule 276: local_declaration → array_dec
@pg.production("local_declaration : array_dec")
def local_declaration_array(p):
    return ASTNode("local_declaration", children=[p[0]])

# Rule 277: typecast_value → FEINTLIT
@pg.production("typecast_value : FEINTLIT")
def typecast_value_feint(p):
    return ASTNode("typecast_value", value=p[0].value)

# Rule 278: typecast_value → FLOATERLIT
@pg.production("typecast_value : FLOATERLIT")
def typecast_value_floater(p):
    return ASTNode("typecast_value", value=p[0].value)

# Rule 279: typecast_value → CHANTLIT
@pg.production("typecast_value : CHANTLIT")
def typecast_value_chant(p):
    return ASTNode("typecast_value", value=p[0].value)

# Rule 280: typecast_value → stat_value
@pg.production("typecast_value : stat_value")
def typecast_value_stat(p):
    return ASTNode("typecast_value", children=[p[0]])

# Rule 281: typecast_value → VAR_INIT
@pg.production("typecast_value : VAR_INIT")
def typecast_value_var(p):
    return ASTNode("typecast_value", value=p[0].value)


#ADDED

# Rule : statement → announce_statement
@pg.production("loop_statement : announce_statement")
def loop_statement_announce(p):
    return ASTNode("loop_statement", children=[p[0]])

# Rule : statement → inbound_statement
@pg.production("loop_statement : inbound_statement")
def loop_statement_inbound(p):
    return ASTNode("loop_statement", children=[p[0]])

# Rule : statement → dribble_statement
@pg.production("loop_statement : dribble_statement")
def loop_statement_dribble(p):
    return ASTNode("loop_statement", children=[p[0]])

# Rule : loop_statement → switch_statement
@pg.production("loop_statement : switch_statement")
def loop_statement_switch(p):
    return ASTNode("loop_statement", children=[p[0]])

# Rule : loop_statement → forward_statement
@pg.production("loop_statement : forward_statement")
def loop_statement_forward(p):
    return ASTNode("loop_statement", children=[p[0]])

# Rule : loop_statement → play_statement
@pg.production("loop_statement : play_statement")
def loop_statement_play(p):
    return ASTNode("loop_statement", children=[p[0]])

# Rule : loop_statement → run_play_statement
@pg.production("loop_statement : run_play_statement")
def loop_statement_run(p):
    return ASTNode("loop_statement", children=[p[0]])

# ADDED
@pg.production("loop_statement : assignment_expression")
def loop_statement_follow(p):
    return ASTNode("loop_statement", children=[p[0]])

# Rule : loop_statement → VAR_INIT follow_statement ;
@pg.production("loop_statement : VAR_INIT follow_statement ")
def loop_statement_follow(p):
    return ASTNode("loop_statement", children=[p[0], p[1]])

@pg.production("loop_statement : timeout_statement")
def loop_statement_follow(p):
    return ASTNode("loop_statement", children=[p[0]])
