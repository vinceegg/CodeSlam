from Analyzers.lexical_analyzer.tokens import TokenType, Token
from typing import List, Optional
from Analyzers.syntax_analyzer.errors import SyntaxError 

# class SyntaxError(Exception):
#     """Custom exception for syntax errors"""
#     def __init__(self, message, line_number=None, column=None):
#         super().__init__(message)
#         self.line_number = line_number
#         self.column = column

class Parser:
    # Define First Sets as class variables
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
        # <feint_parameters>  
        'feint_parameters': {TokenType.FEINT},
        # <feint_param>
        'feint_param': {TokenType.FEINT},
        # <feint_params>
        'feint_params': {TokenType.COMMA},
        # <floater_function>
        'floater_function': {TokenType.FLOATER},
        # <floater_parameters>
        'floater_parameters': {TokenType.FLOATER},
        # <floater_param>
        'floater_param': {TokenType.FLOATER},
        # <floater_params>
        'floater_params': {TokenType.COMMA},
        # <chant_function>
        'chant_function': {TokenType.CHANT},
        # <chant_parameters>
        'chant_parameters': {TokenType.CHANT},
        # <chant_param>
        'chant_param': {TokenType.CHANT},
        # <chant_params>
        'chant_params': {TokenType.COMMA},  
        # <stat_function>
        'stat_function': {TokenType.STAT},
        # <stat_parameters>
        'stat_parameters': {TokenType.STAT},
        # <stat_param>
        'stat_param': {TokenType.STAT},
        # <stat_params>
        'stat_params': {TokenType.COMMA},
        # <dunk_function>
        'dunk_function': {TokenType.VAR_INIT},
        # <dunk_parameters>
        'dunk_parameters': {TokenType.VAR_INIT},
        # <dunk_param>
        'dunk_param': {TokenType.VAR_INIT},
        # <dunk_params>
        'dunk_params': {TokenType.COMMA},
        # <function_def>
        'function_def': {TokenType.WILT, TokenType.DUNK},
        # <function_defined>
        'function_defined': {TokenType.VAR_INIT},
        # <function_param>
        'function_param': {TokenType.VAR_INIT},
        # <param>
        'param': {TokenType.VAR_INIT},
        # <params>
        'params': {TokenType.COMMA},
        # <function_statements>
        'function_statements': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT,
                               TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH,
                               TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.TIMEOUT,
                               TokenType.RESUME, TokenType.VAR_INIT, TokenType.LEFT_PAREN, TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NOT_OP, TokenType.NEGA_FEINTLIT, TokenType.NEGA_FLOATERLIT, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
        # <team_block>
        'team_block': {TokenType.TEAM},
        # <statement>
        'statement': {TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT,
                     TokenType.ANNOUNCE, TokenType.INBOUND, TokenType.DRIBBLE, TokenType.SWITCH,
                     TokenType.FORWARD, TokenType.PLAY, TokenType.RUN, TokenType.TIMEOUT,
                     TokenType.RESUME, TokenType.VAR_INIT},
        # <expression>
        'expression': {TokenType.LEFT_PAREN, TokenType.FEINTLIT, TokenType.FLOATERLIT,
                      TokenType.VAR_INIT, TokenType.NOT_OP, TokenType.NEGA_FEINTLIT, TokenType.NEGA_FLOATERLIT, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
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
        'other_outputs': {TokenType.AMPERSAND},
        # <literal>
        'literal': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGA_FEINTLIT, 
                   TokenType.NEGA_FLOATERLIT, TokenType.CHANTLIT, TokenType.WIN, TokenType.LOSS},
        # <nega_feint_lit>
        'nega_feint_lit': {TokenType.NEGA_FEINTLIT},
        # <nega_floater_lit>
        'nega_floater_lit': {TokenType.NEGA_FLOATERLIT},
        # <arithmetic_expression>
        'arithmetic_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                                 TokenType.NEGA_FEINTLIT, TokenType.NEGA_FLOATERLIT, TokenType.LEFT_PAREN,
                                 TokenType.FEINT, TokenType.FLOATER},
        # <arith_term>
        'arith_term': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                      TokenType.NEGA_FEINTLIT, TokenType.NEGA_FLOATERLIT, TokenType.LEFT_PAREN,
                      TokenType.FEINT, TokenType.FLOATER},
        # <number>
        'number': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                  TokenType.NEGA_FEINTLIT, TokenType.NEGA_FLOATERLIT},
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
        'more_arith_term': {TokenType.PLUS, TokenType.MINUS, TokenType.MULT, TokenType.DIV, TokenType.MOD},
        # <relational_expression>
        'relational_expression': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                                TokenType.NEGA_FEINTLIT, TokenType.NEGA_FLOATERLIT, TokenType.LEFT_PAREN,
                                TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT,
                                TokenType.WIN, TokenType.LOSS, TokenType.CHANTLIT},
        # <relational_operand>
        'relational_operand': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                              TokenType.NEGA_FEINTLIT, TokenType.NEGA_FLOATERLIT, TokenType.FEINT, 
                              TokenType.FLOATER, TokenType.CHANT, TokenType.STAT},
        # <relational_operator>
        'relational_operator': {TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUALS, 
                              TokenType.LESS_THAN_EQUAL, TokenType.GREATER_THAN_EQUAL, TokenType.NOT_EQUALS},
        # <other_relational_operator>
        'other_relational_operator': {TokenType.EQUALS, TokenType.NOT_EQUALS},
        # <logical_expression>
        'logical_expression': {TokenType.NOT_OP, TokenType.LEFT_PAREN, TokenType.FEINTLIT, 
                             TokenType.FLOATERLIT, TokenType.VAR_INIT, TokenType.NEGA_FEINTLIT, 
                             TokenType.NEGA_FLOATERLIT, TokenType.FEINT, TokenType.FLOATER, 
                             TokenType.CHANT, TokenType.STAT, TokenType.WIN, TokenType.LOSS, 
                             TokenType.CHANTLIT},
        # <logic_term>
        'logic_term': {TokenType.NOT_OP, TokenType.LEFT_PAREN, TokenType.FEINTLIT, 
                      TokenType.FLOATERLIT, TokenType.VAR_INIT, TokenType.NEGA_FEINTLIT, 
                      TokenType.NEGA_FLOATERLIT, TokenType.FEINT, TokenType.FLOATER, 
                      TokenType.CHANT, TokenType.STAT, TokenType.WIN, TokenType.LOSS, 
                      TokenType.CHANTLIT},
        # <more_logic_term>
        'more_logic_term': {TokenType.AND_OP, TokenType.OR_OP},
        # <assignment_expression>
        'assignment_expression': {TokenType.VAR_INIT},
        # <assign_operator>
        'assign_operator': {TokenType.ASSIGN, TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN, 
                          TokenType.MULT_ASSIGN, TokenType.DIV_ASSIGN, TokenType.MOD_ASSIGN},
        # <assign_operand>
        'assign_operand': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.VAR_INIT, 
                          TokenType.NEGA_FEINTLIT, TokenType.NEGA_FLOATERLIT, TokenType.LEFT_PAREN,
                          TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT, 
                          TokenType.WIN, TokenType.LOSS, TokenType.CHANTLIT, TokenType.NOT_OP},
        # <function_call>
        'function_call': {TokenType.VAR_INIT},
        # <arguments>
        'arguments': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGA_FEINTLIT, 
                     TokenType.NEGA_FLOATERLIT, TokenType.CHANTLIT, TokenType.WIN, 
                     TokenType.LOSS, TokenType.VAR_INIT},
        # <arg>
        'arg': {TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.NEGA_FEINTLIT, 
               TokenType.NEGA_FLOATERLIT, TokenType.CHANTLIT, TokenType.WIN, 
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
                     TokenType.NEGA_FEINTLIT, TokenType.NEGA_FLOATERLIT, TokenType.LEFT_PAREN,
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

    # def __init__(self, tokens: List[Token]):
    #     self.tokens = tokens
    #     self.current = 0
    #     self.current_token = self.tokens[0] if tokens else None
    #     self.line_number = 1  # Track line numbers
    #     self.column = 0      # Track column position
    #     self.expected_tokens = set()  # Add this to track expected tokens
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.current_token = self.tokens[0] if tokens else None
        self.line_number = 1
        self.column = 0
        self.expected_tokens = set()
        self.line_starts = {1: 0}  # Track the starting position of each line
        self.current_line_content = ""  # Track content of current line

    # def skip_whitespace_and_comments(self):
    #     """Helper method to skip whitespace, newlines and comments"""
    #     while self.current_token and self.current_token.type in [
    #         TokenType.SPACE,
    #         TokenType.TAB,
    #         TokenType.NEWLINE,
    #         TokenType.COMMENT,
    #         TokenType.MULTI_COMMENT
    #     ]:
    #         self.advance()
    def skip_whitespace_and_comments(self):
        """Helper method to skip whitespace, newlines and comments"""
        while self.current_token and self.current_token.type in [
            TokenType.SPACE,
            TokenType.TAB,
            TokenType.NEWLINE,
            TokenType.COMMENT,
            TokenType.MULTI_COMMENT
        ]:
            # Update position tracking for whitespace/comments
            if self.current_token.type == TokenType.NEWLINE:
                self.line_number += 1
                self.column = 0
                self.line_starts[self.line_number] = 0
                self.current_line_content = ""
            elif self.current_token.type in [TokenType.SPACE, TokenType.TAB]:
                # Add spaces to line content
                self.current_line_content += " " * (1 if self.current_token.type == TokenType.TAB else 1)
                
            self.current += 1
            if self.current < len(self.tokens):
                self.current_token = self.tokens[self.current]
            else:
                self.current_token = None
                break

    # ADDED
    def update_position(self, token):
        """Update line and column position based on token content"""
        if token.type == TokenType.NEWLINE:
            self.line_number += 1
            self.column = 0
            self.line_starts[self.line_number] = 0
            self.current_line_content = ""
        else:
            # Only update column for non-whitespace tokens
            if token.type not in [TokenType.SPACE, TokenType.TAB]:
                token_value = token.value if hasattr(token, 'value') and token.value else ""
                self.column = len(self.current_line_content)
                self.current_line_content += token_value

    # def advance(self) -> None:
    #     """Advance to next token and update position tracking"""
    #     self.current += 1
    #     if self.current < len(self.tokens):
    #         self.current_token = self.tokens[self.current]
    #         # Update line and column based on token position
    #         if hasattr(self.current_token, 'line'):
    #             self.line_number = self.current_token.line
    #         if hasattr(self.current_token, 'column'):
    #             self.column = self.current_token.column
    #         # Skip any whitespace or comments after advancing
    #         self.skip_whitespace_and_comments()
    #     else:
    #         self.current_token = None
    def advance(self) -> None:
        """Advance to next token and update position tracking"""
        if self.current_token:
            self.update_position(self.current_token)
            
        self.current += 1
        if self.current < len(self.tokens):
            self.current_token = self.tokens[self.current]
            # Skip any whitespace or comments after advancing
            self.skip_whitespace_and_comments()
        else:
            self.current_token = None

    def peek(self) -> Optional[Token]:
        """Look at next token without advancing"""
        if self.current + 1 >= len(self.tokens):
            return None
        return self.tokens[self.current + 1]

    def match(self, expected_type: TokenType) -> bool:
        """Check if current token matches expected type"""
        if self.current_token and self.current_token.type == expected_type:
            self.advance()
            return True
        return False

    # def expect(self, token_type: TokenType) -> None:
    #     """Expect a specific token type, raise error if not found"""
    #     if self.current_token and self.current_token.type == token_type and \
    #        self.current_token.value.upper() == token_type.value.upper():  # Make case-insensitive comparison
    #         self.advance()
    #     else:
    #         self.expected_tokens.add(token_type)
    #         raise SyntaxError(
    #             f"Expected Token: {{{', '.join(t.value for t in self.expected_tokens)}}}, "
    #             f"Unexpected Token: {self.current_token.value if self.current_token else 'EOF'}",
    #             self.line_number,
    #             self.column
    #         )
    def expect(self, token_type: TokenType) -> None:
        """Expect a specific token type, raise error if not found"""
        # Calculate exact column position for potential error
        error_column = self.column
        
        if self.current_token and self.current_token.type == token_type and \
        self.current_token.value.upper() == token_type.value.upper():
            self.advance()
        else:
            self.expected_tokens.add(token_type)
            expected_tokens_str = ', '.join(t.value for t in self.expected_tokens)
            unexpected_token = self.current_token.value if self.current_token else 'EOF'
            
            raise SyntaxError(
                f"Expected Token: {{{expected_tokens_str}}}, Unexpected Token: {unexpected_token}",
                self.line_number, 
                error_column,  # Use the stored column position
                expected=expected_tokens_str,
                token=unexpected_token
            )
            
    def parse(self) -> None:
        """Start parsing the program"""
        try:
            self.parse_program()
        except SyntaxError as e:
            print(f"Syntax Error: {str(e)}")
            raise

    def parse_program(self) -> None:
        """<program> → <global_decl> <function_decl> <function_def> <team_block>"""
        # Skip any initial whitespace or comments
        self.skip_whitespace_and_comments()
        
        # Check if current token is in FIRST(program)
        if self.current_token and self.current_token.type not in self.FIRST_SETS['program']:
            self.expected_tokens = self.FIRST_SETS['program']  # Set all expected tokens
            raise SyntaxError(
                f"Expected Token: {{{', '.join(t.value for t in self.expected_tokens)}}}, "
                f"Unexpected Token: {self.current_token.value if self.current_token else 'EOF'}",
                self.line_number,
                self.column
            )

        self.parse_global_decl()
        self.parse_function_decl()
        self.parse_function_def()
        self.parse_team_block()

    def parse_global_decl(self) -> None:
        """<global_decl> → <global_declaration><global_decl> | λ"""
        # Check FIRST set for global_decl
        if self.current_token and self.current_token.type in self.FIRST_SETS['global_decl']:
            self.parse_global_declaration()
            self.parse_global_decl()  # Recursive call

    def parse_global_declaration(self) -> None:
        """<global_declaration> → <variable_dec> | <const_dec> | <array_dec>"""
        if self.current_token.type == TokenType.CONST:
            self.parse_const_dec()
        elif self.current_token.type == TokenType.ZONE:
            self.parse_array_dec()
        else:
            self.parse_variable_dec()

    def parse_variable_dec(self) -> None:
        """Parse variable declarations"""
        if self.current_token.type == TokenType.FEINT:
            self.parse_feint_dec()
        elif self.current_token.type == TokenType.FLOATER:
            self.parse_floater_dec()
        elif self.current_token.type == TokenType.CHANT:
            self.parse_chant_dec()
        elif self.current_token.type == TokenType.STAT:
            self.parse_stat_dec()

    def parse_feint_dec(self) -> None:
        """<feint_dec> → Feint @identifier <more_feint>;"""
        self.expect(TokenType.FEINT)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_feint()  # Call the function for <more_feint>
        self.expect(TokenType.SEMICOLON)

    def parse_more_feint(self) -> None:
        """<more_feint> → λ | <feint_init><feint_init_end>"""
        # First set of feint_init is {TokenType.ASSIGN}
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.parse_feint_init()
        self.parse_feint_init_end()

    def parse_feint_init(self) -> None:
        """<feint_init> → λ | = <feint_lit> <feint_init_end>"""
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_feint_lit()
        self.parse_feint_init_end()  

    def parse_feint_lit(self) -> None:
        """<feint_lit> → Feint Literal"""
        self.expect(TokenType.FEINTLIT)

    def parse_feint_init_end(self) -> None:
        """<feint_init_end> → λ | ", @identifier <more_feint>" """
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_feint()

    def parse_floater_dec(self) -> None:
        """<floater_dec> → Floater @identifier <more_floater>;"""
        self.expect(TokenType.FLOATER)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_floater()
        self.expect(TokenType.SEMICOLON)

    def parse_more_floater(self) -> None:
        """<more_floater> → λ | <floater_init><floater_init_end>"""
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.parse_floater_init()
        self.parse_floater_init_end()

    def parse_floater_init(self) -> None:
        """<floater_init> → λ |  = <floater_lit> <floater_init_end>"""
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_floater_lit()
        self.parse_floater_init_end()

    def parse_floater_lit(self) -> None:
        """<floater_lit> → Floater Literal"""
        self.expect(TokenType.FLOATERLIT)

    def parse_floater_init_end(self) -> None:
        """<floater_init_end> → λ | ", @identifier <more_floater>" """
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_floater()

    def parse_chant_dec(self) -> None:
        """<chant_dec> → Chant @identifier <more_chant>;"""
        self.expect(TokenType.CHANT)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_chant()
        self.expect(TokenType.SEMICOLON)

    def parse_more_chant(self) -> None:
        """<more_chant> → λ | <chant_init><chant_init_end>"""
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.parse_chant_init()
        self.parse_chant_init_end()

    def parse_chant_init(self) -> None:
        """<chant_init> → λ | = "<chant_lit>" """
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_chant_lit()
        self.parse_chant_init_end()
        

    def parse_chant_lit(self) -> None:
        """<chant_lit> → Chant Literal"""
        self.expect(TokenType.CHANTLIT)

    def parse_chant_init_end(self) -> None:
        """<chant_init_end> → λ | ", @identifier <more_chant>" """
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_chant()
    
    def parse_stat_dec(self) -> None:
        """<stat_dec> → Stat @identifier <more_stat>;"""
        self.expect(TokenType.STAT)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_stat()
        self.expect(TokenType.SEMICOLON)
        
    def parse_more_stat(self) -> None:
        """<more_stat> → λ | <stat_init><stat_init_end>"""
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.parse_stat_init()
        self.parse_stat_init_end()
        
    def parse_stat_init(self) -> None:
        """<stat_init> → λ | = <stat_value>"""
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_stat_value()
        
    def parse_stat_value(self) -> None:
        """<stat_value> → Win | Loss"""
        if self.current_token.type == TokenType.WIN:
            self.expect(TokenType.WIN)
        elif self.current_token.type == TokenType.LOSS:
            self.expect(TokenType.LOSS)
        else:
            raise SyntaxError(f"Expected stat value, got {self.current_token.type}", self.line_number, self.column)
        
    def parse_stat_init_end(self) -> None:
        """<stat_init_end> → λ | ", @identifier <more_stat_init>" """
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_stat()
        
    def parse_const_dec(self) -> None:
        """<const_dec> → Const <variable_dec>;"""
        self.expect(TokenType.CONST)
        self.parse_variable_dec()
        
    def parse_array_dec(self) -> None:
        """<array_dec> → Zone <feint_array> <floater_array> <chant_array> <stat_array>;"""
        self.expect(TokenType.ZONE)
        if self.current_token.type == TokenType.FEINT:
            self.parse_feint_array()
        elif self.current_token.type == TokenType.FLOATER:
            self.parse_floater_array()
        elif self.current_token.type == TokenType.CHANT:
            self.parse_chant_array()
        
    def parse_feint_array(self) -> None:
        """<feint_array> → Feint @identifier [<feint_lit>]<2D_array><feint_array_init>;"""
        self.expect(TokenType.FEINT)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_feint_lit()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
        self.parse_2D_array()
        self.parse_feint_array_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_2D_array(self) -> None:
        """<2D_array> → λ |  [<feint_lit>]"""
        if not self.current_token or self.current_token.type != TokenType.ARRAY_INDEX_LEFT:
            return  # λ case
        
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_feint_lit()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
        
    def parse_feint_array_init(self) -> None:
        """<feint_array_init> → λ | = {<feint_row>}"""
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_feint_row()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        
    def parse_feint_row(self) -> None:
        """<feint_row> → <feint_lit><more_feint_lit> | {<feint_lit><more_feint_lit>} <2D_feint_row>"""
        if self.current_token.type == TokenType.CODE_BLOCK_LEFT:
            self.expect(TokenType.CODE_BLOCK_LEFT)
            self.parse_feint_lit()
            self.parse_more_feint_lit()
            self.expect(TokenType.CODE_BLOCK_RIGHT)
            self.parse_2D_feint_row()
        else:
            self.parse_feint_lit()
            self.parse_more_feint_lit()
    
    def parse_2D_feint_row(self) -> None:
        """<2D_feint_row> → λ | , {<feint_lit><more_feint_lit>} <2D_feint_row> """
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_feint_lit()
        self.parse_more_feint_lit() # Recursive call
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_2D_feint_row()

    def parse_more_feint_lit(self) -> None:
        """<more_feint_lit> → λ | <feint_lit><more_feint_lit>"""
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.parse_feint_lit()
        self.parse_more_feint_lit() # Recursive call
        
    def parse_floater_array(self) -> None:
        """<floater_array> → Floater @identifier [<feint_lit>]<2D_array><floater_array_init>;"""
        self.expect(TokenType.FLOATER)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_feint_lit()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
        self.parse_2D_array()
        self.parse_floater_array_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_floater_array_init(self) -> None:
        """<floater_array_init> → λ | = {<floater_row>}"""
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_floater_row()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        
    def parse_floater_row(self) -> None:
        """<floater_row> → <floater_lit><more_floater_lit> | {<floater_lit><more_floater_lit>} <2D_floater_row>"""
        if self.current_token.type == TokenType.CODE_BLOCK_LEFT:
            self.expect(TokenType.CODE_BLOCK_LEFT)
            self.parse_floater_lit()
            self.parse_more_floater_lit()
            self.expect(TokenType.CODE_BLOCK_RIGHT)
            self.parse_2D_floater_row()
        else:
            self.parse_floater_lit()
            self.parse_more_floater_lit()
    
    def parse_2D_floater_row(self) -> None:
        """<2D_floater_row> → λ |, {<floater_lit><more_floater_lit>} <2D_floater_row>"""
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_floater_lit()
        self.parse_more_floater_lit() # Recursive call
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_2D_floater_row()

    def parse_more_floater_lit(self) -> None:
        """<more_floater_lit> → λ | <floater_lit><more_floater_lit>"""
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.parse_floater_lit()
        self.parse_more_floater_lit() # Recursive call  
        
    def parse_chant_array(self) -> None:
        """<chant_array> → Chant @identifier [<feint_lit>]<2D_array><chant_array_init>;"""
        self.expect(TokenType.CHANT)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_feint_lit()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
        self.parse_2D_array()
        self.parse_chant_array_init()
        self.expect(TokenType.SEMICOLON)    

    def parse_chant_array_init(self) -> None:
        """<chant_array_init> → λ | = {<chant_row>}"""
        if not self.current_token or self.current_token.type != TokenType.ASSIGN:
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_chant_row()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        
    def parse_chant_row(self) -> None:
        """<chant_row> → <chant_lit><more_chant_lit> | {<chant_lit><more_chant_lit>} <2D_chant_row>"""
        if self.current_token.type == TokenType.CODE_BLOCK_LEFT:
            self.expect(TokenType.CODE_BLOCK_LEFT)
            self.parse_chant_lit()
            self.parse_more_chant_lit()
            self.expect(TokenType.CODE_BLOCK_RIGHT)
            self.parse_2D_chant_row()
        else:   
            self.parse_chant_lit()
            self.parse_more_chant_lit()
            
    def parse_2D_chant_row(self) -> None:
        """<2D_chant_row> → λ | , {<chant_lit><more_chant_lit>} <2D_chant_row>"""
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_chant_lit()
        self.parse_more_chant_lit() # Recursive call
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_2D_chant_row()
        
    def parse_more_chant_lit(self) -> None:
        """<more_chant_lit> → λ | <chant_lit><more_chant_lit>"""
        if not self.current_token or self.current_token.type != TokenType.COMMA:
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.parse_chant_lit()
        self.parse_more_chant_lit() # Recursive call    
        
        
    def parse_function_decl(self) -> None:
        """<function_decl> → Wilt <function_declared> | Dunk <dunk_func_declared> | λ"""
        # First set of function_decl
        first_set = {TokenType.WILT, TokenType.DUNK}
        
        # If no token or token not in first set, it's λ case
        if not self.current_token or self.current_token.type not in first_set:
            return  # λ case
            
        if self.current_token.type == TokenType.WILT:
            self.advance()
            self.parse_function_declared()
        elif self.current_token.type == TokenType.DUNK:
            self.advance()
            self.parse_dunk_func_declared()
            
    def parse_function_def(self) -> None:
        """<function_def> → Wilt <function_declared> | Dunk <dunk_func_declared> | λ"""
        # First set of function_def
        first_set = {TokenType.WILT, TokenType.DUNK}
        
        if not self.current_token or self.current_token.type not in first_set:
            return  # λ case
        
        if self.current_token.type == TokenType.WILT:
            self.advance()
            self.parse_function_declared()
        elif self.current_token.type == TokenType.DUNK:
            self.advance()
            self.parse_dunk_func_declared()
            
    def parse_function_param(self) -> None:
        """<function_param> → λ | <param><params>"""
        if not self.current_token or self.current_token.type != TokenType.VAR_INIT:
            return  # λ case
        
        self.parse_param()
        self.parse_params()

    def parse_team_block(self) -> None:
        """<team_block> → Team() { <local_decl> <other_statements> }"""
        if not self.current_token or self.current_token.type not in self.FIRST_SETS['team_block']:
            raise SyntaxError(
                "Expected Team block at the end of program",
                self.line_number,
                self.column
            )

        self.expect(TokenType.TEAM)
        self.expect(TokenType.LEFT_PAREN)
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_local_decl()
        # self.parse_other_statements()
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    
        
    def parse_local_decl(self) -> None:
        """<local_decl> → <local_declaration><local_decl> | λ"""
        # Check FIRST set for local_decl
        if self.current_token and self.current_token.type in self.FIRST_SETS['global_decl']:
            self.parse_local_declaration()
            self.parse_local_decl()  # Recursive call

    def parse_local_declaration(self) -> None:
        """<local_declaration> → <variable_dec> | <array_dec>"""
        if self.current_token.type == TokenType.ZONE:
            self.parse_array_dec()
        elif self.current_token.type == TokenType.CONST:
            self.parse_const_dec()
        else:
            self.parse_variable_dec()
        

    def error_handler(self, expected_tokens: List[TokenType]) -> None:
        """Handle syntax errors by providing helpful error messages"""
        if self.current_token:
            token_type = self.current_token.type
            token_value = self.current_token.value
            raise SyntaxError(
                f"Unexpected token '{token_value}' of type {token_type}. "
                f"Expected one of: {', '.join(str(t) for t in expected_tokens)}",
                self.line_number,
                self.column
            )
        else:
            raise SyntaxError(
                f"Unexpected end of file. Expected one of: {', '.join(str(t) for t in expected_tokens)}",
                self.line_number,
                self.column
            )
# def parse(tokens: List[Token]) -> bool:
#     """
#     Main parsing function that creates a Parser instance and runs the parsing process.
    
#     Args:
#         tokens: List of tokens from the lexical analyzer
    
#     Returns:
#         bool: True if parsing successful, False if syntax errors found
#     """
#     try:
#         parser = Parser(tokens)
#         parser.parse_program()
#         print("\033[92mSyntax Analysis Complete: No syntax errors found!\033[0m")
#         return True
#     except SyntaxError as e:
#         error_msg = f"Syntax Error at line {e.line_number}, column {e.column}: {str(e)}"
#         print(f"\033[91m{error_msg}\033[0m")
#         return False
def parse(tokens: List[Token]) -> bool:
    """
    Main parsing function that creates a Parser instance and runs the parsing process.
    
    Args:
        tokens: List of tokens from the lexical analyzer
    
    Returns:
        bool: True if parsing successful, False if syntax errors found
    """
    try:
        parser = Parser(tokens)
        parser.parse_program()
        print("\033[92mSyntax Analysis Complete: No syntax errors found!\033[0m")
        return True
    except SyntaxError as e:
        # Instead of printing to console, re-raise the error so it can be caught by the editor
        raise
