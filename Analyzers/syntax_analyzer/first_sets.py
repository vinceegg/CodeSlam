from Analyzers.lexical_analyzer.tokens import TokenType

FIRST_SETS = {
    # <program>
    'program': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
               TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, TokenType.TEAM},

    # <global_decl>
    'global_decl': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                  TokenType.CONST, TokenType.ZONE},
    
    # <global_declaration>
    'global_declaration': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                          TokenType.CONST, TokenType.ZONE},
    
    # <variable_dec>
    'variable_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <feint_dec>
    'feint_dec': {TokenType.FEINT},
    
    # <more_feint>
    'more_feint': {TokenType.ASSIGN, TokenType.COMMA},
    
    # <feint_init>
    'feint_init': {TokenType.ASSIGN},
    
    # <feint_lit>
    'feint_lit': {TokenType.FEINTLIT},
    
    # <feint_init_end>
    'feint_init_end': {TokenType.COMMA},
    
    # <floater_dec>
    'floater_dec': {TokenType.FLOATER},
    
    # <more_floater>
    'more_floater': {TokenType.COMMA, TokenType.ASSIGN},
    
    # <floater_init>
    'floater_init': {TokenType.ASSIGN, },
    
    # <floater_lit>
    'floater_lit': {TokenType.FLOATERLIT},
    
    # <floater_init_end>
    'floater_init_end': {TokenType.COMMA, },
    
    # <chant_dec>
    'chant_dec': {TokenType.CHANT},
    
    # <more_chant>
    'more_chant': {TokenType.COMMA, TokenType.ASSIGN},
    
    # <chant_init>
    'chant_init': {TokenType.ASSIGN, TokenType.COMMA},
    
    # <chant_lit>
    'chant_lit': {TokenType.CHANTLIT},
    
    # <chant_init_end>
    'chant_init_end': {TokenType.COMMA, },
    
    # <stat_dec>
    'stat_dec': {TokenType.STAT},
    
    # <more_stat>
    'more_stat': {TokenType.COMMA, TokenType.COMMA},
    
    # <stat_init>
    'stat_init': {TokenType.ASSIGN, },
    
    # <stat_value>
    'stat_value': {TokenType.WIN, TokenType.LOSS},
    
    # <stat_init_end>
    'stat_init_end': {TokenType.COMMA, },
    
    # <const_dec>
    'const_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <const_feint>
    'const_feint': {TokenType.FEINT},
    
    # <feint_const_init>
    'feint_const_init': {TokenType.ASSIGN},
    
    # <feint_const>
    'feint_const': {TokenType.ASSIGN},
    
    # <feint_const_end>
    'feint_const_end': {TokenType.COMMA, },
    
    # <const_floater>
    'const_floater': {TokenType.FLOATER},
    
    # <floater_const_init>
    'floater_const_init': {TokenType.ASSIGN},
    
    # <floater_const>
    'floater_const': {TokenType.ASSIGN},
    
    # <floater_const_end>
    'floater_const_end': {TokenType.COMMA, },
    
    # <const_chant>
    'const_chant': {TokenType.CHANT},
    
    # <chant_const_init>
    'chant_const_init': {TokenType.ASSIGN},
    
    # <chant_const>
    'chant_const': {TokenType.ASSIGN},
    
    # <chant_const_end>
    'chant_const_end': {TokenType.COMMA, },
    
    # <const_stat>
    'const_stat': {TokenType.STAT},
    
    # <stat_const_init>
    'stat_const_init': {TokenType.ASSIGN},
    
    # <stat_const>
    'stat_const': {TokenType.ASSIGN},
    
    # <stat_const_end>
    'stat_const_end': {TokenType.COMMA, },
    
    # <array_dec>
    'array_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT},
    
    # <feint_array>
    'feint_array': {TokenType.FEINT},
    
    # <2D_array>
    '2D_array': {TokenType.ARRAY_INDEX_LEFT, },
    
    # <feint_array_init>
    'feint_array_init': {TokenType.ASSIGN, },
    
    # <feint_row>
    'feint_row': {TokenType.FEINTLIT, TokenType.CODE_BLOCK_LEFT},
    
    # <2D_feint_row>
    '2D_feint_row': {TokenType.COMMA, },
    
    # <more_feint_lit>
    'more_feint_lit': {TokenType.COMMA, },
    
    # <floater_array>
    'floater_array': {TokenType.FLOATER},
    
    # <floater_array_init>
    'floater_array_init': {TokenType.ASSIGN, },
    
    # <floater_row>
    'floater_row': {TokenType.FLOATERLIT, TokenType.CODE_BLOCK_LEFT},
    
    # <2D_floater_row>
    '2D_floater_row': {TokenType.COMMA, },
    
    # <more_floater_lit>
    'more_floater_lit': {TokenType.COMMA, },
    
    # <chant_array>
    'chant_array': {TokenType.CHANT},
    
    # <chant_array_init>
    'chant_array_init': {TokenType.ASSIGN, },
    
    # <chant_row>
    'chant_row': {TokenType.CHANTLIT, TokenType.CODE_BLOCK_LEFT},
    
    # <2D_chant_row>
    '2D_chant_row': {TokenType.COMMA, },
    
    # <more_chant_lit>
    'more_chant_lit': {TokenType.COMMA, },
    
    # <function_def>
    'function_def': {TokenType.WILT, TokenType.DUNK, },
    
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
    'func_parameters': {TokenType.VAR_INIT, },
    
    # <param_end>
    'param_end': {TokenType.COMMA, },
    
    # <function_statement>
    'function_statement': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, TokenType.ANNOUNCE,
                          TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY,
                          TokenType.RUN, TokenType.VAR_INIT, },
    
    # <team_statement>
    'team_statement': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, TokenType.ANNOUNCE,
                      TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY,
                      TokenType.RUN, TokenType.VAR_INIT},
    
    # <statement>
    'statement': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, TokenType.ANNOUNCE,
                 TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY,
                 TokenType.RUN, TokenType.VAR_INIT},
    
    # <announce_statement>
    'announce_statement': {TokenType.ANNOUNCE},
    
    # <inbound_statement>
    'inbound_statement': {TokenType.INBOUND},
    
    # <dribble_statement>
    'dribble_statement': {TokenType.DRIBBLE},
    
    # <switch_statement>
    'switch_statement': {TokenType.SWITCH},
    
    # <forward_statement>
    'forward_statement': {TokenType.FORWARD},
    
    # <play_statement>
    'play_statement': {TokenType.PLAY},
    
    # <run_play_statement>
    'run_play_statement': {TokenType.RUN},
    
    # <follow_statement>
    'follow_statement': {TokenType.INCREMENT, TokenType.DECREMENT, TokenType.LEFT_PAREN, TokenType.ASSIGN, 
                        TokenType.ADD_ASSIGN, TokenType.SUB_ASSIGN, TokenType.MUL_ASSIGN, 
                        TokenType.DIV_ASSIGN, TokenType.MOD_ASSIGN, TokenType.ARRAY_INDEX_LEFT},

    # <element_index>
    'element_index': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
                     TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
                     TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <2d_manipulation>
    '2d_manipulation': {TokenType.ARRAY_INDEX_LEFT},
    
    # <array_man>
    'array_man': {TokenType.ASSIGN},
    
    # <array_elem>
    'array_elem': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
                  TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
                  TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <rebound_statement>
    'rebound_statement': {TokenType.REBOUND},
    
    # <otpt>
    'otpt': {TokenType.VAR_INIT, TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, 
            TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
    
    # <outputs>
    'outputs': {TokenType.VAR_INIT, TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, 
              TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
    
    # <other_outputs>
    'other_outputs': {TokenType.CHANT_CONCAT},
    
    # <literal>
    'literal': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
               TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},

    # <nega_feint_lit>
    'nega_feint_lit': {TokenType.NEGAFEINT},

    # <nega_floater_lit>
    'nega_floater_lit': {TokenType.NEGAFLOATER}, 
    
    # <expression>
    'expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
                  TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
                  TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <logical_expression>
    'logical_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
                          TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
                          TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <more_logical>
    'more_logical': {TokenType.AND_OP, TokenType.OR_OP},
    
    # <log_operator>
    'log_operator': {TokenType.AND_OP, TokenType.OR_OP},
    
    # <relational_expression>
    'relational_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
                             TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
                             TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <more_relational>
    'more_relational': {TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.NOT_EQUAL, 
                       TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL},
    
    # <arithmetic_expression>
    'arithmetic_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
                             TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
                             TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <more_term>
    'more_term': {TokenType.ADD, TokenType.SUB},
    
    # <term>
    'term': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
            TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
            TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <more_factor>
    'more_factor': {TokenType.MUL, TokenType.DIV, TokenType.MOD},
    
    # <factor>
    'factor': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
              TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
              TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <relational_operator>
    'relational_operator': {TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, 
                           TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <number_type_cast>
    'number_type_cast': {TokenType.FEINT, TokenType.FLOATER},
    
    # <feint_type_casting>
    'feint_type_casting': {TokenType.FEINT},
    
    # <floater_type_casting>
    'floater_type_casting': {TokenType.FLOATER},
    
    # <chant_type_casting>
    'chant_type_casting': {TokenType.CHANT},

    # <stat_type_casting>
        'stat_type_casting': {TokenType.STAT},
    
    # <assign_operand>
    'assign_operand': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
                      TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
                      TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <function_call>
    'function_call': {TokenType.VAR_INIT},
    
    # <arguments>
    'arguments': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
                 TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
                 TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <arg>
    'arg': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, TokenType.NEGAFLOATER,
           TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, TokenType.VAR_INIT, 
           TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, TokenType.FLOATER},
    
    # <more_args>
    'more_args': {TokenType.COMMA},
    
    # <inbound_statement>
    'inbound_statement': {TokenType.INBOUND},
    
    # <dribble_statement>
    'dribble_statement': {TokenType.DRIBBLE},
    
    # <add_condition>
    'add_condition': {TokenType.PASS, TokenType.SHOOT},
    
    # <loop_statements>
    'loop_statements': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                       TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                       TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                       TokenType.RESUME},
    
    # <loop_statement>
    'loop_statement': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                      TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                      TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                      TokenType.RESUME},
    
    # <switch_statement>
    'switch_statement': {TokenType.SWITCH},
    
    # <get_case>
    'get_case': {TokenType.GET},
    
    # <get_value>
    'get_value': {TokenType.FEINTLIT, TokenType.CHANTLIT},
    
    # <timeout_statement>
    'timeout_statement': {TokenType.TIMEOUT},
    
    # <get_case_end>
    'get_case_end': {TokenType.GET},
    
    # <get_default>
    'get_default': {TokenType.DEFAULT},
    
    # <forward_statement>
    'forward_statement': {TokenType.FORWARD},
    
    # <forward_lit>
    'forward_lit': {TokenType.FEINTLIT, TokenType.VAR_INIT},
    
    # <forward_inc_dec>
    'forward_inc_dec': {TokenType.INCREMENT, TokenType.DECREMENT, TokenType.ADD_ASSIGN, TokenType.SUB_ASSIGN},
    
    # <increment>
    'increment': {TokenType.INCREMENT},
    
    # <decrement>
    'decrement': {TokenType.DECREMENT},
    
    # <forward_assign_operator>
    'forward_assign_operator': {TokenType.ADD_ASSIGN, TokenType.SUB_ASSIGN},
    
    # <resume_statement>
    'resume_statement': {TokenType.RESUME},
    
    # <play_statement>
    'play_statement': {TokenType.PLAY},
    
    # <run_play_statement>
    'run_play_statement': {TokenType.RUN},
    
    # <team_block>
    'team_block': {TokenType.TEAM},
    
    # <local_decl>
    'local_decl': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, TokenType.ZONE},
    
    # <local_declaration>
    'local_declaration': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, TokenType.ZONE},
    
    # <typecast_value>
    'typecast_value': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT, TokenType.WIN, 
                      TokenType.LOSS, TokenType.VAR_INIT}
}