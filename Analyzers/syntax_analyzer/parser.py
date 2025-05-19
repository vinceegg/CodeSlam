from Analyzers.lexical_analyzer.tokens import TokenType, Token
from typing import List, Optional, Set, Literal
from Analyzers.syntax_analyzer.errors import SyntaxError 
from Analyzers.syntax_analyzer.first_sets import FIRST_SETS
from Analyzers.syntax_analyzer.follow_sets import FOLLOW_SETS 
from Analyzers.syntax_analyzer.predict_sets import PREDICT_SETS

# Define an ErrorSetType enum using string literals
ErrorSetType = Literal["FIRST", "FOLLOW", "PREDICT"]

class Parser:

    """
        Initialize the parser with a list of tokens from the lexer.
        
        How it works:
        - Stores the token list and sets the current position to the first token
        - Sets up tracking for line numbers and columns for error reporting
        - Prepares to track the current grammar rule being processed
    """
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens                                        # Store all tokens from lexer
        self.current = 0                                            # Index of current token
        self.current_token = self.tokens[0] if tokens else None     # Current token being processed
        self.line_number = 1                                        # Track current line number
        self.column = 0                                             # Track current column position
        self.expected_tokens = set()                                # Set of tokens we might expect
        self.line_starts = {1: 0}                                   # Track the starting position of each line
        self.current_line_content = ""                              # Track content of current line
        self.current_nonterminal = None                             # Track current nonterminal being parsed

        self.skip_whitespace_and_comments()
        
    def get_expected_tokens(self, nonterminal: str) -> Set[TokenType]:
        """
            Get all tokens that can legally appear first in a grammar rule.
            
            How it works:
            - Looks up the grammar rule in the FIRST_SETS dictionary
            - Returns all tokens that can legally start this grammar rule
            - This is used for error reporting and prediction
            
            Example: For a rule like <expr> → id + <expr> | num * <expr>,
                    the FIRST set would be {id, num}
        """
        if nonterminal in FIRST_SETS:
            return FIRST_SETS[nonterminal]
        return set()

    def get_follow_tokens(self, nonterminal: str) -> Set[TokenType]:
        """
        Get all tokens that can legally follow after a grammar rule is completed.
        
        How it works:
        - Looks up the grammar rule in the FOLLOW_SETS dictionary
        - Returns all tokens that can legally come after this rule
        - This helps with error recovery and checking for rule boundaries
        
        Example: For a rule like <term> within <expr> → <term> + <factor>,
                 the FOLLOW set would include {+, ), ;, etc.}
        """
        if nonterminal in FOLLOW_SETS:
            return FOLLOW_SETS[nonterminal]
        return set()
    
    def get_predict_tokens(self, nonterminal: str) -> Set[TokenType]:
        """
        Get all tokens that can predict which production to use for a rule.
        
        How it works:
        - Looks up the grammar rule in the PREDICT_SETS dictionary
        - Returns all tokens that can help predict which production to follow
        - This is used for deterministic parsing decisions
        
        Example: For rules like <stmt> → if(...) {...} | while(...) {...},
                 PREDICT_SETS['stmt'] would include {if, while}
        """
        if nonterminal in PREDICT_SETS:
            return PREDICT_SETS[nonterminal]
        return set()

    def get_production_rule(self, nonterminal: str, token_type: TokenType) -> Optional[int]:
        """
        Get the specific grammar production to use based on the current token.
        
        How it works:
        - Uses the PREDICT_SETS dictionary to look up which production to follow
        - PREDICT_SETS maps (nonterminal, token) pairs to production rule numbers
        - This makes parsing decisions deterministic based on the current token
        
        Example: For rules like <stmt> → if(...) {...} | while(...) {...},
                 PREDICT[(stmt, if)] would return production #1
        """
        if (nonterminal, token_type) in PREDICT_SETS:
            return PREDICT_SETS[(nonterminal, token_type)]
        return None

    def error_handler(self, nonterminal: str, error_set_type: ErrorSetType = "FIRST", expected_tokens: Set[TokenType] = None) -> None:
        """
        Create detailed syntax error messages when parsing fails, using the specified error set type.
        
        How it works:
        - Uses the specified error set type (FIRST, FOLLOW, or PREDICT) to determine expected tokens
        - If expected_tokens is provided, it overrides the error set type
        - Builds a detailed error message with line/column information
        - Reports what token was found vs. what was expected
        
        Parameters:
        - nonterminal: The grammar rule currently being parsed
        - error_set_type: Which set of tokens to use for error reporting ("FIRST", "FOLLOW", or "PREDICT")
        - expected_tokens: Optional explicit set of expected tokens
        
        This enhanced handler adds flexibility in choosing which set of tokens to use for error reporting.
        """
        # If no expected tokens specified, get them based on the error_set_type
        if expected_tokens is None:
            if error_set_type == "FIRST":
                expected_tokens = self.get_expected_tokens(nonterminal)
            elif error_set_type == "FOLLOW":
                expected_tokens = self.get_follow_tokens(nonterminal)
            elif error_set_type == "PREDICT":
                expected_tokens = self.get_predict_tokens(nonterminal)
            else:
                # Default to FIRST set if invalid error_set_type
                expected_tokens = self.get_expected_tokens(nonterminal)

        if self.current_token:
            # We have a token but it's the wrong one
            token_type = self.current_token.type
            token_value = self.current_token.value
            production_rule = self.get_production_rule(nonterminal, token_type)
            
            # Build detailed error message
            error_msg = f"Syntax Error at line {self.line_number}, column {self.column}:\n"
            error_msg += f"Unexpected Token: {token_value}\n"
            
            # Use token values instead of enum names for expected tokens
            expected_tokens_str = ', '.join(t.value for t in expected_tokens if hasattr(t, 'value'))
            error_msg += f"Expected Token ({error_set_type} Set): {{{expected_tokens_str}}}"
            
            # Raise the error with detailed information
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected=', '.join(t.value for t in expected_tokens if hasattr(t, 'value')),
                token=token_value,
                nonterminal=nonterminal,
                production_rule=production_rule
            )
        else:
            # We ran out of tokens unexpectedly (end of file)
            error_msg = f"Syntax Error at line {self.line_number}, column {self.column}:\n"
            error_msg += f"Unexpected end of file while parsing {nonterminal}.\n"
            # Use token values instead of enum names for expected tokens
            expected_tokens_str = ', '.join(t.value for t in expected_tokens if hasattr(t, 'value'))
            error_msg += f"Expected Token ({error_set_type} Set): {{{expected_tokens_str}}}"
            
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected=', '.join(t.value for t in expected_tokens if hasattr(t, 'value')),
                token="EOF",
                nonterminal=nonterminal
            )


    def skip_whitespace_and_comments(self):
        """
        Skip over tokens that don't affect the grammar parsing.
        
        How it works:
        - Skips spaces, tabs, newlines, and comments
        - Updates line/column tracking when encountering newlines
        - Ensures parser only processes meaningful tokens
        """

        # Loop while current token is something we want to skip
        while self.current_token and self.current_token.type in [
            TokenType.SPACE,
            TokenType.TAB,
            TokenType.NEWLINE,
            TokenType.SINGLE_COMMENT,
            TokenType.MULTI_COMMENT
        ]:
            # Update line number when we see a newline
            if self.current_token.type == TokenType.NEWLINE:
                self.line_number += 1
                self.column = 0
                self.line_starts[self.line_number] = 0
                self.current_line_content = ""
            elif self.current_token.type in [TokenType.SPACE, TokenType.TAB]:
                # Add spaces to track column position accurately
                self.current_line_content += " " * (1 if self.current_token.type == TokenType.TAB else 1)
                
            # Move to next token
            self.current += 1
            if self.current < len(self.tokens):
                self.current_token = self.tokens[self.current]
            else:
                self.current_token = None
                break

    def update_position(self, token):
        """
        Update line and column tracking after processing a token.
        
        How it works:
        - Updates line number when encountering a newline
        - Updates column position for accurate error reporting
        - Maintains the current line content for context
        """
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
        """
        Move to the next token in the input stream.
        
        How it works:
        - Updates position tracking for the current token
        - Moves to the next token in the list
        - Automatically skips whitespace and comments
        
        This is a key function used whenever we successfully process a token
        and want to move to the next one.
        """
        if self.current_token:
            self.update_position(self.current_token)
            
        # Move to next token
        self.current += 1
        if self.current < len(self.tokens):
            self.current_token = self.tokens[self.current]
            # Skip any whitespace or comments after advancing
            self.skip_whitespace_and_comments()
        else:
            self.current_token = None

    def peek(self) -> Optional[Token]:
        """
        Look ahead at the next token without advancing.
        
        How it works:
        - Returns the next token without changing the current position
        - Useful for making decisions that require lookahead
        """
        if self.current + 1 >= len(self.tokens):
            return None
        return self.tokens[self.current + 1]

    def get_token_type(self, token_value: str) -> TokenType:
        """
        Convert a token's string value to its TokenType enum.
        
        How it works:
        - Tries to convert a string like "if" to TokenType.IF
        - Returns None if conversion fails
        - Helps match tokens by either their type or value
        """
        try:
            return TokenType[token_value.upper()]
        except KeyError:
            # If not found, return the original token type
            return None

    def match_token_type(self, token: Token, expected_type: TokenType) -> bool:
        """
        Check if a token matches an expected type.
        
        How it works:
        - Matches by either direct type comparison or by comparing the token's value
        - For example, a token with value "if" would match TokenType.IF
        - This flexibility makes the parser more robust
        """
        if not token:
            return False
        
        # Get the TokenType for the token's value
        value_type = self.get_token_type(token.value) if token.value else None
        
        # Check if either the token's type matches or its value converts to the expected type
        return token.type == expected_type or value_type == expected_type

    def expect(self, token_type: TokenType, error_set_type: ErrorSetType = "FIRST", strict: bool = False) -> None:
        """
        Expect a specific token type and consume it, or raise an error.
        
        How it works:
        - If current token matches the expected type, advance to next token
        - If not, raise a syntax error with detailed information based on the specified error set type
        - The strict parameter controls whether to show only the specific expected token
          or a broader set of expected tokens in the error message
        
        Parameters:
        - token_type: The token type expected at this position
        - error_set_type: Which set to use for error reporting ("FIRST", "FOLLOW", or "PREDICT")
        - strict: Whether to only show the specific expected token in error messages
        
        This function is used when a specific token must be present.
        """
        if self.current_token and self.match_token_type(self.current_token, token_type):
            # Token matches, consume it
            self.advance()
        else:
            # In strict mode, only show the specific expected token
            if strict:
                expected_tokens = {token_type}
                self.error_handler(self.current_nonterminal, error_set_type, expected_tokens)
            else:
                # In regular mode, show tokens based on the specified error set type
                if error_set_type == "FIRST":
                    expected_tokens = self.get_expected_tokens(self.current_nonterminal)
                elif error_set_type == "FOLLOW":
                    expected_tokens = self.get_follow_tokens(self.current_nonterminal)
                elif error_set_type == "PREDICT":
                    expected_tokens = self.get_predict_tokens(self.current_nonterminal)
                else:
                    # Default to FIRST set if invalid error_set_type
                    expected_tokens = self.get_expected_tokens(self.current_nonterminal)
                
                # Add the specific expected token
                expected_tokens.add(token_type)
                self.error_handler(self.current_nonterminal, error_set_type, expected_tokens)

    def match(self, expected_type: TokenType) -> bool:
        """
        Check if current token matches expected type and advance if it does.
        
        How it works:
        - Similar to expect() but returns boolean instead of raising error
        - Used when a token is optional or one of several alternatives
        - Returns True if token matched and was consumed, False otherwise
        """
        if self.current_token and self.match_token_type(self.current_token, expected_type):
            self.advance()
            return True
        return False
            
    def parse(self) -> None:
        """
        Start parsing the program from the top-level rule.
        
        How it works:
        - Calls parse_program() to start the recursive descent process
        - Catches and prints any syntax errors that occur
        - This is the main entry point for parsing
        """
        try:
            self.parse_program()
        except SyntaxError as e:
            print(f"Syntax Error: {str(e)}")
            raise

    def parse_program(self) -> None:
        """<program> → <global_decl> <function_def> <team_block>"""
        self.current_nonterminal = "program"
        expected_tokens = self.get_expected_tokens("program")
        
        # Check if we have a valid starting token for the program
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("program", "FIRST", expected_tokens)

        # Track if we've seen each section to enforce order
        seen_global_decl = False
        seen_function_def = False
        seen_team_block = False
        
        # Check for global declarations (can be empty, indicated by λ)
        if self.current_token and any(self.match_token_type(self.current_token, t) 
                                    for t in self.get_expected_tokens("global_decl")):
            seen_global_decl = True
            self.parse_global_decl()
        
        # After global declarations, check for function definitions (can be empty, indicated by λ)
        if self.current_token and any(self.match_token_type(self.current_token, t) 
                                    for t in self.get_expected_tokens("function_def")):
            seen_function_def = True
            self.parse_function_def()
        
        # Finally, the team block is required
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.TEAM):
            error_msg = "Program structure error: Missing required Team block at the end"
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected="Team block",
                token=self.current_token.value if self.current_token else "EOF",
                nonterminal="program"
            )
        
        seen_team_block = True
        self.parse_team_block()
        
        # Ensure no tokens remain after the program
        if self.current_token:
            error_msg = f"Syntax Error at line {self.line_number}, column {self.column}:\n"
            error_msg += f"Unexpected token '{self.current_token.value}' after program end.\n"
            error_msg += "All code must be within the global declarations, function definitions, or Team block."
            
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected="Incorrect Structure of the Program",
                token=self.current_token.value,
                nonterminal="program"
            )

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
        """<global_declaration> → <variable_dec> | Const <const_dec> | Zone <array_dec>"""
        self.current_nonterminal = "global_declaration"
        expected_tokens = self.get_expected_tokens("global_declaration")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("global_declaration", "FIRST", expected_tokens)

        # ADDED
        start_line = self.line_number
        
        # Check which type of declaration follows
        if self.current_token and self.match_token_type(self.current_token, TokenType.CONST):
            self.parse_const_dec()
        elif self.current_token and self.match_token_type(self.current_token, TokenType.ZONE):
            self.expect(TokenType.ZONE)  # Consume ZONE token
            self.parse_array_dec()
        else:
            self.parse_variable_dec()

        # ADDED
        if self.current_token and self.line_number == start_line:
            error_msg = f"Syntax Error at line {self.line_number}, column {self.column}:\n"
            error_msg += "Multiple declarations on the same line are not allowed."
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected="Each declaration must be on a separate line",
                token=self.current_token.value,
                nonterminal="global_declaration"
            )

    def parse_variable_dec(self) -> None:
        """<variable_dec> → <feint_dec> | <floater_dec> | <chant_dec> | <stat_dec>"""
        self.current_nonterminal = "variable_dec"
        expected_tokens = self.get_expected_tokens("variable_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("variable_dec", "FIRST", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINT):
            self.parse_feint_dec()
        elif self.match_token_type(self.current_token, TokenType.FLOATER):
            self.parse_floater_dec()
        elif self.match_token_type(self.current_token, TokenType.CHANT):
            self.parse_chant_dec()
        elif self.match_token_type(self.current_token, TokenType.STAT):
            self.parse_stat_dec()
        else:
            self.error_handler("variable_dec", "FIRST")

    def parse_feint_dec(self) -> None:
        """<feint_dec> → Feint @identifier <more_feint>;"""
        self.current_nonterminal = "feint_dec"
        expected_tokens = self.get_expected_tokens("feint_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("feint_dec", "FIRST", expected_tokens)
        
        self.expect(TokenType.FEINT)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_feint()
        self.expect(TokenType.SEMICOLON)   
        
    def parse_more_feint(self) -> None:
        """<more_feint> → λ | <feint_init> <feint_init_end>"""
        self.current_nonterminal = "more_feint"
        expected_tokens = self.get_predict_tokens("more_feint")  # Using PREDICT set
        
        # If we don't have tokens in FIRST(feint_init), return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # If there's an error, use PREDICT set
        # if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
        #     self.error_handler("more_feint", "PREDICT", expected_tokens)
        
        self.parse_feint_init()
        self.parse_feint_init_end()

    def parse_feint_init(self) -> None:
        """<feint_init> → λ | = <feint_lit> <feint_init_end>"""
        self.current_nonterminal = "feint_init"
        expected_tokens = self.get_expected_tokens("feint_init")
        
        # If we don't have an ASSIGN token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_feint_lit()
        self.parse_feint_init_end()

    def parse_feint_lit(self) -> None:
        """<feint_lit> → Feint Literal | <nega_feint_lit>"""
        self.current_nonterminal = "feint_lit"
        expected_tokens = self.get_expected_tokens("feint_lit")
        
        if self.current_token and self.match_token_type(self.current_token, TokenType.NEGAFEINT):
            # Handle negation case
            self.parse_nega_feint_lit()
        elif not self.current_token or not self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.error_handler("feint_lit", "FIRST", expected_tokens)
        else:
            # Regular feint literal case
            self.expect(TokenType.FEINTLIT)

    def parse_feint_init_end(self) -> None:
        """<feint_init_end> → λ | , @identifier <more_feint>"""
        self.current_nonterminal = "feint_init_end"
        expected_tokens = self.get_expected_tokens("feint_init_end")
        
        # If we don't have a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_feint()

    def parse_floater_dec(self) -> None:
        """<floater_dec> → Floater @identifier <more_floater>;"""
        self.current_nonterminal = "floater_dec"
        expected_tokens = self.get_expected_tokens("floater_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("floater_dec", "FIRST", expected_tokens)
        
        self.expect(TokenType.FLOATER)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_floater()
        self.expect(TokenType.SEMICOLON)

    def parse_more_floater(self) -> None:
        """<more_floater> → λ | <floater_init> <floater_init_end>"""
        self.current_nonterminal = "more_floater"
        expected_tokens = self.get_predict_tokens("more_floater")
        
        # If we don't have tokens in FIRST(floater_init), return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # If there's an error, use PREDICT set
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("more_floater", "PREDICT", expected_tokens)
        
        self.parse_floater_init()
        self.parse_floater_init_end()

    def parse_floater_init(self) -> None:
        """<floater_init> → λ | = <floater_lit> <floater_init_end>"""
        self.current_nonterminal = "floater_init"
        expected_tokens = self.get_expected_tokens("floater_init")
        
        # If we don't have an ASSIGN token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_floater_lit()
        self.parse_floater_init_end()

    def parse_floater_lit(self) -> None:
        """<floater_lit> → Floater Literal | <nega_floater_lit>"""
        self.current_nonterminal = "floater_lit"
        expected_tokens = self.get_expected_tokens("floater_lit")

        if self.current_token and self.match_token_type(self.current_token, TokenType.NEGAFLOATER):
            # Handle negation case
            self.parse_nega_floater_lit()
        elif not self.current_token or not self.match_token_type(self.current_token, TokenType.FLOATERLIT):
            self.error_handler("floater_lit", "FIRST", expected_tokens)
        else:
            # Regular feint literal case
            self.expect(TokenType.FLOATERLIT)

    def parse_floater_init_end(self) -> None:
        """<floater_init_end> → λ | , @identifier <more_floater>"""
        self.current_nonterminal = "floater_init_end"
        expected_tokens = self.get_expected_tokens("floater_init_end")
        
        # If we don't have a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_floater()

    def parse_chant_dec(self) -> None:
        """<chant_dec> → Chant @identifier <more_chant>;"""
        self.current_nonterminal = "chant_dec"
        expected_tokens = self.get_expected_tokens("chant_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("chant_dec", "FIRST", expected_tokens)
        
        self.expect(TokenType.CHANT)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_chant()
        self.expect(TokenType.SEMICOLON)

    def parse_more_chant(self) -> None:
        """<more_chant> → λ | <chant_init> <chant_init_end>"""
        self.current_nonterminal = "more_chant"
        expected_tokens = self.get_predict_tokens("more_chant")
        
        # If we don't have tokens in FIRST(chant_init), return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # If there's an error, use PREDICT set
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("more_chant", "PREDICT", expected_tokens)
        
        self.parse_chant_init()
        self.parse_chant_init_end()

    def parse_chant_init(self) -> None:
        """<chant_init> → λ | = <chant_lit> <chant_init_end>"""
        self.current_nonterminal = "chant_init"
        expected_tokens = self.get_expected_tokens("chant_init")
        
        # If we don't have an ASSIGN token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_chant_lit()
        self.parse_chant_init_end()

    def parse_chant_lit(self) -> None:
        """<chant_lit> → Chant Literal"""
        self.current_nonterminal = "chant_lit"
        expected_tokens = self.get_expected_tokens("chant_lit")
        
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.CHANTLIT):
            self.error_handler("chant_lit", "FIRST", expected_tokens)
        
        self.expect(TokenType.CHANTLIT)

    def parse_chant_init_end(self) -> None:
        """<chant_init_end> → λ | , @identifier <more_chant>"""
        self.current_nonterminal = "chant_init_end"
        expected_tokens = self.get_expected_tokens("chant_init_end")
        
        # If we don't have a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_chant()

    def parse_stat_dec(self) -> None:
        """<stat_dec> → Stat @identifier <more_stat>;"""
        self.current_nonterminal = "stat_dec"
        expected_tokens = self.get_expected_tokens("stat_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("stat_dec", "FIRST", expected_tokens)
        
        self.expect(TokenType.STAT)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_stat()
        self.expect(TokenType.SEMICOLON)

    def parse_more_stat(self) -> None:
        """<more_stat> → λ | <stat_init> <stat_init_end>"""
        self.current_nonterminal = "more_stat"
        expected_tokens = self.get_predict_tokens("more_stat")
        
        # If we don't have tokens in FIRST(stat_init), return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # If there's an error, use PREDICT set
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("more_stat", "PREDICT", expected_tokens)
        
        self.parse_stat_init()
        self.parse_stat_init_end()

    def parse_stat_init(self) -> None:
        """<stat_init> → λ | = <stat_value> <stat_init_end>"""
        self.current_nonterminal = "stat_init"
        expected_tokens = self.get_expected_tokens("stat_init")
            
        # If we don't have an ASSIGN token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        self.expect(TokenType.ASSIGN)
        self.parse_stat_value()
        self.parse_stat_init_end()

    def parse_stat_value(self) -> None:
        """<stat_value> → Win | Loss"""
        self.current_nonterminal = "stat_value"
        expected_tokens = self.get_expected_tokens("stat_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("stat_value", "FIRST", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.WIN):
            self.expect(TokenType.WIN)
        elif self.match_token_type(self.current_token, TokenType.LOSS):
            self.expect(TokenType.LOSS)
        else:
            self.error_handler("stat_value", "FIRST")

    def parse_stat_init_end(self) -> None:
        """<stat_init_end> → λ | , @identifier <more_stat>"""
        self.current_nonterminal = "stat_init_end"
        expected_tokens = self.get_expected_tokens("stat_init_end")
        
        # If we don't have a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_more_stat()

    def parse_const_dec(self) -> None:
        """<const_dec> → <const_feint> | <const_floater> | <const_chant> | <const_stat>"""
        self.current_nonterminal = "const_dec"
        expected_tokens = self.get_expected_tokens("const_dec")
        
        # Expect CONST token
        self.expect(TokenType.CONST)
          
        # Check which type of constant declaration follows
        if self.current_token and self.current_token.type == TokenType.FEINT:
            self.parse_const_feint()
        elif self.current_token and self.current_token.type == TokenType.FLOATER:
            self.parse_const_floater()
        elif self.current_token and self.current_token.type == TokenType.CHANT:
            self.parse_const_chant()
        elif self.current_token and self.current_token.type == TokenType.STAT:
            self.parse_const_stat()
        else:
            self.error_handler("const_dec", "FIRST", expected_tokens)
            
    def parse_const_feint(self) -> None:
        """<const_feint> → Feint @identifier <feint_const_init>;"""
        self.current_nonterminal = "const_feint"
        expected_tokens = self.get_expected_tokens("const_feint")
        
        self.expect(TokenType.FEINT)
        self.expect(TokenType.VAR_INIT)
        self.parse_feint_const_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_feint_const_init(self) -> None:
        """<feint_const_init> → <feint_const><feint_const_end>"""
        self.current_nonterminal = "feint_const_init"
        expected_tokens = self.get_expected_tokens("feint_const_init")
        
        self.parse_feint_const()
        self.parse_feint_const_end()
        
    def parse_feint_const(self) -> None:
        """<feint_const> → = <feint_lit>"""
        self.current_nonterminal = "feint_const"
        expected_tokens = self.get_expected_tokens("feint_const")
        
        self.expect(TokenType.ASSIGN)
        self.parse_feint_lit()
        
    def parse_feint_const_end(self) -> None:
        """<feint_const_end> → ", @identifier <feint_const_init>" | λ"""
        self.current_nonterminal = "feint_const_end"
        expected_tokens = self.get_expected_tokens("feint_const_end")
        
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
            
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_feint_const_init()
        
    def parse_const_floater(self) -> None:
        """<const_floater> → Floater @identifier <floater_const_init>;"""
        self.current_nonterminal = "const_floater"
        expected_tokens = self.get_expected_tokens("const_floater")
        
        self.expect(TokenType.FLOATER)
        self.expect(TokenType.VAR_INIT)
        self.parse_floater_const_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_floater_const_init(self) -> None:
        """<floater_const_init> → <floater_const><floater_const_end>"""
        self.current_nonterminal = "floater_const_init"
        expected_tokens = self.get_expected_tokens("floater_const_init")
        
        self.parse_floater_const()
        self.parse_floater_const_end()
        
    def parse_floater_const(self) -> None:
        """<floater_const> → = <floater_lit>"""
        self.current_nonterminal = "floater_const"
        expected_tokens = self.get_expected_tokens("floater_const")
        
        self.expect(TokenType.ASSIGN)
        self.parse_floater_lit()
        
    def parse_floater_const_end(self) -> None:
        """<floater_const_end> → ", @identifier <floater_const_init>" | λ"""
        self.current_nonterminal = "floater_const_end"
        expected_tokens = self.get_expected_tokens("floater_const_end")
        
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
            
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_floater_const_init()
        
    def parse_const_chant(self) -> None:
        """<const_chant> → Chant @identifier <chant_const_init>;"""
        self.current_nonterminal = "const_chant"
        expected_tokens = self.get_expected_tokens("const_chant")
        
        self.expect(TokenType.CHANT)
        self.expect(TokenType.VAR_INIT)
        self.parse_chant_const_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_chant_const_init(self) -> None:
        """<chant_const_init> → <chant_const><chant_const_end>"""
        self.current_nonterminal = "chant_const_init"
        expected_tokens = self.get_expected_tokens("chant_const_init")
        
        self.parse_chant_const()
        self.parse_chant_const_end()
        
    def parse_chant_const(self) -> None:
        """<chant_const> → = <chant_lit>"""
        self.current_nonterminal = "chant_const"
        expected_tokens = self.get_expected_tokens("chant_const")
        
        self.expect(TokenType.ASSIGN)
        self.parse_chant_lit()
        
    def parse_chant_const_end(self) -> None:
        """<chant_const_end> → ", @identifier <chant_const_init>" | λ"""
        self.current_nonterminal = "chant_const_end"
        expected_tokens = self.get_expected_tokens("chant_const_end")
        
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
            
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_chant_const_init()
        
    def parse_const_stat(self) -> None:
        """<const_stat> → Stat @identifier <stat_const_init>;"""
        self.current_nonterminal = "const_stat"
        expected_tokens = self.get_expected_tokens("const_stat")
        
        self.expect(TokenType.STAT)
        self.expect(TokenType.VAR_INIT)
        self.parse_stat_const_init()
        self.expect(TokenType.SEMICOLON)
        
    def parse_stat_const_init(self) -> None:
        """<stat_const_init> → <stat_const><stat_const_end>"""
        self.current_nonterminal = "stat_const_init"
        expected_tokens = self.get_expected_tokens("stat_const_init")
        
        self.parse_stat_const()
        self.parse_stat_const_end()
        
    def parse_stat_const(self) -> None:
        """<stat_const> → = <stat_value>"""
        self.current_nonterminal = "stat_const"
        expected_tokens = self.get_expected_tokens("stat_const")
        
        self.expect(TokenType.ASSIGN)
        self.parse_stat_value()
        
    def parse_stat_const_end(self) -> None:
        """<stat_const_end> → ", @identifier <stat_const_init>" | λ"""
        self.current_nonterminal = "stat_const_end"
        expected_tokens = self.get_expected_tokens("stat_const_end")
        
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
            
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_stat_const_init()

    def parse_array_dec(self) -> None:
        """<array_dec> → <feint_array> | <floater_array> | <chant_array>"""
        self.current_nonterminal = "array_dec"
        expected_tokens = self.get_predict_tokens("array_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("array_dec", "PREDICT", expected_tokens)
        
        # Expect ZONE token first for all array declarations
        # self.expect(TokenType.ZONE)
        
        if self.match_token_type(self.current_token, TokenType.FEINT):
            self.parse_feint_array()
        elif self.match_token_type(self.current_token, TokenType.FLOATER):
            self.parse_floater_array()
        elif self.match_token_type(self.current_token, TokenType.CHANT):
            self.parse_chant_array()
        else:
            self.error_handler("array_dec", "PREDICT")
    
    def parse_feint_array(self) -> None:
        """<feint_array> → Feint @identifier [<array_size>] <2D_array> <feint_array_init>;"""
        self.current_nonterminal = "feint_array"
        expected_tokens = self.get_expected_tokens("feint_array")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("feint_array", "FIRST", expected_tokens)
        
        self.expect(TokenType.FEINT, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        
        # Parse array size declaration [<array_size>]
        self.expect(TokenType.ARRAY_INDEX_LEFT, strict=True)
        self.parse_array_size()
        self.expect(TokenType.ARRAY_INDEX_RIGHT, strict=True)
        
        # Parse possible 2D array declaration
        self.parse_2D_array()
        
        # Parse initialization if present
        self.parse_feint_array_init()
        
        # Expect semicolon at the end
        self.expect(TokenType.SEMICOLON, strict=True)
    
    def parse_2D_array(self) -> None:
        """<2D_array> → λ | [<feint_lit>]"""
        self.current_nonterminal = "2D_array"
        expected_tokens = self.get_expected_tokens("2D_array")
        
        # If we don't see an ARRAY_INDEX_LEFT token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ARRAY_INDEX_LEFT):
            return  # λ case
        
        # Otherwise parse second dimension
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_array_size() 
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
    
    def parse_feint_array_init(self) -> None:
        """<feint_array_init> → λ | = {<feint_row>}"""
        self.current_nonterminal = "feint_array_init"
        expected_tokens = self.get_expected_tokens("feint_array_init")
        
        # If we don't see an ASSIGN token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        # Otherwise parse initialization
        self.expect(TokenType.ASSIGN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_feint_row()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
    
    def parse_feint_row(self) -> None:
        """<feint_row> → <feint_lit> <more_feint_lit> | {<feint_lit> <more_feint_lit>} <2D_feint_row>"""
        self.current_nonterminal = "feint_row"
        expected_tokens = self.get_expected_tokens("feint_row")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("feint_row", "FIRST", expected_tokens)
        
        # Check if we have a nested block (2D array initialization)
        if self.match_token_type(self.current_token, TokenType.CODE_BLOCK_LEFT):
            self.expect(TokenType.CODE_BLOCK_LEFT)
            self.parse_feint_lit()
            self.parse_more_feint_lit()
            self.expect(TokenType.CODE_BLOCK_RIGHT)
            self.parse_2D_feint_row()
        else:
            # Simple 1D initialization
            self.parse_feint_lit()
            self.parse_more_feint_lit()
    
    def parse_2D_feint_row(self) -> None:
        """<2D_feint_row> → λ | , {<feint_lit> <more_feint_lit>} <2D_feint_row>"""
        self.current_nonterminal = "2D_feint_row"
        expected_tokens = self.get_expected_tokens("2D_feint_row")
        
        # If we don't see a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        # Otherwise parse next row
        self.expect(TokenType.COMMA)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_feint_lit()
        self.parse_more_feint_lit()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_2D_feint_row()
    
    def parse_more_feint_lit(self) -> None:
        """<more_feint_lit> → λ | , <feint_lit> <more_feint_lit>"""
        self.current_nonterminal = "more_feint_lit"
        expected_tokens = self.get_expected_tokens("more_feint_lit")
        
        # If we don't see a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        # Otherwise parse next element
        self.expect(TokenType.COMMA)
        self.parse_feint_lit()
        self.parse_more_feint_lit()
    
    def parse_floater_array(self) -> None:
        """<floater_array> → Floater @identifier [<array_size>] <2D_array> <floater_array_init>;"""
        self.current_nonterminal = "floater_array"
        expected_tokens = self.get_expected_tokens("floater_array")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("floater_array", "FIRST", expected_tokens)
        
        self.expect(TokenType.FLOATER, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        
        # Parse array size declaration [<array_size>]
        self.expect(TokenType.ARRAY_INDEX_LEFT, strict=True)
        self.parse_array_size()
        self.expect(TokenType.ARRAY_INDEX_RIGHT, strict=True)
        
        # Parse possible 2D array declaration
        self.parse_2D_array()
        
        # Parse initialization if present
        self.parse_floater_array_init()
        
        # Expect semicolon at the end
        self.expect(TokenType.SEMICOLON, strict=True)
    
    def parse_floater_array_init(self) -> None:
        """<floater_array_init> → λ | = {<floater_row>}"""
        self.current_nonterminal = "floater_array_init"
        expected_tokens = self.get_expected_tokens("floater_array_init")
        
        # If we don't see an ASSIGN token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        # Otherwise parse initialization
        self.expect(TokenType.ASSIGN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_floater_row()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_floater_row(self) -> None:
        """<floater_row> → <floater_lit> <more_floater_lit> | {<floater_lit> <more_floater_lit>} <2D_floater_row>"""
        self.current_nonterminal = "floater_row"
        expected_tokens = self.get_expected_tokens("floater_row")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("floater_row", "FIRST", expected_tokens)
        
        # Check if we have a nested block (2D array initialization)
        if self.match_token_type(self.current_token, TokenType.CODE_BLOCK_LEFT):
            self.expect(TokenType.CODE_BLOCK_LEFT)
            self.parse_floater_lit()
            self.parse_more_floater_lit()
            self.expect(TokenType.CODE_BLOCK_RIGHT)
            self.parse_2D_floater_row()
        else:
            # Simple 1D initialization
            self.parse_floater_lit()
            self.parse_more_floater_lit()
    
    def parse_2D_floater_row(self) -> None:
        """<2D_floater_row> → λ | , {<floater_lit> <more_floater_lit>} <2D_floater_row>"""
        self.current_nonterminal = "2D_floater_row"
        expected_tokens = self.get_expected_tokens("2D_floater_row")
        
        # If we don't see a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        # Otherwise parse next row
        self.expect(TokenType.COMMA)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_floater_lit()
        self.parse_more_floater_lit()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_2D_floater_row()
    
    def parse_more_floater_lit(self) -> None:
        """<more_floater_lit> → λ | , <floater_lit> <more_floater_lit>"""
        self.current_nonterminal = "more_floater_lit"
        expected_tokens = self.get_expected_tokens("more_floater_lit")
        
        # If we don't see a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        # Otherwise parse next element
        self.expect(TokenType.COMMA)
        self.parse_floater_lit()
        self.parse_more_floater_lit()
    
    def parse_chant_array(self) -> None:
        """<chant_array> → Chant @identifier [<array_size>] <2D_array> <chant_array_init>;"""
        self.current_nonterminal = "chant_array"
        expected_tokens = self.get_expected_tokens("chant_array")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("chant_array", "FIRST", expected_tokens)
        
        self.expect(TokenType.CHANT, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        
        # Parse array size declaration [<array_size>]
        self.expect(TokenType.ARRAY_INDEX_LEFT, strict=True)
        self.parse_array_size()
        self.expect(TokenType.ARRAY_INDEX_RIGHT, strict=True)
        
        # Parse possible 2D array declaration
        self.parse_2D_array()
        
        # Parse initialization if present
        self.parse_chant_array_init()
        
        # Expect semicolon at the end
        self.expect(TokenType.SEMICOLON)
    
    def parse_chant_array_init(self) -> None:
        """<chant_array_init> → λ | = {<chant_row>}"""
        self.current_nonterminal = "chant_array_init"
        expected_tokens = self.get_expected_tokens("chant_array_init")
        
        # If we don't see an ASSIGN token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        # Otherwise parse initialization
        self.expect(TokenType.ASSIGN)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_chant_row()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
    
    def parse_chant_row(self) -> None:
        """<chant_row> → <chant_lit> <more_chant_lit> | {<chant_lit> <more_chant_lit>} <2D_chant_row>"""
        self.current_nonterminal = "chant_row"
        expected_tokens = self.get_expected_tokens("chant_row")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("chant_row", "FIRST", expected_tokens)
        
        # Check if we have a nested block (2D array initialization)
        if self.match_token_type(self.current_token, TokenType.CODE_BLOCK_LEFT):
            self.expect(TokenType.CODE_BLOCK_LEFT)
            self.parse_chant_lit()
            self.parse_more_chant_lit()
            self.expect(TokenType.CODE_BLOCK_RIGHT)
            self.parse_2D_chant_row()
        else:
            # Simple 1D initialization
            self.parse_chant_lit()
            self.parse_more_chant_lit()
    
    def parse_2D_chant_row(self) -> None:
        """<2D_chant_row> → λ | , {<chant_lit> <more_chant_lit>} <2D_chant_row>"""
        self.current_nonterminal = "2D_chant_row"
        expected_tokens = self.get_expected_tokens("2D_chant_row")
        
        # If we don't see a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        # Otherwise parse next row
        self.expect(TokenType.COMMA)
        self.expect(TokenType.CODE_BLOCK_LEFT)
        self.parse_chant_lit()
        self.parse_more_chant_lit()
        self.expect(TokenType.CODE_BLOCK_RIGHT)
        self.parse_2D_chant_row()
    
    def parse_more_chant_lit(self) -> None:
        """<more_chant_lit> → λ | , <chant_lit> <more_chant_lit>"""
        self.current_nonterminal = "more_chant_lit"
        expected_tokens = self.get_expected_tokens("more_chant_lit")
        
        # If we don't see a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        # Otherwise parse next element
        self.expect(TokenType.COMMA)
        self.parse_chant_lit()
        self.parse_more_chant_lit()
    
    def parse_array_size(self) -> None:
        """<array_size> → <feint_lit> | @identifier"""
        self.current_nonterminal = "array_size"
        expected_tokens = self.get_expected_tokens("array_size")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("array_size", "FIRST", expected_tokens)
        
        # Check if the current token is an identifier
        if self.match_token_type(self.current_token, TokenType.VAR_INIT):
            self.expect(TokenType.VAR_INIT)
        else:
            # Otherwise, parse as a feint literal
            self.parse_feint_lit()

    def parse_function_def(self) -> None:
        """<function_def> → λ | Wilt <function_declared> <function_def> | Dunk <dunk_func_declared> <function_def>"""
        self.current_nonterminal = "function_def"
        expected_tokens = self.get_expected_tokens("function_def")
        
        # If we don't see a WILT or DUNK token, return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # Otherwise parse function declaration
        if self.match_token_type(self.current_token, TokenType.WILT):
            self.expect(TokenType.WILT)
            self.parse_function_declared()
            self.parse_function_def()  # Recursively parse next function
        elif self.match_token_type(self.current_token, TokenType.DUNK):
            self.expect(TokenType.DUNK)
            self.parse_dunk_func_declared()
            self.parse_function_def()  # Recursively parse next function
    
    def parse_function_declared(self) -> None:
        """<function_declared> → <feint_function> | <floater_function> | <chant_function> | <stat_function>"""
        self.current_nonterminal = "function_declared"
        expected_tokens = self.get_expected_tokens("function_declared")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("function_declared", "FIRST", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINT):
            self.parse_feint_function()
        elif self.match_token_type(self.current_token, TokenType.FLOATER):
            self.parse_floater_function()
        elif self.match_token_type(self.current_token, TokenType.CHANT):
            self.parse_chant_function()
        elif self.match_token_type(self.current_token, TokenType.STAT):
            self.parse_stat_function()
        else:
            self.error_handler("function_declared")
    
    def parse_dunk_func_declared(self) -> None:
        """<dunk_func_declared> → <dunk_function>"""
        self.current_nonterminal = "dunk_func_declared"
        expected_tokens = self.get_expected_tokens("dunk_func_declared")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("dunk_func_declared", "FIRST", expected_tokens)
        
        self.parse_dunk_function()
    
    def parse_feint_function(self) -> None:
        """<feint_function> → Feint @identifier(<func_parameters>) {<decl> <function_statement> <rebound_statement>}"""
        self.current_nonterminal = "feint_function"
        expected_tokens = self.get_expected_tokens("feint_function")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
        # Use FIRST set for error reporting
            self.error_handler("feint_function", "FIRST", expected_tokens)
        
        self.expect(TokenType.FEINT, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_decl()
        self.parse_function_statement()
        self.parse_rebound_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_floater_function(self) -> None:
        """<floater_function> → Floater @identifier(<func_parameters>) { <decl> <function_statement> <rebound_statement>}"""
        self.current_nonterminal = "floater_function"
        expected_tokens = self.get_expected_tokens("floater_function")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("floater_function", "FIRST", expected_tokens)
        
        self.expect(TokenType.FLOATER, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_decl()
        self.parse_function_statement()
        self.parse_rebound_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_chant_function(self) -> None:
        """<chant_function> → Chant @identifier(<func_parameters>) {<decl> <function_statement> <rebound_statement>}"""
        self.current_nonterminal = "chant_function"
        expected_tokens = self.get_expected_tokens("chant_function")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("chant_function", "FIRST", expected_tokens)
        
        self.expect(TokenType.CHANT, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_decl()
        self.parse_function_statement()
        self.parse_rebound_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_stat_function(self) -> None:
        """<stat_function> → Stat @identifier(<func_parameters>) {<decl> <function_statement> <rebound_statement>}"""
        self.current_nonterminal = "stat_function"
        expected_tokens = self.get_expected_tokens("stat_function")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("stat_function", "FIRST", expected_tokens)
        
        self.expect(TokenType.STAT, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_decl()
        self.parse_function_statement()
        self.parse_rebound_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_dunk_function(self) -> None:
        """<dunk_function> → @identifier(<func_parameters>) {<decl> <function_statement>}"""
        self.current_nonterminal = "dunk_function"
        expected_tokens = self.get_expected_tokens("dunk_function")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("dunk_function", "FIRST", expected_tokens)
        
        self.expect(TokenType.VAR_INIT, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_func_parameters()
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_decl()
        self.parse_function_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_func_parameters(self) -> None:
        """<func_parameters> → λ | @identifier <param_end>"""
        self.current_nonterminal = "func_parameters"
        expected_tokens = self.get_expected_tokens("func_parameters")
        
        # If we don't see a VAR_INIT token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.VAR_INIT):
            return  # λ case
        
        # Otherwise parse parameters
        self.expect(TokenType.VAR_INIT)
        self.parse_param_end()
    
    def parse_param_end(self) -> None:
        """<param_end> → λ | , @identifier <param_end>"""
        self.current_nonterminal = "param_end"
        expected_tokens = self.get_expected_tokens("param_end")
        
        # If we don't see a COMMA token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        # Otherwise parse next parameter
        self.expect(TokenType.COMMA)
        self.expect(TokenType.VAR_INIT)
        self.parse_param_end()
    
    def parse_function_statement(self) -> None:
        """<function_statement> → <statement> <function_statement> | λ"""
        self.current_nonterminal = "function_statement"
        expected_tokens = self.get_expected_tokens("function_statement")
        
        # If no current token or token not in FIRST(statement), we're in the λ case
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # Otherwise, parse statement followed by function_statement
        self.parse_statement()
        self.parse_function_statement()  # Recursive call
    
    def parse_team_statement(self) -> None:
        """<team_statement> → <statement> <team_statement> | λ"""
        self.current_nonterminal = "team_statement"
        expected_tokens = self.get_expected_tokens("team_statement")
        
        # If no current token or token not in FIRST(statement), we're in the λ case
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # Otherwise, parse statement followed by team_statement
        self.parse_statement()
        self.parse_team_statement()  # Recursive call

    def parse_statement(self) -> None:
        """<statement> → <announce_statement> | <inbound_statement> | <dribble_statement> |
                        <switch_statement> | <forward_statement> | <play_statement> |
                        <run_play_statement> | @identifier <follow_statement>;"""
        self.current_nonterminal = "statement"
        expected_tokens = self.get_expected_tokens("statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("statement", "FIRST", expected_tokens)
        
        # Check which statement type we're parsing
        if self.match_token_type(self.current_token, TokenType.ANNOUNCE):
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
            # For @identifier <follow_statement>;
            self.expect(TokenType.VAR_INIT)          
            # Check if the next token is LEFT_PAREN for function call
            if self.current_token and self.match_token_type(self.current_token, TokenType.LEFT_PAREN):
                self.parse_function_call()
                self.expect(TokenType.SEMICOLON)  # Move semicolon expectation here
            else:
                self.parse_follow_statement()
                self.expect(TokenType.SEMICOLON)
        else:
            self.error_handler("statement", "PREDICT")
        
    def parse_follow_statement(self) -> None:
        """<follow_statement> → <increment> | <decrement> | <function_call> | = <assign_operand> |
                            += <assign_operand> | -= <assign_operand> | *= <assign_operand> |
                            /= <assign_operand> | %= <assign_operand> |
                            [<element_index>] <2d_manipulation> <array_man>"""
        self.current_nonterminal = "follow_statement"
        expected_tokens = self.get_expected_tokens("follow_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("follow_statement", "FIRST", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.INCREMENT):
            self.parse_increment()
        elif self.match_token_type(self.current_token, TokenType.DECREMENT):
            self.parse_decrement()
        elif self.match_token_type(self.current_token, TokenType.LEFT_PAREN):
            self.parse_function_call()
        elif self.match_token_type(self.current_token, TokenType.ASSIGN):
            self.expect(TokenType.ASSIGN)
            self.parse_assign_operand()
        elif self.match_token_type(self.current_token, TokenType.ADD_ASSIGN):
            self.expect(TokenType.ADD_ASSIGN)
            self.parse_assign_operand()
        elif self.match_token_type(self.current_token, TokenType.SUB_ASSIGN):
            self.expect(TokenType.SUB_ASSIGN)
            self.parse_assign_operand()
        elif self.match_token_type(self.current_token, TokenType.MUL_ASSIGN):
            self.expect(TokenType.MUL_ASSIGN)
            self.parse_assign_operand()
        elif self.match_token_type(self.current_token, TokenType.DIV_ASSIGN):
            self.expect(TokenType.DIV_ASSIGN)
            self.parse_assign_operand()
        elif self.match_token_type(self.current_token, TokenType.MOD_ASSIGN):
            self.expect(TokenType.MOD_ASSIGN)
            self.parse_assign_operand()
        elif self.match_token_type(self.current_token, TokenType.ARRAY_INDEX_LEFT):
            self.expect(TokenType.ARRAY_INDEX_LEFT)
            self.parse_element_index()
            self.expect(TokenType.ARRAY_INDEX_RIGHT)
            self.parse_2d_manipulation()
            self.parse_array_man()
        else:
            self.error_handler("follow_statement", "FIRST")
    
    def parse_element_index(self) -> None:
        """<element_index> → @identifier | Feint Literal"""
        self.current_nonterminal = "element_index"
        expected_tokens = self.get_expected_tokens("element_index")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("element_index", "FIRST", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.VAR_INIT):
            self.expect(TokenType.VAR_INIT)
        elif self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.expect(TokenType.FEINTLIT)
        else:
            self.error_handler("element_index", "FIRST")
    
    def parse_2d_manipulation(self) -> None:
        """<2d_manipulation> → [<element_index>] | λ"""
        self.current_nonterminal = "2d_manipulation"
        expected_tokens = self.get_expected_tokens("2d_manipulation")
        
        # If not an array index left bracket, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ARRAY_INDEX_LEFT):
            return  # λ case
        
        # Otherwise, parse [<element_index>]
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_element_index()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
    
    def parse_array_man(self) -> None:
        """<array_man> → = <array_elem> | λ"""
        self.current_nonterminal = "array_man"
        expected_tokens = self.get_expected_tokens("array_man")
        
        # If not an assignment operator, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ASSIGN):
            return  # λ case
        
        # Otherwise, parse = <array_elem>
        self.expect(TokenType.ASSIGN)
        self.parse_array_elem()
    
    def parse_array_elem(self) -> None:
        """<array_elem> → <expression>"""
        self.current_nonterminal = "array_elem"
        expected_tokens = self.get_expected_tokens("array_elem")
        
        self.parse_expression()
    
    def parse_rebound_statement(self) -> None:
        """<rebound_statement> → Rebound <expression>;"""
        self.current_nonterminal = "rebound_statement"
        expected_tokens = self.get_expected_tokens("rebound_statement")
        
        self.expect(TokenType.REBOUND)
        self.parse_expression()
        self.expect(TokenType.SEMICOLON)
    
    def parse_announce_statement(self) -> None:
        """<announce_statement> → Announce(<otpt>);"""
        self.current_nonterminal = "announce_statement"
        expected_tokens = self.get_expected_tokens("announce_statement")
        
        self.expect(TokenType.ANNOUNCE, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_otpt()
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.SEMICOLON, strict=True)
    
    def parse_otpt(self) -> None:
        """<otpt> → <outputs><other_outputs>"""
        self.current_nonterminal = "otpt"
        expected_tokens = self.get_expected_tokens("otpt")
        
        self.parse_outputs()
        self.parse_other_outputs()
    
    def parse_outputs(self) -> None:
        """<outputs> → <expression>"""
        self.current_nonterminal = "outputs"
        expected_tokens = self.get_expected_tokens("outputs")
        
        self.parse_expression()
    
    def parse_other_outputs(self) -> None:
        """<other_outputs> → λ | & <otpt>"""
        self.current_nonterminal = "other_outputs"
        expected_tokens = self.get_expected_tokens("other_outputs")
        
        # If not a concatenation operator, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.CHANT_CONCAT):
            return  # λ case
        
        # Otherwise, parse & <otpts>
        self.expect(TokenType.CHANT_CONCAT)
        self.parse_otpt()
    
    def parse_literal(self) -> None:
        """<literal> → <feint_lit> | <floater_lit> | <nega_feint_lit> | <nega_floater_lit> | <chant_lit> | <stat_value>"""
        self.current_nonterminal = "literal"
        expected_tokens = self.get_expected_tokens("literal")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("literal", "FIRST", expected_tokens)
        
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
        elif self.match_token_type(self.current_token, TokenType.WIN) or self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_stat_value()
        else:
            self.error_handler("literal", "FIRST")
    
    def parse_nega_feint_lit(self) -> None:
        """<nega_feint_lit> → Negative Feint Literal"""
        self.current_nonterminal = "nega_feint_lit"
        expected_tokens = self.get_expected_tokens("nega_feint_lit")
        
        self.expect(TokenType.NEGAFEINT)
    
    def parse_nega_floater_lit(self) -> None:
        """<nega_floater_lit> → Negative Floater Literal"""
        self.current_nonterminal = "nega_floater_lit"
        expected_tokens = self.get_expected_tokens("nega_floater_lit")
        
        self.expect(TokenType.NEGAFLOATER)

    def parse_expression(self) -> None:
        """<expression> → <logical_expression>"""
        self.current_nonterminal = "expression"
        expected_tokens = self.get_expected_tokens("expression")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("expression", "FIRST", expected_tokens)
        
        self.parse_logical_expression()
    
    def parse_logical_expression(self) -> None:
        """<logical_expression> → <relational_expression> <more_logical>"""
        self.current_nonterminal = "logical_expression"
        expected_tokens = self.get_expected_tokens("logical_expression")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("logical_expression", "FIRST", expected_tokens)
        
        self.parse_relational_expression()
        self.parse_more_logical()
    
    def parse_more_logical(self) -> None:
        """<more_logical> → <log_operator> <relational_expression> <more_logical> | λ"""
        self.current_nonterminal = "more_logical"
        expected_tokens = self.get_expected_tokens("more_logical")
        
        # If we don't have a logical operator, we return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # We have a logical operator
        self.parse_log_operator()
        self.parse_relational_expression()
        self.parse_more_logical()  # Recursive call
    
    def parse_log_operator(self) -> None:
        """<log_operator> → AND | OR"""
        self.current_nonterminal = "log_operator"
        expected_tokens = self.get_expected_tokens("log_operator")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("log_operator", "FIRST", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.AND_OP):
            self.expect(TokenType.AND_OP)
        elif self.match_token_type(self.current_token, TokenType.OR_OP):
            self.expect(TokenType.OR_OP)
        else:
            self.error_handler("log_operator", "FIRST")
    
    def parse_relational_expression(self) -> None:
        """<relational_expression> → <arithmetic_expression> <more_relational>"""
        self.current_nonterminal = "relational_expression"
        expected_tokens = self.get_expected_tokens("relational_expression")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("relational_expression", "FIRST", expected_tokens)
        
        self.parse_arithmetic_expression()
        self.parse_more_relational()
    
    def parse_more_relational(self) -> None:
        """<more_relational> → <relational_operator> <arithmetic_expression> | λ"""
        self.current_nonterminal = "more_relational"
        expected_tokens = self.get_expected_tokens("more_relational")
        
        # If we don't have a relational operator, we return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # We have a relational operator
        self.parse_relational_operator()
        self.parse_arithmetic_expression()
    
    def parse_arithmetic_expression(self) -> None:
        """<arithmetic_expression> → <term> <more_term>"""
        self.current_nonterminal = "arithmetic_expression"
        expected_tokens = self.get_expected_tokens("arithmetic_expression")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("arithmetic_expression", "FIRST", expected_tokens)
        
        self.parse_term()
        self.parse_more_term()
    
    def parse_more_term(self) -> None:
        """<more_term> → + <term> <more_term> | - <term> <more_term> | λ"""
        self.current_nonterminal = "more_term"
        expected_tokens = self.get_expected_tokens("more_term")
        
        # If we don't have a +/- operator, we return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            # If there's an unexpected token where we expect λ, use FOLLOW set for error reporting
            if self.current_token and self.current_token.type not in self.get_follow_tokens("more_term"):
                self.error_handler("more_term", "FOLLOW")
            return  # λ case
        
        # We have a +/- operator
        if self.match_token_type(self.current_token, TokenType.ADD):
            self.expect(TokenType.ADD)
        elif self.match_token_type(self.current_token, TokenType.SUB):
            self.expect(TokenType.SUB)
        else:
            self.error_handler("more_term", "FIRST", expected_tokens)
        
        self.parse_term()
        self.parse_more_term()  # Recursive call
    
    def parse_term(self) -> None:
        """<term> → <factor> <more_factor>"""
        self.current_nonterminal = "term"
        expected_tokens = self.get_expected_tokens("term")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("term", "FIRST", expected_tokens)
        
        self.parse_factor()
        self.parse_more_factor()
    
    def parse_more_factor(self) -> None:
        """<more_factor> → * <factor> <more_factor> | / <factor> <more_factor> | % <factor> <more_factor> | λ"""
        self.current_nonterminal = "more_factor"
        expected_tokens = self.get_expected_tokens("more_factor")
        
        # If we don't have a */% operator, we return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        # We have a */% operator
        if self.match_token_type(self.current_token, TokenType.MUL):
            self.expect(TokenType.MUL)
        elif self.match_token_type(self.current_token, TokenType.DIV):
            self.expect(TokenType.DIV)
        elif self.match_token_type(self.current_token, TokenType.MOD):
            self.expect(TokenType.MOD)
        else:
            self.error_handler("more_factor", "FIRST", expected_tokens)
        
        self.parse_factor()
        self.parse_more_factor()  # Recursive call
    
    def parse_factor(self) -> None:
        """<factor> → <literal> | @identifier<follow_factor> | (<expression>) | NOT <factor> | <type_casting>"""
        self.current_nonterminal = "factor"
        expected_tokens = self.get_expected_tokens("factor")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("factor", "FIRST", expected_tokens)
        
        # Handle different factor options
        if self.match_token_type(self.current_token, TokenType.VAR_INIT):
            self.expect(TokenType.VAR_INIT)
            self.parse_follow_factor()
        elif self.match_token_type(self.current_token, TokenType.LEFT_PAREN):
            self.expect(TokenType.LEFT_PAREN)
            self.parse_expression()
            self.expect(TokenType.RIGHT_PAREN)
        elif self.match_token_type(self.current_token, TokenType.NOT_OP):
            self.expect(TokenType.NOT_OP)
            self.parse_factor()
        elif (self.match_token_type(self.current_token, TokenType.FEINT) or 
              self.match_token_type(self.current_token, TokenType.FLOATER) or
              self.match_token_type(self.current_token, TokenType.CHANT) or
              self.match_token_type(self.current_token, TokenType.STAT)):
            self.parse_type_casting()
        else:
            # Handle literal case (feintlit, floaterlit, etc.)
            self.parse_literal()

    def parse_follow_factor(self) -> None:
        """<follow_factor> → [<element_index>] <2d_manipulation> <array_man> | <function_call>"""
        self.current_nonterminal = "follow_factor"
        expected_tokens = self.get_expected_tokens("follow_factor")
        
        # Check if this is a function call
        if self.current_token and self.match_token_type(self.current_token, TokenType.LEFT_PAREN):
            self.parse_function_call()
            return
        
        # Otherwise, it's an array element access
        # First, we expect a left array index bracket
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.ARRAY_INDEX_LEFT):
            return  # If no array index, this could be a λ case (just an identifier)
        
        # Parse array element access
        self.expect(TokenType.ARRAY_INDEX_LEFT)
        self.parse_element_index()
        self.expect(TokenType.ARRAY_INDEX_RIGHT)
        
        # Parse optional 2D array access
        self.parse_2d_manipulation()
        
        # Parse optional array element assignment
        self.parse_array_man()

    def parse_relational_operator(self) -> None:
        """<relational_operator> → < | > | == | <= | >= | !="""
        self.current_nonterminal = "relational_operator"
        expected_tokens = self.get_predict_tokens("relational_operator")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("relational_operator", "PREDICT", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.LESS_THAN):
            self.expect(TokenType.LESS_THAN)
        elif self.match_token_type(self.current_token, TokenType.GREATER_THAN):
            self.expect(TokenType.GREATER_THAN)
        elif self.match_token_type(self.current_token, TokenType.EQUAL):
            self.expect(TokenType.EQUAL)
        elif self.match_token_type(self.current_token, TokenType.LESS_EQUAL):
            self.expect(TokenType.LESS_EQUAL)
        elif self.match_token_type(self.current_token, TokenType.GREATER_EQUAL):
            self.expect(TokenType.GREATER_EQUAL)
        elif self.match_token_type(self.current_token, TokenType.NOT_EQUAL):
            self.expect(TokenType.NOT_EQUAL)
        else:
            self.error_handler("relational_operator", "PREDICT")

    def parse_type_casting(self) -> None:
        """<type_casting> → Feint(<typecast_value>) | Floater(<typecast_value>) | 
                            Chant(<typecast_value>) | Stat(<typecast_value>)"""
        self.current_nonterminal = "type_casting"
        expected_tokens = [TokenType.FEINT, TokenType.FLOATER, TokenType.CHANT, TokenType.STAT]

        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("type_casting", "FIRST", expected_tokens)
        
        if self.match_token_type(self.current_token, TokenType.FEINT):
            self.expect(TokenType.FEINT)
            self.expect(TokenType.LEFT_PAREN)
            self.parse_typecast_value()
            self.expect(TokenType.RIGHT_PAREN)
        elif self.match_token_type(self.current_token, TokenType.FLOATER):
            self.expect(TokenType.FLOATER)
            self.expect(TokenType.LEFT_PAREN)
            self.parse_typecast_value()
            self.expect(TokenType.RIGHT_PAREN)
        elif self.match_token_type(self.current_token, TokenType.CHANT):
            self.expect(TokenType.CHANT)
            self.expect(TokenType.LEFT_PAREN)
            self.parse_typecast_value()
            self.expect(TokenType.RIGHT_PAREN)
        elif self.match_token_type(self.current_token, TokenType.STAT):
            self.expect(TokenType.STAT)
            self.expect(TokenType.LEFT_PAREN)
            self.parse_typecast_value()
            self.expect(TokenType.RIGHT_PAREN)
        else:
            self.error_handler("type_casting", "FIRST")

    def parse_assign_operand(self) -> None:
        """<assign_operand> → <expression>"""
        self.current_nonterminal = "assign_operand"
        expected_tokens = self.get_expected_tokens("assign_operand")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("assign_operand", "FIRST", expected_tokens)
        
        self.parse_expression()
    
    def parse_function_call(self) -> None:
        """<function_call> → (<arguments>) | λ"""
        self.current_nonterminal = "function_call"
        expected_tokens = self.get_expected_tokens("function_call")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
    
        self.expect(TokenType.LEFT_PAREN)
        self.parse_arguments()
        self.expect(TokenType.RIGHT_PAREN)
        # self.expect(TokenType.SEMICOLON)
    
    def parse_arguments(self) -> None:
        """<arguments> → <arg> <more_args> | λ"""
        self.current_nonterminal = "arguments"
        expected_tokens = self.get_expected_tokens("arguments")
        
        # If we don't have a token that could be an argument, return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        self.parse_arg()
        self.parse_more_args()
    
    def parse_arg(self) -> None:
        """<arg> → <expression>"""
        self.current_nonterminal = "arg"
        expected_tokens = self.get_expected_tokens("arg")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("arg", "FIRST", expected_tokens)
        
        self.parse_expression()
    
    def parse_more_args(self) -> None:
        """<more_args> → , <arg> <more_args> | λ"""
        self.current_nonterminal = "more_args"
        expected_tokens = self.get_expected_tokens("more_args")
        
        # If there's no comma, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.COMMA):
            return  # λ case
        
        self.expect(TokenType.COMMA)
        self.parse_arg()
        self.parse_more_args()
    
    def parse_inbound_statement(self) -> None:
        """<inbound_statement> → Inbound(<chant_lit>, @identifier);"""
        self.current_nonterminal = "inbound_statement"
        expected_tokens = self.get_expected_tokens("inbound_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("inbound_statement", "FIRST", expected_tokens)
        
        self.expect(TokenType.INBOUND, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_chant_lit()
        self.expect(TokenType.COMMA, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.SEMICOLON, strict=True)
    
    def parse_dribble_statement(self) -> None:
        """<dribble_statement> → Dribble (<expression>) {<loop_statements>} <add_condition>"""
        self.current_nonterminal = "dribble_statement"
        expected_tokens = self.get_expected_tokens("dribble_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("dribble_statement", "FIRST", expected_tokens)
        
        self.expect(TokenType.DRIBBLE, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_expression()
        self.expect(TokenType.RIGHT_PAREN)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_loop_statements()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
        self.parse_add_condition()
    
    def parse_add_condition(self) -> None:
        """<add_condition> → Pass (<expression>) {<loop_statements>} <add_condition> | Shoot {<loop_statements>} | λ"""
        self.current_nonterminal = "add_condition"
        expected_tokens = self.get_expected_tokens("add_condition")
        
        # If no Pass or Shoot token, return (λ case)
        if not self.current_token:
            return  # λ case
        
        if self.match_token_type(self.current_token, TokenType.PASS):
            self.expect(TokenType.PASS, strict=True)
            self.expect(TokenType.LEFT_PAREN, strict=True)
            self.parse_expression()
            self.expect(TokenType.RIGHT_PAREN, strict=True)
            self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
            self.parse_loop_statements()
            self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
            self.parse_add_condition()
        elif self.match_token_type(self.current_token, TokenType.SHOOT):
            self.expect(TokenType.SHOOT)
            self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
            self.parse_loop_statements()
            self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
        # Else λ case is handled by just returning
    
    def parse_loop_statements(self) -> None:
        """<loop_statements> → <loop_statement> <loop_statements> | λ"""
        self.current_nonterminal = "loop_statements"
        expected_tokens = self.get_expected_tokens("loop_statements")
        
        # If we don't have a token that could be a loop statement, return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        self.parse_loop_statement()
        self.parse_loop_statements()
    
    def parse_loop_statement(self) -> None:
        """<loop_statement> → <statement> | <resume_statement> | <timeout_statement>"""
        self.current_nonterminal = "loop_statement"
        expected_tokens = self.get_expected_tokens("loop_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("loop_statement", "FIRST", expected_tokens)
        
        if self.current_token and self.match_token_type(self.current_token, TokenType.RESUME):
            self.parse_resume_statement()
        elif self.current_token and self.match_token_type(self.current_token, TokenType.TIMEOUT):
            self.parse_timeout_statement()
        else:
            self.parse_statement()
    
    def parse_switch_statement(self) -> None:
        """<switch_statement> → Switch (@identifier) { <get_case> <get_default> }"""
        self.current_nonterminal = "switch_statement"
        expected_tokens = self.get_expected_tokens("switch_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("switch_statement", "FIRST", expected_tokens)
        
        self.expect(TokenType.SWITCH, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_get_case()
        self.parse_get_default()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_get_case(self) -> None:
        """<get_case> → Get <get_value> : <team_statement> <timeout_statement> <get_case_end>"""
        self.current_nonterminal = "get_case"
        expected_tokens = self.get_expected_tokens("get_case")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("get_case", "FIRST", expected_tokens)
        
        self.expect(TokenType.GET, strict=True)
        self.parse_get_value()
        self.expect(TokenType.COLON, strict=True)
        self.parse_team_statement()
        self.parse_timeout_statement()
        self.parse_get_case_end()
    
    def parse_get_value(self) -> None:
        """<get_value> → <feint_lit> | <chant_lit>"""
        self.current_nonterminal = "get_value"
        expected_tokens = self.get_expected_tokens("get_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("get_value", "FIRST", expected_tokens)
        
        if self.current_token and self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        elif self.current_token and self.match_token_type(self.current_token, TokenType.CHANTLIT):
            self.parse_chant_lit()
        else:
            self.error_handler("get_value", {TokenType.FEINTLIT, TokenType.CHANTLIT})
    
    def parse_timeout_statement(self) -> None:
        """<timeout_statement> → Timeout; | λ"""
        self.current_nonterminal = "timeout_statement"
        expected_tokens = self.get_expected_tokens("timeout_statement")
        
        # If no Timeout token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.TIMEOUT):
            return  # λ case
        
        self.expect(TokenType.TIMEOUT)
        self.expect(TokenType.SEMICOLON)
    
    def parse_get_case_end(self) -> None:
        """<get_case_end> → λ | <get_case>"""
        self.current_nonterminal = "get_case_end"
        expected_tokens = self.get_expected_tokens("get_case_end")
        
        # If no Get token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.GET):
            return  # λ case
        
        self.parse_get_case()
    
    def parse_get_default(self) -> None:
        """<get_default> → Default: <team_statement> | λ"""
        self.current_nonterminal = "get_default"
        expected_tokens = self.get_expected_tokens("get_default")
        
        # If no Default token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.DEFAULT):
            return  # λ case
        
        self.expect(TokenType.DEFAULT)
        self.expect(TokenType.COLON)
        self.parse_team_statement()
    
    def parse_forward_statement(self) -> None:
        """<forward_statement> → Forward (@identifier = <forward_lit>; <expression>; @identifier <forward_inc_dec>) {<team_statement>}"""
        self.current_nonterminal = "forward_statement"
        expected_tokens = self.get_expected_tokens("forward_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("forward_statement", "FIRST", expected_tokens)
        
        self.expect(TokenType.FORWARD, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        self.expect(TokenType.ASSIGN, strict=True)
        self.parse_forward_lit()
        self.expect(TokenType.SEMICOLON, strict=True)
        self.parse_expression()
        self.expect(TokenType.SEMICOLON, strict=True)
        self.expect(TokenType.VAR_INIT, strict=True)
        self.parse_forward_inc_dec()
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_team_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_forward_lit(self) -> None:
        """<forward_lit> → <feint_lit> | @identifier"""
        self.current_nonterminal = "forward_lit"
        expected_tokens = self.get_expected_tokens("forward_lit")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("forward_lit", "FIRST", expected_tokens)
        
        if self.current_token and self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        elif self.current_token and self.match_token_type(self.current_token, TokenType.VAR_INIT):
            self.expect(TokenType.VAR_INIT)
        else:
            self.error_handler("forward_lit", {TokenType.FEINTLIT, TokenType.VAR_INIT})
    
    def parse_forward_inc_dec(self) -> None:
        """<forward_inc_dec> → <increment> | <decrement> | <forward_assign_operator> <forward_lit>"""
        self.current_nonterminal = "forward_inc_dec"
        expected_tokens = self.get_expected_tokens("forward_inc_dec")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("forward_inc_dec", "FIRST", expected_tokens)
        
        if self.current_token and self.match_token_type(self.current_token, TokenType.INCREMENT):
            self.parse_increment()
        elif self.current_token and self.match_token_type(self.current_token, TokenType.DECREMENT):
            self.parse_decrement()
        else:
            self.parse_forward_assign_operator()
            self.parse_forward_lit()
    
    def parse_increment(self) -> None:
        """<increment> → ++"""
        self.current_nonterminal = "increment"
        expected_tokens = self.get_expected_tokens("increment")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("increment", "FIRST", expected_tokens)
        
        self.expect(TokenType.INCREMENT)
    
    def parse_decrement(self) -> None:
        """<decrement> → --"""
        self.current_nonterminal = "decrement"
        expected_tokens = self.get_expected_tokens("decrement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("decrement", "FIRST", expected_tokens)
        
        self.expect(TokenType.DECREMENT)
    
    def parse_forward_assign_operator(self) -> None:
        """<forward_assign_operator> → += | -="""
        self.current_nonterminal = "forward_assign_operator"
        expected_tokens = self.get_expected_tokens("forward_assign_operator")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("forward_assign_operator", "FIRST", expected_tokens)
        
        if self.current_token and self.match_token_type(self.current_token, TokenType.ADD_ASSIGN):
            self.expect(TokenType.ADD_ASSIGN)
        elif self.current_token and self.match_token_type(self.current_token, TokenType.SUB_ASSIGN):
            self.expect(TokenType.SUB_ASSIGN)
        else:
            self.error_handler("forward_assign_operator", {TokenType.ADD_ASSIGN, TokenType.SUB_ASSIGN})
    
    def parse_resume_statement(self) -> None:
        """<resume_statement> → Resume; | λ"""
        self.current_nonterminal = "resume_statement"
        expected_tokens = self.get_expected_tokens("resume_statement")
        
        # If no Resume token, return (λ case)
        if not self.current_token or not self.match_token_type(self.current_token, TokenType.RESUME):
            return  # λ case
        
        self.expect(TokenType.RESUME, strict=True)
        self.expect(TokenType.SEMICOLON, strict=True)

    def parse_play_statement(self) -> None:
        """<play_statement> → Play (<expression>) {<team_statement>}"""
        self.current_nonterminal = "play_statement"
        expected_tokens = self.get_expected_tokens("play_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("play_statement", "FIRST", expected_tokens)
        
        self.expect(TokenType.PLAY, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_expression()
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_team_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_run_play_statement(self) -> None:
        """<run_play_statement> → Run {<team_statement>} Play (<expression>);"""
        self.current_nonterminal = "run_play_statement"
        expected_tokens = self.get_expected_tokens("run_play_statement")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("run_play_statement", "FIRST", expected_tokens)
        
        self.expect(TokenType.RUN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_team_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
        self.expect(TokenType.PLAY, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.parse_expression()
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.SEMICOLON, strict=True)
    
    def parse_team_block(self) -> None:
        """<team_block> → Team() { <local_dec> <team_statement> }"""
        self.current_nonterminal = "team_block"
        expected_tokens = self.get_expected_tokens("team_block")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("team_block", "FIRST", expected_tokens)
        
        self.expect(TokenType.TEAM, strict=True)
        self.expect(TokenType.LEFT_PAREN, strict=True)
        self.expect(TokenType.RIGHT_PAREN, strict=True)
        self.expect(TokenType.CODE_BLOCK_LEFT, strict=True)
        self.parse_decl()
        self.parse_team_statement()
        self.expect(TokenType.CODE_BLOCK_RIGHT, strict=True)
    
    def parse_decl(self) -> None:
        """<decl> → <declaration> <local_dec> | λ"""
        self.current_nonterminal = "decl"
        expected_tokens = self.get_expected_tokens("decl")
        
        # If we don't have a token that could be a local declaration, return (λ case)
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            return  # λ case
        
        self.parse_declaration()
        self.parse_decl()
    
    def parse_declaration(self) -> None:
        """<declaration> → <variable_dec> | <array_dec>"""
        self.current_nonterminal = "declaration"
        expected_tokens = self.get_expected_tokens("declaration")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("declaration", "FIRST", expected_tokens)
    
        # ADDED
        start_line = self.line_number
        
        if self.current_token and self.match_token_type(self.current_token, TokenType.ZONE):
            self.expect(TokenType.ZONE)  # Consume ZONE token
            self.parse_array_dec()
        else:
            self.parse_variable_dec()
    
        # ADDED
        if (self.current_token and self.line_number == start_line and 
            any(self.match_token_type(self.current_token, t) for t in self.get_expected_tokens("declaration"))):
            error_msg = f"Syntax Error at line {self.line_number}, column {self.column}:\n"
            error_msg += "Multiple declarations on the same line are not allowed."
            raise SyntaxError(
                error_msg,
                self.line_number,
                self.column,
                expected="Each declaration must be on a separate line",
                token=self.current_token.value,
                nonterminal="declaration"
            )
    
    def parse_typecast_value(self) -> None:
        """<typecast_value> → <feint_lit> | <floater_lit> | <chant_lit> | <stat_value> | @identifier"""
        self.current_nonterminal = "typecast_value"
        expected_tokens = self.get_expected_tokens("typecast_value")
        
        if not self.current_token or not any(self.match_token_type(self.current_token, t) for t in expected_tokens):
            self.error_handler("typecast_value", "FIRST", expected_tokens)
        
        # Check which type of value we're dealing with
        if self.match_token_type(self.current_token, TokenType.FEINTLIT):
            self.parse_feint_lit()
        elif self.match_token_type(self.current_token, TokenType.FLOATERLIT):
            self.parse_floater_lit()
        elif self.match_token_type(self.current_token, TokenType.CHANTLIT):
            self.parse_chant_lit()
        elif self.match_token_type(self.current_token, TokenType.WIN) or \
            self.match_token_type(self.current_token, TokenType.LOSS):
            self.parse_stat_value()
        elif self.match_token_type(self.current_token, TokenType.VAR_INIT):
            # Handle identifier
            self.expect(TokenType.VAR_INIT)
        else:
            self.error_handler("typecast_value", "FIRST")
            
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
        return True
    except SyntaxError as e:
        # Instead of printing to console, re-raise the error so it can be caught by the editor
        raise