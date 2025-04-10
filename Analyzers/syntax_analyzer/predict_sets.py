# from Analyzers.lexical_analyzer.tokens import TokenType

# PREDICT_SETS = {
#     # <program> productions
#     ('program', TokenType.FEINT): 1,
#     ('program', TokenType.FLOATER): 1,
#     ('program', TokenType.CHANT): 1,
#     ('program', TokenType.STAT): 1,
#     ('program', TokenType.CONST): 1,
#     ('program', TokenType.ZONE): 1,
#     ('program', TokenType.TEAM): 1,

#     # <global_decl> productions
#     ('global_decl', TokenType.FEINT): 2,
#     ('global_decl', TokenType.FLOATER): 2,
#     ('global_decl', TokenType.CHANT): 2,
#     ('global_decl', TokenType.STAT): 2,
#     ('global_decl', TokenType.CONST): 2,
#     ('global_decl', TokenType.ZONE): 2,
#     ('global_decl', TokenType.WILT): 3,
#     ('global_decl', TokenType.DUNK): 3,
#     ('global_decl', TokenType.TEAM): 3,

#     # <global_declaration> productions
#     ('global_declaration', TokenType.FEINT): 4,
#     ('global_declaration', TokenType.FLOATER): 4,
#     ('global_declaration', TokenType.CHANT): 4,
#     ('global_declaration', TokenType.STAT): 4,
#     ('global_declaration', TokenType.CONST): 5,
#     ('global_declaration', TokenType.ZONE): 6,

#     # <variable_dec> productions
#     ('variable_dec', TokenType.FEINT): 7,
#     ('variable_dec', TokenType.FLOATER): 8,
#     ('variable_dec', TokenType.CHANT): 9,
#     ('variable_dec', TokenType.STAT): 10,

#     # <feint_dec> productions
#     ('feint_dec', TokenType.FEINT): 11,

#     # <more_feint> productions
#     ('more_feint', TokenType.ASSIGN): 13,
#     ('more_feint', TokenType.SEMICOLON): 12,

#     # <feint_init> productions
#     ('feint_init', TokenType.ASSIGN): 15,
#     ('feint_init', TokenType.SEMICOLON): 14,

#     # <feint_init_end> productions
#     ('feint_init_end', TokenType.COMMA): 18,
#     ('feint_init_end', TokenType.SEMICOLON): 17,

#     # <floater_dec> productions
#     ('floater_dec', TokenType.FLOATER): 19,

#     # <more_floater> productions
#     ('more_floater', TokenType.ASSIGN): 21,
#     ('more_floater', TokenType.SEMICOLON): 20,

#     # <floater_init> productions
#     ('floater_init', TokenType.ASSIGN): 23,
#     ('floater_init', TokenType.SEMICOLON): 22,

#     # <floater_init_end> productions
#     ('floater_init_end', TokenType.COMMA): 26,
#     ('floater_init_end', TokenType.SEMICOLON): 25,

#     # <chant_dec> productions
#     ('chant_dec', TokenType.CHANT): 27,

#     # <more_chant> productions
#     ('more_chant', TokenType.ASSIGN): 29,
#     ('more_chant', TokenType.SEMICOLON): 28,

#     # <chant_init> productions
#     ('chant_init', TokenType.ASSIGN): 31,
#     ('chant_init', TokenType.SEMICOLON): 30,

#     # <chant_init_end> productions
#     ('chant_init_end', TokenType.COMMA): 34,
#     ('chant_init_end', TokenType.SEMICOLON): 33,

#     # <stat_dec> productions
#     ('stat_dec', TokenType.STAT): 35,

#     # <more_stat> productions
#     ('more_stat', TokenType.ASSIGN): 37,
#     ('more_stat', TokenType.SEMICOLON): 36,

#     # <stat_init> productions
#     ('stat_init', TokenType.ASSIGN): 39,
#     ('stat_init', TokenType.SEMICOLON): 38,

#     # <stat_value> productions
#     ('stat_value', TokenType.WIN): 40,
#     ('stat_value', TokenType.LOSS): 41,

#     # <stat_init_end> productions
#     ('stat_init_end', TokenType.COMMA): 43,
#     ('stat_init_end', TokenType.SEMICOLON): 42,

#     # <const_dec> productions
#     ('const_dec', TokenType.CONST): 44,
#     ('const_dec', TokenType.FEINT): 44,
#     ('const_dec', TokenType.FLOATER): 45,
#     ('const_dec', TokenType.CHANT): 46,
#     ('const_dec', TokenType.STAT): 47,

#     # <const_feint> productions
#     ('const_feint', TokenType.FEINT): 48,

#     # <feint_const_init> productions
#     ('feint_const_init', TokenType.ASSIGN): 49,

#     # <feint_const> productions
#     ('feint_const', TokenType.ASSIGN): 50,

#     # <feint_const_end> productions
#     ('feint_const_end', TokenType.COMMA): 51,
#     ('feint_const_end', TokenType.SEMICOLON): 52,

#     # <const_floater> productions
#     ('const_floater', TokenType.FLOATER): 53,

#     # <floater_const_init> productions
#     ('floater_const_init', TokenType.ASSIGN): 54,

#     # <floater_const> productions
#     ('floater_const', TokenType.ASSIGN): 55,

#     # <floater_const_end> productions
#     ('floater_const_end', TokenType.COMMA): 56,
#     ('floater_const_end', TokenType.SEMICOLON): 57,

#     # <const_chant> productions
#     ('const_chant', TokenType.CHANT): 58,

#     # <chant_const_init> productions
#     ('chant_const_init', TokenType.ASSIGN): 59,

#     # <chant_const> productions
#     ('chant_const', TokenType.ASSIGN): 60,

#     # <chant_const_end> productions
#     ('chant_const_end', TokenType.COMMA): 61,
#     ('chant_const_end', TokenType.SEMICOLON): 62,

#     # <const_stat> productions
#     ('const_stat', TokenType.STAT): 63,

#     # <stat_const_init> productions
#     ('stat_const_init', TokenType.ASSIGN): 64,

#     # <stat_const> productions
#     ('stat_const', TokenType.ASSIGN): 65,

#     # <stat_const_end> productions
#     ('stat_const_end', TokenType.COMMA): 66,
#     ('stat_const_end', TokenType.SEMICOLON): 67,

#     # <array_dec> productions
#     ('array_dec', TokenType.FEINT): 68,
#     ('array_dec', TokenType.FLOATER): 69,
#     ('array_dec', TokenType.CHANT): 70,

#     # <feint_array> productions
#     ('feint_array', TokenType.FEINT): 71,

#     # <2D_array> productions
#     ('2D_array', TokenType.ARRAY_INDEX_LEFT): 73,
#     ('2D_array', TokenType.ASSIGN): 72,

#     # <feint_array_init> productions
#     ('feint_array_init', TokenType.ASSIGN): 75,
#     ('feint_array_init', TokenType.SEMICOLON): 74,

#     # <feint_row> productions
#     ('feint_row', TokenType.FEINTLIT): 76,
#     ('feint_row', TokenType.CODE_BLOCK_LEFT): 77,

#     # <2d_feint_row> productions
#     ('2d_feint_row', TokenType.COMMA): 79,
#     ('2d_feint_row', TokenType.CODE_BLOCK_RIGHT): 78,

#     # <more_feint_lit> productions
#     ('more_feint_lit', TokenType.COMMA): 81,
#     ('more_feint_lit', TokenType.CODE_BLOCK_RIGHT): 80,

#     # <floater_array> productions
#     ('floater_array', TokenType.FLOATER): 82,

#     # <floater_array_init> productions
#     ('floater_array_init', TokenType.ASSIGN): 84,
#     ('floater_array_init', TokenType.SEMICOLON): 83,

#     # <floater_row> productions
#     ('floater_row', TokenType.FLOATERLIT): 85,
#     ('floater_row', TokenType.CODE_BLOCK_LEFT): 86,

#     # <2d_floater_row> productions
#     ('2d_floater_row', TokenType.COMMA): 88,
#     ('2d_floater_row', TokenType.CODE_BLOCK_RIGHT): 87,

#     # <more_floater_lit> productions
#     ('more_floater_lit', TokenType.COMMA): 90,
#     ('more_floater_lit', TokenType.CODE_BLOCK_RIGHT): 89,

#     # <chant_array> productions
#     ('chant_array', TokenType.CHANT): 91,

#     # <chant_array_init> productions
#     ('chant_array_init', TokenType.ASSIGN): 93,
#     ('chant_array_init', TokenType.SEMICOLON): 92,

#     # <chant_row> productions
#     ('chant_row', TokenType.CHANTLIT): 94,
#     ('chant_row', TokenType.CODE_BLOCK_LEFT): 95,

#     # <2d_chant_row> productions
#     ('2d_chant_row', TokenType.COMMA): 97,
#     ('2d_chant_row', TokenType.CODE_BLOCK_RIGHT): 96,

#     # <more_chant_lit> productions
#     ('more_chant_lit', TokenType.COMMA): 99,
#     ('more_chant_lit', TokenType.CODE_BLOCK_RIGHT): 98,

#     # <function_def> productions
#     ('function_def', TokenType.WILT): 101,
#     ('function_def', TokenType.DUNK): 102,
#     ('function_def', TokenType.TEAM): 100,

#     # <function_declared> productions
#     ('function_declared', TokenType.FEINT): 103,
#     ('function_declared', TokenType.FLOATER): 104,
#     ('function_declared', TokenType.CHANT): 105,
#     ('function_declared', TokenType.STAT): 106,

#     # <dunk_func_declared> productions
#     ('dunk_func_declared', TokenType.VAR_INIT): 107,

#     # <feint_function> productions
#     ('feint_function', TokenType.FEINT): 108,

#     # <floater_function> productions
#     ('floater_function', TokenType.FLOATER): 114,

#     # <chant_function> productions
#     ('chant_function', TokenType.CHANT): 120,

#     # <stat_function> productions
#     ('stat_function', TokenType.STAT): 126,

#     # <dunk_function> productions
#     ('dunk_function', TokenType.VAR_INIT): 132,

#     # <function_param> productions
#     ('func_parameters', TokenType.VAR_INIT): 138,
#     ('func_parameters', TokenType.RIGHT_PAREN): 139,

#     # <param> productions
#     ('param', TokenType.VAR_INIT): 140,

#     # <params> productions
#     ('params', TokenType.COMMA): 142,
#     ('params', TokenType.RIGHT_PAREN): 141,

#     # <function_statements> productions
#     ('function_statements', TokenType.FEINT): 143,
#     ('function_statements', TokenType.FLOATER): 143,
#     ('function_statements', TokenType.CHANT): 143,
#     ('function_statements', TokenType.STAT): 143,
#     ('function_statements', TokenType.ANNOUNCE): 143,
#     ('function_statements', TokenType.INBOUND): 143,
#     ('function_statements', TokenType.DRIBBLE): 143,
#     ('function_statements', TokenType.SWITCH): 143,
#     ('function_statements', TokenType.FORWARD): 143,
#     ('function_statements', TokenType.PLAY): 143,
#     ('function_statements', TokenType.RUN): 143,
#     ('function_statements', TokenType.TIMEOUT): 143,
#     ('function_statements', TokenType.RESUME): 143,
#     ('function_statements', TokenType.VAR_INIT): 143,
#     ('function_statements', TokenType.LEFT_PAREN): 143,
#     ('function_statements', TokenType.FEINTLIT): 143,
#     ('function_statements', TokenType.FLOATERLIT): 143,
#     ('function_statements', TokenType.NOT_OP): 143,
#     ('function_statements', TokenType.NEGAFEINT): 143,
#     ('function_statements', TokenType.NEGAFLOATER): 143,
#     ('function_statements', TokenType.CHANTLIT): 143,
#     ('function_statements', TokenType.WIN): 143,
#     ('function_statements', TokenType.LOSS): 143,
#     ('function_statements', TokenType.REBOUND): 143,

#     # <other_statements> productions
#     ('other_statements', TokenType.FEINT): 145,
#     ('other_statements', TokenType.FLOATER): 145,
#     ('other_statements', TokenType.CHANT): 145,
#     ('other_statements', TokenType.STAT): 145,
#     ('other_statements', TokenType.ANNOUNCE): 145,
#     ('other_statements', TokenType.INBOUND): 145,
#     ('other_statements', TokenType.DRIBBLE): 145,
#     ('other_statements', TokenType.SWITCH): 145,
#     ('other_statements', TokenType.FORWARD): 145,
#     ('other_statements', TokenType.PLAY): 145,
#     ('other_statements', TokenType.RUN): 145,
#     ('other_statements', TokenType.TIMEOUT): 145,
#     ('other_statements', TokenType.RESUME): 145,
#     ('other_statements', TokenType.VAR_INIT): 145,
#     ('other_statements', TokenType.LEFT_PAREN): 145,
#     ('other_statements', TokenType.FEINTLIT): 146,
#     ('other_statements', TokenType.FLOATERLIT): 146,
#     ('other_statements', TokenType.NOT_OP): 146,
#     ('other_statements', TokenType.NEGAFEINT): 146,
#     ('other_statements', TokenType.NEGAFLOATER): 146,
#     ('other_statements', TokenType.CHANTLIT): 146,
#     ('other_statements', TokenType.WIN): 146,
#     ('other_statements', TokenType.LOSS): 146,
#     ('other_statements', TokenType.CODE_BLOCK_RIGHT): 144,
#     ('other_statements', TokenType.REBOUND): 147,

#     # <statement> productions
#     ('statement', TokenType.FEINT): 148,
#     ('statement', TokenType.FLOATER): 148,
#     ('statement', TokenType.CHANT): 148,
#     ('statement', TokenType.STAT): 148,
#     ('statement', TokenType.ANNOUNCE): 149,
#     ('statement', TokenType.INBOUND): 150,
#     ('statement', TokenType.DRIBBLE): 151,
#     ('statement', TokenType.SWITCH): 152,
#     ('statement', TokenType.FORWARD): 153,
#     ('statement', TokenType.PLAY): 154,
#     ('statement', TokenType.RUN): 155,
#     ('statement', TokenType.TIMEOUT): 156,
#     ('statement', TokenType.RESUME): 157,
#     ('statement', TokenType.VAR_INIT): 158,
#     ('statement', TokenType.INCREMENT): 159,
#     ('statement', TokenType.DECREMENT): 160,
#     ('statement', TokenType.REBOUND): 161,

#     # <array_manipulation> productions
#     # ('array_manipulation', TokenType.VAR_INIT): 161,

#     # <element_index> productions
#     ('element_index', TokenType.FEINTLIT): 162,

#     # <2d_manipulation> productions
#     ('2d_manipulation', TokenType.ARRAY_INDEX_LEFT): 163,
#     ('2d_manipulation', TokenType.ASSIGN): 164,

#     # <array_man> productions
#     ('array_man', TokenType.ASSIGN): 165,
#     ('array_man', TokenType.SEMICOLON): 166,

#     # <array_elem> productions
#     ('array_elem', TokenType.FEINTLIT): 167,
#     ('array_elem', TokenType.FLOATERLIT): 168,
#     ('array_elem', TokenType.CHANTLIT): 169,

#     # <rebound_statement> productions
#     ('rebound_statement', TokenType.REBOUND): 170,

#     # <announce_statement> productions
#     ('announce_statement', TokenType.ANNOUNCE): 171,

#     # <outputs> productions
#     ('outputs', TokenType.FEINTLIT): 172,
#     ('outputs', TokenType.FLOATERLIT): 172,
#     ('outputs', TokenType.CHANTLIT): 172,
#     ('outputs', TokenType.LEFT_PAREN): 172,
#     ('outputs', TokenType.VAR_INIT): 172,
#     ('outputs', TokenType.WIN): 172,
#     ('outputs', TokenType.LOSS): 172,

#     # <output> productions
#     ('output', TokenType.FEINTLIT): 173,
#     ('output', TokenType.FLOATERLIT): 173,
#     ('output', TokenType.CHANTLIT): 173,
#     ('output', TokenType.LEFT_PAREN): 174,
#     ('output', TokenType.VAR_INIT): 175,
#     ('output', TokenType.WIN): 176,
#     ('output', TokenType.LOSS): 176,
#     ('output', TokenType.VAR_INIT): 177,

#     # <other_outputs> productions
#     ('other_outputs', TokenType.CHANT_CONCAT): 180,
#     ('other_outputs', TokenType.RIGHT_PAREN): 179,

#     # <literal> productions
#     ('literal', TokenType.FEINTLIT): 181,
#     ('literal', TokenType.FLOATERLIT): 182,
#     ('literal', TokenType.NEGAFEINT): 183,
#     ('literal', TokenType.NEGAFLOATER): 184,
#     ('literal', TokenType.CHANTLIT): 187,
#     ('literal', TokenType.WIN): 188,
#     ('literal', TokenType.LOSS): 188,

#     # <nega_feint_lit> productions
#     ('nega_feint_lit', TokenType.NEGAFEINT): 185,

#     # <nega_floater_lit> productions
#     ('nega_floater_lit', TokenType.NEGAFLOATER): 186,

#     # <expression> productions
#     ('expression', TokenType.LEFT_PAREN): 189,
#     ('expression', TokenType.FEINTLIT): 189,
#     ('expression', TokenType.FLOATERLIT): 189,
#     ('expression', TokenType.VAR_INIT): 189,
#     ('expression', TokenType.NOT_OP): 189,
#     ('expression', TokenType.NEGAFEINT): 189,
#     ('expression', TokenType.NEGAFLOATER): 189,
#     ('expression', TokenType.CHANTLIT): 189,
#     ('expression', TokenType.WIN): 189,
#     ('expression', TokenType.LOSS): 189,
#     ('expression', TokenType.VAR_INIT): 193,

#     # <arithmetic_expression> productions
#     ('arithmetic_expression', TokenType.FEINTLIT): 194,
#     ('arithmetic_expression', TokenType.FLOATERLIT): 194,
#     ('arithmetic_expression', TokenType.VAR_INIT): 194,
#     ('arithmetic_expression', TokenType.NEGAFEINT): 194,
#     ('arithmetic_expression', TokenType.NEGAFLOATER): 194,
#     ('arithmetic_expression', TokenType.LEFT_PAREN): 194,
#     ('arithmetic_expression', TokenType.FEINT): 194,
#     ('arithmetic_expression', TokenType.FLOATER): 194,

#     # <arith_term> productions
#     ('arith_term', TokenType.FEINTLIT): 195,
#     ('arith_term', TokenType.FLOATERLIT): 195,
#     ('arith_term', TokenType.VAR_INIT): 195,
#     ('arith_term', TokenType.NEGAFEINT): 195,
#     ('arith_term', TokenType.NEGAFLOATER): 195,
#     ('arith_term', TokenType.LEFT_PAREN): 196,
#     ('arith_term', TokenType.FEINT): 197,
#     ('arith_term', TokenType.FLOATER): 197,

#     # <number> productions
#     ('number', TokenType.FEINTLIT): 198,
#     ('number', TokenType.FLOATERLIT): 199,
#     ('number', TokenType.VAR_INIT): 200,
#     ('number', TokenType.NEGAFEINT): 201,
#     ('number', TokenType.NEGAFLOATER): 202,

#     # <number_type_cast> productions
#     ('number_type_cast', TokenType.FEINT): 203,
#     ('number_type_cast', TokenType.FLOATER): 204,

#     # <feint_type_casting> productions
#     ('feint_type_casting', TokenType.FEINT): 205,

#     # <floater_type_casting> productions
#     ('floater_type_casting', TokenType.FLOATER): 206,

#     # <chant_type_casting> productions
#     ('chant_type_casting', TokenType.CHANT): 207,

#     # <stat_type_casting> productions
#     ('stat_type_casting', TokenType.STAT): 208,

#     # <more_arith_term> productions
#     ('more_arith_term', TokenType.ADD): 210,
#     ('more_arith_term', TokenType.SUB): 211,
#     ('more_arith_term', TokenType.MUL): 212,
#     ('more_arith_term', TokenType.DIV): 213,
#     ('more_arith_term', TokenType.MOD): 214,
#     ('more_arith_term', TokenType.RIGHT_PAREN): 209,
#     ('more_arith_term', TokenType.SEMICOLON): 209,

#     # <relational_expression> productions
#     ('relational_expression', TokenType.FEINTLIT): 215,
#     ('relational_expression', TokenType.FLOATERLIT): 215,
#     ('relational_expression', TokenType.VAR_INIT): 215,
#     ('relational_expression', TokenType.NEGAFEINT): 215,
#     ('relational_expression', TokenType.NEGAFLOATER): 215,
#     ('relational_expression', TokenType.LEFT_PAREN): 215,
#     ('relational_expression', TokenType.FEINT): 215,
#     ('relational_expression', TokenType.FLOATER): 215,
#     ('relational_expression', TokenType.WIN): 216,
#     ('relational_expression', TokenType.LOSS): 216,
#     ('relational_expression', TokenType.CHANTLIT): 217,
#     ('relational_expression', TokenType.LEFT_PAREN): 218,

#     # <relational_operand> productions
#     ('relational_operand', TokenType.FEINTLIT): 219,
#     ('relational_operand', TokenType.FLOATERLIT): 219,
#     ('relational_operand', TokenType.VAR_INIT): 219,
#     ('relational_operand', TokenType.NEGAFEINT): 219,
#     ('relational_operand', TokenType.NEGAFLOATER): 219,
#     ('relational_operand', TokenType.FEINT): 220,
#     ('relational_operand', TokenType.FLOATER): 220,
#     ('relational_operand', TokenType.CHANT): 221,
#     ('relational_operand', TokenType.STAT): 221,

#     # <relational_operator> productions
#     ('relational_operator', TokenType.LESS_THAN): 222,
#     ('relational_operator', TokenType.GREATER_THAN): 223,
#     ('relational_operator', TokenType.EQUAL): 224,
#     ('relational_operator', TokenType.LESS_EQUAL): 225,
#     ('relational_operator', TokenType.GREATER_EQUAL): 226,
#     ('relational_operator', TokenType.NOT_EQUAL): 227,

#     # <other_relational_operator> productions
#     ('other_relational_operator', TokenType.EQUAL): 228,
#     ('other_relational_operator', TokenType.NOT_EQUAL): 229,

#     # <logical_expression> productions
#     ('logical_expression', TokenType.NOT_OP): 231,
#     ('logical_expression', TokenType.LEFT_PAREN): 232,
#     ('logical_expression', TokenType.FEINTLIT): 233,
#     ('logical_expression', TokenType.FLOATERLIT): 233,
#     ('logical_expression', TokenType.VAR_INIT): 233,
#     ('logical_expression', TokenType.NEGAFEINT): 233,
#     ('logical_expression', TokenType.NEGAFLOATER): 233,
#     ('logical_expression', TokenType.FEINT): 233,
#     ('logical_expression', TokenType.FLOATER): 233,
#     ('logical_expression', TokenType.CHANT): 233,
#     ('logical_expression', TokenType.STAT): 233,
#     ('logical_expression', TokenType.WIN): 233,
#     ('logical_expression', TokenType.LOSS): 233,
#     ('logical_expression', TokenType.CHANTLIT): 233,

#     # <logic_term> productions
#     ('logic_term', TokenType.NOT_OP): 231,
#     ('logic_term', TokenType.LEFT_PAREN): 232,
#     ('logic_term', TokenType.FEINTLIT): 233,
#     ('logic_term', TokenType.FLOATERLIT): 233,
#     ('logic_term', TokenType.VAR_INIT): 233,
#     ('logic_term', TokenType.NEGAFEINT): 233,
#     ('logic_term', TokenType.NEGAFLOATER): 233,
#     ('logic_term', TokenType.FEINT): 233,
#     ('logic_term', TokenType.FLOATER): 233,
#     ('logic_term', TokenType.CHANT): 233,
#     ('logic_term', TokenType.STAT): 233,
#     ('logic_term', TokenType.WIN): 233,
#     ('logic_term', TokenType.LOSS): 233,
#     ('logic_term', TokenType.CHANTLIT): 233,

#     # <more_logic_term> productions
#     ('more_logic_term', TokenType.AND_OP): 235,
#     ('more_logic_term', TokenType.OR_OP): 236,
#     ('more_logic_term', TokenType.RIGHT_PAREN): 234,
#     ('more_logic_term', TokenType.SEMICOLON): 234,

#     # <assignment_expression> productions
#     ('assignment_expression', TokenType.VAR_INIT): 237,

#     # <assign_operator> productions
#     ('assign_operator', TokenType.ASSIGN): 238,
#     ('assign_operator', TokenType.ADD_ASSIGN): 239,
#     ('assign_operator', TokenType.SUB_ASSIGN): 240,
#     ('assign_operator', TokenType.MUL_ASSIGN): 241,
#     ('assign_operator', TokenType.DIV_ASSIGN): 242,
#     ('assign_operator', TokenType.MOD_ASSIGN): 243,

#     # <assign_operand> productions
#     ('assign_operand', TokenType.FEINTLIT): 244,
#     ('assign_operand', TokenType.FLOATERLIT): 244,
#     ('assign_operand', TokenType.VAR_INIT): 244,
#     ('assign_operand', TokenType.NEGAFEINT): 244,
#     ('assign_operand', TokenType.NEGAFLOATER): 244,
#     ('assign_operand', TokenType.LEFT_PAREN): 244,
#     ('assign_operand', TokenType.FEINT): 244,
#     ('assign_operand', TokenType.FLOATER): 244,
#     ('assign_operand', TokenType.CHANT): 244,
#     ('assign_operand', TokenType.STAT): 244,
#     ('assign_operand', TokenType.WIN): 244,
#     ('assign_operand', TokenType.LOSS): 244,
#     ('assign_operand', TokenType.CHANTLIT): 244,
#     ('assign_operand', TokenType.NOT_OP): 244,
#     ('assign_operand', TokenType.VAR_INIT): 247,

#     # <function_call> productions
#     ('function_call', TokenType.VAR_INIT): 249,

#     # <arguments> productions
#     ('arguments', TokenType.FEINTLIT): 250,
#     ('arguments', TokenType.FLOATERLIT): 250,
#     ('arguments', TokenType.NEGAFEINT): 250,
#     ('arguments', TokenType.NEGAFLOATER): 250,
#     ('arguments', TokenType.CHANTLIT): 250,
#     ('arguments', TokenType.WIN): 250,
#     ('arguments', TokenType.LOSS): 250,
#     ('arguments', TokenType.VAR_INIT): 250,

#     # <arg> productions
#     ('arg', TokenType.FEINTLIT): 251,
#     ('arg', TokenType.FLOATERLIT): 251,
#     ('arg', TokenType.NEGAFEINT): 251,
#     ('arg', TokenType.NEGAFLOATER): 251,
#     ('arg', TokenType.CHANTLIT): 251,
#     ('arg', TokenType.WIN): 251,
#     ('arg', TokenType.LOSS): 251,
#     ('arg', TokenType.VAR_INIT): 252,

#     # <more_args> productions
#     ('more_args', TokenType.COMMA): 253,
#     ('more_args', TokenType.RIGHT_PAREN): 252,

#     # <inbound_statement> productions
#     ('inbound_statement', TokenType.INBOUND): 254,

#     # <inputs> productions
#     ('inputs', TokenType.CHANTLIT): 255,

#     # <input> productions
#     ('input', TokenType.CHANTLIT): 256,

#     # <id_input> productions
#     ('id_input', TokenType.COMMA): 257,
#     ('id_input', TokenType.RIGHT_PAREN): 256,

#     # <dribble_statement> productions
#     ('dribble_statement', TokenType.DRIBBLE): 258,

#     # <condition> productions
#     ('condition', TokenType.FEINTLIT): 259,
#     ('condition', TokenType.FLOATERLIT): 259,
#     ('condition', TokenType.VAR_INIT): 259,
#     ('condition', TokenType.NEGAFEINT): 259,
#     ('condition', TokenType.NEGAFLOATER): 259,
#     ('condition', TokenType.LEFT_PAREN): 259,
#     ('condition', TokenType.FEINT): 259,
#     ('condition', TokenType.FLOATER): 259,
#     ('condition', TokenType.CHANT): 259,
#     ('condition', TokenType.STAT): 259,
#     ('condition', TokenType.WIN): 259,
#     ('condition', TokenType.LOSS): 259,
#     ('condition', TokenType.CHANTLIT): 259,
#     ('condition', TokenType.NOT_OP): 260,

#     # <pass_statement> productions
#     ('pass_statement', TokenType.PASS): 261,
#     ('pass_statement', TokenType.SHOOT): 262,

#     # <shoot_statement> productions
#     ('shoot_statement', TokenType.SHOOT): 263,
#     ('shoot_statement', TokenType.CODE_BLOCK_RIGHT): 264,

#     # <switch_statement> productions
#     ('switch_statement', TokenType.SWITCH): 265,

#     # <get_case> productions
#     ('get_case', TokenType.GET): 266,

#     # <get_value> productions
#     ('get_value', TokenType.FEINTLIT): 267,
#     ('get_value', TokenType.CHANTLIT): 268,

#     # <get_case_end> productions
#     ('get_case_end', TokenType.GET): 271,
#     ('get_case_end', TokenType.DEFAULT): 270,

#     # <get_default> productions
#     ('get_default', TokenType.DEFAULT): 272,
#     ('get_default', TokenType.CODE_BLOCK_RIGHT): 273,

#     # <forward_statement> productions
#     ('forward_statement', TokenType.FORWARD): 274,

#     # <forward_lit> productions
#     ('forward_lit', TokenType.FEINTLIT): 275,
#     ('forward_lit', TokenType.VAR_INIT): 276,

#     # <forward_inc_dec> productions
#     ('forward_inc_dec', TokenType.VAR_INIT): 279,
#     ('forward_inc_dec', TokenType.INCREMENT): 277,
#     ('forward_inc_dec', TokenType.DECREMENT): 278,

#     # <increment> productions
#     ('increment', TokenType.VAR_INIT): 280,
#     ('increment', TokenType.INCREMENT): 281,

#     # <decrement> productions
#     ('decrement', TokenType.VAR_INIT): 282,
#     ('decrement', TokenType.DECREMENT): 283,

#     # <resume_statement> productions
#     ('resume_statement', TokenType.RESUME): 284,

#     # <play_statement> productions
#     ('play_statement', TokenType.PLAY): 285,

#     # <run_play_statement> productions
#     ('run_play_statement', TokenType.RUN): 286,

#     # <team_block> productions
#     ('team_block', TokenType.TEAM): 287,

#     # <local_decl> productions
#     ('local_decl', TokenType.FEINT): 288,
#     ('local_decl', TokenType.FLOATER): 288,
#     ('local_decl', TokenType.CHANT): 288,
#     ('local_decl', TokenType.STAT): 288,
#     ('local_decl', TokenType.CONST): 288,
#     ('local_decl', TokenType.ZONE): 288,
#     ('local_decl', TokenType.ANNOUNCE): 289,
#     ('local_decl', TokenType.INBOUND): 289,
#     ('local_decl', TokenType.DRIBBLE): 289,
#     ('local_decl', TokenType.SWITCH): 289,
#     ('local_decl', TokenType.FORWARD): 289,
#     ('local_decl', TokenType.PLAY): 289,
#     ('local_decl', TokenType.RUN): 289,
#     ('local_decl', TokenType.TIMEOUT): 289,
#     ('local_decl', TokenType.RESUME): 289,
#     ('local_decl', TokenType.VAR_INIT): 289,

#     # <local_declaration> productions
#     ('local_declaration', TokenType.FEINT): 290,
#     ('local_declaration', TokenType.FLOATER): 290,
#     ('local_declaration', TokenType.CHANT): 290,
#     ('local_declaration', TokenType.STAT): 290,
#     ('local_declaration', TokenType.CONST): 290,
#     ('local_declaration', TokenType.ZONE): 291,

#     # <feint_typecast_value> productions
#     ('feint_typecast_value', TokenType.FLOATERLIT): 292,
#     ('feint_typecast_value', TokenType.CHANTLIT): 293,
#     ('feint_typecast_value', TokenType.WIN): 294,
#     ('feint_typecast_value', TokenType.LOSS): 294,

#     # <floater_typecast_value> productions
#     ('floater_typecast_value', TokenType.FEINTLIT): 295,
#     ('floater_typecast_value', TokenType.CHANTLIT): 296,
#     ('floater_typecast_value', TokenType.WIN): 297,
#     ('floater_typecast_value', TokenType.LOSS): 297,

#     # <chant_typecast_value> productions
#     ('chant_typecast_value', TokenType.FEINTLIT): 298,
#     ('chant_typecast_value', TokenType.FLOATERLIT): 299,
#     ('chant_typecast_value', TokenType.WIN): 300,
#     ('chant_typecast_value', TokenType.LOSS): 300,

#     # <stat_typecast_value> productions
#     ('stat_typecast_value', TokenType.FEINTLIT): 301,
#     ('stat_typecast_value', TokenType.FLOATERLIT): 301,
#     ('stat_typecast_value', TokenType.CHANTLIT): 303,

#     # <other_type_cast> productions
#     ('other_type_cast', TokenType.CHANT): 304,
#     ('other_type_cast', TokenType.STAT): 304,

#     # <team_statement> productions
#     ('team_statement', TokenType.VAR_INIT): 122,
#     ('team_statement', TokenType.FEINT): 123,
#     ('team_statement', TokenType.FLOATER): 123,
#     ('team_statement', TokenType.CHANT): 123,
#     ('team_statement', TokenType.STAT): 123,
#     ('team_statement', TokenType.ANNOUNCE): 123,
#     ('team_statement', TokenType.INBOUND): 123,
#     ('team_statement', TokenType.DRIBBLE): 123,
#     ('team_statement', TokenType.SWITCH): 123,
#     ('team_statement', TokenType.FORWARD): 123,
#     ('team_statement', TokenType.PLAY): 123,
#     ('team_statement', TokenType.RUN): 123,

#     # <more_team_statements> productions
#     ('more_team_statements', TokenType.FEINT): 119,
#     ('more_team_statements', TokenType.FLOATER): 119,
#     ('more_team_statements', TokenType.CHANT): 119,
#     ('more_team_statements', TokenType.STAT): 119,
#     ('more_team_statements', TokenType.ANNOUNCE): 119,
#     ('more_team_statements', TokenType.INBOUND): 119,
#     ('more_team_statements', TokenType.DRIBBLE): 119,
#     ('more_team_statements', TokenType.SWITCH): 119,
#     ('more_team_statements', TokenType.FORWARD): 119,
#     ('more_team_statements', TokenType.PLAY): 119,
#     ('more_team_statements', TokenType.RUN): 119,
#     ('more_team_statements', TokenType.VAR_INIT): 119,

#     # <team_stmt_end> productions
#     ('team_stmt_end', TokenType.VAR_INIT): 120,
#     ('team_stmt_end', TokenType.FEINT): 120,
#     ('team_stmt_end', TokenType.FLOATER): 120,
#     ('team_stmt_end', TokenType.CHANT): 120,
#     ('team_stmt_end', TokenType.STAT): 120,
#     ('team_stmt_end', TokenType.ANNOUNCE): 120,
#     ('team_stmt_end', TokenType.INBOUND): 120,
#     ('team_stmt_end', TokenType.DRIBBLE): 120,
#     ('team_stmt_end', TokenType.SWITCH): 120,
#     ('team_stmt_end', TokenType.FORWARD): 120,
#     ('team_stmt_end', TokenType.PLAY): 120,
#     ('team_stmt_end', TokenType.RUN): 120,
#     ('team_stmt_end', TokenType.CODE_BLOCK_RIGHT): 121,

#     # <dribble_stmt> productions
#     ('dribble_stmt', TokenType.VAR_INIT): 280,
#     ('dribble_stmt', TokenType.FEINT): 280,
#     ('dribble_stmt', TokenType.FLOATER): 280,
#     ('dribble_stmt', TokenType.CHANT): 280,
#     ('dribble_stmt', TokenType.STAT): 280,
#     ('dribble_stmt', TokenType.ANNOUNCE): 280,
#     ('dribble_stmt', TokenType.INBOUND): 280,
#     ('dribble_stmt', TokenType.DRIBBLE): 280,
#     ('dribble_stmt', TokenType.SWITCH): 280,
#     ('dribble_stmt', TokenType.FORWARD): 280,
#     ('dribble_stmt', TokenType.PLAY): 280,
#     ('dribble_stmt', TokenType.RUN): 280,
#     ('dribble_stmt', TokenType.RESUME): 280,
#     ('dribble_stmt', TokenType.CODE_BLOCK_RIGHT): 281,

#     # <dribble_stmts> productions
#     ('dribble_stmts', TokenType.VAR_INIT): 281,
#     ('dribble_stmts', TokenType.FEINT): 281,
#     ('dribble_stmts', TokenType.FLOATER): 281,
#     ('dribble_stmts', TokenType.CHANT): 281,
#     ('dribble_stmts', TokenType.STAT): 281,
#     ('dribble_stmts', TokenType.ANNOUNCE): 281,
#     ('dribble_stmts', TokenType.INBOUND): 281,
#     ('dribble_stmts', TokenType.DRIBBLE): 281,
#     ('dribble_stmts', TokenType.SWITCH): 281,
#     ('dribble_stmts', TokenType.FORWARD): 281,
#     ('dribble_stmts', TokenType.PLAY): 281,
#     ('dribble_stmts', TokenType.RUN): 281,
#     ('dribble_stmts', TokenType.RESUME): 281,

#     # <more_dribble_stmts> productions
#     ('more_dribble_stmts', TokenType.RESUME): 282,
#     ('more_dribble_stmts', TokenType.VAR_INIT): 283,
#     ('more_dribble_stmts', TokenType.FEINT): 283,
#     ('more_dribble_stmts', TokenType.FLOATER): 283,
#     ('more_dribble_stmts', TokenType.CHANT): 283,
#     ('more_dribble_stmts', TokenType.STAT): 283,
#     ('more_dribble_stmts', TokenType.ANNOUNCE): 283,
#     ('more_dribble_stmts', TokenType.INBOUND): 283,
#     ('more_dribble_stmts', TokenType.DRIBBLE): 283,
#     ('more_dribble_stmts', TokenType.SWITCH): 283,
#     ('more_dribble_stmts', TokenType.FORWARD): 283,
#     ('more_dribble_stmts', TokenType.PLAY): 283,
#     ('more_dribble_stmts', TokenType.RUN): 283,

#     # <forward_lit> productions
#     ('forward_lit', TokenType.FEINTLIT): 257,
#     ('forward_lit', TokenType.VAR_INIT): 258,

#     # <forward_assign_operator> productions
#     ('forward_assign_operator', TokenType.ADD_ASSIGN): 264,
#     ('forward_assign_operator', TokenType.SUB_ASSIGN): 265,

#     # <resume_statement> productions
#     ('resume_statement', TokenType.RESUME): 266,
#     ('resume_statement', TokenType.VAR_INIT): 267,
#     ('resume_statement', TokenType.FEINT): 267,
#     ('resume_statement', TokenType.FLOATER): 267,
#     ('resume_statement', TokenType.CHANT): 267,
#     ('resume_statement', TokenType.STAT): 267,
#     ('resume_statement', TokenType.ANNOUNCE): 267,
#     ('resume_statement', TokenType.INBOUND): 267,
#     ('resume_statement', TokenType.DRIBBLE): 267,
#     ('resume_statement', TokenType.SWITCH): 267,
#     ('resume_statement', TokenType.FORWARD): 267,
#     ('resume_statement', TokenType.PLAY): 267,
#     ('resume_statement', TokenType.RUN): 267,

#     # <typecast_value> productions
#     ('typecast_value', TokenType.FEINTLIT): 275,
#     ('typecast_value', TokenType.FLOATERLIT): 276,
#     ('typecast_value', TokenType.CHANTLIT): 277,
#     ('typecast_value', TokenType.WIN): 278,
#     ('typecast_value', TokenType.LOSS): 278,
#     ('typecast_value', TokenType.VAR_INIT): 279
# } 

from Analyzers.lexical_analyzer.tokens import TokenType

PREDICT_SETS = {
    # <program> productions
    ('program', TokenType.FEINT): 1,
    ('program', TokenType.FLOATER): 1,
    ('program', TokenType.CHANT): 1,
    ('program', TokenType.STAT): 1,
    ('program', TokenType.CONST): 1,
    ('program', TokenType.ZONE): 1,
    ('program', TokenType.TEAM): 1,

    # <global_decl> productions
    ('global_decl', TokenType.FEINT): 2,
    ('global_decl', TokenType.FLOATER): 2,
    ('global_decl', TokenType.CHANT): 2,
    ('global_decl', TokenType.STAT): 2,
    ('global_decl', TokenType.CONST): 2,
    ('global_decl', TokenType.ZONE): 2,
    ('global_decl', TokenType.WILT): 3,
    ('global_decl', TokenType.DUNK): 3,
    ('global_decl', TokenType.TEAM): 3,

    # <global_declaration> productions
    ('global_declaration', TokenType.FEINT): 4,
    ('global_declaration', TokenType.FLOATER): 4,
    ('global_declaration', TokenType.CHANT): 4,
    ('global_declaration', TokenType.STAT): 4,
    ('global_declaration', TokenType.CONST): 5,
    ('global_declaration', TokenType.ZONE): 6,

    # <variable_dec> productions
    ('variable_dec', TokenType.FEINT): 7,
    ('variable_dec', TokenType.FLOATER): 8,
    ('variable_dec', TokenType.CHANT): 9,
    ('variable_dec', TokenType.STAT): 10,

    # <feint_dec> productions
    ('feint_dec', TokenType.FEINT): 11,

    # <more_feint> productions
    ('more_feint', TokenType.ASSIGN): 13,
    ('more_feint', TokenType.SEMICOLON): 12,

    # <feint_init> productions
    ('feint_init', TokenType.ASSIGN): 15,
    ('feint_init', TokenType.SEMICOLON): 14,

    # <feint_init_end> productions
    ('feint_init_end', TokenType.COMMA): 18,
    ('feint_init_end', TokenType.SEMICOLON): 17,

    # <floater_dec> productions
    ('floater_dec', TokenType.FLOATER): 19,

    # <more_floater> productions
    ('more_floater', TokenType.ASSIGN): 21,
    ('more_floater', TokenType.SEMICOLON): 20,

    # <floater_init> productions
    ('floater_init', TokenType.ASSIGN): 23,
    ('floater_init', TokenType.SEMICOLON): 22,

    # <floater_init_end> productions
    ('floater_init_end', TokenType.COMMA): 26,
    ('floater_init_end', TokenType.SEMICOLON): 25,

    # <chant_dec> productions
    ('chant_dec', TokenType.CHANT): 27,

    # <more_chant> productions
    ('more_chant', TokenType.ASSIGN): 29,
    ('more_chant', TokenType.SEMICOLON): 28,

    # <chant_init> productions
    ('chant_init', TokenType.ASSIGN): 31,
    ('chant_init', TokenType.SEMICOLON): 30,

    # <chant_init_end> productions
    ('chant_init_end', TokenType.COMMA): 34,
    ('chant_init_end', TokenType.SEMICOLON): 33,

    # <stat_dec> productions
    ('stat_dec', TokenType.STAT): 35,

    # <more_stat> productions
    ('more_stat', TokenType.ASSIGN): 37,
    ('more_stat', TokenType.SEMICOLON): 36,

    # <stat_init> productions
    ('stat_init', TokenType.ASSIGN): 39,
    ('stat_init', TokenType.SEMICOLON): 38,

    # <stat_value> productions
    ('stat_value', TokenType.WIN): 40,
    ('stat_value', TokenType.LOSS): 41,

    # <stat_init_end> productions
    ('stat_init_end', TokenType.COMMA): 43,
    ('stat_init_end', TokenType.SEMICOLON): 42,

    # <const_dec> productions
    ('const_dec', TokenType.FEINT): 44,
    ('const_dec', TokenType.FLOATER): 45,
    ('const_dec', TokenType.CHANT): 46,
    ('const_dec', TokenType.STAT): 47,

    # <const_feint> productions
    ('const_feint', TokenType.FEINT): 48,

    # <feint_const_init> productions
    ('feint_const_init', TokenType.ASSIGN): 49,

    # <feint_const> productions
    ('feint_const', TokenType.ASSIGN): 50,

    # <feint_const_end> productions
    ('feint_const_end', TokenType.COMMA): 51,
    ('feint_const_end', TokenType.SEMICOLON): 52,

    # <const_floater> productions
    ('const_floater', TokenType.FLOATER): 53,

    # <floater_const_init> productions
    ('floater_const_init', TokenType.ASSIGN): 54,

    # <floater_const> productions
    ('floater_const', TokenType.ASSIGN): 55,

    # <floater_const_end> productions
    ('floater_const_end', TokenType.COMMA): 56,
    ('floater_const_end', TokenType.SEMICOLON): 57,

    # <const_chant> productions
    ('const_chant', TokenType.CHANT): 58,

    # <chant_const_init> productions
    ('chant_const_init', TokenType.ASSIGN): 59,

    # <chant_const> productions
    ('chant_const', TokenType.ASSIGN): 60,

    # <chant_const_end> productions
    ('chant_const_end', TokenType.COMMA): 61,
    ('chant_const_end', TokenType.SEMICOLON): 62,

    # <const_stat> productions
    ('const_stat', TokenType.STAT): 63,

    # <stat_const_init> productions
    ('stat_const_init', TokenType.ASSIGN): 64,

    # <stat_const> productions
    ('stat_const', TokenType.ASSIGN): 65,

    # <stat_const_end> productions
    ('stat_const_end', TokenType.COMMA): 66,
    ('stat_const_end', TokenType.SEMICOLON): 67,

    # <array_dec> productions
    ('array_dec', TokenType.FEINT): 68,
    ('array_dec', TokenType.FLOATER): 69,
    ('array_dec', TokenType.CHANT): 70,

    # <feint_array> productions
    ('feint_array', TokenType.FEINT): 71,

    # <2D_array> productions
    ('2D_array', TokenType.ARRAY_INDEX_LEFT): 73,
    ('2D_array', TokenType.ASSIGN): 72,
    ('2D_array', TokenType.SEMICOLON): 72,

    # <feint_array_init> productions
    ('feint_array_init', TokenType.ASSIGN): 75,
    ('feint_array_init', TokenType.SEMICOLON): 74,

    # <feint_row> productions
    ('feint_row', TokenType.FEINTLIT): 76,
    ('feint_row', TokenType.CODE_BLOCK_LEFT): 77,

    # <2D_feint_row> productions
    ('2D_feint_row', TokenType.COMMA): 79,
    ('2D_feint_row', TokenType.CODE_BLOCK_RIGHT): 78,

    # <more_feint_lit> productions
    ('more_feint_lit', TokenType.COMMA): 81,
    ('more_feint_lit', TokenType.CODE_BLOCK_RIGHT): 80,

    # <floater_array> productions
    ('floater_array', TokenType.FLOATER): 82,

    # <floater_array_init> productions
    ('floater_array_init', TokenType.ASSIGN): 84,
    ('floater_array_init', TokenType.SEMICOLON): 83,

    # <floater_row> productions
    ('floater_row', TokenType.FLOATERLIT): 85,
    ('floater_row', TokenType.CODE_BLOCK_LEFT): 86,

    # <2D_floater_row> productions
    ('2D_floater_row', TokenType.COMMA): 88,
    ('2D_floater_row', TokenType.CODE_BLOCK_RIGHT): 87,

    # <more_floater_lit> productions
    ('more_floater_lit', TokenType.COMMA): 90,
    ('more_floater_lit', TokenType.CODE_BLOCK_RIGHT): 89,

    # <chant_array> productions
    ('chant_array', TokenType.CHANT): 91,

    # <chant_array_init> productions
    ('chant_array_init', TokenType.ASSIGN): 93,
    ('chant_array_init', TokenType.SEMICOLON): 92,

    # <chant_row> productions
    ('chant_row', TokenType.CHANTLIT): 94,
    ('chant_row', TokenType.CODE_BLOCK_LEFT): 95,

    # <2D_chant_row> productions
    ('2D_chant_row', TokenType.COMMA): 97,
    ('2D_chant_row', TokenType.CODE_BLOCK_RIGHT): 96,

    # <more_chant_lit> productions
    ('more_chant_lit', TokenType.COMMA): 99,
    ('more_chant_lit', TokenType.CODE_BLOCK_RIGHT): 98,

    # <function_def> productions
    ('function_def', TokenType.WILT): 101,
    ('function_def', TokenType.DUNK): 102,
    ('function_def', TokenType.TEAM): 100,

    # <function_declared> productions
    ('function_declared', TokenType.FEINT): 103,
    ('function_declared', TokenType.FLOATER): 104,
    ('function_declared', TokenType.CHANT): 105,
    ('function_declared', TokenType.STAT): 106,

    # <dunk_func_declared> productions
    ('dunk_func_declared', TokenType.VAR_INIT): 107,

    # <feint_function> productions
    ('feint_function', TokenType.FEINT): 108,

    # <floater_function> productions
    ('floater_function', TokenType.FLOATER): 109,

    # <chant_function> productions
    ('chant_function', TokenType.CHANT): 110,

    # <stat_function> productions
    ('stat_function', TokenType.STAT): 111,

    # <dunk_function> productions
    ('dunk_function', TokenType.VAR_INIT): 112,

    # <func_parameters> productions
    ('func_parameters', TokenType.VAR_INIT): 114,
    ('func_parameters', TokenType.RIGHT_PAREN): 113,

    # <param_end> productions
    ('param_end', TokenType.COMMA): 115,
    ('param_end', TokenType.RIGHT_PAREN): 116,

    # <function_statement> productions
    ('function_statement', TokenType.FEINT): 117,
    ('function_statement', TokenType.FLOATER): 117,
    ('function_statement', TokenType.CHANT): 117,
    ('function_statement', TokenType.STAT): 117,
    ('function_statement', TokenType.ANNOUNCE): 117,
    ('function_statement', TokenType.INBOUND): 117,
    ('function_statement', TokenType.DRIBBLE): 117,
    ('function_statement', TokenType.SWITCH): 117,
    ('function_statement', TokenType.FORWARD): 117,
    ('function_statement', TokenType.PLAY): 117,
    ('function_statement', TokenType.RUN): 117,
    ('function_statement', TokenType.VAR_INIT): 117,
    ('function_statement', TokenType.REBOUND): 117,
    ('function_statement', TokenType.CODE_BLOCK_RIGHT): 118,

    # <team_statement> productions
    ('team_statement', TokenType.FEINT): 119,
    ('team_statement', TokenType.FLOATER): 119,
    ('team_statement', TokenType.CHANT): 119,
    ('team_statement', TokenType.STAT): 119,
    ('team_statement', TokenType.ANNOUNCE): 119,
    ('team_statement', TokenType.INBOUND): 119,
    ('team_statement', TokenType.DRIBBLE): 119,
    ('team_statement', TokenType.SWITCH): 119,
    ('team_statement', TokenType.FORWARD): 119,
    ('team_statement', TokenType.PLAY): 119,
    ('team_statement', TokenType.RUN): 119,
    ('team_statement', TokenType.VAR_INIT): 119,
    ('team_statement', TokenType.CODE_BLOCK_RIGHT): 120,

    # <statement> productions
    ('statement', TokenType.FEINT): 121,
    ('statement', TokenType.FLOATER): 121,
    ('statement', TokenType.CHANT): 121,
    ('statement', TokenType.STAT): 121,
    ('statement', TokenType.ANNOUNCE): 122,
    ('statement', TokenType.INBOUND): 123,
    ('statement', TokenType.DRIBBLE): 124,
    ('statement', TokenType.SWITCH): 125,
    ('statement', TokenType.FORWARD): 126,
    ('statement', TokenType.PLAY): 127,
    ('statement', TokenType.RUN): 128,
    ('statement', TokenType.VAR_INIT): 129,

    # <follow_statement> productions
    ('follow_statement', TokenType.INCREMENT): 130,
    ('follow_statement', TokenType.DECREMENT): 131,
    ('follow_statement', TokenType.LEFT_PAREN): 132,
    ('follow_statement', TokenType.ASSIGN): 133,
    ('follow_statement', TokenType.ADD_ASSIGN): 133,
    ('follow_statement', TokenType.SUB_ASSIGN): 133,
    ('follow_statement', TokenType.MUL_ASSIGN): 133,
    ('follow_statement', TokenType.DIV_ASSIGN): 133,
    ('follow_statement', TokenType.MOD_ASSIGN): 133,
    ('follow_statement', TokenType.ARRAY_INDEX_LEFT): 134,

    # <array_manipulation> productions
    ('array_manipulation', TokenType.ARRAY_INDEX_LEFT): 135,

    # <element_index> productions
    ('element_index', TokenType.FEINTLIT): 136,
    ('element_index', TokenType.VAR_INIT): 136,

    # <2d_manipulation> productions
    ('2d_manipulation', TokenType.ARRAY_INDEX_LEFT): 137,
    ('2d_manipulation', TokenType.ASSIGN): 138,
    ('2d_manipulation', TokenType.SEMICOLON): 138,

    # <array_man> productions
    ('array_man', TokenType.ASSIGN): 139,
    ('array_man', TokenType.SEMICOLON): 140,

    # <array_elem> productions
    ('array_elem', TokenType.FEINTLIT): 141,
    ('array_elem', TokenType.FLOATERLIT): 142,
    ('array_elem', TokenType.CHANTLIT): 143,
    ('array_elem', TokenType.VAR_INIT): 141,
    ('array_elem', TokenType.LEFT_PAREN): 141,

    # <rebound_statement> productions
    ('rebound_statement', TokenType.REBOUND): 144,

    # <rebound_value> productions
    ('rebound_value', TokenType.FEINTLIT): 145,
    ('rebound_value', TokenType.FLOATERLIT): 145,
    ('rebound_value', TokenType.CHANTLIT): 145,
    ('rebound_value', TokenType.VAR_INIT): 146,
    ('rebound_value', TokenType.WIN): 145,
    ('rebound_value', TokenType.LOSS): 145,
    ('rebound_value', TokenType.LEFT_PAREN): 147,
    ('rebound_value', TokenType.NEGAFEINT): 145,
    ('rebound_value', TokenType.NEGAFLOATER): 145,
    ('rebound_value', TokenType.NOT_OP): 147,
    ('rebound_value',TokenType.LEFT_PAREN): 147,

    # <announce_statement> productions
    ('announce_statement', TokenType.ANNOUNCE): 148,

    # <outputs> productions
    ('outputs', TokenType.FEINTLIT): 149,
    ('outputs', TokenType.FLOATERLIT): 149,
    ('outputs', TokenType.CHANTLIT): 149,
    ('outputs', TokenType.VAR_INIT): 149,
    ('outputs', TokenType.WIN): 149, 
    ('outputs', TokenType.LOSS): 149,
    ('outputs', TokenType.LEFT_PAREN): 149,
    ('outputs', TokenType.NEGAFEINT): 149,
    ('outputs', TokenType.NEGAFLOATER): 149,
    ('outputs', TokenType.NOT_OP): 149,

    # <output> productions
    ('output', TokenType.FEINTLIT): 150,
    ('output', TokenType.FLOATERLIT): 150,
    ('output', TokenType.CHANTLIT): 150,
    ('output', TokenType.VAR_INIT): 152,
    ('output', TokenType.WIN): 153,
    ('output', TokenType.LOSS): 153,
    ('output', TokenType.LEFT_PAREN): 151,
    ('output', TokenType.NEGAFEINT): 150,
    ('output', TokenType.NEGAFLOATER): 150,
    ('output', TokenType.NOT_OP): 151,

    # <array_access> productions  
    ('array_access', TokenType.VAR_INIT): 155,

    # <other_outputs> productions
    ('other_outputs', TokenType.CHANT_CONCAT): 157,
    ('other_outputs', TokenType.RIGHT_PAREN): 156,

    # <literal> productions
    ('literal', TokenType.FEINTLIT): 158,
    ('literal', TokenType.FLOATERLIT): 159,
    ('literal', TokenType.NEGAFEINT): 160,
    ('literal', TokenType.NEGAFLOATER): 161,
    ('literal', TokenType.CHANTLIT): 162,
    ('literal', TokenType.WIN): 163,
    ('literal', TokenType.LOSS): 163,

    # <nega_feint_lit> productions
    ('nega_feint_lit', TokenType.NEGAFEINT): 164,

    # <nega_floater_lit> productions
    ('nega_floater_lit', TokenType.NEGAFLOATER): 165,

    # <expression> productions
    ('expression', TokenType.FEINTLIT): 166,
    ('expression', TokenType.FLOATERLIT): 166,
    ('expression', TokenType.VAR_INIT): 166,
    ('expression', TokenType.LEFT_PAREN): 166,
    ('expression', TokenType.NOT_OP): 168,
    ('expression', TokenType.NEGAFEINT): 166,
    ('expression', TokenType.NEGAFLOATER): 166,
    ('expression', TokenType.CHANTLIT): 167,
    ('expression', TokenType.WIN): 168,
    ('expression', TokenType.LOSS): 168,
    ('expression', TokenType.FEINT): 166,
    ('expression', TokenType.FLOATER): 166,
    ('expression', TokenType.CHANT): 167,
    ('expression', TokenType.STAT): 168,

    # <arithmetic_expression> productions
    ('arithmetic_expression', TokenType.LEFT_PAREN): 170,
    ('arithmetic_expression', TokenType.FEINTLIT): 169,
    ('arithmetic_expression', TokenType.FLOATERLIT): 169,
    ('arithmetic_expression', TokenType.VAR_INIT): 169,
    ('arithmetic_expression', TokenType.NEGAFEINT): 169,
    ('arithmetic_expression', TokenType.NEGAFLOATER): 169,
    ('arithmetic_expression', TokenType.FEINT): 169,
    ('arithmetic_expression', TokenType.FLOATER): 169,

    # <arith_term> productions
    ('arith_term', TokenType.LEFT_PAREN): 172,
    ('arith_term', TokenType.FEINTLIT): 171,
    ('arith_term', TokenType.FLOATERLIT): 171,
    ('arith_term', TokenType.VAR_INIT): 171,
    ('arith_term', TokenType.NEGAFEINT): 171,
    ('arith_term', TokenType.NEGAFLOATER): 171,

    # <number> productions
    ('number', TokenType.FEINTLIT): 173,
    ('number', TokenType.FLOATERLIT): 174,
    ('number', TokenType.VAR_INIT): 175,
    ('number', TokenType.NEGAFEINT): 176,
    ('number', TokenType.NEGAFLOATER): 177,

    # <number_type_cast> productions
    ('number_type_cast', TokenType.FEINT): 178,
    ('number_type_cast', TokenType.FLOATER): 179,

    # <feint_type_casting> productions
    ('feint_type_casting', TokenType.FEINT): 180,

    # <floater_type_casting> productions
    ('floater_type_casting', TokenType.FLOATER): 181,

    # <chant_type_casting> productions
    ('chant_type_casting', TokenType.CHANT): 182,

    # <stat_type_casting> productions
    ('stat_type_casting', TokenType.STAT): 183,

    # <more_arith_term> productions
    ('more_arith_term', TokenType.ADD): 185,
    ('more_arith_term', TokenType.SUB): 186,
    ('more_arith_term', TokenType.MUL): 187,
    ('more_arith_term', TokenType.DIV): 188,
    ('more_arith_term', TokenType.MOD): 189,
    ('more_arith_term', TokenType.RIGHT_PAREN): 184,
    ('more_arith_term', TokenType.COMMA): 184,
    ('more_arith_term', TokenType.SEMICOLON): 184,
    ('more_arith_term', TokenType.CODE_BLOCK_RIGHT): 184,

    # <relational_expression> productions
    ('relational_expression', TokenType.FEINTLIT): 190,
    ('relational_expression', TokenType.FLOATERLIT): 190,
    ('relational_expression', TokenType.VAR_INIT): 190,
    ('relational_expression', TokenType.NEGAFEINT): 190,
    ('relational_expression', TokenType.NEGAFLOATER): 190,
    ('relational_expression', TokenType.LEFT_PAREN): 193,
    ('relational_expression', TokenType.FEINT): 190,
    ('relational_expression', TokenType.FLOATER): 190,
    ('relational_expression', TokenType.CHANTLIT): 192,
    ('relational_expression', TokenType.CHANT): 192,
    ('relational_expression', TokenType.STAT): 191,
    ('relational_expression', TokenType.WIN): 191,
    ('relational_expression', TokenType.LOSS): 191,

    # <number_rel_operand> productions
    ('number_rel_operand', TokenType.FEINTLIT): 194,
    ('number_rel_operand', TokenType.FLOATERLIT): 194,
    ('number_rel_operand', TokenType.VAR_INIT): 194,
    ('number_rel_operand', TokenType.NEGAFEINT): 194,
    ('number_rel_operand', TokenType.NEGAFLOATER): 194,
    ('number_rel_operand', TokenType.FEINT): 195,
    ('number_rel_operand', TokenType.FLOATER): 195,
    ('number_rel_operand', TokenType.LEFT_PAREN): 194,

    # <relational_operator> productions
    ('relational_operator', TokenType.LESS_THAN): 196,
    ('relational_operator', TokenType.GREATER_THAN): 197,
    ('relational_operator', TokenType.EQUAL): 198,
    ('relational_operator', TokenType.LESS_EQUAL): 199,
    ('relational_operator', TokenType.GREATER_EQUAL): 200,
    ('relational_operator', TokenType.NOT_EQUAL): 201,

    # <other_relational_operator> productions
    ('other_relational_operator', TokenType.EQUAL): 202,
    ('other_relational_operator', TokenType.NOT_EQUAL): 203,

    # <stat_rel_operand> productions
    ('stat_rel_operand', TokenType.WIN): 204,
    ('stat_rel_operand', TokenType.LOSS): 204,
    ('stat_rel_operand', TokenType.VAR_INIT): 205,
    ('stat_rel_operand', TokenType.STAT): 206,

    # <chant_rel_operand> productions
    ('chant_rel_operand', TokenType.CHANTLIT): 209,
    ('chant_rel_operand', TokenType.VAR_INIT): 207,
    ('chant_rel_operand', TokenType.CHANT): 208,

    # <logical_expression> productions
    ('logical_expression', TokenType.NOT_OP): 210,
    ('logical_expression', TokenType.LEFT_PAREN): 211,
    ('logical_expression', TokenType.FEINTLIT): 211,
    ('logical_expression', TokenType.FLOATERLIT): 211,
    ('logical_expression', TokenType.VAR_INIT): 211,
    ('logical_expression', TokenType.NEGAFEINT): 211,
    ('logical_expression', TokenType.NEGAFLOATER): 211,
    ('logical_expression', TokenType.WIN): 211,
    ('logical_expression', TokenType.LOSS): 211,

    # <not_expr> productions
    ('not_expr', TokenType.NOT_OP): 212,

    # <compound_log_expr> productions
    ('compound_log_expr', TokenType.LEFT_PAREN): 213,
    ('compound_log_expr', TokenType.FEINTLIT): 213,
    ('compound_log_expr', TokenType.FLOATERLIT): 213,
    ('compound_log_expr', TokenType.VAR_INIT): 213,
    ('compound_log_expr', TokenType.NEGAFEINT): 213,
    ('compound_log_expr', TokenType.NEGAFLOATER): 213,
    ('compound_log_expr', TokenType.WIN): 213,
    ('compound_log_expr', TokenType.LOSS): 213,

    # <log_term> productions
    ('log_term', TokenType.NOT_OP): 214,
    ('log_term', TokenType.LEFT_PAREN): 215,
    ('log_term', TokenType.FEINTLIT): 215,
    ('log_term', TokenType.FLOATERLIT): 215,
    ('log_term', TokenType.VAR_INIT): 215,
    ('log_term', TokenType.NEGAFEINT): 215,
    ('log_term', TokenType.NEGAFLOATER): 215,
    ('log_term', TokenType.WIN): 215,
    ('log_term', TokenType.LOSS): 215,

    # <other_log_term> productions
    ('other_log_term', TokenType.WIN): 216,
    ('other_log_term', TokenType.LOSS): 216,
    ('other_log_term', TokenType.LEFT_PAREN): 217,
    ('other_log_term', TokenType.FEINTLIT): 218,
    ('other_log_term', TokenType.FLOATERLIT): 218,
    ('other_log_term', TokenType.VAR_INIT): 218,
    ('other_log_term', TokenType.NEGAFEINT): 218,
    ('other_log_term', TokenType.NEGAFLOATER): 218,

    # <more_log_term> productions
    ('more_log_term', TokenType.AND_OP): 220,
    ('more_log_term', TokenType.OR_OP): 220,
    ('more_log_term', TokenType.RIGHT_PAREN): 219,
    ('more_log_term', TokenType.SEMICOLON): 219,
    ('more_log_term', TokenType.CODE_BLOCK_RIGHT): 219,

    # <log_operator> productions
    ('log_operator', TokenType.AND_OP): 221,
    ('log_operator', TokenType.OR_OP): 222,

    # <assignment_expression> productions
    ('assignment_expression', TokenType.ASSIGN): 223,
    ('assignment_expression', TokenType.ADD_ASSIGN): 223,
    ('assignment_expression', TokenType.SUB_ASSIGN): 223,
    ('assignment_expression', TokenType.MUL_ASSIGN): 223,
    ('assignment_expression', TokenType.DIV_ASSIGN): 223,
    ('assignment_expression', TokenType.MOD_ASSIGN): 223,

    # <assign_operator> productions
    ('assign_operator', TokenType.ASSIGN): 224,
    ('assign_operator', TokenType.ADD_ASSIGN): 225,
    ('assign_operator', TokenType.SUB_ASSIGN): 226,
    ('assign_operator', TokenType.MUL_ASSIGN): 227,
    ('assign_operator', TokenType.DIV_ASSIGN): 228,
    ('assign_operator', TokenType.MOD_ASSIGN): 229,

    # <assign_operand> productions
    ('assign_operand', TokenType.LEFT_PAREN): 230,
    ('assign_operand', TokenType.FEINTLIT): 230,
    ('assign_operand', TokenType.FLOATERLIT): 230,
    ('assign_operand', TokenType.VAR_INIT): 230,
    ('assign_operand', TokenType.NEGAFEINT): 230,
    ('assign_operand', TokenType.NEGAFLOATER): 230,
    ('assign_operand', TokenType.NOT_OP): 232,
    ('assign_operand', TokenType.CHANTLIT): 232,
    ('assign_operand', TokenType.WIN): 232,
    ('assign_operand', TokenType.LOSS): 232,

    # <function_call> productions
    ('function_call', TokenType.LEFT_PAREN): 234,

    # <arguments> productions
    ('arguments', TokenType.FEINTLIT): 235,
    ('arguments', TokenType.FLOATERLIT): 235,
    ('arguments', TokenType.CHANTLIT): 235,
    ('arguments', TokenType.VAR_INIT): 235,
    ('arguments', TokenType.WIN): 235,
    ('arguments', TokenType.LOSS): 235,
    ('arguments', TokenType.NEGAFEINT): 235,
    ('arguments', TokenType.NEGAFLOATER): 235,
    ('arguments', TokenType.RIGHT_PAREN): 239,

    # <arg> productions
    ('arg', TokenType.FEINTLIT): 236,
    ('arg', TokenType.FLOATERLIT): 236,
    ('arg', TokenType.CHANTLIT): 236,
    ('arg', TokenType.VAR_INIT): 237,
    ('arg', TokenType.WIN): 236,
    ('arg', TokenType.LOSS): 236,
    ('arg', TokenType.NEGAFEINT): 236,
    ('arg', TokenType.NEGAFLOATER): 236,

    # <more_args> productions
    ('more_args', TokenType.COMMA): 238,
    ('more_args', TokenType.RIGHT_PAREN): 239,

    # <inbound_statement> productions
    ('inbound_statement', TokenType.INBOUND): 240,

    # <dribble_statement> productions
    ('dribble_statement', TokenType.DRIBBLE): 241,

    # <add_condition> productions
    ('add_condition', TokenType.PASS): 242,
    ('add_condition', TokenType.SHOOT): 243,
    ('add_condition', TokenType.SEMICOLON): 244,
    ('add_condition', TokenType.ANNOUNCE): 244,
    ('add_condition', TokenType.INBOUND): 244,
    ('add_condition', TokenType.DRIBBLE): 244,
    ('add_condition', TokenType.SWITCH): 244,
    ('add_condition', TokenType.FORWARD): 244,
    ('add_condition', TokenType.PLAY): 244,
    ('add_condition', TokenType.RUN): 244,
    ('add_condition', TokenType.VAR_INIT): 244,
    ('add_condition', TokenType.CODE_BLOCK_RIGHT): 244,

    # <loop_statements> productions
    ('loop_statements', TokenType.FEINT): 245,
    ('loop_statements', TokenType.FLOATER): 245,
    ('loop_statements', TokenType.CHANT): 245,
    ('loop_statements', TokenType.STAT): 245,
    ('loop_statements', TokenType.ANNOUNCE): 245,
    ('loop_statements', TokenType.INBOUND): 245,
    ('loop_statements', TokenType.DRIBBLE): 245,
    ('loop_statements', TokenType.SWITCH): 245,
    ('loop_statements', TokenType.FORWARD): 245,
    ('loop_statements', TokenType.PLAY): 245,
    ('loop_statements', TokenType.RUN): 245,
    ('loop_statements', TokenType.VAR_INIT): 245,
    ('loop_statements', TokenType.RESUME): 245,
    ('loop_statements', TokenType.CODE_BLOCK_RIGHT): 246,

    # <loop_statement> productions
    ('loop_statement', TokenType.FEINT): 247,
    ('loop_statement', TokenType.FLOATER): 247,
    ('loop_statement', TokenType.CHANT): 247,
    ('loop_statement', TokenType.STAT): 247,
    ('loop_statement', TokenType.ANNOUNCE): 247,
    ('loop_statement', TokenType.INBOUND): 247,
    ('loop_statement', TokenType.DRIBBLE): 247,
    ('loop_statement', TokenType.SWITCH): 247,
    ('loop_statement', TokenType.FORWARD): 247,
    ('loop_statement', TokenType.PLAY): 247,
    ('loop_statement', TokenType.RUN): 247,
    ('loop_statement', TokenType.VAR_INIT): 247,
    ('loop_statement', TokenType.RESUME): 248,

    # <resume_statement> productions
    ('resume_statement', TokenType.RESUME): 268,

    # <switch_statement> productions
    ('switch_statement', TokenType.SWITCH): 249,

    # <get_case> productions
    ('get_case', TokenType.GET): 250,

    # <get_value> productions
    ('get_value', TokenType.FEINTLIT): 251,
    ('get_value', TokenType.CHANTLIT): 252,

    # <timeout_statement> productions
    ('timeout_statement', TokenType.TIMEOUT): 253,

    # <get_case_end> productions
    ('get_case_end', TokenType.GET): 255,
    ('get_case_end', TokenType.DEFAULT): 254,
    ('get_case_end', TokenType.CODE_BLOCK_RIGHT): 254,

    # <get_default> productions
    ('get_default', TokenType.DEFAULT): 256,
    ('get_default', TokenType.CODE_BLOCK_RIGHT): 257,

    # <forward_statement> productions
    ('forward_statement', TokenType.FORWARD): 258,

    # <forward_lit> productions
    ('forward_lit', TokenType.FEINTLIT): 259,
    ('forward_lit', TokenType.VAR_INIT): 260,

    # <forward_inc_dec> productions
    ('forward_inc_dec', TokenType.INCREMENT): 261,
    ('forward_inc_dec', TokenType.DECREMENT): 262,
    ('forward_inc_dec', TokenType.ADD_ASSIGN): 263,
    ('forward_inc_dec', TokenType.SUB_ASSIGN): 263,

    # <increment> productions
    ('increment', TokenType.INCREMENT): 264,

    # <decrement> productions
    ('decrement', TokenType.DECREMENT): 265,

    # <forward_assign_operator> productions
    ('forward_assign_operator', TokenType.ADD_ASSIGN): 266,
    ('forward_assign_operator', TokenType.SUB_ASSIGN): 267,

    # <play_statement> productions
    ('play_statement', TokenType.PLAY): 270,

    # <run_play_statement> productions
    ('run_play_statement', TokenType.RUN): 271,

    # <team_block> productions
    ('team_block', TokenType.TEAM): 272,

    # <local_decl> productions
    ('local_decl', TokenType.FEINT): 273,
    ('local_decl', TokenType.FLOATER): 273,
    ('local_decl', TokenType.CHANT): 273,
    ('local_decl', TokenType.STAT): 273,
    ('local_decl', TokenType.CODE_BLOCK_LEFT): 273,
    ('local_decl', TokenType.CODE_BLOCK_RIGHT): 274,

    # <local_declaration> productions
    ('local_declaration', TokenType.FEINT): 275,
    ('local_declaration', TokenType.FLOATER): 275,
    ('local_declaration', TokenType.CHANT): 275,
    ('local_declaration', TokenType.STAT): 275,
    ('local_declaration', TokenType.ZONE): 276,

    # <typecast_value> productions
    ('typecast_value', TokenType.FEINTLIT): 277,
    ('typecast_value', TokenType.FLOATERLIT): 278,
    ('typecast_value', TokenType.CHANTLIT): 279,
    ('typecast_value', TokenType.WIN): 280,
    ('typecast_value', TokenType.LOSS): 280,
    ('typecast_value', TokenType.VAR_INIT): 281,
}