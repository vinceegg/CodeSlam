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
    'more_feint': {TokenType.ASSIGN},
    # <feint_init>
    'feint_init': {TokenType.ASSIGN},
    # <feint_init_end>
    'feint_init_end': {TokenType.COMMA},
    # <feint_lit>
    'feint_lit': {TokenType.FEINTLIT},
    # <floater_dec>
    'floater_dec': {TokenType.FLOATER},
    # <more_floater>
    'more_floater': {TokenType.ASSIGN},
    # <floater_init>
    'floater_init': {TokenType.ASSIGN},
    # <floater_init_end>
    'floater_init_end': {TokenType.COMMA},
    # <floater_lit>
    'floater_lit': {TokenType.FLOATERLIT},
    # <chant_dec>
    'chant_dec': {TokenType.CHANT},
    # <more_chant>
    'more_chant': {TokenType.ASSIGN},
    # <chant_init>
    'chant_init': {TokenType.ASSIGN},
    # <chant_init_end>
    'chant_init_end': {TokenType.COMMA},
    # <chant_lit>
    'chant_lit': {TokenType.CHANTLIT},
    # <stat_dec>
    'stat_dec': {TokenType.STAT},
    # <more_stat>
    'more_stat': {TokenType.ASSIGN},
    # <stat_init>
    'stat_init': {TokenType.ASSIGN},
    # <stat_value>
    'stat_value': {TokenType.WIN, TokenType.LOSS},
    # <stat_init_end>
    'stat_init_end': {TokenType.COMMA},
    # <const_dec>
    'const_dec': {TokenType.CONST},
    # <const_feint>
    'const_feint': {TokenType.FEINT},
    # <feint_const_init>
    'feint_const_init': {TokenType.ASSIGN},
    # <feint_const>
    'feint_const': {TokenType.ASSIGN},
    # <feint_const_end>
    'feint_const_end': {TokenType.COMMA},
    # <const_floater>
    'const_floater': {TokenType.FLOATER},
    # <floater_const_init>
    'floater_const_init': {TokenType.ASSIGN},
    # <floater_const>
    'floater_const': {TokenType.ASSIGN},
    # <floater_const_end>
    'floater_const_end': {TokenType.COMMA},
    # <const_chant>
    'const_chant': {TokenType.CHANT},
    # <chant_const_init>
    'chant_const_init': {TokenType.ASSIGN},
    # <chant_const>
    'chant_const': {TokenType.ASSIGN},
    # <chant_const_end>
    'chant_const_end': {TokenType.COMMA},
    # <const_stat>
    'const_stat': {TokenType.STAT},
    # <stat_const_init>
    'stat_const_init': {TokenType.ASSIGN},
    # <stat_const>
    'stat_const': {TokenType.ASSIGN},
    # <stat_const_end>
    'stat_const_end': {TokenType.COMMA},
    # <array_dec>
    'array_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT},
    # <feint_array>
    'feint_array': {TokenType.FEINT},
    # <2D_array>
    '2D_array': {TokenType.ARRAY_INDEX_LEFT},
    # <feint_array_init>
    'feint_array_init': {TokenType.ASSIGN},
    # <feint_row>
    'feint_row': {TokenType.FEINTLIT, TokenType.CODE_BLOCK_LEFT},
    # <2d_feint_row>
    '2d_feint_row': {TokenType.COMMA},
    # <more_feint_lit>
    'more_feint_lit': {TokenType.COMMA},
    # <floater_array>
    'floater_array': {TokenType.FLOATER},
    # <floater_array_init>
    'floater_array_init': {TokenType.ASSIGN},
    # <floater_row>
    'floater_row': {TokenType.FLOATERLIT, TokenType.CODE_BLOCK_LEFT},
    # <2d_floater_row>
    '2d_floater_row': {TokenType.COMMA},
    # <more_floater_lit>
    'more_floater_lit': {TokenType.COMMA},
    # <chant_array>
    'chant_array': {TokenType.CHANT},   
    # <chant_array_init>
    'chant_array_init': {TokenType.ASSIGN},
    # <chant_row>
    'chant_row': {TokenType.CHANTLIT, TokenType.CODE_BLOCK_LEFT},
    # <2d_chant_row>
    '2d_chant_row': {TokenType.COMMA},  
    # <more_chant_lit>
    'more_chant_lit': {TokenType.COMMA},
    # <function_decl>
    'function_decl': {TokenType.WILT, TokenType.DUNK},
    # <function_declared>
    'function_declared': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    # <dunk_func_declared>
    'dunk_func_declared': {TokenType.VAR_INIT},
    # <feint_function>
    'feint_function': {TokenType.FEINT},
    # <dunk_function>
    'dunk_function': {TokenType.VAR_INIT},
    # <function_def>
    'function_def': {TokenType.WILT, TokenType.DUNK},
    # <function_defined>
    'function_defined': {TokenType.VAR_INIT},
    # <func_parameters>
    'func_parameters': {TokenType.VAR_INIT},
    # <param>
    'param': {TokenType.VAR_INIT},
    # <params>
    'params': {TokenType.COMMA},
    # <function_statements>
    'function_statements': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT,
                           TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH,
                           TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.TIMEOUT,
                           TokenType.RESUME, TokenType.VAR_INIT, TokenType.LEFT_PAREN, TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NOT_OP, TokenType.NEGAFEINT, TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
    # <team_block>
    'team_block': {TokenType.TEAM},
    # <statement>
    'statement': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT,
                 TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH,
                 TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.TIMEOUT,
                 TokenType.RESUME, TokenType.VAR_INIT},
    # <expression>
    'expression': {TokenType.LEFT_PAREN, TokenType.FEINTLIT, TokenType.FLOATERLIT,
                  TokenType.VAR_INIT, TokenType.NOT_OP, TokenType.NEGAFEINT, TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
    # <variable_dec>
    'variable_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    # <array_dec>
    'array_dec': {TokenType.ZONE},
    # <const_dec>
    'const_dec': {TokenType.CONST},
    # Additional FIRST sets based on the CFG
    # <rebound_statement>
    'rebound_statement': {TokenType.REBOUND},
    # <announce_statement>
    'announce_statement': {TokenType.ANNOUNCE},
    # <outputs>
    'outputs': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT, 
               TokenType.LEFT_PAREN, TokenType.VAR_INIT, TokenType.WIN, TokenType.LOSS},
    # <output>
    'output': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT, 
              TokenType.LEFT_PAREN, TokenType.VAR_INIT, TokenType.WIN, TokenType.LOSS},
    # <other_outputs>
    'other_outputs': {TokenType.CHANT_CONCAT},
    # <literal>
    'literal': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, 
               TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
    # <nega_feint_lit>
    'nega_feint_lit': {TokenType.NEGAFEINT},
    # <nega_floater_lit>
    'nega_floater_lit': {TokenType.NEGAFLOATER},
    # <arithmetic_expression>
    'arithmetic_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                             TokenType.NEGAFEINT, TokenType.NEGAFLOATER, TokenType.LEFT_PAREN,
                             TokenType.FEINT, TokenType.FLOATER},
    # <arith_term>
    'arith_term': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                  TokenType.NEGAFEINT, TokenType.NEGAFLOATER, TokenType.LEFT_PAREN,
                  TokenType.FEINT, TokenType.FLOATER},
    # <number>
    'number': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
              TokenType.NEGAFEINT, TokenType.NEGAFLOATER},
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
    # <more_arith_term>
    'more_arith_term': {TokenType.ADD, TokenType.SUB, TokenType.MUL, TokenType.DIV, TokenType.MOD},
    # <relational_expression>
    'relational_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                            TokenType.NEGAFEINT, TokenType.NEGAFLOATER, TokenType.LEFT_PAREN,
                            TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT,
                            TokenType.WIN, TokenType.LOSS, TokenType.CHANTLIT},
    # <relational_operand>
    'relational_operand': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                          TokenType.NEGAFEINT, TokenType.NEGAFLOATER, TokenType.FEINT, 
                          TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    # <relational_operator>
    'relational_operator': {TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, 
                          TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    # <other_relational_operator>
    'other_relational_operator': {TokenType.EQUAL, TokenType.NOT_EQUAL},
    # <logical_expression>
    'logical_expression': {TokenType.NOT_OP, TokenType.LEFT_PAREN, TokenType.FEINTLIT, 
                         TokenType.FLOATERLIT, TokenType.VAR_INIT, TokenType.NEGAFEINT, 
                         TokenType.NEGAFLOATER, TokenType.FEINT, TokenType.FLOATER, 
                         TokenType.CHANT, TokenType.STAT, TokenType.WIN, TokenType.LOSS, 
                         TokenType.CHANTLIT},
    # <logic_term>
    'logic_term': {TokenType.NOT_OP, TokenType.LEFT_PAREN, TokenType.FEINTLIT, 
                  TokenType.FLOATERLIT, TokenType.VAR_INIT, TokenType.NEGAFEINT, 
                  TokenType.NEGAFLOATER, TokenType.FEINT, TokenType.FLOATER, 
                  TokenType.CHANT, TokenType.STAT, TokenType.WIN, TokenType.LOSS, 
                  TokenType.CHANTLIT},
    # <more_logic_term>
    'more_logic_term': {TokenType.AND_OP, TokenType.OR_OP},
    # <assignment_expression>
    'assignment_expression': {TokenType.VAR_INIT},
    # <assign_operator>
    'assign_operator': {TokenType.ASSIGN, TokenType.ADD_ASSIGN, TokenType.SUB_ASSIGN, 
                      TokenType.MUL_ASSIGN, TokenType.DIV_ASSIGN, TokenType.MOD_ASSIGN},
    # <assign_operand>
    'assign_operand': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                      TokenType.NEGAFEINT, TokenType.NEGAFLOATER, TokenType.LEFT_PAREN,
                      TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                      TokenType.WIN, TokenType.LOSS, TokenType.CHANTLIT, TokenType.NOT_OP},
    # <function_call>
    'function_call': {TokenType.VAR_INIT},
    # <arguments>
    'arguments': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, 
                 TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, 
                 TokenType.LOSS, TokenType.VAR_INIT},
    # <arg>
    'arg': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, 
           TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, 
           TokenType.LOSS, TokenType.VAR_INIT},
    # <more_args>
    'more_args': {TokenType.COMMA},
    # <inbound_statement>
    'inbound_statement': {TokenType.INBOUND},
    # <inputs>
    'inputs': {TokenType.CHANTLIT},
    # <input>
    'input': {TokenType.CHANTLIT},
    # <id_input>
    'id_input': {TokenType.COMMA},
    # <dribble_statement>
    'dribble_statement': {TokenType.DRIBBLE},
    # <condition>
    'condition': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                 TokenType.NEGAFEINT, TokenType.NEGAFLOATER, TokenType.LEFT_PAREN,
                 TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                 TokenType.WIN, TokenType.LOSS, TokenType.CHANTLIT, TokenType.NOT_OP},
    # <pass_statement>
    'pass_statement': {TokenType.PASS},
    # <shoot_statement>
    'shoot_statement': {TokenType.SHOOT},
    # <switch_statement>
    'switch_statement': {TokenType.SWITCH},
    # <get_case>
    'get_case': {TokenType.GET},
    # <get_value>
    'get_value': {TokenType.FEINTLIT, TokenType.CHANTLIT},
    # <get_case_end>
    'get_case_end': {TokenType.GET},
    # <get_default>
    'get_default': {TokenType.DEFAULT},
    # <forward_statement>
    'forward_statement': {TokenType.FORWARD},
    # <forward_lit>
    'forward_lit': {TokenType.FEINTLIT, TokenType.VAR_INIT},
    # <forward_inc_dec>
    'forward_inc_dec': {TokenType.VAR_INIT, TokenType.INCREMENT, TokenType.DECREMENT},
    # <increment>
    'increment': {TokenType.VAR_INIT, TokenType.INCREMENT},
    # <decrement>
    'decrement': {TokenType.VAR_INIT, TokenType.DECREMENT},
    # <resume_statement>
    'resume_statement': {TokenType.RESUME},
    # <play_statement>
    'play_statement': {TokenType.PLAY},
    # <run_play_statement>
    'run_play_statement': {TokenType.RUN},
    # <local_decl>
    'local_decl': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                  TokenType.CONST, TokenType.ZONE},
    # <local_declaration>
    'local_declaration': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                         TokenType.CONST, TokenType.ZONE},
    # <array_manipulation>
    'array_manipulation': {TokenType.VAR_INIT},
    # <element_index>
    'element_index': {TokenType.FEINTLIT},
    # <2d_manipulation>
    '2d_manipulation': {TokenType.ARRAY_INDEX_LEFT},
    # <array_man>
    'array_man': {TokenType.ASSIGN},
    # <array_elem>
    'array_elem': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT},
    # <array_access>
    'array_access': {TokenType.VAR_INIT},
    # <feint_typecast_value>
    'feint_typecast_value': {TokenType.FLOATERLIT, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
    # <floater_typecast_value>
    'floater_typecast_value': {TokenType.FEINTLIT, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
    # <chant_typecast_value>
    'chant_typecast_value': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.WIN, TokenType.LOSS},
    # <stat_typecast_value>
    'stat_typecast_value': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT},
    # <other_statements>
    'other_statements': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT,
                        TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH,
                        TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.TIMEOUT,
                        TokenType.RESUME, TokenType.VAR_INIT, TokenType.LEFT_PAREN, TokenType.FEINTLIT, 
                        TokenType.FLOATERLIT, TokenType.NOT_OP},
    # <other_type_cast>
    'other_type_cast': {TokenType.CHANT, TokenType.STAT}
} 