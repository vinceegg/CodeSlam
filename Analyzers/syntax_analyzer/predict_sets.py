from Analyzers.lexical_analyzer.tokens import TokenType

PREDICT_SETS = {
    # <program>
    'program': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                TokenType.TEAM},
    
    # <global_decl>
    'global_decl': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                   TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                   TokenType.TEAM},
    
    # <global_declaration>
    'global_declaration': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                          TokenType.CONST, TokenType.ZONE},
    
    # <variable_dec>
    'variable_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <feint_dec>
    'feint_dec': {TokenType.FEINT},
    
    # <more_feint>
    'more_feint': {TokenType.SEMICOLON, TokenType.COMMA, TokenType.ASSIGN},
    
    # <feint_init>
    'feint_init': {TokenType.SEMICOLON, TokenType.COMMA, TokenType.ASSIGN},
    
    # <feint_lit>
    'feint_lit': {TokenType.FEINTLIT, TokenType.NEGAFEINT},
    
    # <feint_init_end>
    'feint_init_end': {TokenType.SEMICOLON, TokenType.COMMA},
    
    # <floater_dec>
    'floater_dec': {TokenType.FLOATER},
    
    # <more_floater>
    'more_floater': {TokenType.SEMICOLON, TokenType.COMMA, TokenType.ASSIGN},
    
    # <floater_init>
    'floater_init': {TokenType.SEMICOLON, TokenType.COMMA, TokenType.ASSIGN},
    
    # <floater_lit>
    'floater_lit': {TokenType.FLOATERLIT, TokenType.NEGAFLOATER},
    
    # <floater_init_end>
    'floater_init_end': {TokenType.SEMICOLON, TokenType.COMMA},
    
    # <chant_dec>
    'chant_dec': {TokenType.CHANT},
    
    # <more_chant>
    'more_chant': {TokenType.SEMICOLON, TokenType.COMMA, TokenType.ASSIGN},
    
    # <chant_init>
    'chant_init': {TokenType.SEMICOLON, TokenType.COMMA, TokenType.ASSIGN},
    
    # <chant_lit>
    'chant_lit': {TokenType.CHANTLIT},
    
    # <chant_init_end>
    'chant_init_end': {TokenType.SEMICOLON, TokenType.COMMA},
    
    # <stat_dec>
    'stat_dec': {TokenType.STAT},
    
    # <more_stat>
    'more_stat': {TokenType.SEMICOLON, TokenType.COMMA, TokenType.ASSIGN},
    
    # <stat_init>
    'stat_init': {TokenType.SEMICOLON, TokenType.COMMA, TokenType.ASSIGN},
    
    # <stat_value>
    'stat_value': {TokenType.WIN, TokenType.LOSS},
    
    # <stat_init_end>
    'stat_init_end': {TokenType.SEMICOLON, TokenType.COMMA},
    
    # <const_dec>
    'const_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <const_feint>
    'const_feint': {TokenType.FEINT},
    
    # <feint_const_init>
    'feint_const_init': {TokenType.ASSIGN},
    
    # <feint_const>
    'feint_const': {TokenType.ASSIGN},
    
    # <feint_const_end>
    'feint_const_end': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <const_floater>
    'const_floater': {TokenType.FLOATER},
    
    # <floater_const_init>
    'floater_const_init': {TokenType.ASSIGN},
    
    # <floater_const>
    'floater_const': {TokenType.ASSIGN},
    
    # <floater_const_end>
    'floater_const_end': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <const_chant>
    'const_chant': {TokenType.CHANT},
    
    # <chant_const_init>
    'chant_const_init': {TokenType.ASSIGN},
    
    # <chant_const>
    'chant_const': {TokenType.ASSIGN},
    
    # <chant_const_end>
    'chant_const_end': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <const_stat>
    'const_stat': {TokenType.STAT},
    
    # <stat_const_init>
    'stat_const_init': {TokenType.ASSIGN},
    
    # <stat_const>
    'stat_const': {TokenType.ASSIGN},
    
    # <stat_const_end>
    'stat_const_end': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <array_dec>
    'array_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT},
    
    # <feint_array>
    'feint_array': {TokenType.FEINT},
    
    # <array_size>
    'array_size': {TokenType.FEINTLIT, TokenType.VAR_INIT},
    
    # <2D_array>
    '2D_array': {TokenType.ASSIGN, TokenType.SEMICOLON, TokenType.ARRAY_INDEX_LEFT},
    
    # <feint_array_init>
    'feint_array_init': {TokenType.SEMICOLON, TokenType.ASSIGN},
    
    # <feint_row>
    'feint_row': {TokenType.FEINTLIT, TokenType.CODE_BLOCK_LEFT},
    
    # <2D_feint_row>
    '2D_feint_row': {TokenType.CODE_BLOCK_RIGHT, TokenType.COMMA},
    
    # <more_feint_lit>
    'more_feint_lit': {TokenType.CODE_BLOCK_RIGHT, TokenType.COMMA},
    
    # <floater_array>
    'floater_array': {TokenType.FLOATER},
    
    # <floater_array_init>
    'floater_array_init': {TokenType.SEMICOLON, TokenType.ASSIGN},
    
    # <floater_row>
    'floater_row': {TokenType.FLOATERLIT, TokenType.CODE_BLOCK_LEFT},
    
    # <2D_floater_row>
    '2D_floater_row': {TokenType.CODE_BLOCK_RIGHT, TokenType.COMMA},
    
    # <more_floater_lit>
    'more_floater_lit': {TokenType.CODE_BLOCK_RIGHT, TokenType.COMMA},
    
    # <chant_array>
    'chant_array': {TokenType.CHANT},
    
    # <chant_array_init>
    'chant_array_init': {TokenType.SEMICOLON, TokenType.ASSIGN},
    
    # <chant_row>
    'chant_row': {TokenType.CHANTLIT, TokenType.CODE_BLOCK_LEFT},
    
    # <2D_chant_row>
    '2D_chant_row': {TokenType.CODE_BLOCK_RIGHT, TokenType.COMMA},
    
    # <more_chant_lit>
    'more_chant_lit': {TokenType.CODE_BLOCK_RIGHT, TokenType.COMMA},
    
    # <function_def>
    'function_def': {TokenType.TEAM, TokenType.WILT, TokenType.DUNK},
    
    # <function_declared>
    'function_declared': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <dunk_func_declared>
    'dunk_func_declared': {TokenType.VAR_INIT},
    
    # <feint_function>
    'feint_function': {TokenType.FEINT},
    
    # <floater_function>
    'floater_function': {TokenType.FLOATER},
    
    # <chant_function>
    'chant_function': {TokenType.CHANT},
    
    # <stat_function>
    'stat_function': {TokenType.STAT},
    
    # <dunk_function>
    'dunk_function': {TokenType.VAR_INIT},
    
    # <func_parameters>
    'func_parameters': {TokenType.RIGHT_PAREN, TokenType.VAR_INIT},
    
    # <param_end>
    'param_end': {TokenType.COMMA, TokenType.RIGHT_PAREN},
    
    # <decl>
    'decl': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
            TokenType.ZONE, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, 
            TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, 
            TokenType.VAR_INIT, TokenType.REBOUND},
    
    # <declaration>
    'declaration': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                   TokenType.ZONE},
    
    # <function_statement>
    'function_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, 
                          TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, 
                          TokenType.RUN, TokenType.VAR_INIT, TokenType.REBOUND, 
                          TokenType.CODE_BLOCK_RIGHT},
    
    # <rebound_statement>
    'rebound_statement': {TokenType.REBOUND},
    
    # <statement>
    'statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                 TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                 TokenType.VAR_INIT},
    
    # <follow_statement>
    'follow_statement': {TokenType.INCREMENT, TokenType.DECREMENT, TokenType.LEFT_PAREN,
                        TokenType.ASSIGN, TokenType.ADD_ASSIGN, TokenType.SUB_ASSIGN,
                        TokenType.MUL_ASSIGN, TokenType.DIV_ASSIGN, TokenType.MOD_ASSIGN,
                        TokenType.ARRAY_INDEX_LEFT},
    
    # <assign_operand>
    'assign_operand': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
                      TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
                      TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
                      TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
                      TokenType.CHANT, TokenType.STAT},
    
    # <element_index>
    'element_index': {TokenType.VAR_INIT, TokenType.FEINTLIT},
    
    # <2d_manipulation>
    '2d_manipulation': {TokenType.ARRAY_INDEX_LEFT, TokenType.ASSIGN, TokenType.SEMICOLON},
    
    # <array_man>
    'array_man': {TokenType.ASSIGN, TokenType.SEMICOLON},
    
    # <array_elem>
    'array_elem': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
                  TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
                  TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
                  TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
                  TokenType.CHANT, TokenType.STAT},
    
    # <expression>
    'expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
                  TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
                  TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
                  TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
                  TokenType.CHANT, TokenType.STAT},
    
    # <logical_expression>
    'logical_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
                          TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
                          TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
                          TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
                          TokenType.CHANT, TokenType.STAT},
    
    # <more_logical>
    'more_logical': {TokenType.AND_OP, TokenType.OR_OP, TokenType.SEMICOLON,
                    TokenType.RIGHT_PAREN, TokenType.COMMA, TokenType.CHANT_CONCAT,
                    TokenType.COLON, TokenType.ARRAY_INDEX_RIGHT},
    
    # <log_operator>
    'log_operator': {TokenType.AND_OP, TokenType.OR_OP},
    
    # <relational_expression>
    'relational_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
                             TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
                             TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
                             TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
                             TokenType.CHANT, TokenType.STAT},
    
    # <arithmetic_expression>
    'arithmetic_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
                             TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
                             TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
                             TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
                             TokenType.CHANT, TokenType.STAT},
    
    # <more_relational>
    'more_relational': {TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL,
                       TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL,
                       TokenType.AND_OP, TokenType.OR_OP, TokenType.SEMICOLON,
                       TokenType.RIGHT_PAREN, TokenType.COMMA, TokenType.CHANT_CONCAT,
                       TokenType.COLON, TokenType.ARRAY_INDEX_RIGHT},
    
    # <term>
    'term': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
            TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
            TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
            TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
            TokenType.CHANT, TokenType.STAT},
    
    # <more_term>
    'more_term': {TokenType.ADD, TokenType.SUB, TokenType.LESS_THAN, TokenType.GREATER_THAN,
                 TokenType.EQUAL, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL,
                 TokenType.NOT_EQUAL},
    
    # <more_factor>
    'more_factor': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB,
                   TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL,
                   TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <factor>
    'factor': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
              TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
              TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
              TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
              TokenType.CHANT, TokenType.STAT},
    
    # <literal>
    'literal': {TokenType.FEINTLIT, TokenType.NEGAFEINT, TokenType.FLOATERLIT, 
               TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
    
    # <nega_feint_lit>
    'nega_feint_lit': {TokenType.NEGAFEINT},
    
    # <nega_floater_lit>
    'nega_floater_lit': {TokenType.NEGAFLOATER},
    
    # <follow_factor>
    'follow_factor': {TokenType.ARRAY_INDEX_LEFT, TokenType.LEFT_PAREN},
    
    # <function_call>
    'function_call': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB,
                     TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL,
                     TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL,
                     TokenType.SEMICOLON, TokenType.LEFT_PAREN},
    
    # <arguments>
    'arguments': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
                 TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
                 TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
                 TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
                 TokenType.CHANT, TokenType.STAT, TokenType.RIGHT_PAREN},
    
    # <arg>
    'arg': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
           TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
           TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
           TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
           TokenType.CHANT, TokenType.STAT},
    
    # <more_args>
    'more_args': {TokenType.COMMA, TokenType.RIGHT_PAREN},
    
    # <relational_operator>
    'relational_operator': {TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL,
                           TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <type_casting>
    'type_casting': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <typecast_value>
    'typecast_value': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT,
                      TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT},
    
    # <announce_statement>
    'announce_statement': {TokenType.ANNOUNCE},
    
    # <otpt>
    'otpt': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
            TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
            TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
            TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
            TokenType.CHANT, TokenType.STAT},
    
    # <outputs>
    'outputs': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT,
               TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN,
               TokenType.LOSS, TokenType.VAR_INIT, TokenType.LEFT_PAREN,
               TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER,
               TokenType.CHANT, TokenType.STAT},
    
    # <other_outputs>
    'other_outputs': {TokenType.CHANT_CONCAT, TokenType.RIGHT_PAREN},
    
    # <inbound_statement>
    'inbound_statement': {TokenType.INBOUND},
    
    # <dribble_statement>
    'dribble_statement': {TokenType.DRIBBLE},
    
    # <add_condition>
    'add_condition': {TokenType.PASS, TokenType.SHOOT, TokenType.ANNOUNCE,
                     TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH,
                     TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                     TokenType.VAR_INIT, TokenType.RESUME, TokenType.TIMEOUT,
                     TokenType.TEAM},
    
    # <loop_statements>
    'loop_statements': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                       TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY,
                       TokenType.RUN, TokenType.VAR_INIT, TokenType.RESUME,
                       TokenType.TIMEOUT, TokenType.CODE_BLOCK_RIGHT},
    
    # <loop_statement>
    'loop_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                      TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY,
                      TokenType.RUN, TokenType.VAR_INIT, TokenType.RESUME,
                      TokenType.TIMEOUT},
    
    # <timeout_statement>
    'timeout_statement': {TokenType.TIMEOUT},
    
    # <switch_statement>
    'switch_statement': {TokenType.SWITCH},
    
    # <get_case>
    'get_case': {TokenType.GET},
    
    # <get_value>
    'get_value': {TokenType.FEINTLIT, TokenType.CHANTLIT},
    
    # <get_case_end>
    'get_case_end': {TokenType.DEFAULT, TokenType.RIGHT_PAREN, TokenType.GET},
    
    # <get_default>
    'get_default': {TokenType.DEFAULT, TokenType.CODE_BLOCK_RIGHT},
    
    # <forward_statement>
    'forward_statement': {TokenType.FORWARD},
    
    # <forward_lit>
    'forward_lit': {TokenType.FEINTLIT, TokenType.VAR_INIT},
    
    # <forward_inc_dec>
    'forward_inc_dec': {TokenType.INCREMENT, TokenType.DECREMENT, TokenType.ADD_ASSIGN,
                       TokenType.SUB_ASSIGN},
    
    # <increment>
    'increment': {TokenType.INCREMENT},
    
    # <decrement>
    'decrement': {TokenType.DECREMENT},
    
    # <forward_assign_operator>
    'forward_assign_operator': {TokenType.ADD_ASSIGN, TokenType.SUB_ASSIGN},
    
    # <resume_statement>
    'resume_statement': {TokenType.RESUME, TokenType.ANNOUNCE, TokenType.INBOUND,
                        TokenType.DRIBBLE, TokenType.SWITCH, TokenType.FORWARD,
                        TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT,
                        TokenType.TIMEOUT},
    
    # <play_statement>
    'play_statement': {TokenType.PLAY},
    
    # <run_play_statement>
    'run_play_statement': {TokenType.RUN},
    
    # <team_block>
    'team_block': {TokenType.TEAM},
    
    # <team_statement>
    'team_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                      TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY,
                      TokenType.RUN, TokenType.VAR_INIT, TokenType.TIMEOUT}
}