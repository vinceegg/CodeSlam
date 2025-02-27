from enum import Enum

class TokenType(Enum):
    # Data Types
    FEINT = "FEINT"       # Equivalent to int
    CHANT = "CHANT"       # Equivalent to str
    FLOATER = "FLOATER"   # Equivalent to float
    STAT = "STAT"         # Equivalent to bool
    CONST = "CONST"       # Equivalent to const

    # Input/Output Statements
    INBOUND = "INBOUND"   # Equivalent to input
    ANNOUNCE = "ANNOUNCE" # Equivalent to print

    # Control Statements
    DRIBBLE = "DRIBBLE"   # Equivalent to if
    SHOOT = "SHOOT"       # Equivalent to else
    PASS = "PASS"         # Equivalent to elif
    DEFAULT = "DEFAULT"   # Equivalent to default
    SWITCH = "SWITCH"     # Equivalent to switch
    GET = "GET"           # Equivalent to case

    # Loop Statements
    FORWARD = "FORWARD"   # Equivalent to for
    PLAY = "PLAY"         # Equivalent to while
    TIMEOUT = "TIMEOUT"   # Equivalent to break
    RESUME = "RESUME"     # Equivalent to continue
    RUN = "RUN"          # Equivalent to do-while

    # Functions and Returns
    REBOUND = "REBOUND"   # Equivalent to return
    TEAM = "TEAM"         # Equivalent to Main
    DUNK = "DUNK"         # Equivalent to Void

    # Boolean Values
    WIN = "WIN"           # Equivalent to True
    LOSS = "LOSS"        # Equivalent to False

    # Operators
    ASSIGN = "ASSIGN"          # =
    ADD_ASSIGN = "ADD_ASSIGN"  # +=
    SUB_ASSIGN = "SUB_ASSIGN"  # -=
    MUL_ASSIGN = "MUL_ASSIGN"  # *=
    DIV_ASSIGN = "DIV_ASSIGN"  # /=
    MOD_ASSIGN = "MOD_ASSIGN"  # %=
    
    # Arithmetic Operators
    ADD = "ADD"               # +
    SUB = "SUB"              # -
    MUL = "MUL"              # *
    DIV = "DIV"              # /
    MOD = "MOD"              # %
    
    # Relational Operators
    EQUAL = "EQUAL"              # ==
    NOT_EQUAL = "NOT_EQUAL"      # !=
    LESS_THAN = "LESS_THAN"      # <
    GREATER_THAN = "GREATER_THAN" # >
    LESS_EQUAL = "LESS_EQUAL"    # <=
    GREATER_EQUAL = "GREATER_EQUAL" # >=

    # Logical Operators
    AND = "AND"              # AND
    OR = "OR"                # OR
    NOT = "NOT"              # NOT

    # Literals
    FEINTLIT = "FEINTLIT"     # Integer literal
    FLOATERLIT = "FLOATERLIT" # Float literal
    CHANTLIT = "CHANTLIT"     # String literal
    
    # Special Characters
    AMPERSAND = "AMPERSAND"           # &
    LEFT_PAREN = "LEFT_PAREN"         # (
    RIGHT_PAREN = "RIGHT_PAREN"       # )
    LEFT_BRACKET = "LEFT_BRACKET"     # [
    RIGHT_BRACKET = "RIGHT_BRACKET"   # ]
    CODE_BLOCK_LEFT = "CODE_BLOCK_LEFT"   # {
    CODE_BLOCK_RIGHT = "CODE_BLOCK_RIGHT" # }
    COMMA = "COMMA"                   # ,
    SEMICOLON = "SEMICOLON"           # ;
    COLON = "COLON"                   # :
    
    # Identifiers and Variables
    VAR_INIT = "VAR_INIT"             # @ (for variables)
    IDENTIFIER = "IDENTIFIER"          # For other identifiers
    
    # Whitespace
    SPACE = "SPACE"
    TAB = "TAB"
    NEWLINE = "NEWLINE"
    
    # Comments
    COMMENT = "COMMENT"               # Single line comment
    MULTI_COMMENT = "MULTI_COMMENT"   # Multi-line comment


class Token:
    """
    Represents a single token in the basketball-themed programming language.
    Each token consists of a type (from TokenType) and an optional value.
    """
    def __init__(self, type_, value=None, line=0, column=0):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        if self.value:
            return f"{self.type} | {self.value}"
        return f"{self.type}"
