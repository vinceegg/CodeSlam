# Importing the lexemes and token types
from Analyzers.lexical_analyzer.delimiters import *  # Import lexemes
from Analyzers.lexical_analyzer.tokens import TokenType, Token  # Import token types and Token class
from Analyzers.lexical_analyzer.errors import *
from Analyzers.lexical_analyzer.positions import Position

"""
Example Code:
Feint Team() {
    Announce("Hello World");
}

Output:
Lexeme              Token
-------------------------
Feint               FEINT
Team                TEAM
(                   LEFT_PAREN
)                   RIGHT_PAREN 
{                   CODE_BLOCK_LEFT
Announce            ANNOUNCE
(                   LEFT_PAREN
"Hello World"       CHANT
)                   RIGHT_PAREN
;                   SEMICOLON
}                   CODE_BLOCK_RIGHT
"""
class Lexer:

    def __init__(self, fn, text, ln):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, ln, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(
            self.text) else None

    def make_tokens(self):
        tokens = []
        errors = []

        while self.current_char is not None:
            # SYMBOLS
            if self.current_char in " ":
                tokens.append(Token(TokenType.SPACE.value, self.current_char))
                self.advance()
            elif self.current_char in "(":
                tokens.append(Token(TokenType.LEFT_PAREN.value, self.current_char))
                self.advance()
            elif self.current_char in ")":
                tokens.append(Token(TokenType.RIGHT_PAREN.value, self.current_char))
                self.advance()
            elif self.current_char in "[":
                tokens.append(Token(TokenType.ARRAY_INDEX_LEFT.value, self.current_char))
                self.advance()
            elif self.current_char in "]":
                tokens.append(Token(TokenType.ARRAY_INDEX_RIGHT.value, self.current_char))
                self.advance()
            elif self.current_char in "{":
                tokens.append(Token(TokenType.CODE_BLOCK_LEFT.value, self.current_char))
                self.advance()
            elif self.current_char in "}":
                tokens.append(Token(TokenType.CODE_BLOCK_RIGHT.value, self.current_char))
                self.advance()
            elif self.current_char in ";":
                tokens.append(Token(TokenType.SEMICOLON.value, self.current_char))
                self.advance()
            elif self.current_char in ":":
                tokens.append(Token(TokenType.COLON.value, self.current_char))
                self.advance()
            elif self.current_char in ",":
                tokens.append(Token(TokenType.COMMA.value, self.current_char))
                self.advance()
            elif self.current_char in "~":
                tokens.append(Token(TokenType.NEGATIVE.value, self.current_char))
                self.advance()
            elif self.current_char in "_":
                tokens.append(Token(TokenType.UNDERSCORE.value, self.current_char))
                self.advance()
            elif self.current_char in "&":
                tokens.append(Token(TokenType.CHANT_CONCAT.value, self.current_char))
                self.advance()
            elif self.current_char in "@":
                tokens.append(Token(TokenType.VAR_INIT.value, self.current_char))
                self.advance()
            elif self.current_char in "\\":
                self.advance()
                match self.current_char:
                    case "newline":
                        tokens.append(Token(TokenType.NEWLINE.value, "\\n"))
                        self.advance()
                    case "tab":
                        tokens.append(Token(TokenType.TAB.value, "\\t"))
                        self.advance()
                    case "\"":
                        tokens.append(Token(TokenType.BACKSLASH.value, "\\"))
                        self.advance()
                    case "&":
                        tokens.append(Token(TokenType.BACKSLASH_AND.value, "\\&"))
                        self.advance()
                    case "@":
                        tokens.append(Token(TokenType.BACKSLASH_AT.value, "\\@"))
                        self.advance()
            # Reserved Words

"""
# AND state 0-4
AND - Announce
Chant - Const
Default - Dribble - Dunk
Feint - Floater - Forward
Inbound 
Loss
NOT
OR
Pass - Play
Rebound - Resume - Run
Shoot - Stat - Switch
Team - Timeout
Win
"""