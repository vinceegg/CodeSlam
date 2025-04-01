from Analyzers.lexical_analyzer.tokens import TokenType, Token
from typing import List, Optional, Set
from Analyzers.syntax_analyzer.errors import SyntaxError 
from Analyzers.syntax_analyzer.first_sets import FIRST_SETS
from Analyzers.syntax_analyzer.predict_sets import PREDICT_SETS

# class SyntaxError(Exception):
#     """Custom exception for syntax errors"""
#     def __init__(self, message, line_number=None, column=None):
#         super().__init__(message)
#         self.line_number = line_number
#         self.column = column

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.current_token = self.tokens[0] if tokens else None
        self.line_number = 1
        self.column = 0
        self.expected_tokens = set()
        self.line_starts = {1: 0}  # Track the starting position of each line
        self.current_line_content = ""  # Track content of current line
        self.current_nonterminal = None  # Track current nonterminal being parsed

    def get_expected_tokens(self, nonterminal: str) -> Set[TokenType]:
        """Get all expected tokens for a nonterminal based on FIRST sets"""
        if nonterminal in FIRST_SETS:
            return FIRST_SETS[nonterminal]
        return set()

    def get_production_rule(self, nonterminal: str, token_type: TokenType) -> Optional[int]:
        """Get the production rule number based on PREDICT sets"""
        if (nonterminal, token_type) in PREDICT_SETS:
            return PREDICT_SETS[(nonterminal, token_type)]
        return None

    def error_handler(self, nonterminal: str, expected_tokens: Set[TokenType] = None) -> None:
        """Enhanced error handler that uses PREDICT sets and FIRST sets"""
        if expected_tokens is None:
            expected_tokens = self.get_expected_tokens(nonterminal)

        if self.current_token:
            token_type = self.current_token.type
            token_value = self.current_token.value
            production_rule = self.get_production_rule(nonterminal, token_type)
            
            # Build detailed error message
            error_msg = f"Syntax Error at line {self.line_number}, column {self.column}:\n"
            error_msg += f"While parsing {nonterminal}, "
            
            if production_rule:
                error_msg += f"expected production rule {production_rule} "
            else:
                error_msg += "unexpected "
            
            error_msg += f"token '{token_value}' of type {token_type}.\n"
            error_msg += f"Expected one of: {', '.join(str(t.value) for t in expected_tokens)}"
            
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected=', '.join(str(t.value) for t in expected_tokens),
                token=token_value,
                nonterminal=nonterminal,
                production_rule=production_rule
            )
        else:
            error_msg = f"Syntax Error at line {self.line_number}, column {self.column}:\n"
            error_msg += f"Unexpected end of file while parsing {nonterminal}.\n"
            error_msg += f"Expected one of: {', '.join(str(t.value) for t in expected_tokens)}"
            
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected=', '.join(str(t.value) for t in expected_tokens),
                token="EOF",
                nonterminal=nonterminal
            )

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

    def get_token_type(self, token_value: str) -> TokenType:
        """Convert a token value to its corresponding TokenType"""
        try:
            return TokenType[token_value.upper()]
        except KeyError:
            # If not found, return the original token type
            return None

    def match_token_type(self, token: Token, expected_type: TokenType) -> bool:
        """Match a token against an expected token type, considering both type and value"""
        if not token:
            return False
        
        # Get the TokenType for the token's value
        value_type = self.get_token_type(token.value) if token.value else None
        
        # Check if either the token's type matches or its value converts to the expected type
        return token.type == expected_type or value_type == expected_type

    def expect(self, token_type: TokenType) -> None:
        """Expect a specific token type, raise error if not found"""
        if self.current_token and self.match_token_type(self.current_token, token_type):
            self.advance()
        else:
            expected_tokens = {token_type}
            self.error_handler(self.current_nonterminal, expected_tokens)

    def match(self, expected_type: TokenType) -> bool:
        """Check if current token matches expected type"""
        if self.current_token and self.match_token_type(self.current_token, expected_type):
            self.advance()
            return True
        return False
            
    def parse(self) -> None:
        """Start parsing the program"""
        try:
            self.parse_program()
        except SyntaxError as e:
            print(f"Syntax Error: {str(e)}")
            raise

    def parse_program(self) -> None:
        """<program> → <global_decl> <function_decl> <function_def> <team_block>""" 
        self.current_nonterminal = "program"
        expected_tokens = self.get_expected_tokens("program")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("program", expected_tokens)
            
        self.skip_whitespace_and_comments()
        # All three of these can be null (λ), so we only parse them if we see tokens in their FIRST sets
        
        # Check if current token is in FIRST(global_decl)
        if self.current_token and any(self.match_token_type(self.current_token, t) for t in self.get_expected_tokens("global_decl")):
            self.parse_global_decl()
        
        # Check if current token is in FIRST(function_decl)
        if self.current_token and any(self.match_token_type(self.current_token, t) for t in self.get_expected_tokens("function_decl")):
            self.parse_function_decl()
        
        # Check if current token is in FIRST(function_def)
        if self.current_token and any(self.match_token_type(self.current_token, t) for t in self.get_expected_tokens("function_def")):
            self.parse_function_def()
            
        # Team block is required and should be the last part of the program
        self.parse_team_block()

    def parse_global_decl(self) -> None:
        """<global_decl> → <global_declaration><global_decl> | λ"""
        self.current_nonterminal = "global_decl"
        expected_tokens = self.get_expected_tokens("global_decl")
        
        # If we have a token that's in FIRST(global_declaration)
        if self.current_token and any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.parse_global_declaration()
            self.parse_global_decl()  # Recursive call
        # The λ case is handled implicitly by just returning

    def parse_global_declaration(self) -> None:
        """<global_declaration> → <variable_dec> | <const_dec> | <array_dec>"""
        self.current_nonterminal = "global_declaration"
        expected_tokens = self.get_expected_tokens("global_declaration")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("global_declaration", expected_tokens)

        if self.match_token_type(self.current_token, TokenType.CONST):
            self.parse_const_dec()
        elif self.match_token_type(self.current_token, TokenType.ZONE):
            self.parse_array_dec()
        else:
            self.parse_variable_dec()

    def parse_variable_dec(self) -> None:
        """Parse variable declarations"""
        self.current_nonterminal = "variable_dec"
        expected_tokens = self.get_expected_tokens("variable_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("variable_dec", expected_tokens)

        if self.match_token_type(self.current_token, TokenType.FEINT):
            self.parse_feint_dec()
        elif self.match_token_type(self.current_token, TokenType.FLOATER):
            self.parse_floater_dec()
        elif self.match_token_type(self.current_token, TokenType.CHANT):
            self.parse_chant_dec()
        elif self.match_token_type(self.current_token, TokenType.STAT):
            self.parse_stat_dec()

    def parse_feint_dec(self) -> None:
        """<feint_dec> → Feint @identifier <more_feint>;"""
        self.current_nonterminal = "feint_dec"
        expected_tokens = self.get_expected_tokens("feint_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("feint_dec", expected_tokens)

        self.expect(TokenType.FEINT)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_feint()
        self.expect(TokenType.SEMICOLON)

    def parse_more_feint(self) -> None:
        """<more_feint> → λ | <feint_init><feint_init_end>"""
        self.current_nonterminal = "more_feint"
        expected_tokens = self.get_expected_tokens("more_feint")
        
        # Only proceed if we see an ASSIGN token, otherwise return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case

        # If we get here, we have an ASSIGN token
        self.parse_feint_init()
        self.parse_feint_init_end()

    def parse_feint_init(self) -> None:
        """<feint_init> → λ | = <feint_lit> <feint_init_end>"""
        self.current_nonterminal = "feint_init"
        expected_tokens = self.get_expected_tokens("feint_init")
        
        # Only proceed if we see an ASSIGN token, otherwise return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case

        # If we get here, we have an ASSIGN token
        self.expect(TokenType.ASSIGN)
        self.parse_feint_lit()
        self.parse_feint_init_end()

    def parse_feint_lit(self) -> None:
        """<feint_lit> → Feint Literal"""
        self.current_nonterminal = "feint_lit"
        expected_tokens = self.get_expected_tokens("feint_lit")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("feint_lit", expected_tokens)

        self.expect(TokenType.FEINTLIT)

    def parse_feint_init_end(self) -> None:
        """<feint_init_end> → λ | ", @identifier <more_feint>" """
        self.current_nonterminal = "feint_init_end"
        expected_tokens = self.get_expected_tokens("feint_init_end")
        
        # Only proceed if we see a COMMA token, otherwise return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case

        # If we get here, we have a COMMA token
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
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.parse_floater_init()
        self.parse_floater_init_end()

    def parse_floater_init(self) -> None:
        """<floater_init> → λ |  = <floater_lit> <floater_init_end>"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_floater_lit()
        self.parse_floater_init_end()

    def parse_floater_lit(self) -> None:
        """<floater_lit> → Floater Literal"""
        self.expect(TokenType.FLOATERLIT)

    def parse_floater_init_end(self) -> None:
        """<floater_init_end> → λ | ", @identifier <more_floater>" """
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
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
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.parse_chant_init()
        self.parse_chant_init_end()

    def parse_chant_init(self) -> None:
        """<chant_init> → λ | = "<chant_lit>" """
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_chant_lit()
        self.parse_chant_init_end()
        

    def parse_chant_lit(self) -> None:
        """<chant_lit> → Chant Literal"""
        self.expect(TokenType.CHANTLIT)

    def parse_chant_init_end(self) -> None:
        """<chant_init_end> → λ | ", @identifier <more_chant>" """
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
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
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.parse_stat_init()
        self.parse_stat_init_end()
        
    def parse_stat_init(self) -> None:
        """<stat_init> → λ | = <stat_value>"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_stat_value()
        
    def parse_stat_value(self) -> None:
        """<stat_value> → Win | Loss"""
        if self.match_token_type(self.current_token, TokenType.WIN):
            self.expect(TokenType.WIN)
        elif self.match_token_type(self.current_token, TokenType.LOSS):
            self.expect(TokenType.LOSS)
        else:
            raise SyntaxError(f"Expected stat value, got {self.current_token.type}", self.line_number, self.column)
        
    def parse_stat_init_end(self) -> None:
        """<stat_init_end> → λ | ", @identifier <more_stat_init>" """
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
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
        if self.match_token_type(self.current_token, TokenType.FEINT):
            self.parse_feint_array()
        elif self.match_token_type(self.current_token, TokenType.FLOATER):
            self.parse_floater_array()
        elif self.match_token_type(self.current_token, TokenType.CHANT):
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
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ARRAY_INDEX_LEFT):
            return  # λ case
        
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_feint_lit()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
        
    def parse_feint_array_init(self) -> None:
        """<feint_array_init> → λ | = {<feint_row>}"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_feint_row()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        
    def parse_feint_row(self) -> None:
        """<feint_row> → <feint_lit><more_feint_lit> | {<feint_lit><more_feint_lit>} <2D_feint_row>"""
        if self.match_token_type(self.current_token, TokenType.CODE_BLOCK_LEFT):
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
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_feint_lit()
        self.parse_more_feint_lit() # Recursive call
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_2D_feint_row()

    def parse_more_feint_lit(self) -> None:
        """<more_feint_lit> → λ | <feint_lit><more_feint_lit>"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
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
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_floater_row()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        
    def parse_floater_row(self) -> None:
        """<floater_row> → <floater_lit><more_floater_lit> | {<floater_lit><more_floater_lit>} <2D_floater_row>"""
        if self.match_token_type(self.current_token, TokenType.CODE_BLOCK_LEFT):
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
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_floater_lit()
        self.parse_more_floater_lit() # Recursive call
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_2D_floater_row()

    def parse_more_floater_lit(self) -> None:
        """<more_floater_lit> → λ | <floater_lit><more_floater_lit>"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
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
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_chant_row()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        
    def parse_chant_row(self) -> None:
        """<chant_row> → <chant_lit><more_chant_lit> | {<chant_lit><more_chant_lit>} <2D_chant_row>"""
        if self.match_token_type(self.current_token, TokenType.CODE_BLOCK_LEFT):
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
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_chant_lit()
        self.parse_more_chant_lit() # Recursive call
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_2D_chant_row()
        
    def parse_more_chant_lit(self) -> None:
        """<more_chant_lit> → λ | <chant_lit><more_chant_lit>"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.parse_chant_lit()
        self.parse_more_chant_lit() # Recursive call    
        
        
    def parse_function_decl(self) -> None:
        """<function_decl> → Wilt <function_declared> | Dunk <dunk_func_declared> | λ"""
        self.current_nonterminal = "function_decl"
        # First set of function_decl
        first_set = {TokenType.WILT, TokenType.DUNK}
        
        # If no token or token not in first set, it's λ case
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in first_set):
            return  # λ case - just return to handle the empty case
            
        if self.match_token_type(self.current_token, TokenType.WILT):
            self.advance()
            self.parse_function_declared()
        elif self.match_token_type(self.current_token, TokenType.DUNK):
            self.advance()
            self.parse_dunk_func_declared()

    def parse_function_declared(self) -> None:
        """<function_declared> → <function_param> <function_statements>"""
        self.parse_function_param()
        self.parse_function_statements()
            
    def parse_function_def(self) -> None:
        """<function_def> → Wilt <function_declared> | Dunk <dunk_func_declared> | λ"""
        self.current_nonterminal = "function_def"
        # First set of function_def
        first_set = {TokenType.WILT, TokenType.DUNK}
        
        # If no token or token not in first set, it's λ case
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in first_set):
            return  # λ case - just return to handle the empty case
        
        if self.match_token_type(self.current_token, TokenType.WILT):
            self.advance()
            self.parse_function_declared()
        elif self.match_token_type(self.current_token, TokenType.DUNK):
            self.advance()
            self.parse_dunk_func_declared()
            
    def parse_function_param(self) -> None:
        """<function_param> → λ | <param><params>"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.VAR_INIT):
            return  # λ case
        
        self.parse_param()
        self.parse_params()

    def parse_team_block(self) -> None:
        """<team_block> → Team() { <local_decl> <other_statements> }"""
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in FIRST_SETS['team_block']):
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
        if self.current_token and any(self.match_token_type(self.current_token, t) for t in FIRST_SETS['global_decl']):
            self.parse_local_declaration()
            self.parse_local_decl()  # Recursive call

    def parse_local_declaration(self) -> None:
        """<local_declaration> → <variable_dec> | <array_dec>"""
        if self.match_token_type(self.current_token, TokenType.ZONE):
            self.parse_array_dec()
        elif self.match_token_type(self.current_token, TokenType.CONST):
            self.parse_const_dec()
        else:
            self.parse_variable_dec()
        

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
