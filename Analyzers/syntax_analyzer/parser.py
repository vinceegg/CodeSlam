from Analyzers.lexical_analyzer.tokens import TokenType, Token
from typing import List, Optional, Set
from Analyzers.syntax_analyzer.errors import SyntaxError 
from Analyzers.syntax_analyzer.first_sets import FIRST_SETS
from Analyzers.syntax_analyzer.predict_sets import PREDICT_SETS

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
        """<program> → <global_decl> <function_def> <team_block>"""
        self.current_nonterminal = "program"
        expected_tokens = self.get_expected_tokens("program")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("program", expected_tokens)

        # Check if current token is in FIRST(global_decl)
        if self.current_token and any(self.match_token_type(self.current_token, t) for t in self.get_expected_tokens("global_decl")):
            self.parse_global_decl()
        
        # Check if current token is in FIRST(function_def)
        if self.current_token and any(self.match_token_type(self.current_token, t) for t in self.get_expected_tokens("function_def")):
            self.parse_function_def()
            
        # Team block is required
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
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in FIRST_SETS['stat_value']):
            raise SyntaxError(
                "Expected stat value, got",
                self.line_number,
                self.column,
                expected="WIN, LOSS",
                token="EOF" if not self.current_token else self.current_token.value,
                nonterminal="stat_value"
            )
        
    def parse_stat_init_end(self) -> None:
        """<stat_init_end> → λ | ", @identifier <more_stat_init>" """
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_stat()
        
    def parse_const_dec(self) -> None:
        """<const_dec> → <const_feint> | <const_floater> | <const_chant> | <const_stat>"""
        self.current_nonterminal = "const_dec"
        expected_tokens = self.get_expected_tokens("const_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("const_dec", expected_tokens)    
        
        self.expect(TokenType.CONST)
        if self.match_token_type(self.current_token, TokenType.FEINT):
            self.parse_const_feint()
        elif self.match_token_type(self.current_token, TokenType.FLOATER):
            self.parse_const_floater()
        elif self.match_token_type(self.current_token, TokenType.CHANT):
            self.parse_const_chant()
        elif self.match_token_type(self.current_token, TokenType.STAT):
            self.parse_const_stat()
        else:
            self.error_handler("const_dec")
            
    def parse_const_feint(self) -> None:
        """<const_feint> → Feint @identifier <feint_const_init>;"""
        self.expect(TokenType.FEINT)
        self.expect(TokenType.VAR_INIT)
        self.parse_feint_const_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_feint_const_init(self) -> None:
        """<feint_const_init> → <feint_const><feint_const_end>"""
        self.parse_feint_const()
        self.parse_feint_const_end()
        
    def parse_feint_const(self) -> None:
        """<feint_const> → = <feint_lit>"""
        self.expect(TokenType.ASSIGN)
        self.parse_feint_lit()
        
    def parse_feint_const_end(self) -> None:
        """<feint_const_end> → ", @identifier <feint_const_init>" | λ"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
            
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_feint_const_init()
        
    def parse_const_floater(self) -> None:
        """<const_floater> → Floater @identifier <floater_const_init>;"""
        self.expect(TokenType.FLOATER)
        self.expect(TokenType.VAR_INIT)
        self.parse_floater_const_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_floater_const_init(self) -> None:
        """<floater_const_init> → <floater_const><floater_const_end>"""
        self.parse_floater_const()
        self.parse_floater_const_end()
        
    def parse_floater_const(self) -> None:
        """<floater_const> → = <floater_lit>"""
        self.expect(TokenType.ASSIGN)
        self.parse_floater_lit()
        
    def parse_floater_const_end(self) -> None:
        """<floater_const_end> → ", @identifier <floater_const_init>" | λ"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
            
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_floater_const_init()
        
    def parse_const_chant(self) -> None:
        """<const_chant> → Chant @identifier <chant_const_init>;"""
        self.expect(TokenType.CHANT)
        self.expect(TokenType.VAR_INIT)
        self.parse_chant_const_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_chant_const_init(self) -> None:
        """<chant_const_init> → <chant_const><chant_const_end>"""
        self.parse_chant_const()
        self.parse_chant_const_end()
        
    def parse_chant_const(self) -> None:
        """<chant_const> → = <chant_lit>"""
        self.expect(TokenType.ASSIGN)
        self.parse_chant_lit()
        
    def parse_chant_const_end(self) -> None:
        """<chant_const_end> → ", @identifier <chant_const_init>" | λ"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
            
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_chant_const_init()
        
    def parse_const_stat(self) -> None:
        """<const_stat> → Stat @identifier <stat_const_init>;"""
        self.expect(TokenType.STAT)
        self.expect(TokenType.VAR_INIT)
        self.parse_stat_const_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_stat_const_init(self) -> None:
        """<stat_const_init> → <stat_const><stat_const_end>"""
        self.parse_stat_const()
        self.parse_stat_const_end()
        
    def parse_stat_const(self) -> None:
        """<stat_const> → = <stat_value>"""
        self.expect(TokenType.ASSIGN)
        self.parse_stat_value()
        
    def parse_stat_const_end(self) -> None:
        """<stat_const_end> → ", @identifier <stat_const_init>" | λ"""
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
            
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_stat_const_init()
        
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
        
    """ VINCE AGAIN """

    def parse_function_def(self) -> None:
        """<function_def> → λ | Wilt <function_declared><function_def> | Dunk <dunk_func_declared><function_def>"""
        self.current_nonterminal = "function_def"
        expected_tokens = self.get_expected_tokens("function_def")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        if self.match_token_type(self.current_token, TokenType.WILT):
            self.parse_function_declared()
            self.parse_function_def()  # Recursive call
        elif self.match_token_type(self.current_token, TokenType.DUNK):
            self.parse_dunk_func_declared()
            self.parse_function_def()  # Recursive call

    def parse_function_declared(self) -> None:
        """<function_declared> → <feint_function> | <floater_function> | <chant_function> | <stat_function>"""
        self.current_nonterminal = "function_declared"
        expected_tokens = self.get_expected_tokens("function_declared")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("function_declared", expected_tokens)

        if self.match_token_type(self.current_token, TokenType.FEINT):
            self.parse_feint_function()
        elif self.match_token_type(self.current_token, TokenType.FLOATER):
            self.parse_floater_function()
        elif self.match_token_type(self.current_token, TokenType.CHANT):
            self.parse_chant_function()
        elif self.match_token_type(self.current_token, TokenType.STAT):
            self.parse_stat_function()

    def parse_feint_function(self) -> None:
        """<feint_function> → Feint @identifier(<func_parameters>) {<function_statement> <rebound_statement>}"""
        self.current_nonterminal = "feint_function"
        expected_tokens = self.get_expected_tokens("feint_function")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("feint_function", expected_tokens)
        
        self.expect(TokenType.FEINT)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_function_statement()
        self.parse_rebound_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_floater_function(self) -> None:
        """<floater_function> → Floater @identifier(<func_parameters>) {<function_statement> <rebound_statement>}"""
        self.current_nonterminal = "floater_function"
        
        self.expect(TokenType.FLOATER)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_function_statement()
        self.parse_rebound_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_chant_function(self) -> None:
        """<chant_function> → Chant @identifier(<func_parameters>) {<function_statement> <rebound_statement>}"""
        self.current_nonterminal = "chant_function"
        
        self.expect(TokenType.CHANT)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_function_statement()
        self.parse_rebound_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_stat_function(self) -> None:
        """<stat_function> → Stat @identifier(<func_parameters>) {<function_statement> <rebound_statement>}"""
        self.current_nonterminal = "stat_function"
        
        self.expect(TokenType.STAT)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_function_statement()
        self.parse_rebound_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_dunk_func_declared(self) -> None:
        """<dunk_func_declared> → <dunk_function>"""
        self.current_nonterminal = "dunk_func_declared"
        expected_tokens = self.get_expected_tokens("dunk_func_declared")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("dunk_func_declared", expected_tokens)
        
        self.parse_dunk_function()

    def parse_dunk_function(self) -> None:
        """<dunk_function> → @identifier(<func_parameters>) {<function_statement>}"""
        self.current_nonterminal = "dunk_function"
        expected_tokens = self.get_expected_tokens("dunk_function")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("dunk_function", expected_tokens)
        
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_function_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_func_parameters(self) -> None:
        """<func_parameters> → λ | @identifier <param_end>"""
        self.current_nonterminal = "func_parameters"
        expected_tokens = self.get_expected_tokens("func_parameters")
        
        # If current token is not VAR_INIT, then it's the λ case
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.VAR_INIT):
            return  # λ case
        
        self.expect(TokenType.VAR_INIT)
        self.parse_param_end()

    def parse_param_end(self) -> None:
        """<param_end> → λ | , @identifier <param_end>"""
        self.current_nonterminal = "param_end"
        
        # If current token is not COMMA, then it's the λ case
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_param_end()  # Recursive call

    def parse_function_statement(self) -> None:
        """<function_statement> → <statement><function_statement> | λ"""
        self.current_nonterminal = "function_statement"
        expected_tokens = self.get_expected_tokens("function_statement")
        
        # If not a statement start, it's the λ case
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        self.parse_statement()
        self.parse_function_statement()  # Recursive call

    def parse_team_statements(self) -> None:
        """<team_statements> → <statement><team_statements> | λ"""
        self.current_nonterminal = "team_statements"
        expected_tokens = self.get_expected_tokens("team_statements")
        
        # If not a statement start, it's the λ case
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        self.parse_statement()
        self.parse_team_statements()  # Recursive call

    def parse_statement(self) -> None:
        """<statement> → <variable_dec> | <announce_statement> | <inbound_statement> | <dribble_statement> | <switch_statement> | <forward_statement> | <play_statement> | <run_play_statement> | @identifier <follow_statement>;"""
        self.current_nonterminal = "statement"
        expected_tokens = self.get_expected_tokens("statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("statement", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINT) or \
        self.match_token_type(self.current_token, TokenType.FLOATER) or \
        self.match_token_type(self.current_token, TokenType.CHANT) or \
        self.match_token_type(self.current_token, TokenType.STAT):
            self.parse_variable_dec()
        elif self.match_token_type(self.current_token, TokenType.ANNOUNCE):
            self.parse_announce_statement()
        elif self.match_token_type(self.current_token, TokenType.INBOUND):
            self.parse_inbound_statement()
        elif self.match_token_type(self.current_token, TokenType.DRIBBLE):
            self.parse_dribble_statement()
        elif self.match_token_type(self.current_token, TokenType.SWITCH):
            self.parse_switch_statement()
        elif self.match_token_type(self.current_token, TokenType.FORWARD):
            self.parse_forward_statement()
        elif self.match_token_type(self.current_token, TokenType.PLAY):
            self.parse_play_statement()
        elif self.match_token_type(self.current_token, TokenType.RUN):
            self.parse_run_play_statement()
        elif self.match_token_type(self.current_token, TokenType.VAR_INIT):
            self.expect(TokenType.VAR_INIT)
            self.parse_follow_statement()
            self.expect(TokenType.SEMICOLON)

    def parse_follow_statement(self) -> None:
        """<follow_statement> → <increment>; | <decrement>; | <function_call>; | <assignment_expression><team_statements> | <array_manipulation>"""
        self.current_nonterminal = "follow_statement"
        expected_tokens = self.get_expected_tokens("follow_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("follow_statement", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.INCREMENT):
            self.parse_increment()
            self.expect(TokenType.SEMICOLON)
        elif self.match_token_type(self.current_token, TokenType.DECREMENT):
            self.parse_decrement()
            self.expect(TokenType.SEMICOLON)
        elif self.match_token_type(self.current_token, TokenType.LEFT_PAREN):
            self.parse_function_call()
            self.expect(TokenType.SEMICOLON)
        elif self.match_token_type(self.current_token, TokenType.ASSIGN):
            self.parse_assignment_expression()
            self.parse_team_statements()
        elif self.match_token_type(self.current_token, TokenType.ARRAY_INDEX_LEFT):
            self.parse_array_manipulation()

    def parse_array_manipulation(self) -> None:
        """<array_manipulation> → [<element_index>]<2d_manipulation><array_man>"""
        self.current_nonterminal = "array_manipulation"
        expected_tokens = self.get_expected_tokens("array_manipulation")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("array_manipulation", expected_tokens)
        
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_element_index()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
        self.parse_2d_manipulation()
        self.parse_array_man()

    def parse_element_index(self) -> None:
        """<element_index> → <feint_lit>"""
        self.current_nonterminal = "element_index"
        expected_tokens = self.get_expected_tokens("element_index")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("element_index", expected_tokens)
        
        self.parse_feint_lit()

    def parse_2d_manipulation(self) -> None:
        """<2d_manipulation> → [<element_index>] | λ"""
        self.current_nonterminal = "2d_manipulation"
        
        # If current token is not ARRAY_INDEX_LEFT, then it's the λ case
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ARRAY_INDEX_LEFT):
            return  # λ case
        
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_element_index()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)

    def parse_array_man(self) -> None:
        """<array_man> → = <array_elem> | λ"""
        self.current_nonterminal = "array_man"
        
        # If current token is not ASSIGN, then it's the λ case
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_array_elem()

    def parse_array_elem(self) -> None:
        """<array_elem> → <feint_lit> | <floater_lit> | <chant_lit>"""
        self.current_nonterminal = "array_elem"
        expected_tokens = self.get_expected_tokens("array_elem")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("array_elem", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        elif self.match_token_type(self.current_token, TokenType.FLOATERLIT):
            self.parse_floater_lit()
        elif self.match_token_type(self.current_token, TokenType.CHANTLIT):
            self.parse_chant_lit()

    def parse_rebound_statement(self) -> None:
        """<rebound_statement> → Rebound <rebound_value>;"""
        self.current_nonterminal = "rebound_statement"
        expected_tokens = self.get_expected_tokens("rebound_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("rebound_statement", expected_tokens)
        
        self.expect(TokenType.REBOUND)
        self.parse_rebound_value()
        self.expect(TokenType.SEMICOLON)

    def parse_rebound_value(self) -> None:
        """<rebound_value> → <literal> | @identifier | <expression>"""
        self.current_nonterminal = "rebound_value"
        expected_tokens = self.get_expected_tokens("rebound_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("rebound_value", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT) or \
        self.match_token_type(self.current_token, TokenType.FLOATERLIT) or \
        self.match_token_type(self.current_token, TokenType.NEGAFEINT) or \
        self.match_token_type(self.current_token, TokenType.NEGAFLOATER) or \
        self.match_token_type(self.current_token, TokenType.CHANTLIT) or \
        self.match_token_type(self.current_token, TokenType.WIN) or \
        self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_literal()
        elif self.match_token_type(self.current_token, TokenType.VAR_INIT):
            self.expect(TokenType.VAR_INIT)
        elif self.match_token_type(self.current_token, TokenType.LEFT_PAREN):
            self.parse_expression()

    def parse_announce_statement(self) -> None:
        """<announce_statement> → Announce(<outputs>);"""
        self.current_nonterminal = "announce_statement"
        expected_tokens = self.get_expected_tokens("announce_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("announce_statement", expected_tokens)
        
        self.expect(TokenType.ANNOUNCE)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_outputs()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.SEMICOLON)

    def parse_outputs(self) -> None:
        """<outputs> → <output><other_outputs>"""
        self.current_nonterminal = "outputs"
        expected_tokens = self.get_expected_tokens("outputs")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("outputs", expected_tokens)
        
        self.parse_output()
        self.parse_other_outputs()

    def parse_output(self) -> None:
        """<output> → <literal> | <expression> | @identifier | <stat_value> | <array_access>"""
        self.current_nonterminal = "output"
        expected_tokens = self.get_expected_tokens("output")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("output", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT) or \
        self.match_token_type(self.current_token, TokenType.FLOATERLIT) or \
        self.match_token_type(self.current_token, TokenType.NEGAFEINT) or \
        self.match_token_type(self.current_token, TokenType.NEGAFLOATER) or \
        self.match_token_type(self.current_token, TokenType.CHANTLIT) or \
        self.match_token_type(self.current_token, TokenType.WIN) or \
        self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_literal()
        elif self.match_token_type(self.current_token, TokenType.LEFT_PAREN):
            self.parse_expression()
        elif self.match_token_type(self.current_token, TokenType.VAR_INIT):
            # Check next token to determine if it's an array access
            next_token = self.peek()
            if next_token and self.match_token_type(next_token, TokenType.ARRAY_INDEX_LEFT):
                self.parse_array_access()
            else:
                self.expect(TokenType.VAR_INIT)
        elif self.match_token_type(self.current_token, TokenType.WIN) or \
            self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_stat_value()

    def parse_array_access(self) -> None:
        """<array_access> → @identifier[<element_index>]<2d_manipulation>"""
        self.current_nonterminal = "array_access"
        expected_tokens = self.get_expected_tokens("array_access")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("array_access", expected_tokens)
        
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_element_index()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
        self.parse_2d_manipulation()

    def parse_other_outputs(self) -> None:
        """<other_outputs> → λ | & <outputs>"""
        self.current_nonterminal = "other_outputs"
        
        # If current token is not CHANT_CONCAT, then it's the λ case
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.CHANT_CONCAT):
            return  # λ case
        
        self.expect(TokenType.CHANT_CONCAT)
        self.parse_outputs()

    def parse_literal(self) -> None:
        """<literal> → <feint_lit> | <floater_lit> | <nega_feint_lit> | <nega_floater_lit> | <chant_lit> | <stat_value>"""
        self.current_nonterminal = "literal"
        expected_tokens = self.get_expected_tokens("literal")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("literal", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        elif self.match_token_type(self.current_token, TokenType.FLOATERLIT):
            self.parse_floater_lit()
        elif self.match_token_type(self.current_token, TokenType.NEGAFEINT):
            self.parse_nega_feint_lit()
        elif self.match_token_type(self.current_token, TokenType.NEGAFLOATER):
            self.parse_nega_floater_lit()
        elif self.match_token_type(self.current_token, TokenType.CHANTLIT):
            self.parse_chant_lit()
        elif self.match_token_type(self.current_token, TokenType.WIN) or \
            self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_stat_value()

    def parse_nega_feint_lit(self) -> None:
        """<nega_feint_lit> → Negative Feint Literal"""
        self.current_nonterminal = "nega_feint_lit"
        expected_tokens = self.get_expected_tokens("nega_feint_lit")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("nega_feint_lit", expected_tokens)
        
        self.expect(TokenType.NEGAFEINT)

    def parse_nega_floater_lit(self) -> None:
        """<nega_floater_lit> → Negative Floater Literal"""
        self.current_nonterminal = "nega_floater_lit"
        expected_tokens = self.get_expected_tokens("nega_floater_lit")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("nega_floater_lit", expected_tokens)
        
        self.expect(TokenType.NEGAFLOATER)

    """ VINCE START HERE """

    def parse_expression(self) -> None:
        """<expression> → <arithmetic_expression> | <relational_expression> | <logical_expression>"""
        self.current_nonterminal = "expression"
        expected_tokens = self.get_expected_tokens("expression")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("expression", expected_tokens)

        # Lookahead to determine which type of expression to parse
        if self.current_token and self.match_token_type(self.current_token, TokenType.NOT_OP):
            # NOT operator indicates logical expression
            self.parse_logical_expression()
        elif self.peek() and any(self.match_token_type(self.peek(), t) for t in [
            TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, 
            TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL
        ]):
            # Relational operators indicate relational expression
            self.parse_relational_expression()
        else:
            # Default to arithmetic expression
            self.parse_arithmetic_expression()

    def parse_arithmetic_expression(self) -> None:
        """<arithmetic_expression> → <arith_term><more_arith_term>"""
        self.current_nonterminal = "arithmetic_expression"
        expected_tokens = self.get_expected_tokens("arithmetic_expression")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("arithmetic_expression", expected_tokens)
        
        self.parse_arith_term()
        self.parse_more_arith_term()

    def parse_arith_term(self) -> None:
        """<arith_term> → <number> | (<arithmetic_expression>)"""
        self.current_nonterminal = "arith_term"
        expected_tokens = self.get_expected_tokens("arith_term")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("arith_term", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.LEFT_PAREN):
            self.expect(TokenType.LEFT_PAREN)
            self.parse_arithmetic_expression()
            self.expect(TokenType.RIGHT_PAREN)
        else:
            self.parse_number()

    def parse_number(self) -> None:
        """<number> → <feint_lit> | <floater_lit> | @identifier | <nega_feint_lit> | <nega_floater_lit> | <number_type_cast>"""
        self.current_nonterminal = "number"
        expected_tokens = self.get_expected_tokens("number")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("number", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        elif self.match_token_type(self.current_token, TokenType.FLOATERLIT):
            self.parse_floater_lit()
        elif self.match_token_type(self.current_token, TokenType.VAR_INIT):
            self.expect(TokenType.VAR_INIT)
        elif self.match_token_type(self.current_token, TokenType.NEGAFEINT):
            self.parse_nega_feint_lit()
        elif self.match_token_type(self.current_token, TokenType.NEGAFLOATER):
            self.parse_nega_floater_lit()
        elif any(self.match_token_type(self.current_token, t) for t in [TokenType.FEINT, TokenType.FLOATER]):
            self.parse_number_type_cast()

    def parse_nega_feint_lit(self) -> None:
        """<nega_feint_lit> → Negative Feint Literal"""
        self.current_nonterminal = "nega_feint_lit"
        expected_tokens = self.get_expected_tokens("nega_feint_lit")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("nega_feint_lit", expected_tokens)
        
        self.expect(TokenType.NEGAFEINT)

    def parse_nega_floater_lit(self) -> None:
        """<nega_floater_lit> → Negative Floater Literal"""
        self.current_nonterminal = "nega_floater_lit"
        expected_tokens = self.get_expected_tokens("nega_floater_lit")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("nega_floater_lit", expected_tokens)
        
        self.expect(TokenType.NEGAFLOATER)

    def parse_number_type_cast(self) -> None:
        """<number_type_cast> → <feint_type_casting> | <floater_type_casting>"""
        self.current_nonterminal = "number_type_cast"
        expected_tokens = self.get_expected_tokens("number_type_cast")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("number_type_cast", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINT):
            self.parse_feint_type_casting()
        elif self.match_token_type(self.current_token, TokenType.FLOATER):
            self.parse_floater_type_casting()

    def parse_feint_type_casting(self) -> None:
        """<feint_type_casting> → Feint(<typecast_value>)"""
        self.current_nonterminal = "feint_type_casting"
        expected_tokens = self.get_expected_tokens("feint_type_casting")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("feint_type_casting", expected_tokens)
        
        self.expect(TokenType.FEINT)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_typecast_value()
        self.expect(TokenType.RIGHT_PAREN)

    def parse_floater_type_casting(self) -> None:
        """<floater_type_casting> → Floater(<typecast_value>)"""
        self.current_nonterminal = "floater_type_casting"
        expected_tokens = self.get_expected_tokens("floater_type_casting")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("floater_type_casting", expected_tokens)
        
        self.expect(TokenType.FLOATER)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_typecast_value()
        self.expect(TokenType.RIGHT_PAREN)

    def parse_chant_type_casting(self) -> None:
        """<chant_type_casting> → Chant(<typecast_value>)"""
        self.current_nonterminal = "chant_type_casting"
        expected_tokens = self.get_expected_tokens("chant_type_casting")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("chant_type_casting", expected_tokens)
        
        self.expect(TokenType.CHANT)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_typecast_value()
        self.expect(TokenType.RIGHT_PAREN)

    def parse_stat_type_casting(self) -> None:
        """<stat_type_casting> → Stat(<typecast_value>)"""
        self.current_nonterminal = "stat_type_casting"
        expected_tokens = self.get_expected_tokens("stat_type_casting")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("stat_type_casting", expected_tokens)
        
        self.expect(TokenType.STAT)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_typecast_value()
        self.expect(TokenType.RIGHT_PAREN)

    def parse_typecast_value(self) -> None:
        """Helper method to parse typecast value (can be any expression)"""
        self.parse_expression()

    def parse_more_arith_term(self) -> None:
        """<more_arith_term> → λ | + <arith_term><more_arith_term> | - <arith_term><more_arith_term> | 
                            * <arith_term><more_arith_term> | / <arith_term><more_arith_term> | 
                            % <arith_term><more_arith_term>"""
        self.current_nonterminal = "more_arith_term"
        
        # Check if current token is an arithmetic operator
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in [
            TokenType.ADD, TokenType.SUB, TokenType.MUL, TokenType.DIV, TokenType.MOD
        ]):
            return  # λ case
        
        # Handle each arithmetic operator
        if self.match(TokenType.ADD):
            self.parse_arith_term()
            self.parse_more_arith_term()
        elif self.match(TokenType.SUB):
            self.parse_arith_term()
            self.parse_more_arith_term()
        elif self.match(TokenType.MUL):
            self.parse_arith_term()
            self.parse_more_arith_term()
        elif self.match(TokenType.DIV):
            self.parse_arith_term()
            self.parse_more_arith_term()
        elif self.match(TokenType.MOD):
            self.parse_arith_term()
            self.parse_more_arith_term()    

    def parse_relational_expression(self) -> None:
        """<relational_expression> → <number_rel_operand><relational_operator><number_rel_operand> |
                                    <stat_rel_operand><other_relational_operator><stat_rel_operand> |
                                    <chant_rel_operand><other_relational_operator><chant_rel_operand> |
                                    <arithmetic_expression><relational_operator><arithmetic_expression>"""
        self.current_nonterminal = "relational_expression"
        expected_tokens = self.get_expected_tokens("relational_expression")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("relational_expression", expected_tokens)
        
        # Lookahead to determine which type of relational expression
        if self.current_token and self.match_token_type(self.current_token, TokenType.WIN) or self.match_token_type(self.current_token, TokenType.LOSS):
            # Stat relational expression
            self.parse_stat_rel_operand()
            self.parse_other_relational_operator()
            self.parse_stat_rel_operand()
        elif self.current_token and self.match_token_type(self.current_token, TokenType.CHANTLIT):
            # Chant relational expression
            self.parse_chant_rel_operand()
            self.parse_other_relational_operator()
            self.parse_chant_rel_operand()
        else:
            # Default to number/arithmetic relational expression
            self.parse_arithmetic_expression()
            self.parse_relational_operator()
            self.parse_arithmetic_expression()

    def parse_number_rel_operand(self) -> None:
        """<number_rel_operand> → <number> | <number_type_cast>"""
        self.current_nonterminal = "number_rel_operand"
        expected_tokens = self.get_expected_tokens("number_rel_operand")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("number_rel_operand", expected_tokens)
        
        if any(self.match_token_type(self.current_token, t) for t in [TokenType.FEINT, TokenType.FLOATER]):
            self.parse_number_type_cast()
        else:
            self.parse_number()

    def parse_relational_operator(self) -> None:
        """<relational_operator> → < | > | == | <= | >= | !="""
        self.current_nonterminal = "relational_operator"
        expected_tokens = self.get_expected_tokens("relational_operator")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("relational_operator", expected_tokens)
        
        if self.match(TokenType.LESS_THAN):
            pass  # Already advanced in match
        elif self.match(TokenType.GREATER_THAN):
            pass  # Already advanced in match
        elif self.match(TokenType.EQUAL):
            pass  # Already advanced in match
        elif self.match(TokenType.LESS_EQUAL):
            pass  # Already advanced in match
        elif self.match(TokenType.GREATER_EQUAL):
            pass  # Already advanced in match
        elif self.match(TokenType.NOT_EQUAL):
            pass  # Already advanced in match

    def parse_other_relational_operator(self) -> None:
        """<other_relational_operator> → == | !="""
        self.current_nonterminal = "other_relational_operator"
        expected_tokens = self.get_expected_tokens("other_relational_operator")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("other_relational_operator", expected_tokens)
        
        if self.match(TokenType.EQUAL):
            pass  # Already advanced in match
        elif self.match(TokenType.NOT_EQUAL):
            pass  # Already advanced in match

    def parse_stat_rel_operand(self) -> None:
        """<stat_rel_operand> → <stat_value> | @identifier | <stat_type_casting>"""
        self.current_nonterminal = "stat_rel_operand"
        expected_tokens = self.get_expected_tokens("stat_rel_operand")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("stat_rel_operand", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.WIN) or self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_stat_value()
        elif self.match(TokenType.VAR_INIT):
            pass  # Already advanced in match
        elif self.match_token_type(self.current_token, TokenType.STAT):
            self.parse_stat_type_casting()

    def parse_stat_value(self) -> None:
        """<stat_value> → WIN | LOSS"""
        self.current_nonterminal = "stat_value"
        
        if self.match(TokenType.WIN):
            pass  # Already advanced in match
        elif self.match(TokenType.LOSS):
            pass  # Already advanced in match
        else:
            self.error_handler("stat_value", {TokenType.WIN, TokenType.LOSS})

    def parse_chant_rel_operand(self) -> None:
        """<chant_rel_operand> → @identifier | <chant_type_casting> | <chant_lit>"""
        self.current_nonterminal = "chant_rel_operand"
        expected_tokens = self.get_expected_tokens("chant_rel_operand")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("chant_rel_operand", expected_tokens)
        
        if self.match(TokenType.VAR_INIT):
            pass  # Already advanced in match
        elif self.match_token_type(self.current_token, TokenType.CHANT):
            self.parse_chant_type_casting()
        elif self.match_token_type(self.current_token, TokenType.CHANTLIT):
            self.parse_chant_lit()

    def parse_logical_expression(self) -> None:
        """<logical_expression> → <not_expr> | <compound_log_expr>"""
        self.current_nonterminal = "logical_expression"
        expected_tokens = self.get_expected_tokens("logical_expression")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("logical_expression", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.NOT_OP):
            self.parse_not_expr()
        else:
            self.parse_compound_log_expr()

    def parse_not_expr(self) -> None:
        """<not_expr> → NOT <other_log_term>"""
        self.current_nonterminal = "not_expr"
        
        self.expect(TokenType.NOT_OP)
        self.parse_other_log_term()

    def parse_compound_log_expr(self) -> None:
        """<compound_log_expr> → <log_term><log_operator><log_term><more_log_term>"""
        self.current_nonterminal = "compound_log_expr"
        
        self.parse_log_term()
        self.parse_log_operator()
        self.parse_log_term()
        self.parse_more_log_term()

    def parse_log_term(self) -> None:
        """<log_term> → <not_expr> | <other_log_term>"""
        self.current_nonterminal = "log_term"
        expected_tokens = self.get_expected_tokens("log_term")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("log_term", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.NOT_OP):
            self.parse_not_expr()
        else:
            self.parse_other_log_term()

    def parse_other_log_term(self) -> None:
        """<other_log_term> → <stat_value> | (<relational_expression>) | <number>"""
        self.current_nonterminal = "other_log_term"
        expected_tokens = self.get_expected_tokens("other_log_term")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("other_log_term", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.WIN) or self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_stat_value()
        elif self.match(TokenType.LEFT_PAREN):
            self.parse_relational_expression()
            self.expect(TokenType.RIGHT_PAREN)
        else:
            self.parse_number()

    def parse_more_log_term(self) -> None:
        """<more_log_term> → λ | <log_operator><log_term><more_log_term>"""
        self.current_nonterminal = "more_log_term"
        
        # Check if we should continue or return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in [TokenType.AND_OP, TokenType.OR_OP]):
            return  # λ case
        
        self.parse_log_operator()
        self.parse_log_term()
        self.parse_more_log_term()

    def parse_log_operator(self) -> None:
        """<log_operator> → AND | OR"""
        self.current_nonterminal = "log_operator"
        expected_tokens = self.get_expected_tokens("log_operator")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("log_operator", expected_tokens)
        
        if self.match(TokenType.AND_OP):
            pass  # Already advanced in match
        elif self.match(TokenType.OR_OP):
            pass  # Already advanced in match

    def parse_assignment_expression(self) -> None:
        """<assignment_expression> → @identifier <assign_operator> <assign_operand>;"""
        self.current_nonterminal = "assignment_expression"
        expected_tokens = self.get_expected_tokens("assignment_expression")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("assignment_expression", expected_tokens)
        
        self.expect(TokenType.VAR_INIT)
        self.parse_assign_operator()
        self.parse_assign_operand()
        self.expect(TokenType.SEMICOLON)

    def parse_assign_operator(self) -> None:
        """<assign_operator> → = | += | -= | *= | /= | %="""
        self.current_nonterminal = "assign_operator"
        expected_tokens = self.get_expected_tokens("assign_operator")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("assign_operator", expected_tokens)
        
        if self.match(TokenType.ASSIGN):
            pass  # Already advanced in match
        elif self.match(TokenType.ADD_ASSIGN):
            pass  # Already advanced in match
        elif self.match(TokenType.SUB_ASSIGN):
            pass  # Already advanced in match
        elif self.match(TokenType.MUL_ASSIGN):
            pass  # Already advanced in match
        elif self.match(TokenType.DIV_ASSIGN):
            pass  # Already advanced in match
        elif self.match(TokenType.MOD_ASSIGN):
            pass  # Already advanced in match

    def parse_assign_operand(self) -> None:
        """<assign_operand> → <arithmetic_expression> | <relational_expression> | <logical_expression> | <function_call>"""
        self.current_nonterminal = "assign_operand"
        expected_tokens = self.get_expected_tokens("assign_operand")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("assign_operand", expected_tokens)
        
        # Check for function call first (special case)
        if self.current_token and self.match_token_type(self.current_token, TokenType.VAR_INIT) and self.peek() and self.match_token_type(self.peek(), TokenType.LEFT_PAREN):
            self.parse_function_call()
            return
        
        # Then try to determine the type of expression
        if self.current_token and self.match_token_type(self.current_token, TokenType.NOT_OP):
            self.parse_logical_expression()
        elif self.peek() and any(self.match_token_type(self.peek(), t) for t in [
            TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL, 
            TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL, TokenType.NOT_EQUAL
        ]):
            self.parse_relational_expression()
        else:
            self.parse_arithmetic_expression()

    def parse_function_call(self) -> None:
        """<function_call> → @identifier(<arguments>)"""
        self.current_nonterminal = "function_call"
        expected_tokens = self.get_expected_tokens("function_call")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("function_call", expected_tokens)
        
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_arguments()
        self.expect(TokenType.RIGHT_PAREN)

    def parse_arguments(self) -> None:
        """<arguments> → <arg><more_args> | λ"""
        self.current_nonterminal = "arguments"
        expected_tokens = self.get_expected_tokens("arguments")
        
        # If we have a token that could start an argument, parse it
        if self.current_token and any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.parse_arg()
            self.parse_more_args()
        # The λ case is handled implicitly by just returning

    def parse_arg(self) -> None:
        """<arg> → <literal> | @identifier"""
        self.current_nonterminal = "arg"
        expected_tokens = self.get_expected_tokens("arg")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("arg", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.VAR_INIT):
            self.advance()  # Already matched VAR_INIT
        else:
            self.parse_literal()

    def parse_more_args(self) -> None:
        """<more_args> → , <arg><more_args> | λ"""
        self.current_nonterminal = "more_args"
        expected_tokens = self.get_expected_tokens("more_args")
        
        # If we have a comma, parse more arguments
        if self.current_token and self.match_token_type(self.current_token, TokenType.COMMA):
            self.advance()  # Already matched COMMA
            self.parse_arg()
            self.parse_more_args()
        # The λ case is handled implicitly by just returning

    def parse_inbound_statement(self) -> None:
        """<inbound_statement> → Inbound(<chant_lit>, @identifier);"""
        self.current_nonterminal = "inbound_statement"
        expected_tokens = self.get_expected_tokens("inbound_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("inbound_statement", expected_tokens)
        
        self.expect(TokenType.INBOUND)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_chant_lit()
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.SEMICOLON)

    def parse_dribble_statement(self) -> None:
        """<dribble_statement> → Dribble (<expression>) {<loop_statements>} <add_condition>"""
        self.current_nonterminal = "dribble_statement"
        expected_tokens = self.get_expected_tokens("dribble_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("dribble_statement", expected_tokens)
        
        self.expect(TokenType.DRIBBLE)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_expression()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_loop_statements()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_add_condition()

    def parse_add_condition(self) -> None:
        """<add_condition> → Pass (<expression>) {<loop_statements>} <add_condition>
                            | Shoot {<loop_statements>}
                            | λ"""
        self.current_nonterminal = "add_condition"
        
        if not self.current_token:
            return  # λ case
        
        if self.match_token_type(self.current_token, TokenType.PASS):
            self.advance()
            self.expect(TokenType.LEFT_PAREN)
            self.parse_expression()
            self.expect(TokenType.RIGHT_PAREN)
            self.expect(TokenType.CODE_BLOCK_LEFT)
            self.parse_loop_statements()
            self.expect(TokenType.CODE_BLOCK_RIGHT)
            self.parse_add_condition()
        elif self.match_token_type(self.current_token, TokenType.SHOOT):
            self.advance()
            self.expect(TokenType.CODE_BLOCK_LEFT)
            self.parse_loop_statements()
            self.expect(TokenType.CODE_BLOCK_RIGHT)
        # The λ case is handled implicitly by just returning

    def parse_loop_statements(self) -> None:
        """<loop_statements> → <loop_statement><loop_statements> | λ"""
        self.current_nonterminal = "loop_statements"
        
        # If we've reached the end of loop block or no token, return
        if not self.current_token or self.match_token_type(self.current_token, TokenType.CODE_BLOCK_RIGHT):
            return  # λ case
        
        self.parse_loop_statement()
        self.parse_loop_statements()  # Recursive call

    def parse_loop_statement(self) -> None:
        """<loop_statement> → <team_statements> | <resume_statement>"""
        self.current_nonterminal = "loop_statement"
        
        if self.match_token_type(self.current_token, TokenType.RESUME):
            self.parse_resume_statement()
        else:
            self.parse_team_statements()

    def parse_resume_statement(self) -> None:
        """<resume_statement> → Resume; | λ"""
        self.current_nonterminal = "resume_statement"
        
        if self.match_token_type(self.current_token, TokenType.RESUME):
            self.advance()
            self.expect(TokenType.SEMICOLON) 
            return  # λ case

    def parse_switch_statement(self) -> None:
        """<switch_statement> → Switch (@identifier) { <get_case> <get_default> }"""
        self.current_nonterminal = "switch_statement"
        expected_tokens = self.get_expected_tokens("switch_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("switch_statement", expected_tokens)
        
        self.expect(TokenType.SWITCH)
        self.expect(TokenType.LEFT_PAREN)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_get_case()
        self.parse_get_default()
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_get_case(self) -> None:
        """<get_case> → Get <get_value>: <team_statements> <timeout_statement> <get_case_end>"""
        self.current_nonterminal = "get_case"
        expected_tokens = self.get_expected_tokens("get_case")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("get_case", expected_tokens)
        
        self.expect(TokenType.GET)
        self.parse_get_value()
        self.expect(TokenType.COLON)
        self.parse_team_statements()
        self.parse_timeout_statement()
        self.parse_get_case_end()

    def parse_get_value(self) -> None:
        """<get_value> → <feint_lit> | <chant_lit>"""
        self.current_nonterminal = "get_value"
        expected_tokens = self.get_expected_tokens("get_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("get_value", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        else:
            self.parse_chant_lit()

    def parse_timeout_statement(self) -> None:
        """<timeout_statement> → Timeout;"""
        self.current_nonterminal = "timeout_statement"
        
        self.expect(TokenType.TIMEOUT)
        self.expect(TokenType.SEMICOLON)

    def parse_get_case_end(self) -> None:
        """<get_case_end> → λ | <get_case>"""
        self.current_nonterminal = "get_case_end"
        
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.GET):
            return  # λ case
        
        self.parse_get_case()  # Recursive call for multiple cases

    def parse_get_default(self) -> None:
        """<get_default> → Default: <team_statements> | λ"""
        self.current_nonterminal = "get_default"
        expected_tokens = self.get_expected_tokens("get_default")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        self.expect(TokenType.DEFAULT)
        self.expect(TokenType.COLON)
        self.parse_team_statements()

    def parse_forward_statement(self) -> None:
        """<forward_statement> → Forward (@identifier = <forward_lit>; <expression>; @identifier <forward_inc_dec>) { <team_statements> }"""
        self.current_nonterminal = "forward_statement"
        expected_tokens = self.get_expected_tokens("forward_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("forward_statement", expected_tokens)
        
        self.expect(TokenType.FORWARD)
        self.expect(TokenType.LEFT_PAREN)
        self.expect(TokenType.VAR_INIT)
        self.expect(TokenType.ASSIGN)
        self.parse_forward_lit()
        self.expect(TokenType.SEMICOLON)
        self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        self.expect(TokenType.VAR_INIT)
        self.parse_forward_inc_dec()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_team_statements()
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_forward_lit(self) -> None:
        """<forward_lit> → Feint literal | @identifier"""
        self.current_nonterminal = "forward_lit"
        expected_tokens = self.get_expected_tokens("forward_lit")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("forward_lit", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.advance()
        else:
            self.expect(TokenType.VAR_INIT)

    def parse_forward_inc_dec(self) -> None:
        """<forward_inc_dec> → <increment> | <decrement> | <forward_assign_operator> <forward_lit>"""
        self.current_nonterminal = "forward_inc_dec"
        
        if self.match_token_type(self.current_token, TokenType.INCREMENT):
            self.advance()  # Already matched INCREMENT
        elif self.match_token_type(self.current_token, TokenType.DECREMENT):
            self.advance()  # Already matched DECREMENT
        else:
            self.parse_forward_assign_operator()
            self.parse_forward_lit()

    def parse_increment(self) -> None:
        """<increment> → ++"""
        self.current_nonterminal = "increment"
        expected_tokens = self.get_expected_tokens("increment")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("increment", expected_tokens)
            
        self.expect(TokenType.INCREMENT)

    def parse_decrement(self) -> None:
        """<decrement> → --"""
        self.current_nonterminal = "decrement"
        expected_tokens = self.get_expected_tokens("decrement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("decrement", expected_tokens)
            
        self.expect(TokenType.DECREMENT)

    def parse_forward_assign_operator(self) -> None:
        """<forward_assign_operator> → += | -="""
        self.current_nonterminal = "forward_assign_operator"
        
        if self.match_token_type(self.current_token, TokenType.ADD_ASSIGN):
            self.advance()
        elif self.match_token_type(self.current_token, TokenType.SUB_ASSIGN):
            self.advance()
        else:
            self.error_handler("forward_assign_operator", {TokenType.ADD_ASSIGN, TokenType.SUB_ASSIGN})

    def parse_play_statement(self) -> None:
        """<play_statement> → Play (<expression>){<team_statements>}"""
        self.current_nonterminal = "play_statement"
        expected_tokens = self.get_expected_tokens("play_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("play_statement", expected_tokens)
        
        self.expect(TokenType.PLAY)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_expression()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_team_statements()
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_run_play_statement(self) -> None:
        """<run_play_statement> → Run{<team_statements>} Play (<expression>);"""
        self.current_nonterminal = "run_play_statement"
        expected_tokens = self.get_expected_tokens("run_play_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("run_play_statement", expected_tokens)
        
        self.expect(TokenType.RUN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_team_statements()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.expect(TokenType.PLAY)
        self.expect(TokenType.LEFT_PAREN)
        self.parse_expression()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.SEMICOLON)

    def parse_team_block(self) -> None:
        """<team_block> → Team() { <local_decl> <team_statements> }"""
        self.current_nonterminal = "team_block"
        expected_tokens = self.get_expected_tokens("team_block")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("team_block", expected_tokens)
        
        self.expect(TokenType.TEAM)
        self.expect(TokenType.LEFT_PAREN)
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        
        # Parse local declarations
        self.parse_local_decl()
        
        # Parse team statements
        self.parse_team_statements()
        
        self.expect(TokenType.CODE_BLOCK_RIGHT)

    def parse_local_decl(self) -> None:
        """<local_decl> → <local_declaration><local_decl> | λ"""
        self.current_nonterminal = "local_decl"
        expected_tokens = self.get_expected_tokens("local_decl")
        
        # Check if current token is in FIRST(local_declaration)
        if self.current_token and any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.parse_local_declaration()
            self.parse_local_decl()  # Recursive call for more local declarations
        # The λ case is handled implicitly by just returning

    def parse_local_declaration(self) -> None:
        """<local_declaration> → <variable_dec> | <array_dec>"""
        self.current_nonterminal = "local_declaration"
        expected_tokens = self.get_expected_tokens("local_declaration")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("local_declaration", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.ZONE):
            self.parse_array_dec()
        else:
            self.parse_variable_dec()

    def parse_typecast_value(self) -> None:
        """<typecast_value> → <feint_typecast_value> | <floater_typecast_value> | <chant_typecast_value> | <stat_typecast_value> | @identifier"""
        self.current_nonterminal = "typecast_value"
        expected_tokens = self.get_expected_tokens("typecast_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("typecast_value", expected_tokens)
        
        # Determine which type of typecast value we're dealing with
        if self.match_token_type(self.current_token, TokenType.VAR_INIT):
            self.expect(TokenType.VAR_INIT)
        elif self.match_token_type(self.current_token, TokenType.FLOATERLIT) and any(self.match_token_type(self.peek(), t) for t in [TokenType.FEINT]):
            self.parse_feint_typecast_value()
        elif self.match_token_type(self.current_token, TokenType.FEINTLIT) and any(self.match_token_type(self.peek(), t) for t in [TokenType.FLOATER]):
            self.parse_floater_typecast_value()
        elif any(self.match_token_type(self.current_token, t) for t in [TokenType.FEINTLIT, TokenType.FLOATERLIT]) and any(self.match_token_type(self.peek(), t) for t in [TokenType.CHANT]):
            self.parse_chant_typecast_value()
        elif any(self.match_token_type(self.current_token, t) for t in [TokenType.FEINTLIT, TokenType.FLOATERLIT, TokenType.CHANTLIT]) and any(self.match_token_type(self.peek(), t) for t in [TokenType.STAT]):
            self.parse_stat_typecast_value()
        else:
            # Default case - handle based on token type
            if self.match_token_type(self.current_token, TokenType.FEINTLIT):
                self.parse_feint_lit()
            elif self.match_token_type(self.current_token, TokenType.FLOATERLIT):
                self.parse_floater_lit()
            elif self.match_token_type(self.current_token, TokenType.CHANTLIT):
                self.parse_chant_lit()
            elif self.match_token_type(self.current_token, TokenType.WIN) or self.match_token_type(self.current_token, TokenType.LOSS):
                self.parse_stat_value()

    def parse_feint_typecast_value(self) -> None:
        """<feint_typecast_value> → <floater_lit> | <chant_lit> | <stat_value>"""
        self.current_nonterminal = "feint_typecast_value"
        expected_tokens = self.get_expected_tokens("feint_typecast_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("feint_typecast_value", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FLOATERLIT):
            self.parse_floater_lit()
        elif self.match_token_type(self.current_token, TokenType.CHANTLIT):
            self.parse_chant_lit()
        elif self.match_token_type(self.current_token, TokenType.WIN) or self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_stat_value()

    def parse_floater_typecast_value(self) -> None:
        """<floater_typecast_value> → <feint_lit> | <chant_lit> | <stat_value>"""
        self.current_nonterminal = "floater_typecast_value"
        expected_tokens = self.get_expected_tokens("floater_typecast_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("floater_typecast_value", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        elif self.match_token_type(self.current_token, TokenType.CHANTLIT):
            self.parse_chant_lit()
        elif self.match_token_type(self.current_token, TokenType.WIN) or self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_stat_value()

    def parse_chant_typecast_value(self) -> None:
        """<chant_typecast_value> → <feint_lit> | <floater_lit> | <stat_value>"""
        self.current_nonterminal = "chant_typecast_value"
        expected_tokens = self.get_expected_tokens("chant_typecast_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("chant_typecast_value", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        elif self.match_token_type(self.current_token, TokenType.FLOATERLIT):
            self.parse_floater_lit()
        elif self.match_token_type(self.current_token, TokenType.WIN) or self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_stat_value()

    def parse_stat_typecast_value(self) -> None:
        """<stat_typecast_value> → <feint_lit> | <floater_lit> | <chant_lit>"""
        self.current_nonterminal = "stat_typecast_value"
        expected_tokens = self.get_expected_tokens("stat_typecast_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("stat_typecast_value", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        elif self.match_token_type(self.current_token, TokenType.FLOATERLIT):
            self.parse_floater_lit()
        elif self.match_token_type(self.current_token, TokenType.CHANTLIT):
            self.parse_chant_lit()

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
        # print("\033[92mSyntax Analysis Complete: No syntax errors found!\033[0m")
        return True
    except SyntaxError as e:
        # Instead of printing to console, re-raise the error so it can be caught by the editor
        raise