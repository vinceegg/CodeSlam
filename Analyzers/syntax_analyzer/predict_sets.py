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
    ('more_feint', TokenType.COMMA): 12,
    ('more_feint', TokenType.ASSIGN): 13,
    
    # <feint_init> productions
    ('feint_init', TokenType.SEMICOLON): 14,
    ('feint_init', TokenType.COMMA): 14,
    ('feint_init', TokenType.ASSIGN): 15,
    
    # <feint_lit> productions
    ('feint_lit', TokenType.FEINTLIT): 16,
    ('feint_lit', TokenType.NEGAFEINT): 17,
    
    # <feint_init_end> productions
    ('feint_init_end', TokenType.SEMICOLON): 18,
    ('feint_init_end', TokenType.COMMA): 19,
    
    # <floater_dec> productions
    ('floater_dec', TokenType.FLOATER): 20,
    
    # <more_floater> productions
    ('more_floater', TokenType.SEMICOLON): 21,
    ('more_floater', TokenType.COMMA): 21,
    ('more_floater', TokenType.ASSIGN): 22,
    
    # <floater_init> productions
    ('floater_init', TokenType.SEMICOLON): 23,
    ('floater_init', TokenType.COMMA): 23,
    ('floater_init', TokenType.ASSIGN): 24,
    
    # <floater_lit> productions
    ('floater_lit', TokenType.FLOATERLIT): 25,
    ('floater_lit', TokenType.NEGAFLOATER): 26,
    
    # <floater_init_end> productions
    ('floater_init_end', TokenType.SEMICOLON): 27,
    ('floater_init_end', TokenType.COMMA): 28,
    
    # <chant_dec> productions
    ('chant_dec', TokenType.CHANT): 29,
    
    # <more_chant> productions
    ('more_chant', TokenType.SEMICOLON): 30,
    ('more_chant', TokenType.COMMA): 30,
    ('more_chant', TokenType.ASSIGN): 31,
    
    # <chant_init> productions
    ('chant_init', TokenType.SEMICOLON): 32,
    ('chant_init', TokenType.COMMA): 32,
    ('chant_init', TokenType.ASSIGN): 33,
    
    # <chant_lit> productions
    ('chant_lit', TokenType.CHANTLIT): 34,
    
    # <chant_init_end> productions
    ('chant_init_end', TokenType.SEMICOLON): 35,
    ('chant_init_end', TokenType.COMMA): 36,
    
    # <stat_dec> productions
    ('stat_dec', TokenType.STAT): 37,
    
    # <more_stat> productions
    ('more_stat', TokenType.SEMICOLON): 38,
    ('more_stat', TokenType.COMMA): 38,
    ('more_stat', TokenType.ASSIGN): 39,
    
    # <stat_init> productions
    ('stat_init', TokenType.SEMICOLON): 40,
    ('stat_init', TokenType.COMMA): 40,
    ('stat_init', TokenType.ASSIGN): 41,
    
    # <stat_value> productions
    ('stat_value', TokenType.WIN): 42,
    ('stat_value', TokenType.LOSS): 43,
    
    # <stat_init_end> productions
    ('stat_init_end', TokenType.SEMICOLON): 44,
    ('stat_init_end', TokenType.COMMA): 45,

    # <const_dec> productions
    ('const_dec', TokenType.FEINT): 46,
    ('const_dec', TokenType.FLOATER): 47,
    ('const_dec', TokenType.CHANT): 48,
    ('const_dec', TokenType.FEINT): 49,
    ('const_dec', TokenType.FLOATER): 49,
    ('const_dec', TokenType.CHANT): 49,
    ('const_dec', TokenType.STAT): 49,
    ('const_dec', TokenType.CONST): 49,
    ('const_dec', TokenType.ZONE): 49,
    ('const_dec', TokenType.WILT): 49,
    ('const_dec', TokenType.DUNK): 49,
    ('const_dec', TokenType.TEAM): 49,
    
    # <const_feint> productions
    ('const_feint', TokenType.FEINT): 50,
    
    # <feint_const_init> productions
    ('feint_const_init', TokenType.ASSIGN): 51,
    
    # <feint_const> productions
    ('feint_const', TokenType.ASSIGN): 52,
    
    # <feint_const_end> productions
    ('feint_const_end', TokenType.COMMA): 53,
    ('feint_const_end', TokenType.SEMICOLON): 54,
    
    # <const_floater> productions
    ('const_floater', TokenType.FLOATER): 55,
    
    # <floater_const_init> productions
    ('floater_const_init', TokenType.ASSIGN): 56,
    
    # <floater_const> productions
    ('floater_const', TokenType.ASSIGN): 57,
    
    # <floater_const_end> productions
    ('floater_const_end', TokenType.COMMA): 58,
    ('floater_const_end', TokenType.SEMICOLON): 59,
    
    # <const_chant> productions
    ('const_chant', TokenType.CHANT): 60,
    
    # <chant_const_init> productions
    ('chant_const_init', TokenType.ASSIGN): 61,
    
    # <chant_const> productions
    ('chant_const', TokenType.ASSIGN): 62,
    
    # <chant_const_end> productions
    ('chant_const_end', TokenType.COMMA): 63,
    ('chant_const_end', TokenType.SEMICOLON): 64,
    
    # <const_stat> productions
    ('const_stat', TokenType.STAT): 65,
    
    # <stat_const_init> productions
    ('stat_const_init', TokenType.ASSIGN): 66,
    
    # <stat_const> productions
    ('stat_const', TokenType.ASSIGN): 67,
    
    # <stat_const_end> productions
    ('stat_const_end', TokenType.COMMA): 68,
    ('stat_const_end', TokenType.SEMICOLON): 69,
    
    # <array_dec> productions
    ('array_dec', TokenType.FEINT): 70,
    ('array_dec', TokenType.FLOATER): 71,
    ('array_dec', TokenType.CHANT): 72,
    
    # <feint_array> productions
    ('feint_array', TokenType.FEINT): 73,
    
    # <array_size> productions
    ('array_size', TokenType.FEINTLIT): 74,
    ('array_size', TokenType.VAR_INIT): 75,
    
    # <2D_array> productions
    ('2D_array', TokenType.ASSIGN): 76,
    ('2D_array', TokenType.SEMICOLON): 76,
    ('2D_array', TokenType.ARRAY_INDEX_LEFT): 77,
    
    # <feint_array_init> productions
    ('feint_array_init', TokenType.SEMICOLON): 78,
    ('feint_array_init', TokenType.ASSIGN): 79,
    
    # <feint_row> productions
    ('feint_row', TokenType.FEINTLIT): 80,
    ('feint_row', TokenType.CODE_BLOCK_LEFT): 81,
    
    # <2D_feint_row> productions
    ('2D_feint_row', TokenType.CODE_BLOCK_RIGHT): 82,
    ('2D_feint_row', TokenType.COMMA): 83,
    
    # <more_feint_lit> productions
    ('more_feint_lit', TokenType.CODE_BLOCK_RIGHT): 84,
    ('more_feint_lit', TokenType.COMMA): 85,
    
    # <floater_array> productions
    ('floater_array', TokenType.FLOATER): 86,
    
    # <floater_array_init> productions
    ('floater_array_init', TokenType.SEMICOLON): 87,
    ('floater_array_init', TokenType.ASSIGN): 88,
    
    # <floater_row> productions
    ('floater_row', TokenType.FLOATERLIT): 89,
    ('floater_row', TokenType.CODE_BLOCK_LEFT): 90,
    
    # <2D_floater_row> productions
    ('2D_floater_row', TokenType.CODE_BLOCK_RIGHT): 91,
    ('2D_floater_row', TokenType.COMMA): 92,
    
    # <more_floater_lit> productions
    ('more_floater_lit', TokenType.CODE_BLOCK_RIGHT): 93,
    ('more_floater_lit', TokenType.COMMA): 94,
    
    # <chant_array> productions
    ('chant_array', TokenType.CHANT): 95,
    
    # <chant_array_init> productions
    ('chant_array_init', TokenType.SEMICOLON): 96,
    ('chant_array_init', TokenType.ASSIGN): 97,
    
    # <chant_row> productions
    ('chant_row', TokenType.CHANTLIT): 98,
    ('chant_row', TokenType.CODE_BLOCK_LEFT): 99,
    
    # <2D_chant_row> productions
    ('2D_chant_row', TokenType.CODE_BLOCK_RIGHT): 100,
    ('2D_chant_row', TokenType.COMMA): 101,
    
    # <more_chant_lit> productions
    ('more_chant_lit', TokenType.CODE_BLOCK_RIGHT): 102,
    ('more_chant_lit', TokenType.COMMA): 103,
    
    # <function_def> productions
    ('function_def', TokenType.TEAM): 104,
    ('function_def', TokenType.WILT): 105,

     # <function_def> productions
    ('function_def', TokenType.DUNK): 106,
    
    # <function_declared> productions
    ('function_declared', TokenType.FEINT): 107,
    ('function_declared', TokenType.FLOATER): 108,
    ('function_declared', TokenType.CHANT): 109,
    ('function_declared', TokenType.STAT): 110,
    
    # <dunk_func_declared> productions
    ('dunk_func_declared', TokenType.VAR_INIT): 111,
    
    # <feint_function> productions
    ('feint_function', TokenType.FEINT): 112,
    
    # <floater_function> productions
    ('floater_function', TokenType.FLOATER): 113,
    
    # <chant_function> productions
    ('chant_function', TokenType.CHANT): 114,
    
    # <stat_function> productions
    ('stat_function', TokenType.STAT): 115,
    
    # <dunk_function> productions
    ('dunk_function', TokenType.VAR_INIT): 116,
    
    # <func_parameters> productions
    ('func_parameters', TokenType.RIGHT_PAREN): 117,
    ('func_parameters', TokenType.VAR_INIT): 118,
    
    # <param_end> productions
    ('param_end', TokenType.COMMA): 119,
    ('param_end', TokenType.RIGHT_PAREN): 120,
    
    # <decl> productions
    ('decl', TokenType.FEINT): 121,
    ('decl', TokenType.FLOATER): 121,
    ('decl', TokenType.CHANT): 121,
    ('decl', TokenType.STAT): 121,
    ('decl', TokenType.ZONE): 121,
    ('decl', TokenType.ANNOUNCE): 122,
    ('decl', TokenType.INBOUND): 122,
    ('decl', TokenType.DRIBBLE): 122,
    ('decl', TokenType.SWITCH): 122,
    ('decl', TokenType.FORWARD): 122,
    ('decl', TokenType.PLAY): 122,
    ('decl', TokenType.RUN): 122,
    ('decl', TokenType.VAR_INIT): 122,
    ('decl', TokenType.REBOUND): 122,
    
    # <declaration> productions
    ('declaration', TokenType.FEINT): 123,
    ('declaration', TokenType.FLOATER): 123,
    ('declaration', TokenType.CHANT): 123,
    ('declaration', TokenType.STAT): 123,
    ('declaration', TokenType.ZONE): 124,
    
    # <function_statement> productions
    ('function_statement', TokenType.ANNOUNCE): 125,
    ('function_statement', TokenType.INBOUND): 125,
    ('function_statement', TokenType.DRIBBLE): 125,
    ('function_statement', TokenType.SWITCH): 125,
    ('function_statement', TokenType.FORWARD): 125,
    ('function_statement', TokenType.PLAY): 125,
    ('function_statement', TokenType.RUN): 125,
    ('function_statement', TokenType.VAR_INIT): 125,
    ('function_statement', TokenType.REBOUND): 126,
    ('function_statement', TokenType.CODE_BLOCK_RIGHT): 126,
    
    # <rebound_statement> productions
    ('rebound_statement', TokenType.REBOUND): 127,
    
    # <statement> productions
    ('statement', TokenType.ANNOUNCE): 128,
    ('statement', TokenType.INBOUND): 129,
    ('statement', TokenType.DRIBBLE): 130,
    ('statement', TokenType.SWITCH): 131,
    ('statement', TokenType.FORWARD): 132,
    ('statement', TokenType.PLAY): 133,
    ('statement', TokenType.RUN): 134,
    ('statement', TokenType.VAR_INIT): 135,
    
    # <follow_statement> productions
    ('follow_statement', TokenType.INCREMENT): 136,
    ('follow_statement', TokenType.DECREMENT): 137,
    ('follow_statement', TokenType.LEFT_PAREN): 138,
    ('follow_statement', TokenType.ASSIGN): 139,
    ('follow_statement', TokenType.ADD_ASSIGN): 140,
    ('follow_statement', TokenType.SUB_ASSIGN): 141,
    ('follow_statement', TokenType.MUL_ASSIGN): 142,
    ('follow_statement', TokenType.DIV_ASSIGN): 143,
    ('follow_statement', TokenType.MOD_ASSIGN): 144,
    ('follow_statement', TokenType.ARRAY_INDEX_LEFT): 145,
    
    # <assign_operand> productions
    ('assign_operand', TokenType.FEINTLIT): 146,
    ('assign_operand', TokenType.FLOATERLIT): 146,
    ('assign_operand', TokenType.NEGAFEINT): 146,
    ('assign_operand', TokenType.NEGAFLOATER): 146,
    ('assign_operand', TokenType.CHANTLIT): 146,
    ('assign_operand', TokenType.WIN): 146,
    ('assign_operand', TokenType.LOSS): 146,
    ('assign_operand', TokenType.VAR_INIT): 146,
    ('assign_operand', TokenType.LEFT_PAREN): 146,
    ('assign_operand', TokenType.NOT_OP): 146,
    ('assign_operand', TokenType.FEINT): 146,
    ('assign_operand', TokenType.FLOATER): 146,
    ('assign_operand', TokenType.CHANT): 146,
    ('assign_operand', TokenType.STAT): 146,
    
    # <element_index> productions
    ('element_index', TokenType.VAR_INIT): 147,
    ('element_index', TokenType.FEINTLIT): 148,
    
    # <2d_manipulation> productions
    ('2d_manipulation', TokenType.ARRAY_INDEX_LEFT): 149,
    ('2d_manipulation', TokenType.ASSIGN): 150,
    ('2d_manipulation', TokenType.SEMICOLON): 150,
    
    # <array_man> productions
    ('array_man', TokenType.ASSIGN): 151,
    ('array_man', TokenType.SEMICOLON): 152,
    
    # <array_elem> productions
    ('array_elem', TokenType.FEINTLIT): 153,
    ('array_elem', TokenType.FLOATERLIT): 153,
    ('array_elem', TokenType.NEGAFEINT): 153,
    ('array_elem', TokenType.NEGAFLOATER): 153,
    ('array_elem', TokenType.CHANTLIT): 153,
    ('array_elem', TokenType.WIN): 153,
    ('array_elem', TokenType.LOSS): 153,
    ('array_elem', TokenType.VAR_INIT): 153,
    ('array_elem', TokenType.LEFT_PAREN): 153,
    ('array_elem', TokenType.NOT_OP): 153,
    ('array_elem', TokenType.FEINT): 153,
    ('array_elem', TokenType.FLOATER): 153,
    ('array_elem', TokenType.CHANT): 153,
    ('array_elem', TokenType.STAT): 153,
    
    # <expression> productions
    ('expression', TokenType.FEINTLIT): 154,
    ('expression', TokenType.FLOATERLIT): 154,
    ('expression', TokenType.NEGAFEINT): 154,
    ('expression', TokenType.NEGAFLOATER): 154,
    ('expression', TokenType.CHANTLIT): 154,
    ('expression', TokenType.WIN): 154,
    ('expression', TokenType.LOSS): 154,
    ('expression', TokenType.VAR_INIT): 154,
    ('expression', TokenType.LEFT_PAREN): 154,
    ('expression', TokenType.NOT_OP): 154,
    ('expression', TokenType.FEINT): 154,
    ('expression', TokenType.FLOATER): 154,
    ('expression', TokenType.CHANT): 154,
    ('expression', TokenType.STAT): 154,

    # <logical_expression> productions
    ('logical_expression', TokenType.FEINTLIT): 155,
    ('logical_expression', TokenType.FLOATERLIT): 155,
    ('logical_expression', TokenType.NEGAFEINT): 155,
    ('logical_expression', TokenType.NEGAFLOATER): 155,
    ('logical_expression', TokenType.CHANTLIT): 155,
    ('logical_expression', TokenType.WIN): 155,
    ('logical_expression', TokenType.LOSS): 155,
    ('logical_expression', TokenType.VAR_INIT): 155,
    ('logical_expression', TokenType.LEFT_PAREN): 155,
    ('logical_expression', TokenType.NOT_OP): 155,
    ('logical_expression', TokenType.FEINT): 155,
    ('logical_expression', TokenType.FLOATER): 155,
    ('logical_expression', TokenType.CHANT): 155,
    ('logical_expression', TokenType.STAT): 155,
    
    # <more_logical> productions
    ('more_logical', TokenType.AND_OP): 156,
    ('more_logical', TokenType.OR_OP): 156,
    ('more_logical', TokenType.SEMICOLON): 157,
    ('more_logical', TokenType.RIGHT_PAREN): 157,
    ('more_logical', TokenType.COMMA): 157,
    ('more_logical', TokenType.CHANT_CONCAT): 157,
    ('more_logical', TokenType.COLON): 157,
    ('more_logical', TokenType.ARRAY_INDEX_RIGHT): 157,
    
    # <log_operator> productions
    ('log_operator', TokenType.AND_OP): 158,
    ('log_operator', TokenType.OR_OP): 159,
    
    # <relational_expression> productions
    ('relational_expression', TokenType.FEINTLIT): 160,
    ('relational_expression', TokenType.FLOATERLIT): 160,
    ('relational_expression', TokenType.NEGAFEINT): 160,
    ('relational_expression', TokenType.NEGAFLOATER): 160,
    ('relational_expression', TokenType.CHANTLIT): 160,
    ('relational_expression', TokenType.WIN): 160,
    ('relational_expression', TokenType.LOSS): 160,
    ('relational_expression', TokenType.VAR_INIT): 160,
    ('relational_expression', TokenType.LEFT_PAREN): 160,
    ('relational_expression', TokenType.NOT_OP): 160,
    ('relational_expression', TokenType.FEINT): 160,
    ('relational_expression', TokenType.FLOATER): 160,
    ('relational_expression', TokenType.CHANT): 160,
    ('relational_expression', TokenType.STAT): 160,
    
    # <arithmetic_expression> productions
    ('arithmetic_expression', TokenType.FEINTLIT): 161,
    ('arithmetic_expression', TokenType.FLOATERLIT): 161,
    ('arithmetic_expression', TokenType.NEGAFEINT): 161,
    ('arithmetic_expression', TokenType.NEGAFLOATER): 161,
    ('arithmetic_expression', TokenType.CHANTLIT): 161,
    ('arithmetic_expression', TokenType.WIN): 161,
    ('arithmetic_expression', TokenType.LOSS): 161,
    ('arithmetic_expression', TokenType.VAR_INIT): 161,
    ('arithmetic_expression', TokenType.LEFT_PAREN): 161,
    ('arithmetic_expression', TokenType.NOT_OP): 161,
    ('arithmetic_expression', TokenType.FEINT): 161,
    ('arithmetic_expression', TokenType.FLOATER): 161,
    ('arithmetic_expression', TokenType.CHANT): 161,
    ('arithmetic_expression', TokenType.STAT): 161,
    
    # <more_relational> productions
    ('more_relational', TokenType.LESS_THAN): 162,
    ('more_relational', TokenType.GREATER_THAN): 162,
    ('more_relational', TokenType.EQUAL): 162,
    ('more_relational', TokenType.LESS_EQUAL): 162,
    ('more_relational', TokenType.GREATER_EQUAL): 162,
    ('more_relational', TokenType.NOT_EQUAL): 162,
    ('more_relational', TokenType.AND_OP): 163,
    ('more_relational', TokenType.OR_OP): 163,
    ('more_relational', TokenType.SEMICOLON): 163,
    ('more_relational', TokenType.RIGHT_PAREN): 163,
    ('more_relational', TokenType.COMMA): 163,
    ('more_relational', TokenType.CHANT_CONCAT): 163,
    ('more_relational', TokenType.COLON): 163,
    ('more_relational', TokenType.ARRAY_INDEX_RIGHT): 163,
    
    # <term> productions
    ('term', TokenType.FEINTLIT): 164,
    ('term', TokenType.FLOATERLIT): 164,
    ('term', TokenType.NEGAFEINT): 164,
    ('term', TokenType.NEGAFLOATER): 164,
    ('term', TokenType.CHANTLIT): 164,
    ('term', TokenType.WIN): 164,
    ('term', TokenType.LOSS): 164,
    ('term', TokenType.VAR_INIT): 164,
    ('term', TokenType.LEFT_PAREN): 164,
    ('term', TokenType.NOT_OP): 164,
    ('term', TokenType.FEINT): 164,
    ('term', TokenType.FLOATER): 164,
    ('term', TokenType.CHANT): 164,
    ('term', TokenType.STAT): 164,
    
    # <more_term> productions
    ('more_term', TokenType.ADD): 165,
    ('more_term', TokenType.SUB): 166,
    ('more_term', TokenType.LESS_THAN): 167,
    ('more_term', TokenType.GREATER_THAN): 167,
    ('more_term', TokenType.EQUAL): 167,
    ('more_term', TokenType.LESS_EQUAL): 167,
    ('more_term', TokenType.GREATER_EQUAL): 167,
    ('more_term', TokenType.NOT_EQUAL): 167,
    
    # <more_factor> productions
    ('more_factor', TokenType.MUL): 168,
    ('more_factor', TokenType.DIV): 169,
    ('more_factor', TokenType.MOD): 170,
    ('more_factor', TokenType.ADD): 171,
    ('more_factor', TokenType.SUB): 171,
    ('more_factor', TokenType.LESS_THAN): 171,
    ('more_factor', TokenType.GREATER_THAN): 171,
    ('more_factor', TokenType.EQUAL): 171,
    ('more_factor', TokenType.LESS_EQUAL): 171,
    ('more_factor', TokenType.GREATER_EQUAL): 171,
    ('more_factor', TokenType.NOT_EQUAL): 171,
    
    # <factor> productions
    ('factor', TokenType.FEINTLIT): 172,
    ('factor', TokenType.FLOATERLIT): 172,
    ('factor', TokenType.NEGAFEINT): 172,
    ('factor', TokenType.NEGAFLOATER): 172,
    ('factor', TokenType.CHANTLIT): 172,
    ('factor', TokenType.WIN): 172,
    ('factor', TokenType.LOSS): 172,
    ('factor', TokenType.VAR_INIT): 173,
    ('factor', TokenType.LEFT_PAREN): 174,
    ('factor', TokenType.NOT_OP): 175,
    ('factor', TokenType.FEINT): 176,
    ('factor', TokenType.FLOATER): 176,
    ('factor', TokenType.CHANT): 176,
    ('factor', TokenType.STAT): 176,
    
    # <literal> productions
    ('literal', TokenType.FEINTLIT): 177,
    ('literal', TokenType.NEGAFEINT): 177,
    ('literal', TokenType.FLOATERLIT): 178,
    ('literal', TokenType.NEGAFLOATER): 178,
    ('literal', TokenType.NEGAFEINT): 179,
    ('literal', TokenType.NEGAFLOATER): 180,
    ('literal', TokenType.CHANTLIT): 181,
    ('literal', TokenType.WIN): 182,
    ('literal', TokenType.LOSS): 182,
    
    # <nega_feint_lit> and <nega_floater_lit> productions
    ('nega_feint_lit', TokenType.NEGAFEINT): 183,
    ('nega_floater_lit', TokenType.NEGAFLOATER): 184,
    
    # <follow_factor> productions
    ('follow_factor', TokenType.ARRAY_INDEX_LEFT): 185,
    ('follow_factor', TokenType.LEFT_PAREN): 186,
    
    # <function_call> productions
    ('function_call', TokenType.MUL): 187,
    ('function_call', TokenType.DIV): 187,
    ('function_call', TokenType.MOD): 187,
    ('function_call', TokenType.ADD): 187,
    ('function_call', TokenType.SUB): 187,
    ('function_call', TokenType.LESS_THAN): 187,
    ('function_call', TokenType.GREATER_THAN): 187,
    ('function_call', TokenType.EQUAL): 187,
    ('function_call', TokenType.LESS_EQUAL): 187,
    ('function_call', TokenType.GREATER_EQUAL): 187,
    ('function_call', TokenType.NOT_EQUAL): 187,
    ('function_call', TokenType.SEMICOLON): 187,
    ('function_call', TokenType.LEFT_PAREN): 188,
    
    # <arguments> productions
    ('arguments', TokenType.FEINTLIT): 189,
    ('arguments', TokenType.FLOATERLIT): 189,
    ('arguments', TokenType.NEGAFEINT): 189,
    ('arguments', TokenType.NEGAFLOATER): 189,
    ('arguments', TokenType.CHANTLIT): 189,
    ('arguments', TokenType.WIN): 189,
    ('arguments', TokenType.LOSS): 189,
    ('arguments', TokenType.VAR_INIT): 189,
    ('arguments', TokenType.LEFT_PAREN): 189,
    ('arguments', TokenType.NOT_OP): 189,
    ('arguments', TokenType.FEINT): 189,
    ('arguments', TokenType.FLOATER): 189,
    ('arguments', TokenType.CHANT): 189,
    ('arguments', TokenType.STAT): 189,
    ('arguments', TokenType.RIGHT_PAREN): 190,
    
    # <arg> productions
    ('arg', TokenType.FEINTLIT): 191,
    ('arg', TokenType.FLOATERLIT): 191,
    ('arg', TokenType.NEGAFEINT): 191,
    ('arg', TokenType.NEGAFLOATER): 191,
    ('arg', TokenType.CHANTLIT): 191,
    ('arg', TokenType.WIN): 191,
    ('arg', TokenType.LOSS): 191,
    ('arg', TokenType.VAR_INIT): 191,
    ('arg', TokenType.LEFT_PAREN): 191,
    ('arg', TokenType.NOT_OP): 191,
    ('arg', TokenType.FEINT): 191,
    ('arg', TokenType.FLOATER): 191,
    ('arg', TokenType.CHANT): 191,
    ('arg', TokenType.STAT): 191,
    
    # <more_args> productions
    ('more_args', TokenType.COMMA): 192,
    ('more_args', TokenType.RIGHT_PAREN): 193,
    
    # <relational_operator> productions
    ('relational_operator', TokenType.LESS_THAN): 194,
    ('relational_operator', TokenType.GREATER_THAN): 195,
    ('relational_operator', TokenType.EQUAL): 196,
    ('relational_operator', TokenType.LESS_EQUAL): 197,
    ('relational_operator', TokenType.GREATER_EQUAL): 198,
    ('relational_operator', TokenType.NOT_EQUAL): 199,
    
    # <type_casting> productions
    ('type_casting', TokenType.FEINT): 200,
    ('type_casting', TokenType.FLOATER): 201,
    ('type_casting', TokenType.CHANT): 202,
    ('type_casting', TokenType.STAT): 203,
    
    # <typecast_value> productions
    ('typecast_value', TokenType.FEINTLIT): 204,
    ('typecast_value', TokenType.FLOATERLIT): 205,
    ('typecast_value', TokenType.CHANTLIT): 206,
    ('typecast_value', TokenType.WIN): 207,
    ('typecast_value', TokenType.LOSS): 207,
    ('typecast_value', TokenType.VAR_INIT): 208,
    
    # <announce_statement> productions
    ('announce_statement', TokenType.ANNOUNCE): 209,
    
    # <otpt> productions
    ('otpt', TokenType.FEINTLIT): 210,
    ('otpt', TokenType.FLOATERLIT): 210,
    ('otpt', TokenType.NEGAFEINT): 210,
    ('otpt', TokenType.NEGAFLOATER): 210,
    ('otpt', TokenType.CHANTLIT): 210,
    ('otpt', TokenType.WIN): 210,
    ('otpt', TokenType.LOSS): 210,
    ('otpt', TokenType.VAR_INIT): 210,
    ('otpt', TokenType.LEFT_PAREN): 210,
    ('otpt', TokenType.NOT_OP): 210,
    ('otpt', TokenType.FEINT): 210,
    ('otpt', TokenType.FLOATER): 210,
    ('otpt', TokenType.CHANT): 210,
    ('otpt', TokenType.STAT): 210,
    
    # <outputs> productions
    ('outputs', TokenType.FEINTLIT): 211,
    ('outputs', TokenType.FLOATERLIT): 211,
    ('outputs', TokenType.NEGAFEINT): 211,
    ('outputs', TokenType.NEGAFLOATER): 211,
    ('outputs', TokenType.CHANTLIT): 211,
    ('outputs', TokenType.WIN): 211,
    ('outputs', TokenType.LOSS): 211,
    ('outputs', TokenType.VAR_INIT): 211,
    ('outputs', TokenType.LEFT_PAREN): 211,
    ('outputs', TokenType.NOT_OP): 211,
    ('outputs', TokenType.FEINT): 211,
    ('outputs', TokenType.FLOATER): 211,
    ('outputs', TokenType.CHANT): 211,
    ('outputs', TokenType.STAT): 211,
    
    # <other_outputs> productions
    ('other_outputs', TokenType.CHANT_CONCAT): 212,
    ('other_outputs', TokenType.RIGHT_PAREN): 213,
    
    # <inbound_statement> productions
    ('inbound_statement', TokenType.INBOUND): 214,
    
    # <dribble_statement> productions
    ('dribble_statement', TokenType.DRIBBLE): 215,
    
    # <add_condition> productions
    ('add_condition', TokenType.PASS): 216,
    ('add_condition', TokenType.SHOOT): 217,
    ('add_condition', TokenType.ANNOUNCE): 218,
    ('add_condition', TokenType.INBOUND): 218,
    ('add_condition', TokenType.DRIBBLE): 218,
    ('add_condition', TokenType.SWITCH): 218,
    ('add_condition', TokenType.FORWARD): 218,
    ('add_condition', TokenType.PLAY): 218,
    ('add_condition', TokenType.RUN): 218,
    ('add_condition', TokenType.VAR_INIT): 218,
    ('add_condition', TokenType.RESUME): 218,
    ('add_condition', TokenType.TIMEOUT): 218,
    ('add_condition', TokenType.TEAM): 218,
    
    # <loop_statements> productions
    ('loop_statements', TokenType.ANNOUNCE): 219,
    ('loop_statements', TokenType.INBOUND): 219,
    ('loop_statements', TokenType.DRIBBLE): 219,
    ('loop_statements', TokenType.SWITCH): 219,
    ('loop_statements', TokenType.FORWARD): 219,
    ('loop_statements', TokenType.PLAY): 219,
    ('loop_statements', TokenType.RUN): 219,
    ('loop_statements', TokenType.VAR_INIT): 219,
    ('loop_statements', TokenType.RESUME): 219,
    ('loop_statements', TokenType.TIMEOUT): 219,
    ('loop_statements', TokenType.CODE_BLOCK_RIGHT): 220,
    
    # <loop_statement> productions
    ('loop_statement', TokenType.ANNOUNCE): 221,
    ('loop_statement', TokenType.INBOUND): 221,
    ('loop_statement', TokenType.DRIBBLE): 221,
    ('loop_statement', TokenType.SWITCH): 221,
    ('loop_statement', TokenType.FORWARD): 221,
    ('loop_statement', TokenType.PLAY): 221,
    ('loop_statement', TokenType.RUN): 221,
    ('loop_statement', TokenType.VAR_INIT): 221,
    ('loop_statement', TokenType.RESUME): 222,
    ('loop_statement', TokenType.TIMEOUT): 223,
    
    # <timeout_statement> productions
    ('timeout_statement', TokenType.TIMEOUT): 224,
    
    # <switch_statement> productions
    ('switch_statement', TokenType.SWITCH): 225,
    
    # <get_case> productions
    ('get_case', TokenType.GET): 226,
    
    # <get_value> productions
    ('get_value', TokenType.FEINTLIT): 227,
    ('get_value', TokenType.CHANTLIT): 228,
    
    # <get_case_end> productions
    ('get_case_end', TokenType.DEFAULT): 229,
    ('get_case_end', TokenType.RIGHT_PAREN): 229,
    ('get_case_end', TokenType.GET): 230,
    
    # <get_default> productions
    ('get_default', TokenType.DEFAULT): 231,
    ('get_default', TokenType.CODE_BLOCK_RIGHT): 232,
    
    # <forward_statement> productions
    ('forward_statement', TokenType.FORWARD): 233,
    
    # <forward_lit> productions
    ('forward_lit', TokenType.FEINTLIT): 234,
    ('forward_lit', TokenType.VAR_INIT): 235,
    
    # <forward_inc_dec> productions
    ('forward_inc_dec', TokenType.INCREMENT): 236,
    ('forward_inc_dec', TokenType.DECREMENT): 237,
    ('forward_inc_dec', TokenType.ADD_ASSIGN): 238,
    ('forward_inc_dec', TokenType.SUB_ASSIGN): 238,
    
    # <increment> productions
    ('increment', TokenType.INCREMENT): 239,
    
    # <decrement> productions
    ('decrement', TokenType.DECREMENT): 240,
    
    # <forward_assign_operator> productions
    ('forward_assign_operator', TokenType.ADD_ASSIGN): 241,
    ('forward_assign_operator', TokenType.SUB_ASSIGN): 242,
    
    # <resume_statement> productions
    ('resume_statement', TokenType.RESUME): 243,
    ('resume_statement', TokenType.ANNOUNCE): 244,
    ('resume_statement', TokenType.INBOUND): 244,
    ('resume_statement', TokenType.DRIBBLE): 244,
    ('resume_statement', TokenType.SWITCH): 244,
    ('resume_statement', TokenType.FORWARD): 244,
    ('resume_statement', TokenType.PLAY): 244,
    ('resume_statement', TokenType.RUN): 244,
    ('resume_statement', TokenType.VAR_INIT): 244,
    ('resume_statement', TokenType.RESUME): 244,
    ('resume_statement', TokenType.TIMEOUT): 244,
    
    # <play_statement> productions
    ('play_statement', TokenType.PLAY): 245,
    
    # <run_play_statement> productions
    ('run_play_statement', TokenType.RUN): 246,
    
    # <team_block> productions
    ('team_block', TokenType.TEAM): 247,
    
    # <team_statement> productions
    ('team_statement', TokenType.ANNOUNCE): 248,
    ('team_statement', TokenType.INBOUND): 248,
    ('team_statement', TokenType.DRIBBLE): 248,
    ('team_statement', TokenType.SWITCH): 248,
    ('team_statement', TokenType.FORWARD): 248,
    ('team_statement', TokenType.PLAY): 248,
    ('team_statement', TokenType.RUN): 248,
    ('team_statement', TokenType.VAR_INIT): 248,
    ('team_statement', TokenType.TIMEOUT): 249
    
}