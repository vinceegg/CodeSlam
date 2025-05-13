from Analyzers.lexical_analyzer.tokens import TokenType

FOLLOW_SETS = {
    # <program>
    'program': {None},
    
    # <global_decl>
    'global_decl': {TokenType.WILT, TokenType.DUNK, TokenType.TEAM},
    
    # <global_declaration>
    'global_declaration': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                          TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                          TokenType.TEAM},
    
    # <variable_dec>
    'variable_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                    TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                    TokenType.TEAM, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                    TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                    TokenType.VAR_INIT},
                    
    # <feint_dec>
    'feint_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                 TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                 TokenType.TEAM, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                 TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                 TokenType.VAR_INIT},
                 
    # <more_feint>
    'more_feint': {TokenType.SEMICOLON, TokenType.COMMA},
    
    # <feint_init>
    'feint_init': {TokenType.SEMICOLON, TokenType.COMMA},
    
    # <feint_lit>
    'feint_lit': {TokenType.COMMA, TokenType.ASSIGN, TokenType.SEMICOLON, TokenType.ARRAY_INDEX_RIGHT,
                 TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB,
                 TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL,
                 TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL, TokenType.AND_OP, TokenType.OR_OP,
                 TokenType.RIGHT_PAREN, TokenType.CHANT_CONCAT, TokenType.COLON},
                 
    # <feint_init_end>
    'feint_init_end': {TokenType.SEMICOLON, TokenType.COMMA},
    
    # <floater_dec>
    'floater_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                   TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                   TokenType.TEAM, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                   TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                   TokenType.VAR_INIT},
                   
    # <more_floater>
    'more_floater': {TokenType.SEMICOLON, TokenType.COMMA},
    
    # <floater_init>
    'floater_init': {TokenType.SEMICOLON, TokenType.COMMA},
    
    # <floater_lit>
    'floater_lit': {TokenType.COMMA, TokenType.CODE_BLOCK_RIGHT, TokenType.MUL, TokenType.DIV, 
                   TokenType.MOD, TokenType.ADD, TokenType.SUB, TokenType.LESS_THAN, 
                   TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
                   TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
                   
    # <floater_init_end>
    'floater_init_end': {TokenType.SEMICOLON},
    
    # <chant_dec>
    'chant_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                 TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                 TokenType.TEAM, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                 TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                 TokenType.VAR_INIT},
                 
    # <more_chant>
    'more_chant': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <chant_init>
    'chant_init': {TokenType.COMMA, TokenType.SEMICOLON},

    # <chant_lit>
    'chant_lit': {TokenType.COMMA, TokenType.SEMICOLON, TokenType.MUL, TokenType.DIV,
                 TokenType.MOD, TokenType.ADD, TokenType.SUB, TokenType.LESS_THAN, TokenType.GREATER_THAN,
                 TokenType.EQUAL, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL, TokenType.AND_OP,
                 TokenType.OR_OP, TokenType.RIGHT_PAREN, TokenType.CHANT_CONCAT},
                  
    # <chant_init_end>
    'chant_init_end': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <stat_dec>
    'stat_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                TokenType.TEAM, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                TokenType.VAR_INIT},
                
    # <more_stat>
    'more_stat': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <stat_init>
    'stat_init': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <stat_value>
    'stat_value': {TokenType.COMMA, TokenType.SEMICOLON, TokenType.MUL, TokenType.DIV, 
                  TokenType.MOD, TokenType.ADD, TokenType.SUB, TokenType.LESS_THAN,
                  TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
                  TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL, TokenType.AND_OP, 
                  TokenType.OR_OP, TokenType.RIGHT_PAREN, TokenType.CHANT_CONCAT},
                  
    # <stat_init_end>
    'stat_init_end': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <const_dec>
    'const_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                 TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                 TokenType.TEAM},
                 
    # <const_feint>
    'const_feint': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                   TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                   TokenType.TEAM},
                   
    # <feint_const_init>
    'feint_const_init': {TokenType.SEMICOLON},
    
    # <feint_const>
    'feint_const': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <feint_const_end>
    'feint_const_end': {TokenType.SEMICOLON},
    
    # <const_floater>
    'const_floater': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                     TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                     TokenType.TEAM},
                     
    # <floater_const_init>
    'floater_const_init': {TokenType.SEMICOLON},
    
    # <floater_const>
    'floater_const': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <floater_const_end>
    'floater_const_end': {TokenType.SEMICOLON},
    
    # <const_chant>
    'const_chant': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                   TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                   TokenType.TEAM},
                   
    # <chant_const_init>
    'chant_const_init': {TokenType.SEMICOLON},
    
    # <chant_const>
    'chant_const': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <chant_const_end>
    'chant_const_end': {TokenType.SEMICOLON},
    
    # <const_stat>
    'const_stat': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                  TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                  TokenType.TEAM},
                  
    # <stat_const_init>
    'stat_const_init': {TokenType.SEMICOLON},
    
    # <stat_const>
    'stat_const': {TokenType.COMMA, TokenType.SEMICOLON},
    
    # <stat_const_end>
    'stat_const_end': {TokenType.SEMICOLON},
    
    # <array_dec>
    'array_dec': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                 TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                 TokenType.TEAM, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                 TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                 TokenType.VAR_INIT, TokenType.REBOUND},
                 
    # <feint_array>
    'feint_array': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                   TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                   TokenType.TEAM, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                   TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                   TokenType.VAR_INIT, TokenType.REBOUND},
                   
    # <array_size>
    'array_size': {TokenType.ARRAY_INDEX_RIGHT, TokenType.ARRAY_INDEX_LEFT},
    
    # <2D_array>
    '2D_array': {TokenType.ASSIGN, TokenType.SEMICOLON},
    
    # <feint_array_init>
    'feint_array_init': {TokenType.SEMICOLON},
    
    # <feint_row>
    'feint_row': {TokenType.CODE_BLOCK_RIGHT},
    
    # <2D_feint_row>
    '2D_feint_row': {TokenType.CODE_BLOCK_RIGHT},
    
    # <more_feint_lit>
    'more_feint_lit': {TokenType.CODE_BLOCK_RIGHT, TokenType.COMMA},
    
    # <floater_array>
    'floater_array': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                     TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                     TokenType.TEAM, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                     TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                     TokenType.VAR_INIT, TokenType.REBOUND},
    
    # <floater_array_init>
    'floater_array_init': {TokenType.SEMICOLON},
    
    # <floater_row>
    'floater_row': {TokenType.CODE_BLOCK_RIGHT},
    
    # <2D_floater_row>
    '2D_floater_row': {TokenType.CODE_BLOCK_RIGHT},
    
    # <more_floater_lit>
    'more_floater_lit': {TokenType.CODE_BLOCK_RIGHT, TokenType.COMMA},
    
    # <chant_array>
    'chant_array': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                   TokenType.CONST, TokenType.ZONE, TokenType.WILT, TokenType.DUNK, 
                   TokenType.TEAM, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                   TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN,
                   TokenType.VAR_INIT, TokenType.REBOUND},
    
    # <chant_array_init>
    'chant_array_init': {TokenType.SEMICOLON},
    
    # <chant_row>
    'chant_row': {TokenType.CODE_BLOCK_RIGHT},
    
    # <2D_chant_row>
    '2D_chant_row': {TokenType.CODE_BLOCK_RIGHT},
    
    # <more_chant_lit>
    'more_chant_lit': {TokenType.CODE_BLOCK_RIGHT, TokenType.COMMA},
    
    # <function_def>
    'function_def': {TokenType.TEAM},
    
    # <function_declared>
    'function_declared': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <dunk_func_declared>
    'dunk_func_declared': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <feint_function>
    'feint_function': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <floater_function>
    'floater_function': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <chant_function>
    'chant_function': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <stat_function>
    'stat_function': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <dunk_function>
    'dunk_function': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <func_parameters>
    'func_parameters': {TokenType.CODE_BLOCK_RIGHT},
    
    # <param_end>
    'param_end': {TokenType.CODE_BLOCK_RIGHT},
    
    # <decl>
    'decl': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
            TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
            TokenType.REBOUND},
    
    # <declarations>
    'declarations': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                    TokenType.ZONE, TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE,
                    TokenType.SWITCH, TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, 
                    TokenType.VAR_INIT, TokenType.REBOUND},

    # <function_statement>
    'function_statement': {TokenType.REBOUND, TokenType.CODE_BLOCK_RIGHT},
    
    # <rebound_statement>
    'rebound_statement': {TokenType.CODE_BLOCK_RIGHT},
    
    # <statement>
    'statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                TokenType.RESUME, TokenType.TIMEOUT, TokenType.TEAM},
    
    # <follow_statement>
    'follow_statement': {TokenType.SEMICOLON},
    
    # <assign_operand>
    'assign_operand': {TokenType.SEMICOLON},
    
    # <element_index>
    'element_index': {TokenType.ARRAY_INDEX_RIGHT},
    
    # <2d_manipulation>
    '2d_manipulation': {TokenType.SEMICOLON, TokenType.ASSIGN},
    
    # <array_man>
    'array_man': {TokenType.SEMICOLON},
    
    # <array_elem>
    'array_elem': {TokenType.ASSIGN, TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, 
                  TokenType.SUB, TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, 
                  TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL, TokenType.SEMICOLON},
    
    # <expression>
    'expression': {TokenType.SEMICOLON, TokenType.RIGHT_PAREN, TokenType.COMMA, TokenType.CHANT_CONCAT, TokenType.MUL, TokenType.DIV,
                  TokenType.MOD, TokenType.ADD, TokenType.SUB, TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL,
                  TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <logical_expression>
    'logical_expression': {TokenType.SEMICOLON, TokenType.RIGHT_PAREN, TokenType.COMMA, TokenType.CHANT_CONCAT, TokenType.MUL, TokenType.DIV,
                  TokenType.MOD, TokenType.ADD, TokenType.SUB, TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL,
                  TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <more_logical>
    'more_logical': {TokenType.SEMICOLON, TokenType.RIGHT_PAREN, TokenType.COMMA, TokenType.CHANT_CONCAT, TokenType.MUL, TokenType.DIV,
                  TokenType.MOD, TokenType.ADD, TokenType.SUB, TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL,
                  TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <log_operator>
    'log_operator': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, 
                    TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, 
                    TokenType.VAR_INIT, TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, 
                    TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <relational_expression>
    'relational_expression': {TokenType.AND_OP, TokenType.OR_OP, TokenType.SEMICOLON, 
                             TokenType.RIGHT_PAREN, TokenType.COMMA, TokenType.CHANT_CONCAT},
    
    # <more_relational>
    'more_relational': {TokenType.AND_OP, TokenType.OR_OP, TokenType.SEMICOLON, TokenType.RIGHT_PAREN, 
                       TokenType.COMMA, TokenType.CHANT_CONCAT},
    
    # <arithmetic_expression>
    'arithmetic_expression': {TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, 
                             TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <more_term>
    'more_term': {TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
                 TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <term>
    'term': {TokenType.ADD, TokenType.SUB, TokenType.LESS_THAN, TokenType.GREATER_THAN, 
            TokenType.EQUAL, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <more_factor>
    'more_factor': {TokenType.ADD, TokenType.SUB, TokenType.LESS_THAN, TokenType.GREATER_THAN, 
                   TokenType.EQUAL, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <factor>
    'factor': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB, 
              TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
              TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <literal>
    'literal': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB, 
               TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
               TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <nega_feint_lit>
    'nega_feint_lit': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB, 
                      TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
                      TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL, TokenType.CODE_BLOCK_LEFT, 
                      TokenType.SEMICOLON, TokenType.RIGHT_PAREN, TokenType.CODE_BLOCK_RIGHT, 
                      TokenType.COLON, TokenType.AND_OP, TokenType.OR_OP, TokenType.ARRAY_INDEX_RIGHT, 
                      TokenType.CHANT_CONCAT},
    
    # <nega_floater_lit>
    'nega_floater_lit': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB, 
                        TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
                        TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL, TokenType.CODE_BLOCK_LEFT, 
                        TokenType.SEMICOLON, TokenType.RIGHT_PAREN, TokenType.CODE_BLOCK_RIGHT, 
                        TokenType.COLON, TokenType.AND_OP, TokenType.OR_OP, TokenType.CHANT_CONCAT},
    
    # <follow_factor>
    'follow_factor': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB, 
                     TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
                     TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <function_call>
    'function_call': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB, 
                     TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
                     TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL, TokenType.SEMICOLON},
    
    # <arguments>
    'arguments': {TokenType.RIGHT_PAREN},
    
    # <arg>
    'arg': {TokenType.COMMA, TokenType.RIGHT_PAREN},
    
    # <more_args>
    'more_args': {TokenType.RIGHT_PAREN},
    
    # <relational_operator>
    'relational_operator': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGAFEINT, 
                           TokenType.NEGAFLOATER, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS, 
                           TokenType.VAR_INIT, TokenType.LEFT_PAREN, TokenType.NOT_OP, TokenType.FEINT, 
                           TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
    
    # <type_casting>
    'type_casting': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB, 
                    TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
                    TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <typecast_value>
    'typecast_value': {TokenType.MUL, TokenType.DIV, TokenType.MOD, TokenType.ADD, TokenType.SUB, 
                      TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, TokenType.LESS_EQUAL, 
                      TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL},
    
    # <announce_statement>
    'announce_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                          TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                          TokenType.RESUME, TokenType.TIMEOUT, TokenType.TEAM},
    
    # <otpt>
    'otpt': {TokenType.RIGHT_PAREN},
    
    # <outputs>
    'outputs': {TokenType.CHANT_CONCAT, TokenType.RIGHT_PAREN},
    
    # <other_outputs>
    'other_outputs': {TokenType.RIGHT_PAREN},
    
    # <inbound_statement>
    'inbound_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                         TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                         TokenType.RESUME, TokenType.TIMEOUT, TokenType.TEAM},
    
    # <dribble_statement>
    'dribble_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                         TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                         TokenType.RESUME, TokenType.TIMEOUT, TokenType.TEAM},
    
    # <add_condition>
    'add_condition': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                     TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                     TokenType.RESUME, TokenType.TIMEOUT, TokenType.TEAM},
    
    # <loop_statements>
    'loop_statements': {TokenType.CODE_BLOCK_RIGHT},
    
    # <loop_statement>
    'loop_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                      TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                      TokenType.RESUME, TokenType.TIMEOUT},
    
    # <timeout_statement>
    'timeout_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                         TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                         TokenType.RESUME, TokenType.TIMEOUT},
    
    # <switch_statement>
    'switch_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                        TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                        TokenType.RESUME, TokenType.TIMEOUT, TokenType.TEAM},
    
    # <get_case>
    'get_case': {TokenType.DEFAULT, TokenType.RIGHT_PAREN},
    
    # <get_value>
    'get_value': {TokenType.COLON},
    
    # <get_case_end>
    'get_case_end': {TokenType.DEFAULT, TokenType.RIGHT_PAREN},
    
    # <get_default>
    'get_default': {TokenType.CODE_BLOCK_RIGHT},
    
    # <forward_statement>
    'forward_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                         TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                         TokenType.RESUME, TokenType.TIMEOUT, TokenType.TEAM},
    
    # <forward_lit>
    'forward_lit': {TokenType.SEMICOLON},
    
    # <forward_inc_dec>
    'forward_inc_dec': {TokenType.RIGHT_PAREN},
    
    # <increment>
    'increment': {TokenType.RIGHT_PAREN},
    
    # <decrement>
    'decrement': {TokenType.RIGHT_PAREN},
    
    # <forward_assign_operator>
    'forward_assign_operator': {TokenType.FEINTLIT, TokenType.VAR_INIT},
    
    # <resume_statement>
    'resume_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                        TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                        TokenType.RESUME, TokenType.TIMEOUT},
    
    # <play_statement>
    'play_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                      TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                      TokenType.RESUME, TokenType.TIMEOUT, TokenType.TEAM},
    
    # <run_play_statement>
    'run_play_statement': {TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH, 
                          TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.VAR_INIT, 
                          TokenType.RESUME, TokenType.TIMEOUT, TokenType.TEAM},
    
    # <team_block>
    'team_block': {None},
    
    # <team_statement>
    'team_statement': {TokenType.TIMEOUT}

}