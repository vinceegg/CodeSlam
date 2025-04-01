from Analyzers.lexical_analyzer.tokens import TokenType

PREDICT_SETS = {
    # <program> productions
    ('program', TokenType.FEINT): 1,
    ('program', TokenType.FLOATER): 1,
    ('program', TokenType.CHANT): 1,
    ('program', TokenType.STAT): 1,
    ('program', TokenType.CONST): 1,
    ('program', TokenType.ZONE): 1,
    ('program', TokenType.WILT): 1,
    ('program', TokenType.DUNK): 1,
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
    ('const_dec', TokenType.CONST): 44,

    # <array_dec> productions
    ('array_dec', TokenType.FEINT): 45,
    ('array_dec', TokenType.FLOATER): 46,
    ('array_dec', TokenType.CHANT): 47,

    # <feint_array> productions
    ('feint_array', TokenType.FEINT): 48,

    # <2D_array> productions
    ('2D_array', TokenType.ARRAY_INDEX_LEFT): 50,
    ('2D_array', TokenType.ASSIGN): 49,

    # <feint_array_init> productions
    ('feint_array_init', TokenType.ASSIGN): 52,
    ('feint_array_init', TokenType.SEMICOLON): 51,

    # <feint_row> productions
    ('feint_row', TokenType.FEINTLIT): 53,
    ('feint_row', TokenType.CODE_BLOCK_LEFT): 54,

    # <2d_feint_row> productions
    ('2d_feint_row', TokenType.COMMA): 56,
    ('2d_feint_row', TokenType.CODE_BLOCK_RIGHT): 55,

    # <more_feint_lit> productions
    ('more_feint_lit', TokenType.COMMA): 58,
    ('more_feint_lit', TokenType.CODE_BLOCK_RIGHT): 57,

    # <floater_array> productions
    ('floater_array', TokenType.FLOATER): 59,

    # <floater_array_init> productions
    ('floater_array_init', TokenType.ASSIGN): 61,
    ('floater_array_init', TokenType.SEMICOLON): 60,

    # <floater_row> productions
    ('floater_row', TokenType.FLOATERLIT): 62,
    ('floater_row', TokenType.CODE_BLOCK_LEFT): 63,

    # <2d_floater_row> productions
    ('2d_floater_row', TokenType.COMMA): 65,
    ('2d_floater_row', TokenType.CODE_BLOCK_RIGHT): 64,

    # <more_floater_lit> productions
    ('more_floater_lit', TokenType.COMMA): 67,
    ('more_floater_lit', TokenType.CODE_BLOCK_RIGHT): 66,

    # <chant_array> productions
    ('chant_array', TokenType.CHANT): 68,

    # <chant_array_init> productions
    ('chant_array_init', TokenType.ASSIGN): 70,
    ('chant_array_init', TokenType.SEMICOLON): 69,

    # <chant_row> productions
    ('chant_row', TokenType.CHANTLIT): 71,
    ('chant_row', TokenType.CODE_BLOCK_LEFT): 72,

    # <2d_chant_row> productions
    ('2d_chant_row', TokenType.COMMA): 74,
    ('2d_chant_row', TokenType.CODE_BLOCK_RIGHT): 73,

    # <more_chant_lit> productions
    ('more_chant_lit', TokenType.COMMA): 76,
    ('more_chant_lit', TokenType.CODE_BLOCK_RIGHT): 75,

    # <function_decl> productions
    ('function_decl', TokenType.WILT): 78,
    ('function_decl', TokenType.DUNK): 79,
    ('function_decl', TokenType.FEINT): 77,
    ('function_decl', TokenType.FLOATER): 77,
    ('function_decl', TokenType.CHANT): 77,
    ('function_decl', TokenType.STAT): 77,

    # <function_declared> productions
    ('function_declared', TokenType.FEINT): 80,
    ('function_declared', TokenType.FLOATER): 81,
    ('function_declared', TokenType.CHANT): 82,
    ('function_declared', TokenType.STAT): 83,

    # <dunk_func_declared> productions
    ('dunk_func_declared', TokenType.VAR_INIT): 84,

    # <feint_function> productions
    ('feint_function', TokenType.FEINT): 85,

    # <feint_parameters> productions
    ('feint_parameters', TokenType.FEINT): 87,
    ('feint_parameters', TokenType.RIGHT_PAREN): 86,

    # <feint_param> productions
    ('feint_param', TokenType.FEINT): 88,

    # <feint_params> productions
    ('feint_params', TokenType.COMMA): 90,
    ('feint_params', TokenType.RIGHT_PAREN): 89,

    # <floater_function> productions
    ('floater_function', TokenType.FLOATER): 91,

    # <floater_parameters> productions
    ('floater_parameters', TokenType.FLOATER): 93,
    ('floater_parameters', TokenType.RIGHT_PAREN): 92,

    # <floater_param> productions
    ('floater_param', TokenType.FLOATER): 94,

    # <floater_params> productions
    ('floater_params', TokenType.COMMA): 96,
    ('floater_params', TokenType.RIGHT_PAREN): 95,

    # <chant_function> productions
    ('chant_function', TokenType.CHANT): 97,

    # <chant_parameters> productions
    ('chant_parameters', TokenType.CHANT): 99,
    ('chant_parameters', TokenType.RIGHT_PAREN): 98,

    # <chant_param> productions
    ('chant_param', TokenType.CHANT): 100,

    # <chant_params> productions
    ('chant_params', TokenType.COMMA): 102,
    ('chant_params', TokenType.RIGHT_PAREN): 101,

    # <stat_function> productions
    ('stat_function', TokenType.STAT): 103,

    # <stat_parameters> productions
    ('stat_parameters', TokenType.STAT): 105,
    ('stat_parameters', TokenType.RIGHT_PAREN): 104,

    # <stat_param> productions
    ('stat_param', TokenType.STAT): 106,

    # <stat_params> productions
    ('stat_params', TokenType.COMMA): 108,
    ('stat_params', TokenType.RIGHT_PAREN): 107,

    # <dunk_function> productions
    ('dunk_function', TokenType.VAR_INIT): 109,

    # <dunk_parameters> productions
    ('dunk_parameters', TokenType.VAR_INIT): 111,
    ('dunk_parameters', TokenType.RIGHT_PAREN): 110,

    # <dunk_param> productions
    ('dunk_param', TokenType.VAR_INIT): 112,

    # <dunk_params> productions
    ('dunk_params', TokenType.COMMA): 114,
    ('dunk_params', TokenType.RIGHT_PAREN): 113,

    # <function_def> productions
    ('function_def', TokenType.WILT): 115,
    ('function_def', TokenType.DUNK): 116,

    # <function_defined> productions
    ('function_defined', TokenType.VAR_INIT): 117,

    # <function_param> productions
    ('function_param', TokenType.VAR_INIT): 119,
    ('function_param', TokenType.RIGHT_PAREN): 118,

    # <param> productions
    ('param', TokenType.VAR_INIT): 120,

    # <params> productions
    ('params', TokenType.COMMA): 122,
    ('params', TokenType.RIGHT_PAREN): 121,

    # <function_statements> productions
    ('function_statements', TokenType.FEINT): 123,
    ('function_statements', TokenType.FLOATER): 123,
    ('function_statements', TokenType.CHANT): 123,
    ('function_statements', TokenType.STAT): 123,
    ('function_statements', TokenType.ANNOUNCE): 123,
    ('function_statements', TokenType.INBOUND): 123,
    ('function_statements', TokenType.DRIBBLE): 123,
    ('function_statements', TokenType.SWITCH): 123,
    ('function_statements', TokenType.FORWARD): 123,
    ('function_statements', TokenType.PLAY): 123,
    ('function_statements', TokenType.RUN): 123,
    ('function_statements', TokenType.TIMEOUT): 123,
    ('function_statements', TokenType.RESUME): 123,
    ('function_statements', TokenType.VAR_INIT): 123,
    ('function_statements', TokenType.LEFT_PAREN): 123,
    ('function_statements', TokenType.FEINTLIT): 123,
    ('function_statements', TokenType.FLOATERLIT): 123,
    ('function_statements', TokenType.NOT_OP): 123,
    ('function_statements', TokenType.NEGAFEINT): 123,
    ('function_statements', TokenType.NEGAFLOATER): 123,
    ('function_statements', TokenType.CHANTLIT): 123,
    ('function_statements', TokenType.WIN): 123,
    ('function_statements', TokenType.LOSS): 123,
    ('function_statements', TokenType.REBOUND): 123,

    # <other_statements> productions
    ('other_statements', TokenType.FEINT): 125,
    ('other_statements', TokenType.FLOATER): 125,
    ('other_statements', TokenType.CHANT): 125,
    ('other_statements', TokenType.STAT): 125,
    ('other_statements', TokenType.ANNOUNCE): 125,
    ('other_statements', TokenType.INBOUND): 125,
    ('other_statements', TokenType.DRIBBLE): 125,
    ('other_statements', TokenType.SWITCH): 125,
    ('other_statements', TokenType.FORWARD): 125,
    ('other_statements', TokenType.PLAY): 125,
    ('other_statements', TokenType.RUN): 125,
    ('other_statements', TokenType.TIMEOUT): 125,
    ('other_statements', TokenType.RESUME): 125,
    ('other_statements', TokenType.VAR_INIT): 125,
    ('other_statements', TokenType.LEFT_PAREN): 125,
    ('other_statements', TokenType.FEINTLIT): 126,
    ('other_statements', TokenType.FLOATERLIT): 126,
    ('other_statements', TokenType.NOT_OP): 126,
    ('other_statements', TokenType.NEGAFEINT): 126,
    ('other_statements', TokenType.NEGAFLOATER): 126,
    ('other_statements', TokenType.CHANTLIT): 126,
    ('other_statements', TokenType.WIN): 126,
    ('other_statements', TokenType.LOSS): 126,
    ('other_statements', TokenType.CODE_BLOCK_RIGHT): 124,

    # <statement> productions
    ('statement', TokenType.FEINT): 128,
    ('statement', TokenType.FLOATER): 128,
    ('statement', TokenType.CHANT): 128,
    ('statement', TokenType.STAT): 128,
    ('statement', TokenType.ANNOUNCE): 129,
    ('statement', TokenType.INBOUND): 130,
    ('statement', TokenType.DRIBBLE): 131,
    ('statement', TokenType.SWITCH): 132,
    ('statement', TokenType.FORWARD): 133,
    ('statement', TokenType.PLAY): 134,
    ('statement', TokenType.RUN): 135,
    ('statement', TokenType.TIMEOUT): 136,
    ('statement', TokenType.RESUME): 137,
    ('statement', TokenType.VAR_INIT): 138,
    ('statement', TokenType.VAR_INIT): 139,
    ('statement', TokenType.VAR_INIT): 140,

    # <array_manipulation> productions
    ('array_manipulation', TokenType.VAR_INIT): 141,

    # <element_index> productions
    ('element_index', TokenType.FEINTLIT): 142,

    # <2d_manipulation> productions
    ('2d_manipulation', TokenType.ARRAY_INDEX_LEFT): 143,
    ('2d_manipulation', TokenType.ASSIGN): 144,

    # <array_man> productions
    ('array_man', TokenType.ASSIGN): 145,
    ('array_man', TokenType.SEMICOLON): 146,

    # <array_elem> productions
    ('array_elem', TokenType.FEINTLIT): 147,
    ('array_elem', TokenType.FLOATERLIT): 148,
    ('array_elem', TokenType.CHANTLIT): 149,

    # <rebound_statement> productions
    ('rebound_statement', TokenType.REBOUND): 150,

    # <announce_statement> productions
    ('announce_statement', TokenType.ANNOUNCE): 151,

    # <outputs> productions
    ('outputs', TokenType.FEINTLIT): 152,
    ('outputs', TokenType.FLOATERLIT): 152,
    ('outputs', TokenType.CHANTLIT): 152,
    ('outputs', TokenType.LEFT_PAREN): 152,
    ('outputs', TokenType.VAR_INIT): 152,
    ('outputs', TokenType.WIN): 152,
    ('outputs', TokenType.LOSS): 152,

    # <output> productions
    ('output', TokenType.FEINTLIT): 153,
    ('output', TokenType.FLOATERLIT): 153,
    ('output', TokenType.CHANTLIT): 153,
    ('output', TokenType.LEFT_PAREN): 154,
    ('output', TokenType.VAR_INIT): 155,
    ('output', TokenType.WIN): 156,
    ('output', TokenType.LOSS): 156,
    ('output', TokenType.VAR_INIT): 157,

    # <other_outputs> productions
    ('other_outputs', TokenType.CHANT_CONCAT): 160,
    ('other_outputs', TokenType.RIGHT_PAREN): 159,

    # <literal> productions
    ('literal', TokenType.FEINTLIT): 161,
    ('literal', TokenType.FLOATERLIT): 162,
    ('literal', TokenType.NEGAFEINT): 163,
    ('literal', TokenType.NEGAFLOATER): 164,
    ('literal', TokenType.CHANTLIT): 167,
    ('literal', TokenType.WIN): 168,
    ('literal', TokenType.LOSS): 168,

    # <nega_feint_lit> productions
    ('nega_feint_lit', TokenType.NEGAFEINT): 165,

    # <nega_floater_lit> productions
    ('nega_floater_lit', TokenType.NEGAFLOATER): 166,

    # <expression> productions
    ('expression', TokenType.LEFT_PAREN): 169,
    ('expression', TokenType.FEINTLIT): 169,
    ('expression', TokenType.FLOATERLIT): 169,
    ('expression', TokenType.VAR_INIT): 169,
    ('expression', TokenType.NOT_OP): 169,
    ('expression', TokenType.NEGAFEINT): 169,
    ('expression', TokenType.NEGAFLOATER): 169,
    ('expression', TokenType.CHANTLIT): 169,
    ('expression', TokenType.WIN): 169,
    ('expression', TokenType.LOSS): 169,
    ('expression', TokenType.VAR_INIT): 173,

    # <arithmetic_expression> productions
    ('arithmetic_expression', TokenType.FEINTLIT): 174,
    ('arithmetic_expression', TokenType.FLOATERLIT): 174,
    ('arithmetic_expression', TokenType.VAR_INIT): 174,
    ('arithmetic_expression', TokenType.NEGAFEINT): 174,
    ('arithmetic_expression', TokenType.NEGAFLOATER): 174,
    ('arithmetic_expression', TokenType.LEFT_PAREN): 174,
    ('arithmetic_expression', TokenType.FEINT): 174,
    ('arithmetic_expression', TokenType.FLOATER): 174,

    # <arith_term> productions
    ('arith_term', TokenType.FEINTLIT): 175,
    ('arith_term', TokenType.FLOATERLIT): 175,
    ('arith_term', TokenType.VAR_INIT): 175,
    ('arith_term', TokenType.NEGAFEINT): 175,
    ('arith_term', TokenType.NEGAFLOATER): 175,
    ('arith_term', TokenType.LEFT_PAREN): 176,
    ('arith_term', TokenType.FEINT): 177,
    ('arith_term', TokenType.FLOATER): 177,

    # <number> productions
    ('number', TokenType.FEINTLIT): 178,
    ('number', TokenType.FLOATERLIT): 179,
    ('number', TokenType.VAR_INIT): 180,
    ('number', TokenType.NEGAFEINT): 181,
    ('number', TokenType.NEGAFLOATER): 182,

    # <number_type_cast> productions
    ('number_type_cast', TokenType.FEINT): 183,
    ('number_type_cast', TokenType.FLOATER): 184,

    # <feint_type_casting> productions
    ('feint_type_casting', TokenType.FEINT): 185,

    # <floater_type_casting> productions
    ('floater_type_casting', TokenType.FLOATER): 186,

    # <chant_type_casting> productions
    ('chant_type_casting', TokenType.CHANT): 187,

    # <stat_type_casting> productions
    ('stat_type_casting', TokenType.STAT): 188,

    # <more_arith_term> productions
    ('more_arith_term', TokenType.ADD): 190,
    ('more_arith_term', TokenType.SUB): 191,
    ('more_arith_term', TokenType.MUL): 192,
    ('more_arith_term', TokenType.DIV): 193,
    ('more_arith_term', TokenType.MOD): 194,
    ('more_arith_term', TokenType.RIGHT_PAREN): 189,
    ('more_arith_term', TokenType.SEMICOLON): 189,

    # <relational_expression> productions
    ('relational_expression', TokenType.FEINTLIT): 195,
    ('relational_expression', TokenType.FLOATERLIT): 195,
    ('relational_expression', TokenType.VAR_INIT): 195,
    ('relational_expression', TokenType.NEGAFEINT): 195,
    ('relational_expression', TokenType.NEGAFLOATER): 195,
    ('relational_expression', TokenType.LEFT_PAREN): 195,
    ('relational_expression', TokenType.FEINT): 195,
    ('relational_expression', TokenType.FLOATER): 195,
    ('relational_expression', TokenType.WIN): 196,
    ('relational_expression', TokenType.LOSS): 196,
    ('relational_expression', TokenType.CHANTLIT): 197,
    ('relational_expression', TokenType.LEFT_PAREN): 198,

    # <relational_operand> productions
    ('relational_operand', TokenType.FEINTLIT): 199,
    ('relational_operand', TokenType.FLOATERLIT): 199,
    ('relational_operand', TokenType.VAR_INIT): 199,
    ('relational_operand', TokenType.NEGAFEINT): 199,
    ('relational_operand', TokenType.NEGAFLOATER): 199,
    ('relational_operand', TokenType.FEINT): 200,
    ('relational_operand', TokenType.FLOATER): 200,
    ('relational_operand', TokenType.CHANT): 201,
    ('relational_operand', TokenType.STAT): 201,

    # <relational_operator> productions
    ('relational_operator', TokenType.LESS_THAN): 202,
    ('relational_operator', TokenType.GREATER_THAN): 203,
    ('relational_operator', TokenType.EQUAL): 204,
    ('relational_operator', TokenType.LESS_EQUAL): 205,
    ('relational_operator', TokenType.GREATER_EQUAL): 206,
    ('relational_operator', TokenType.NOT_EQUAL): 207,

    # <other_relational_operator> productions
    ('other_relational_operator', TokenType.EQUAL): 208,
    ('other_relational_operator', TokenType.NOT_EQUAL): 209,

    # <logical_expression> productions
    ('logical_expression', TokenType.NOT_OP): 211,
    ('logical_expression', TokenType.LEFT_PAREN): 212,
    ('logical_expression', TokenType.FEINTLIT): 213,
    ('logical_expression', TokenType.FLOATERLIT): 213,
    ('logical_expression', TokenType.VAR_INIT): 213,
    ('logical_expression', TokenType.NEGAFEINT): 213,
    ('logical_expression', TokenType.NEGAFLOATER): 213,
    ('logical_expression', TokenType.FEINT): 213,
    ('logical_expression', TokenType.FLOATER): 213,
    ('logical_expression', TokenType.CHANT): 213,
    ('logical_expression', TokenType.STAT): 213,
    ('logical_expression', TokenType.WIN): 213,
    ('logical_expression', TokenType.LOSS): 213,
    ('logical_expression', TokenType.CHANTLIT): 213,

    # <logic_term> productions
    ('logic_term', TokenType.NOT_OP): 211,
    ('logic_term', TokenType.LEFT_PAREN): 212,
    ('logic_term', TokenType.FEINTLIT): 213,
    ('logic_term', TokenType.FLOATERLIT): 213,
    ('logic_term', TokenType.VAR_INIT): 213,
    ('logic_term', TokenType.NEGAFEINT): 213,
    ('logic_term', TokenType.NEGAFLOATER): 213,
    ('logic_term', TokenType.FEINT): 213,
    ('logic_term', TokenType.FLOATER): 213,
    ('logic_term', TokenType.CHANT): 213,
    ('logic_term', TokenType.STAT): 213,
    ('logic_term', TokenType.WIN): 213,
    ('logic_term', TokenType.LOSS): 213,
    ('logic_term', TokenType.CHANTLIT): 213,

    # <more_logic_term> productions
    ('more_logic_term', TokenType.AND_OP): 215,
    ('more_logic_term', TokenType.OR_OP): 216,
    ('more_logic_term', TokenType.RIGHT_PAREN): 214,
    ('more_logic_term', TokenType.SEMICOLON): 214,

    # <assignment_expression> productions
    ('assignment_expression', TokenType.VAR_INIT): 217,

    # <assign_operator> productions
    ('assign_operator', TokenType.ASSIGN): 218,
    ('assign_operator', TokenType.ADD_ASSIGN): 219,
    ('assign_operator', TokenType.SUB_ASSIGN): 220,
    ('assign_operator', TokenType.MUL_ASSIGN): 221,
    ('assign_operator', TokenType.DIV_ASSIGN): 222,
    ('assign_operator', TokenType.MOD_ASSIGN): 223,

    # <assign_operand> productions
    ('assign_operand', TokenType.FEINTLIT): 224,
    ('assign_operand', TokenType.FLOATERLIT): 224,
    ('assign_operand', TokenType.VAR_INIT): 224,
    ('assign_operand', TokenType.NEGAFEINT): 224,
    ('assign_operand', TokenType.NEGAFLOATER): 224,
    ('assign_operand', TokenType.LEFT_PAREN): 224,
    ('assign_operand', TokenType.FEINT): 224,
    ('assign_operand', TokenType.FLOATER): 224,
    ('assign_operand', TokenType.CHANT): 224,
    ('assign_operand', TokenType.STAT): 224,
    ('assign_operand', TokenType.WIN): 224,
    ('assign_operand', TokenType.LOSS): 224,
    ('assign_operand', TokenType.CHANTLIT): 224,
    ('assign_operand', TokenType.NOT_OP): 224,
    ('assign_operand', TokenType.VAR_INIT): 227,

    # <function_call> productions
    ('function_call', TokenType.VAR_INIT): 229,

    # <arguments> productions
    ('arguments', TokenType.FEINTLIT): 230,
    ('arguments', TokenType.FLOATERLIT): 230,
    ('arguments', TokenType.NEGAFEINT): 230,
    ('arguments', TokenType.NEGAFLOATER): 230,
    ('arguments', TokenType.CHANTLIT): 230,
    ('arguments', TokenType.WIN): 230,
    ('arguments', TokenType.LOSS): 230,
    ('arguments', TokenType.VAR_INIT): 230,

    # <arg> productions
    ('arg', TokenType.FEINTLIT): 231,
    ('arg', TokenType.FLOATERLIT): 231,
    ('arg', TokenType.NEGAFEINT): 231,
    ('arg', TokenType.NEGAFLOATER): 231,
    ('arg', TokenType.CHANTLIT): 231,
    ('arg', TokenType.WIN): 231,
    ('arg', TokenType.LOSS): 231,
    ('arg', TokenType.VAR_INIT): 232,

    # <more_args> productions
    ('more_args', TokenType.COMMA): 233,
    ('more_args', TokenType.RIGHT_PAREN): 232,

    # <inbound_statement> productions
    ('inbound_statement', TokenType.INBOUND): 234,

    # <inputs> productions
    ('inputs', TokenType.CHANTLIT): 235,

    # <input> productions
    ('input', TokenType.CHANTLIT): 236,

    # <id_input> productions
    ('id_input', TokenType.COMMA): 237,
    ('id_input', TokenType.RIGHT_PAREN): 236,

    # <dribble_statement> productions
    ('dribble_statement', TokenType.DRIBBLE): 238,

    # <condition> productions
    ('condition', TokenType.FEINTLIT): 239,
    ('condition', TokenType.FLOATERLIT): 239,
    ('condition', TokenType.VAR_INIT): 239,
    ('condition', TokenType.NEGAFEINT): 239,
    ('condition', TokenType.NEGAFLOATER): 239,
    ('condition', TokenType.LEFT_PAREN): 239,
    ('condition', TokenType.FEINT): 239,
    ('condition', TokenType.FLOATER): 239,
    ('condition', TokenType.CHANT): 239,
    ('condition', TokenType.STAT): 239,
    ('condition', TokenType.WIN): 239,
    ('condition', TokenType.LOSS): 239,
    ('condition', TokenType.CHANTLIT): 239,
    ('condition', TokenType.NOT_OP): 240,

    # <pass_statement> productions
    ('pass_statement', TokenType.PASS): 241,
    ('pass_statement', TokenType.SHOOT): 242,

    # <shoot_statement> productions
    ('shoot_statement', TokenType.SHOOT): 243,
    ('shoot_statement', TokenType.CODE_BLOCK_RIGHT): 244,

    # <switch_statement> productions
    ('switch_statement', TokenType.SWITCH): 245,

    # <get_case> productions
    ('get_case', TokenType.GET): 246,

    # <get_value> productions
    ('get_value', TokenType.FEINTLIT): 247,
    ('get_value', TokenType.CHANTLIT): 248,

    # <get_case_end> productions
    ('get_case_end', TokenType.GET): 251,
    ('get_case_end', TokenType.DEFAULT): 250,

    # <get_default> productions
    ('get_default', TokenType.DEFAULT): 252,
    ('get_default', TokenType.CODE_BLOCK_RIGHT): 253,

    # <forward_statement> productions
    ('forward_statement', TokenType.FORWARD): 254,

    # <forward_lit> productions
    ('forward_lit', TokenType.FEINTLIT): 255,
    ('forward_lit', TokenType.VAR_INIT): 256,

    # <forward_inc_dec> productions
    ('forward_inc_dec', TokenType.VAR_INIT): 259,
    ('forward_inc_dec', TokenType.INCREMENT): 257,
    ('forward_inc_dec', TokenType.DECREMENT): 258,

    # <increment> productions
    ('increment', TokenType.VAR_INIT): 260,
    ('increment', TokenType.INCREMENT): 261,

    # <decrement> productions
    ('decrement', TokenType.VAR_INIT): 262,
    ('decrement', TokenType.DECREMENT): 263,

    # <resume_statement> productions
    ('resume_statement', TokenType.RESUME): 264,

    # <play_statement> productions
    ('play_statement', TokenType.PLAY): 265,

    # <run_play_statement> productions
    ('run_play_statement', TokenType.RUN): 266,

    # <team_block> productions
    ('team_block', TokenType.TEAM): 267,

    # <local_decl> productions
    ('local_decl', TokenType.FEINT): 268,
    ('local_decl', TokenType.FLOATER): 268,
    ('local_decl', TokenType.CHANT): 268,
    ('local_decl', TokenType.STAT): 268,
    ('local_decl', TokenType.CONST): 268,
    ('local_decl', TokenType.ZONE): 268,
    ('local_decl', TokenType.ANNOUNCE): 269,
    ('local_decl', TokenType.INBOUND): 269,
    ('local_decl', TokenType.DRIBBLE): 269,
    ('local_decl', TokenType.SWITCH): 269,
    ('local_decl', TokenType.FORWARD): 269,
    ('local_decl', TokenType.PLAY): 269,
    ('local_decl', TokenType.RUN): 269,
    ('local_decl', TokenType.TIMEOUT): 269,
    ('local_decl', TokenType.RESUME): 269,
    ('local_decl', TokenType.VAR_INIT): 269,

    # <local_declaration> productions
    ('local_declaration', TokenType.FEINT): 270,
    ('local_declaration', TokenType.FLOATER): 270,
    ('local_declaration', TokenType.CHANT): 270,
    ('local_declaration', TokenType.STAT): 270,
    ('local_declaration', TokenType.CONST): 270,
    ('local_declaration', TokenType.ZONE): 271,

    # <feint_typecast_value> productions
    ('feint_typecast_value', TokenType.FLOATERLIT): 272,
    ('feint_typecast_value', TokenType.CHANTLIT): 273,
    ('feint_typecast_value', TokenType.WIN): 274,
    ('feint_typecast_value', TokenType.LOSS): 274,

    # <floater_typecast_value> productions
    ('floater_typecast_value', TokenType.FEINTLIT): 275,
    ('floater_typecast_value', TokenType.CHANTLIT): 276,
    ('floater_typecast_value', TokenType.WIN): 277,
    ('floater_typecast_value', TokenType.LOSS): 277,

    # <chant_typecast_value> productions
    ('chant_typecast_value', TokenType.FEINTLIT): 278,
    ('chant_typecast_value', TokenType.FLOATERLIT): 279,
    ('chant_typecast_value', TokenType.WIN): 280,
    ('chant_typecast_value', TokenType.LOSS): 280,

    # <stat_typecast_value> productions
    ('stat_typecast_value', TokenType.FEINTLIT): 281,
    ('stat_typecast_value', TokenType.FLOATERLIT): 281,
    ('stat_typecast_value', TokenType.CHANTLIT): 283,

    # <other_type_cast> productions
    ('other_type_cast', TokenType.CHANT): 284,
    ('other_type_cast', TokenType.STAT): 284
} 