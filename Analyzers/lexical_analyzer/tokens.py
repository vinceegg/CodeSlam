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
    FORWARD = "FORWARD"     # Equivalent to for
    PLAY = "PLAY"           # Equivalent to while
    TIMEOUT = "TIMEOUT"     # Equivalent to break
    RESUME = "RESUME"       # Equivalent to continue
    RUN = "RUN"             # Equivalent to do-while

    # Others/Functions
    REBOUND = "REBOUND"   # Equivalent to return
    WIN = "WIN"           # Equivalent to True
    LOSS = "LOSS"         # Equivalent to False
    TEAM = "TEAM"         # Equivalent to Main
    DUNK = "DUNK"         # Equivalent to Void

    # Reserved Symbols
    # Assignment Operators
    ASSIGN = "ASSIGN"          # Assignment: Assigns a value to a variable
    ADD_ASSIGN = "ADD_ASSIGN"  # Add and Assign: Adds and assigns the result to a variable
    SUB_ASSIGN = "SUB_ASSIGN"  # Subtract and Assign: Subtracts and assigns the result to a variable
    MUL_ASSIGN = "MUL_ASSIGN"  # Multiply and Assign: Multiplies and assigns the result to a variable
    DIV_ASSIGN = "DIV_ASSIGN"  # Divide and Assign: Divides and assigns the result to a variable
    MOD_ASSIGN = "MOD_ASSIGN"  # Modulus and Assign: Finds modulus and assigns the result to a variable

    # Arithmetic Operators
    ADD = "ADD"             # Addition: Adds two values together
    SUB = "SUB"             # Subtraction: Finds the difference between two values
    NEG = "NEG"
    MUL = "MUL"             # Multiplication: Multiplies two values
    DIV = "DIV"             # Division: Divides one value by another
    MOD = "MOD"             # Modulus: Finds the remainder after division
    FEINTLIT = "FEINT_LIT"   # Integer Literal: Represents an integer value
    FLOATERLIT = "FLOATER_LIT" # Float Literal: Represents a floating-point value
    NEGAFEINT = "NEGA_FEINT"     # Negative: Negates the numerical values, making positive negative and vice versa
    NEGAFLOATER = "NEGA_FLOATER" # Negative: Negates the numerical values, making positive negative and vice versa
    CHANTLIT = "CHANT_LIT"

    # Relational Operators
    EQUAL = "EQUAL"                    # Equal to: Checks if two values are equal
    NOT_EQUAL = "NOT_EQUAL"            # Not equal to: Checks if two values are not equal
    LESS_THAN = "LESS_THAN"            # Less than: Checks if one value is smaller than another
    GREATER_THAN = "GREATER_THAN"      # Greater than: Checks if one value is larger than another
    LESS_EQUAL = "LESS_EQUAL"          # Less than or equal to: Checks if one value is smaller or equal to another
    GREATER_EQUAL = "GREATER_EQUAL"    # Greater than or equal to: Checks if one value is larger or equal to another

    # Logical Operators
    AND_OP = "AND_OP"        # Logical AND: Returns True if the value of both operands are True
    OR_OP = "OR_OP"          # Logical OR: Returns True if at least one operand is True
    NOT_OP = "NOT_OP"        # Logical NOT: Returns the opposite Boolean value of the operand

    # Other Operators
    CHANT_CONCAT = "CHANT_CONCAT"         # Chant Concatenation: Concatenates Chant together when working with Chant data types
    ARRAY_INDEX_LEFT = "ARRAY_INDEX_LEFT"     # Array Size/Index: Used to specify the size or index of an array
    ARRAY_INDEX_RIGHT = "ARRAY_INDEX_RIGHT"    # Array Size/Index: Used to specify the size or index of an array
    CODE_BLOCK_LEFT = "CODE_BLOCK_LEFT"      # Code Blocks: Used to define the start and end points of a programming structure
    CODE_BLOCK_RIGHT = "CODE_BLOCK_RIGHT"     # Code Blocks: Used to define the start and end points of a programming structure
    LEFT_PAREN = "LEFT_PAREN"           # Grouping: Used to group values or expressions
    RIGHT_PAREN = "RIGHT_PAREN"          # Grouping: Used to group values or expressions
    NEGATIVE = "NEGATIVE"             # Negative: Negates the numerical values, making positive negative and vice versa
    VAR_INIT = "VAR_INIT"             # Variable Initialization: Every identifier must start with an "@" sign
    SPACE = "SPACE"            # Space: Used to separate tokens
    COMMA = "COMMA"                # Comma: Used to separate values in a list
    COLON = "COLON"                # Colon: Used to separate key-value pairs in a dictionary
    SEMICOLON = "SEMICOLON"            # Semicolon: Used to terminate statements
    COMMENT = "SINGLE_COMMENT"              # Comment: Used to add comments in the code
    MULTI_COMMENT = "MULTI_COMMENT"       # Multi-line Comment: Used to add multi-line comments in the code
    TAB = "TAB"                # Tab: Used to separate tokens
    NEWLINE = "NEWLINE"        # New Line: Used to separate tokens
    UNDERSCORE = "UNDERSCORE"           # Underscore: Used to separate words in identifiers
    BACKSLASH = "BACKSLASH"           # Backslash: Used to escape special characters
    QUOTE = "QUOTE"               # Quote: Used to define string literals
    BACKSLASH_AND = "BACKSLASH_AND"
    BACKSLASH_AT = "BACKSLASH_AT"

class Token:
    """
    Represents a single token in the basketball-themed programming language.
    Each token consists of a type (from TokenType) and an optional value.
    """

    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        '''
        Generates a string representation of the token.
        '''
        if self.value:
            return f"{self.type} | {self.value}"
        return f"{self.type}"
