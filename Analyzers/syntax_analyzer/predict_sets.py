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
    ('more_feint', TokenType.SEMICOLON): 12,
    ('more_feint', TokenType.ASSIGN): 13,
    
    # <feint_init> productions
    ('feint_init', TokenType.SEMICOLON): 14,
    ('feint_init', TokenType.COMMA): 14,
    ('feint_init', TokenType.ASSIGN): 15,
    
    # <feint_lit> productions
    ('feint_lit', TokenType.FEINTLIT): 16,
    
    # <feint_init_end> productions
    ('feint_init_end', TokenType.SEMICOLON): 17,
    ('feint_init_end', TokenType.COMMA): 18,
    
    # <floater_dec> productions
    ('floater_dec', TokenType.FLOATER): 19,
    
    # <more_floater> productions
    ('more_floater', TokenType.SEMICOLON): 20,
    ('more_floater', TokenType.ASSIGN): 21,
    
    # <floater_init> productions
    ('floater_init', TokenType.SEMICOLON): 22,
    ('floater_init', TokenType.COMMA): 22,
    ('floater_init', TokenType.ASSIGN): 23,
    
    # <floater_lit> productions
    ('floater_lit', TokenType.FLOATERLIT): 24,
    
    # <floater_init_end> productions
    ('floater_init_end', TokenType.SEMICOLON): 25,
    ('floater_init_end', TokenType.COMMA): 26,
    
    # <chant_dec> productions
    ('chant_dec', TokenType.CHANT): 27,
    
    # <more_chant> productions
    ('more_chant', TokenType.SEMICOLON): 28,
    ('more_chant', TokenType.ASSIGN): 29,
    
    # <chant_init> productions
    ('chant_init', TokenType.SEMICOLON): 30,
    ('chant_init', TokenType.COMMA): 30,
    ('chant_init', TokenType.ASSIGN): 31,
    
    # <chant_lit> productions
    ('chant_lit', TokenType.CHANTLIT): 32,
    
    # <chant_init_end> productions
    ('chant_init_end', TokenType.SEMICOLON): 33,
    ('chant_init_end', TokenType.COMMA): 34,
    
    # <stat_dec> productions
    ('stat_dec', TokenType.STAT): 35,
    
    # <more_stat> productions
    ('more_stat', TokenType.SEMICOLON): 36,
    ('more_stat', TokenType.COMMA): 37,
    
    # <stat_init> productions
    ('stat_init', TokenType.SEMICOLON): 38,
    ('stat_init', TokenType.COMMA): 38,
    ('stat_init', TokenType.ASSIGN): 39,
    
    # <stat_value> productions
    ('stat_value', TokenType.WIN): 40,
    ('stat_value', TokenType.LOSS): 41,
    
    # <stat_init_end> productions
    ('stat_init_end', TokenType.SEMICOLON): 42,
    ('stat_init_end', TokenType.COMMA): 43,
    
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
    ('2D_array', TokenType.SEMICOLON): 72,
    ('2D_array', TokenType.ARRAY_INDEX_LEFT): 73,
    
    # <feint_array_init> productions
    ('feint_array_init', TokenType.SEMICOLON): 74,
    ('feint_array_init', TokenType.ASSIGN): 75,
    
    # <feint_row> productions
    ('feint_row', TokenType.FEINTLIT): 76,

     # <feint_row> productions 
    ('feint_row', TokenType.CODE_BLOCK_RIGHT): 77,
    
    # <2D_feint_row> productions
    ('2D_feint_row', TokenType.CODE_BLOCK_RIGHT): 78,
    ('2D_feint_row', TokenType.COMMA): 79,
    
    # <more_feint_lit> productions
    ('more_feint_lit', TokenType.CODE_BLOCK_RIGHT): 80,
    ('more_feint_lit', TokenType.RIGHT_PAREN): 80,
    ('more_feint_lit', TokenType.COMMA): 81,
    
    # <floater_array> productions
    ('floater_array', TokenType.FLOATER): 82,
    
    # <floater_array_init> productions
    ('floater_array_init', TokenType.SEMICOLON): 83,
    ('floater_array_init', TokenType.ASSIGN): 84,
    
    # <floater_row> productions
    ('floater_row', TokenType.FLOATERLIT): 85,
    ('floater_row', TokenType.CODE_BLOCK_RIGHT): 86,
    
    # <2D_floater_row> productions
    ('2D_floater_row', TokenType.CODE_BLOCK_RIGHT): 87,
    ('2D_floater_row', TokenType.COMMA): 88,
    
    # <more_floater_lit> productions
    ('more_floater_lit', TokenType.CODE_BLOCK_RIGHT): 89,
    ('more_floater_lit', TokenType.RIGHT_PAREN): 89,
    ('more_floater_lit', TokenType.COMMA): 90,
    
    # <chant_array> productions
    ('chant_array', TokenType.CHANT): 91,
    
    # <chant_array_init> productions
    ('chant_array_init', TokenType.SEMICOLON): 92,
    ('chant_array_init', TokenType.ASSIGN): 93,
    
    # <chant_row> productions
    ('chant_row', TokenType.CHANTLIT): 94,
    ('chant_row', TokenType.CODE_BLOCK_RIGHT): 95,
    
    # <2D_chant_row> productions
    ('2D_chant_row', TokenType.CODE_BLOCK_RIGHT): 96,
    ('2D_chant_row', TokenType.COMMA): 97,
    
    # <more_chant_lit> productions
    ('more_chant_lit', TokenType.CODE_BLOCK_RIGHT): 98,
    ('more_chant_lit', TokenType.RIGHT_PAREN): 98,
    ('more_chant_lit', TokenType.COMMA): 99,
    
    # <function_def> productions
    ('function_def', TokenType.TEAM): 100,
    ('function_def', TokenType.WILT): 101,
    ('function_def', TokenType.DUNK): 102,
    
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
    ('func_parameters', TokenType.RIGHT_PAREN): 113,
    ('func_parameters', TokenType.VAR_INIT): 114,
    
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
    ('function_statement', TokenType.REBOUND): 118,
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
    ('team_statement', TokenType.TIMEOUT): 120,
    ('team_statement', TokenType.DEFAULT): 120,
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
    ('follow_statement', TokenType.ADD_ASSIGN): 134,
    ('follow_statement', TokenType.SUB_ASSIGN): 135,
    ('follow_statement', TokenType.MUL_ASSIGN): 136,
    ('follow_statement', TokenType.DIV_ASSIGN): 137,
    ('follow_statement', TokenType.MOD_ASSIGN): 138,
    ('follow_statement', TokenType.ARRAY_INDEX_LEFT): 139,
    
    # <element_index> productions
    ('element_index', TokenType.FEINTLIT): 140,
    ('element_index', TokenType.FLOATERLIT): 140,
    ('element_index', TokenType.NEGAFEINT): 140,
    ('element_index', TokenType.NEGAFLOATER): 140,
    ('element_index', TokenType.CHANTLIT): 140,
    ('element_index', TokenType.WIN): 140,
    ('element_index', TokenType.LOSS): 140,
    ('element_index', TokenType.VAR_INIT): 140,
    ('element_index', TokenType.LEFT_PAREN): 140,
    ('element_index', TokenType.NOT_OP): 140,
    ('element_index', TokenType.FEINT): 140,
    ('element_index', TokenType.FLOATER): 140,

    # <2d_manipulation> productions
    ('2d_manipulation', TokenType.ARRAY_INDEX_LEFT): 141,
    ('2d_manipulation', TokenType.ASSIGN): 142,
    ('2d_manipulation', TokenType.SEMICOLON): 142,
    
    # <array_man> productions
    ('array_man', TokenType.ASSIGN): 143,
    ('array_man', TokenType.SEMICOLON): 144,
    
    # <array_elem> productions
    ('array_elem', TokenType.FEINTLIT): 145,
    ('array_elem', TokenType.FLOATERLIT): 145,
    ('array_elem', TokenType.NEGAFEINT): 145,
    ('array_elem', TokenType.NEGAFLOATER): 145,
    ('array_elem', TokenType.CHANTLIT): 145,
    ('array_elem', TokenType.WIN): 145,
    ('array_elem', TokenType.LOSS): 145,
    ('array_elem', TokenType.VAR_INIT): 145,
    ('array_elem', TokenType.LEFT_PAREN): 145,
    ('array_elem', TokenType.NOT_OP): 145,
    ('array_elem', TokenType.FEINT): 145,
    ('array_elem', TokenType.FLOATER): 145,
    
    # <rebound_statement> productions
    ('rebound_statement', TokenType.REBOUND): 146,
    
    # <announce_statement> productions
    ('announce_statement', TokenType.ANNOUNCE): 150,
    
    # <otpt> productions
    ('otpt', TokenType.FEINTLIT): 151,
    ('otpt', TokenType.FLOATERLIT): 151,
    ('otpt', TokenType.NEGAFEINT): 151,
    ('otpt', TokenType.NEGAFLOATER): 151,
    ('otpt', TokenType.CHANTLIT): 151,
    ('otpt', TokenType.WIN): 151,
    ('otpt', TokenType.LOSS): 151,
    ('otpt', TokenType.VAR_INIT): 151,
    
    # <outputs> productions
    ('outputs', TokenType.VAR_INIT): 152,

    # <otpts> productions
    ('otpts', TokenType.RIGHT_PAREN): 153,
    ('otpts', TokenType.CHANT_CONCAT): 153,
    ('otpts', TokenType.ARRAY_INDEX_LEFT): 154,

    ('outputs', TokenType.FEINTLIT): 155,
    ('outputs', TokenType.FLOATERLIT): 155,
    ('outputs', TokenType.NEGAFEINT): 155,
    ('outputs', TokenType.NEGAFLOATER): 155,
    ('outputs', TokenType.CHANTLIT): 155,
    ('outputs', TokenType.WIN): 155,
    ('outputs', TokenType.LOSS): 155,
    ('outputs', TokenType.FEINTLIT): 156,
    ('outputs', TokenType.FLOATERLIT): 156,
    ('outputs', TokenType.NEGAFEINT): 156,
    ('outputs', TokenType.NEGAFLOATER): 156,
    ('outputs', TokenType.CHANTLIT): 156,
    ('outputs', TokenType.WIN): 156,
    ('outputs', TokenType.LOSS): 156,
    ('outputs', TokenType.VAR_INIT): 156,
    ('outputs', TokenType.LEFT_PAREN): 156,
    ('outputs', TokenType.NOT_OP): 156,
    ('outputs', TokenType.FEINT): 156,
    ('outputs', TokenType.FLOATER): 156,
    ('outputs', TokenType.WIN): 157,
    ('outputs', TokenType.LOSS): 157,
    
    # <other_outputs> productions
    ('other_outputs', TokenType.RIGHT_PAREN): 158,
    ('other_outputs', TokenType.CHANT_CONCAT): 159,
    
    # <literal> productions
    ('literal', TokenType.FEINTLIT): 160,
    ('literal', TokenType.FLOATERLIT): 161,
    ('literal', TokenType.NEGAFEINT): 162,
    ('literal', TokenType.NEGAFLOATER): 163,
    ('literal', TokenType.CHANTLIT): 164,
    ('literal', TokenType.WIN): 165,
    ('literal', TokenType.LOSS): 165,
    
    # <nega_feint_lit> productions
    ('nega_feint_lit', TokenType.NEGAFEINT): 166,
    
    # <nega_floater_lit> productions
    ('nega_floater_lit', TokenType.NEGAFLOATER): 167,
    
    # <expression> productions
    ('expression', TokenType.FEINTLIT): 168,
    ('expression', TokenType.FLOATERLIT): 168,
    ('expression', TokenType.NEGAFEINT): 168,
    ('expression', TokenType.NEGAFLOATER): 168,
    ('expression', TokenType.CHANTLIT): 168,
    ('expression', TokenType.WIN): 168,
    ('expression', TokenType.LOSS): 168,
    ('expression', TokenType.VAR_INIT): 168,
    ('expression', TokenType.LEFT_PAREN): 168,
    ('expression', TokenType.NOT_OP): 168,
    ('expression', TokenType.FEINT): 168,
    ('expression', TokenType.FLOATER): 168,
    
    # <logical_expression> productions
    ('logical_expression', TokenType.FEINTLIT): 169,
    ('logical_expression', TokenType.FLOATERLIT): 169,
    ('logical_expression', TokenType.NEGAFEINT): 169,
    ('logical_expression', TokenType.NEGAFLOATER): 169,
    ('logical_expression', TokenType.CHANTLIT): 169,
    ('logical_expression', TokenType.WIN): 169,
    ('logical_expression', TokenType.LOSS): 169,
    ('logical_expression', TokenType.VAR_INIT): 169,
    ('logical_expression', TokenType.LEFT_PAREN): 169,
    ('logical_expression', TokenType.NOT_OP): 169,
    ('logical_expression', TokenType.FEINT): 169,
    ('logical_expression', TokenType.FLOATER): 169,
    
    # <more_logical> productions
    ('more_logical', TokenType.AND_OP): 170,
    ('more_logical', TokenType.OR_OP): 170,
    ('more_logical', TokenType.RIGHT_PAREN): 171,
    ('more_logical', TokenType.SEMICOLON): 171,
    ('more_logical', TokenType.COMMA): 171,
    ('more_logical', TokenType.CODE_BLOCK_RIGHT): 171,
    ('more_logical', TokenType.ARRAY_INDEX_RIGHT): 171,
    ('more_logical', TokenType.COLON): 171,

    # <log_operator> productions
    ('log_operator', TokenType.AND_OP): 172,
    ('log_operator', TokenType.OR_OP): 173,
    
    # <relational_expression> productions
    ('relational_expression', TokenType.FEINTLIT): 174,
    ('relational_expression', TokenType.FLOATERLIT): 174,
    ('relational_expression', TokenType.NEGAFEINT): 174,
    ('relational_expression', TokenType.NEGAFLOATER): 174,
    ('relational_expression', TokenType.CHANTLIT): 174,
    ('relational_expression', TokenType.WIN): 174,
    ('relational_expression', TokenType.LOSS): 174,
    ('relational_expression', TokenType.VAR_INIT): 174,
    ('relational_expression', TokenType.LEFT_PAREN): 174,
    ('relational_expression', TokenType.NOT_OP): 174,
    ('relational_expression', TokenType.FEINT): 174,
    ('relational_expression', TokenType.FLOATER): 174,
    
    # <more_relational> productions
    ('more_relational', TokenType.LESS_THAN): 175,
    ('more_relational', TokenType.GREATER_THAN): 175,
    ('more_relational', TokenType.EQUAL): 175,
    ('more_relational', TokenType.LESS_EQUAL): 175,
    ('more_relational', TokenType.GREATER_EQUAL): 175,
    ('more_relational', TokenType.NOT_EQUAL): 175,

    ('more_relational', TokenType.AND_OP): 176,
    ('more_relational', TokenType.OR_OP): 176,
    ('more_relational', TokenType.RIGHT_PAREN): 176,
    ('more_relational', TokenType.SEMICOLON): 176,
    ('more_relational', TokenType.COMMA): 176,
    ('more_relational', TokenType.CODE_BLOCK_RIGHT): 176,
    ('more_relational', TokenType.ARRAY_INDEX_RIGHT): 176,
    ('more_relational', TokenType.COLON): 176,
    
    # <arithmetic_expression> productions
    ('arithmetic_expression', TokenType.FEINTLIT): 177,
    ('arithmetic_expression', TokenType.FLOATERLIT): 177,
    ('arithmetic_expression', TokenType.NEGAFEINT): 177,
    ('arithmetic_expression', TokenType.NEGAFLOATER): 177,
    ('arithmetic_expression', TokenType.CHANTLIT): 177,
    ('arithmetic_expression', TokenType.WIN): 177,
    ('arithmetic_expression', TokenType.LOSS): 177,
    ('arithmetic_expression', TokenType.VAR_INIT): 177,
    ('arithmetic_expression', TokenType.LEFT_PAREN): 177,
    ('arithmetic_expression', TokenType.NOT_OP): 177,
    ('arithmetic_expression', TokenType.FEINT): 177,
    ('arithmetic_expression', TokenType.FLOATER): 177,
    
    # <more_term> productions
    ('more_term', TokenType.ADD): 178,
    ('more_term', TokenType.SUB): 179,
    
    ('more_term', TokenType.LESS_THAN): 180,
    ('more_term', TokenType.GREATER_THAN): 180,
    ('more_term', TokenType.EQUAL): 180,
    ('more_term', TokenType.LESS_EQUAL): 180,
    ('more_term', TokenType.GREATER_EQUAL): 180,
    ('more_term', TokenType.NOT_EQUAL): 180,
    ('more_term', TokenType.AND_OP): 180,
    ('more_term', TokenType.OR_OP): 180,
    ('more_term', TokenType.RIGHT_PAREN): 180,
    ('more_term', TokenType.SEMICOLON): 180,
    ('more_term', TokenType.COMMA): 180,
    ('more_term', TokenType.CODE_BLOCK_RIGHT): 180,
    ('more_term', TokenType.ARRAY_INDEX_RIGHT): 180,
    ('more_term', TokenType.COLON): 180,
    
    # <term> productions
    ('term', TokenType.FEINTLIT): 181,
    ('term', TokenType.FLOATERLIT): 181,
    ('term', TokenType.NEGAFEINT): 181,
    ('term', TokenType.NEGAFLOATER): 181,
    ('term', TokenType.CHANTLIT): 181,
    ('term', TokenType.WIN): 181,
    ('term', TokenType.LOSS): 181,
    ('term', TokenType.VAR_INIT): 181,
    ('term', TokenType.LEFT_PAREN): 181,
    ('term', TokenType.NOT_OP): 181,
    ('term', TokenType.FEINT): 181,
    ('term', TokenType.FLOATER): 181,
    
    # <more_factor> productions
    ('more_factor', TokenType.MUL): 182,
    ('more_factor', TokenType.DIV): 183,
    ('more_factor', TokenType.MOD): 184,

    ('more_factor', TokenType.ADD): 185,
    ('more_factor', TokenType.SUB): 185,
    ('more_factor', TokenType.LESS_THAN): 185,
    ('more_factor', TokenType.GREATER_THAN): 185,
    ('more_factor', TokenType.EQUAL): 185,
    ('more_factor', TokenType.LESS_EQUAL): 185,
    ('more_factor', TokenType.GREATER_EQUAL): 185,
    ('more_factor', TokenType.NOT_EQUAL): 185,
    ('more_factor', TokenType.AND_OP): 185,
    ('more_factor', TokenType.OR_OP): 185,
    ('more_factor', TokenType.RIGHT_PAREN): 185,
    ('more_factor', TokenType.SEMICOLON): 185,
    ('more_factor', TokenType.COMMA): 185,
    ('more_factor', TokenType.CODE_BLOCK_RIGHT): 185,
    ('more_factor', TokenType.ARRAY_INDEX_RIGHT): 185,
    ('more_factor', TokenType.COLON): 185,
    
    # <factor> productions
    ('factor', TokenType.FEINTLIT): 186,
    ('factor', TokenType.FLOATERLIT): 186,
    ('factor', TokenType.NEGAFEINT): 186,
    ('factor', TokenType.NEGAFLOATER): 186,
    ('factor', TokenType.CHANTLIT): 186,
    ('factor', TokenType.WIN): 186,
    ('factor', TokenType.LOSS): 186,
    ('factor', TokenType.VAR_INIT): 187,
    ('factor', TokenType.LEFT_PAREN): 188,
    ('factor', TokenType.NOT_OP): 189,
    ('factor', TokenType.FEINT): 190,
    ('factor', TokenType.FLOATER): 190,
    ('factor', TokenType.CHANT): 190,
    ('factor', TokenType.STAT): 190,
    
    # <relational_operator> productions
    ('relational_operator', TokenType.LESS_THAN): 191,
    ('relational_operator', TokenType.GREATER_THAN): 192,
    ('relational_operator', TokenType.EQUAL): 193,
    ('relational_operator', TokenType.LESS_EQUAL): 194,
    ('relational_operator', TokenType.GREATER_EQUAL): 195,
    ('relational_operator', TokenType.NOT_EQUAL): 196,
    
    # <number_type_cast> productions
    ('number_type_cast', TokenType.FEINT): 197,
    ('number_type_cast', TokenType.FLOATER): 198,
    
    # <feint_type_casting> productions
    ('feint_type_casting', TokenType.FEINT): 199,
    
    # <floater_type_casting> productions
    ('floater_type_casting', TokenType.FLOATER): 200,
    
    # <chant_type_casting> productions
    ('chant_type_casting', TokenType.CHANT): 201,
    
    # <stat_type_casting> productions
    ('stat_type_casting', TokenType.STAT): 202,
    
    # <assign_operand> productions
    ('assign_operand', TokenType.FEINTLIT): 203,
    ('assign_operand', TokenType.FLOATERLIT): 203,
    ('assign_operand', TokenType.NEGAFEINT): 203,
    ('assign_operand', TokenType.NEGAFLOATER): 203,
    ('assign_operand', TokenType.CHANTLIT): 203,
    ('assign_operand', TokenType.WIN): 203,
    ('assign_operand', TokenType.LOSS): 203,
    ('assign_operand', TokenType.VAR_INIT): 203,
    ('assign_operand', TokenType.LEFT_PAREN): 203,
    ('assign_operand', TokenType.NOT_OP): 203,
    ('assign_operand', TokenType.FEINT): 203,
    ('assign_operand', TokenType.FLOATER): 203,
    ('assign_operand', TokenType.VAR_INIT): 204,
    
    # <function_call> productions
    ('function_call', TokenType.VAR_INIT): 205,
    
    # <arguments> productions
    ('arguments', TokenType.FEINTLIT): 206,
    ('arguments', TokenType.FLOATERLIT): 206,
    ('arguments', TokenType.NEGAFEINT): 206,
    ('arguments', TokenType.NEGAFLOATER): 206,
    ('arguments', TokenType.CHANTLIT): 206,
    ('arguments', TokenType.WIN): 206,
    ('arguments', TokenType.LOSS): 206,
    ('arguments', TokenType.VAR_INIT): 206,
    ('arguments', TokenType.RIGHT_PAREN): 207,
    
    # <arg> productions
    ('arg', TokenType.FEINTLIT): 208,
    ('arg', TokenType.FLOATERLIT): 208,
    ('arg', TokenType.NEGAFEINT): 208,
    ('arg', TokenType.NEGAFLOATER): 208,
    ('arg', TokenType.CHANTLIT): 208,
    ('arg', TokenType.WIN): 208,
    ('arg', TokenType.LOSS): 208,
    ('arg', TokenType.VAR_INIT): 209,
    ('arg', TokenType.FEINTLIT): 210,
    ('arg', TokenType.FLOATERLIT): 210,
    ('arg', TokenType.NEGAFEINT): 210,
    ('arg', TokenType.NEGAFLOATER): 210,
    ('arg', TokenType.CHANTLIT): 210,
    ('arg', TokenType.WIN): 210,
    ('arg', TokenType.LOSS): 210,
    ('arg', TokenType.VAR_INIT): 210,
    ('arg', TokenType.LEFT_PAREN): 210,
    ('arg', TokenType.NOT_OP): 210,
    ('arg', TokenType.FEINT): 210,
    ('arg', TokenType.FLOATER): 210,
    
    # <more_args> productions
    ('more_args', TokenType.COMMA): 211,
    ('more_args', TokenType.RIGHT_PAREN): 212,

    ('inbound_statement', TokenType.INBOUND): 213,
    ('dribble_statement', TokenType.DRIBBLE): 214,
    ('add_condition', TokenType.PASS): 215,
    ('add_condition', TokenType.SHOOT): 216,
    ('add_condition', TokenType.FEINT): 217,
    ('add_condition', TokenType.FLOATER): 217,
    ('add_condition', TokenType.CHANT): 217,
    ('add_condition', TokenType.STAT): 217,
    ('add_condition', TokenType.ANNOUNCE): 217,
    ('add_condition', TokenType.INBOUND): 217,
    ('add_condition', TokenType.DRIBBLE): 217,
    ('add_condition', TokenType.SWITCH): 217,
    ('add_condition', TokenType.FORWARD): 217,
    ('add_condition', TokenType.PLAY): 217,
    ('add_condition', TokenType.RUN): 217,
    ('add_condition', TokenType.VAR_INIT): 217, 
    ('add_condition', TokenType.REBOUND): 217,
    ('add_condition', TokenType.CODE_BLOCK_RIGHT): 217,
    ('add_condition', TokenType.TIMEOUT): 217,
    ('add_condition', TokenType.DEFAULT): 217,
    
    ('loop_statements', TokenType.FEINT): 218,
    ('loop_statements', TokenType.FLOATER): 218,
    ('loop_statements', TokenType.CHANT): 218,
    ('loop_statements', TokenType.STAT): 218,
    ('loop_statements', TokenType.ANNOUNCE): 218,
    ('loop_statements', TokenType.INBOUND): 218,
    ('loop_statements', TokenType.DRIBBLE): 218,
    ('loop_statements', TokenType.SWITCH): 218,
    ('loop_statements', TokenType.FORWARD): 218,
    ('loop_statements', TokenType.PLAY): 218,
    ('loop_statements', TokenType.RUN): 218,
    ('loop_statements', TokenType.VAR_INIT): 218, 
    ('loop_statements', TokenType.RESUME): 218,
    
    ('loop_statements', TokenType.CODE_BLOCK_RIGHT): 219, 
    
    ('loop_statement', TokenType.FEINT): 220,
    ('loop_statement', TokenType.FLOATER): 220,
    ('loop_statement', TokenType.CHANT): 220,
    ('loop_statement', TokenType.STAT): 220,
    ('loop_statement', TokenType.ANNOUNCE): 220,
    ('loop_statement', TokenType.INBOUND): 220,
    ('loop_statement', TokenType.DRIBBLE): 220,
    ('loop_statement', TokenType.SWITCH): 220,
    ('loop_statement', TokenType.FORWARD): 220,
    ('loop_statement', TokenType.PLAY): 220,
    ('loop_statement', TokenType.RUN): 220,
    ('loop_statement', TokenType.VAR_INIT): 220, 
    
    ('loop_statement', TokenType.RESUME): 221,
    
    ('switch_statement', TokenType.SWITCH): 222,
    ('get_case', TokenType.GET): 223,
    ('get_value', TokenType.FEINTLIT): 224,
    ('get_value', TokenType.CHANTLIT): 225,
    ('timeout_statement', TokenType.TIMEOUT): 226,
    ('get_case_end', TokenType.DEFAULT): 227, 
    ('get_case_end', TokenType.CODE_BLOCK_RIGHT): 227,  
    ('get_case_end', TokenType.GET): 228,
    ('get_default', TokenType.DEFAULT): 229,
    ('get_default', TokenType.CODE_BLOCK_RIGHT): 230, 
    
    ('forward_statement', TokenType.FORWARD): 231,
    ('forward_lit', TokenType.FEINTLIT): 232,
    ('forward_lit', TokenType.VAR_INIT): 233,  
    ('forward_inc_dec', TokenType.INCREMENT): 234,
    ('forward_inc_dec', TokenType.DECREMENT): 235,
    ('forward_inc_dec', TokenType.ADD_ASSIGN): 236,
    ('forward_inc_dec', TokenType.SUB_ASSIGN): 236,
    
    ('increment', TokenType.INCREMENT): 237,
    ('decrement', TokenType.DECREMENT): 238,
    ('forward_assign_operator', TokenType.ADD_ASSIGN): 239,
    ('forward_assign_operator', TokenType.SUB_ASSIGN): 240,
    
    ('resume_statement', TokenType.RESUME): 241,

    ('resume_statement', TokenType.FEINT): 242,  
    ('resume_statement', TokenType.FLOATER): 242,
    ('resume_statement', TokenType.CHANT): 242,
    ('resume_statement', TokenType.STAT): 242,
    ('resume_statement', TokenType.ANNOUNCE): 242,
    ('resume_statement', TokenType.INBOUND): 242,
    ('resume_statement', TokenType.DRIBBLE): 242,
    ('resume_statement', TokenType.SWITCH): 242,
    ('resume_statement', TokenType.FORWARD): 242,
    ('resume_statement', TokenType.PLAY): 242,
    ('resume_statement', TokenType.RUN): 242,
    ('resume_statement', TokenType.VAR_INIT): 242,
    ('resume_statement', TokenType.RESUME): 242,
    ('resume_statement', TokenType.CODE_BLOCK_RIGHT): 242,
    
    ('play_statement', TokenType.PLAY): 243,
    ('run_play_statement', TokenType.RUN): 244,
    
    ('team_block', TokenType.TEAM): 245,
    ('local_decl', TokenType.FEINT): 246,
    ('local_decl', TokenType.FLOATER): 246,
    ('local_decl', TokenType.CHANT): 246,
    ('local_decl', TokenType.STAT): 246,
    
    ('local_decl', TokenType.FEINT): 247,  
    ('local_decl', TokenType.FLOATER): 247,
    ('local_decl', TokenType.CHANT): 247,
    ('local_decl', TokenType.STAT): 247,
    ('local_decl', TokenType.ANNOUNCE): 247,
    ('local_decl', TokenType.INBOUND): 247,
    ('local_decl', TokenType.DRIBBLE): 247,
    ('local_decl', TokenType.SWITCH): 247,
    ('local_decl', TokenType.FORWARD): 247,
    ('local_decl', TokenType.PLAY): 247,
    ('local_decl', TokenType.RUN): 247,
    ('local_decl', TokenType.VAR_INIT): 247,
    
    ('local_declaration', TokenType.FEINT): 248,
    ('local_declaration', TokenType.FLOATER): 248,
    ('local_declaration', TokenType.CHANT): 248,
    ('local_declaration', TokenType.STAT): 248,
    
    ('local_declaration', TokenType.ZONE): 249,
    
    ('typecast_value', TokenType.FEINTLIT): 250,
    ('typecast_value', TokenType.FLOATERLIT): 251,
    ('typecast_value', TokenType.CHANTLIT): 252,
    ('typecast_value', TokenType.WIN): 253,
    ('typecast_value', TokenType.LOSS): 253,
    ('typecast_value', TokenType.VAR_INIT): 254, 
    
}