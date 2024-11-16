# Importing the lexemes and token types
from Analyzers.lexical_analyzer.delimiters import *  # Import lexemes
from Analyzers.lexical_analyzer.tokens import TokenType, Token  # Import token types and Token class
from Analyzers.lexical_analyzer.errors import *
from Analyzers.lexical_analyzer.positions import Position

"""
Example Code:
Feint Main() {
    Announce("Hello World");
}

Output:
Lexeme              Token
-------------------------
Feint               FEINT
Main                MAIN
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