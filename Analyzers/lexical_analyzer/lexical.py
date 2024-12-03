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

'''
Reserved Words
Tony Stark - Floater - Play
Jack of All Trades - Rebound - Win

Reserved Symbols
Tony Stark - 144 - 166
Jack of All Trades - 167 - 191

Identifiers
Tony Stark - 193 - 213 
Jack of All Trades - 212 - 233

'''
class Lexer:

    def __init__(self, text):
        # Initialize the lexer with the input text
        self.text = text
        # Initialize the position tracker with starting values
        self.pos = Position(-1, -1, text)
        # Initialize the current character to None
        self.current_char = None
        # Advance to the first character in the text
        self.advance()
    
    def advance(self):
        # Update the position tracker with the current character
        self.pos.advance(self.current_char)
        # Update the current character to the next character in the text
        # If the end of the text is reached, set current_char to None
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

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
            # elif self.current_char in "~":
            #     tokens.append(Token(TokenType.NEGATIVE.value, self.current_char))
            #     self.advance()
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
            elif self.current_char == "A":
                pos_start = self.pos.copy()
                valid, input_str = self.state1()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "C":
                pos_start = self.pos.copy()
                valid, input_str = self.state13()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "D":
                pos_start = self.pos.copy()
                valid, input_str = self.state24()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "F":
                pos_start = self.pos.copy()
                valid, input_str = self.state43()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "G":
                pos_start = self.pos.copy()
                valid, input_str = self.state63()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "I":
                pos_start = self.pos.copy()
                valid, input_str = self.state67()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "L":
                pos_start = self.pos.copy()
                valid, input_str = self.state75()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "N":
                pos_start = self.pos.copy()
                valid, input_str = self.state80()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "O":
                pos_start = self.pos.copy()
                valid, input_str = self.state84()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "P":
                pos_start = self.pos.copy()
                valid, input_str = self.state87()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "R":
                pos_start = self.pos.copy()
                valid, input_str = self.state96()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "S":
                pos_start = self.pos.copy()
                valid, input_str = self.state112()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "T":
                pos_start = self.pos.copy()
                valid, input_str = self.state128()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            elif self.current_char == "W":
                pos_start = self.pos.copy()
                valid, input_str = self.state140()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())           
            # Reserved Symbols
            elif self.current_char == "=":
                pos_start = self.pos.copy()
                valid, input_str = self.state144()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                   
            elif self.current_char == "+":
                pos_start = self.pos.copy()
                valid, input_str = self.state148()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                   
            elif self.current_char == "-":
                pos_start = self.pos.copy()
                valid, input_str = self.state152()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                   
            elif self.current_char == "*":
                pos_start = self.pos.copy()
                valid, input_str = self.state156()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                  
            elif self.current_char == "/":
                pos_start = self.pos.copy()
                valid, input_str = self.state160()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                   
            elif self.current_char == "%":
                pos_start = self.pos.copy()
                valid, input_str = self.state164()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                    
            elif self.current_char == "!":
                pos_start = self.pos.copy()
                valid, input_str = self.state168()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                   
            elif self.current_char == "<":
                pos_start = self.pos.copy()
                valid, input_str = self.state171()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                   
            elif self.current_char == ">":
                pos_start = self.pos.copy()
                valid, input_str = self.state175()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                    
            elif self.current_char == "&":
                pos_start = self.pos.copy()
                valid, input_str = self.state179()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                  
            elif self.current_char == "[":
                pos_start = self.pos.copy()
                valid, input_str = self.state181()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                   
            elif self.current_char == "{":
                pos_start = self.pos.copy()
                valid, input_str = self.state185()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                    
            elif self.current_char == "(":
                pos_start = self.pos.copy()
                valid, input_str = self.state189()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())                   
            elif self.current_char == "@":
                pos_start = self.pos.copy()
                valid, input_str = self.state193()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(InvalidIdentifierError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            #######################################
            # NUMERIC LITERALS
            #######################################
            elif self.current_char in num:
                pos_start = self.pos.copy()
                valid, input_str = self.state235()
                if valid:
                    tokens.append(input_str)
                elif not valid and "." in input_str:
                    periods = input_str.count(".")
                    if periods == 1:
                        whole, fractional = input_str.split(".")
                        # If the number of digits in the fractional part is more than 13, place overflowing digits in another
                        # variable
                        if len(fractional) > 13:
                            rounded = ""
                            for i, char in enumerate(fractional):
                                if i < 13:
                                    rounded += char
                            input_str = f"{whole}.{rounded}"
                            self.text = ""
                            for i, char in enumerate(fractional):
                                if i > 12:
                                    self.text += char
                            # Reset current_char
                            self.pos.reset()
                            pos_start = self.pos.copy()
                            self.current_char = self.text[self.pos.idx] if self.pos.idx < len(
                                self.text) else None
                            errors.append(OverflowError(
                                pos_start, self.pos, "'" + input_str + "'").as_string())
                        else:
                            errors.append(IllegalCharError(
                                pos_start, self.pos, "'" + input_str + "'").as_string())
                    elif periods > 1:
                        period_index = input_str.index(".")
                        whole_part = input_str[:period_index]
                        fractional_part = input_str[period_index +
                                                    1:period_index + 14]
                        self.text = input_str[period_index + 14:]
                        input_str = f"{whole_part}.{fractional_part}"
                        # Reset current_char
                        self.pos.reset()
                        pos_start = self.pos.copy()
                        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(
                            self.text) else None
                        errors.append(OverflowError(
                            pos_start, self.pos, "'" + input_str + "'").as_string())
                elif not valid and len(input_str) > 12:
                    errors.append(OverflowError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
            return tokens, errors                 
    """
    States 1 - 12 AND - Announce
    Chant 13 - 23 - Const
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

    # STARTING STATE AND - Announce
    def state1(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "N":
                return self.state2(input_str)
            case "n":
                return self.state5(input_str)
            case _:
                return False, input_str

    def state2(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "D":
                return self.state3(input_str)
            case _:
                return False, input_str
        
    def state3(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state4(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state4(self, input_str):
        return True, Token(TokenType.AND_OP.value, input_str)

    def state5(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state6(input_str)
            case _:
                return False, input_str
            
    def state6(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "o":
                return self.state7(input_str)
            case _:
                return False, input_str
            
    def state7(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "u":
                return self.state8(input_str)
            case _:
                return False, input_str

    def state8(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state9(input_str)
            case _:
                return False, input_str
            
    def state9(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "c":
                return self.state10(input_str)
            case _:
                return False, input_str

    def state10(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state11(input_str)
            case _:
                return False, input_str

    def state11(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
                return self.state12(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state12(self, input_str):
        return True, Token(TokenType.ANNOUNCE.value, input_str)
    
    def state13(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "h":
                return self.state14(input_str)
            case "o":
                return self.state19(input_str)
            case _:
                return False, input_str
            
    def state14(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state15(input_str)
            case _:
                return False, input_str
            
    def state15(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state16(input_str)
            case _:
                return False, input_str
            
    def state16(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state17(input_str)
            case _:
                return False, input_str
            
    def state17(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
                return self.state18(input_str)
        else:
            return False, input_str
        
    # FINAL STATE
    def state18(self, input_str):
        return True, Token(TokenType.CHANT.value, input_str)
    
    def state19(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state20(input_str)
            case _:
                return False, input_str
    def state20(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "s":
                return self.state21(input_str)
            case _:
                return False, input_str
            
    def state21(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state22(input_str)
            case _:
                return False, input_str
            
    def state22(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim7:
                return self.state23(input_str)
        else:
            return False, input_str
        
    # FINAL STATE
    def state23(self, input_str):
        return True, Token(TokenType.CONST.value, input_str)

    def state24(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state25(input_str)
            case "r":
                return self.state32(input_str)
            case "u":
                return self.state39(input_str)
            case _:
                return False, input_str
            
    def state25(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "f":
                return self.state26(input_str)
            case _:
                return False, input_str
            
    def state26(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state27(input_str)
            case _:
                return False, input_str
            
    def state27(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "u":
                return self.state28(input_str)
            case _:
                return False, input_str
            
    def state28(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "l":
                return self.state29(input_str)
            case _:
                return False, input_str
            
    def state29(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state30(input_str)
            case _:
                return False, input_str
            
    def state30(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
                return self.state31(input_str)
        else:
            return False, input_str
        
    # FINAL STATE
    def state31(self, input_str):
        return True, Token(TokenType.DEFAULT.value, input_str)
    
    def state32(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "i":
                return self.state33(input_str)
            case _:
                return False, input_str

    def state33(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "b":
                return self.state34(input_str)
            case _:
                return False, input_str
            
    def state34(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "b":
                return self.state35(input_str)
            case _:
                return False, input_str
            
    def state35(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "l":
                return self.state36(input_str)
            case _:
                return False, input_str
            
    def state36(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state37(input_str)
            case _:
                return False, input_str
        
    def state37(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
            return self.state38(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state38(self, input_str):
        return True, Token(TokenType.DRIBBLE.value, input_str)
    
    def state39(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state40(input_str)
            case _:
                return False, input_str

    def state40(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "k":
                return self.state41(input_str)
            case _:
                return False, input_str
            
    def state41(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
            return self.state42(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state42(self, input_str):
        return True, Token(TokenType.DUNK.value, input_str)

    def state43(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state44(input_str)
            case _:
                return False, input_str

    def state44(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "i":
                return self.state45(input_str)
            case _:
                return False, input_str
            
    def state45(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state46(input_str)
            case _:
                return False, input_str
            
    def state46(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state47(input_str)
            case _:
                return False, input_str
            
    def state47(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
            return self.state48(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state48(self, input_str):
        return True, Token(TokenType.FEINT.value, input_str)
    
    '''
    =, ==
    +, +=
    =, -=
    *, *=

    
    '''

    # REBOUND STATE 96 - 103
    def state96(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state97(input_str)
            case "u":
                return self.state109(input_str)
            case _:
                return False, input_str
    
    def state97(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "b":
                return self.state98(input_str)
            case "s":
                return self.state104(input_str)
            case _:
                return False, input_str
    
    def state98(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "o":
                return self.state99(input_str)
            case _:
                return False, input_str

    def state99(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "u":
                return self.state100(input_str)
            case _:
                return False, input_str

    def state100(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state101(input_str)
            case _:
                return False, input_str

    def state101(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "d":
                return self.state102(input_str)
            case _:
                return False, input_str

    def state102(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
            return self.state103(input_str)
        else:
            return False, input_str

    # REBOUND FINAL STATE
    def state103(self, input_str):
        return True, Token(TokenType.REBOUND.value, input_str)

    
    # RESUME STATE 
    def state104(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "u":
                return self.state105(input_str)
            case _:
                return False, input_str
    
    def state105(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "m":
                return self.state106(input_str)
            case _:
                return False, input_str
    
    def state106(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state107(input_str)
            case _:
                return False, input_str

    def state107(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim3:
            return self.state108(input_str)
        else:
            return False, input_str

    # RESUME FINAL STATE
    def state108(self, input_str):
        return True, Token(TokenType.RESUME.value, input_str)

    # RUN STATE
    def state109(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state110(input_str)
            case _:
                return False, input_str
    
    def state110(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim2:
            return self.state111(input_str)
        else:
            return False, input_str

    # RUN FINAL STATE
    def state111(self, input_str):
        return True, Token(TokenType.RUN.value, input_str)

    # SHOOT STATE
    def state112(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "h":
                return self.state113(input_str)
            case "t":
                return self.state118(input_str)
            case "w":
                return self.state122(input_str)
            case _:
                return False, input_str

    def state113(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "o":
                return self.state114(input_str)
            case _:
                return False, input_str

    def state114(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "o":
                return self.state115(input_str)
            case _:
                return False, input_str
    
    def state115(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state116(input_str)
            case _:
                return False, input_str

    def state116(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim2:
            return self.state117(input_str)
        else:
            return False, input_str

    # SHOOT FINAL STATE
    def state117(self, input_str):
        return True, Token(TokenType.SHOOT.value, input_str)

    # STAT FINAL STATE
    def state118(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state119(input_str)
            case _:
                return False, input_str
    
    def state119(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state120(input_str)
            case _:
                return False, input_str

    def state120(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
            return self.state121(input_str)
        else:
            return False, input_str

    # STAT FINAL STATE
    def state121(self, input_str):
        return True, Token(TokenType.STAT.value, input_str)

    # SWITCH STATE
    def state122(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "i":
                return self.state123(input_str)
            case _:
                return False, input_str
    
    def state123(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state124(input_str)
            case _:
                return False, input_str
    
    def state124(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "c":
                return self.state125(input_str)
            case _:
                return False, input_str

    def state125(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "h":
                return self.state126(input_str)
            case _:
                return False, input_str

    def state126(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
            return self.state127(input_str)
        else:
            return False, input_str

    # SWITCH FINAL STATE
    def state127(self, input_str):
        return True, Token(TokenType.SWITCH.value, input_str)

    # TEAM STATE
    def state128(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state129(input_str)
            case "i":
                return self.state133(input_str)    
            case _:
                return False, input_str

    def state129(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state130(input_str)
            case _:
                return False, input_str

    def state130(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "m":
                return self.state131(input_str)
            case _:
                return False, input_str

    def state131(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
            return self.state132(input_str)
        else:
            return False, input_str

    # TEAM FINAL STATE
    def state132(self, input_str):
        return True, Token(TokenType.TEAM.value, input_str)
    
    # TIMEOUT STATE
    def state133(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "m":
                return self.state134(input_str)
            case _:
                return False, input_str

    def state134(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state135(input_str)
            case _:
                return False, input_str
    
    def state135(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "o":
                return self.state136(input_str)
            case _:
                return False, input_str
    
    def state136(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "u":
                return self.state137(input_str)
            case _:
                return False, input_str

    def state137(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state138(input_str)
            case _:
                return False, input_str

    def state138(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim3:
            return self.state139(input_str)
        else:
            return False, input_str

    # TIMEOUT FINAL STATE
    def state139(self, input_str):
        return True, Token(TokenType.TIMEOUT.value, input_str)

    # WIN STATE
    def state140(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "i":
                return self.state141(input_str)
            case _:
                return False, input_str

    def state141(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state142(input_str)
            case _:
                return False, input_str
    
    def state142(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim3:
            return self.state143(input_str)
        else:
            return False, input_str

    # WIN FINAL STATE
    def state143(self, input_str):
        return True, Token(TokenType.WIN.value, input_str)


    # RESERVE SYMBOLS NI JACK

    # NOT EQUAL STATE
    def state168(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char == "=":
            return self.state169(input_str)
        else:
            return False, input_str

    # NOT EQUAL STATE
    def state169(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state170(input_str)
        else:
            return False, input_str

    # NOT EQUAL FINAL STATE
    def state170(self, input_str):
        return True, Token(TokenType.NOT_EQUAL.value, input_str)

    # LESS STATE
    def state171(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state172(input_str)
        elif self.current_char == "=":
            return self.state173(input_str)
        else:
            return False, input_str

    # LESS FINAL STATE
    def state172(self, input_str):
        return True, Token(TokenType.LESS_THAN.value, input_str)

    # LESS EQUAL STATE
    def state173(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state174(input_str)
        else:
            return False, input_str

    # LESS EQUAL FINAL STATE
    def state174(self, input_str):
        return True, Token(TokenType.LESS_EQUAL.value, input_str)

    # GREATER STATE
    def state175(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state176(input_str)
        elif self.current_char == "=":
            return self.state177(input_str)
        else:
            return False, input_str

    # GREATER FINAL STATE
    def state176(self, input_str):
        return True, Token(TokenType.GREATER_THAN.value, input_str)

    # GREATER EQUAL STATE
    def state177(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state178(input_str)
        else:
            return False, input_str

    # GREATER EQUAL FINAL STATE
    def state178(self, input_str):
        return True, Token(TokenType.GREATER_EQUAL.value, input_str)
    
    # CHANT_CONCAT STATE
    def state179(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim5:
            return self.state180(input_str)
        else:
            return False, input_str

    # CHANT_CONCAT FINAL STATE
    def state180(self, input_str):
        return True, Token(TokenType.CHANT_CONCAT.value, input_str)

    # ARRAY INDEX LEFT STATE
    def state181(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state182(input_str)
        elif self.current_char == "]":
            return self.state183(input_str)
        else:
            return False, input_str

    # ARRAY INDEX LEFT FINAL STATE
    def state182(self, input_str):
        return True, Token(TokenType.ARRAY_INDEX_LEFT.value, input_str)

    # ARRAY INDEX RIGHT STATE
    def state183(self, input_str):
        input_str <= self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state184(input_str)
        else:
            return False, input_str

    # ARRAY INDEX RIGHT FINAL STATE
    def state184(self, input_str):
        return True, Token(TokenType.ARRAY_INDEX_RIGHT.value, input_str)

    # CODE BLOCK LEFT STATE
    def state185(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state186(input_str)
        elif self.current_char == "}":
            return self.state187(input_str)
        else:
            return False, input_str

    # CODE BLOCK LEFT FINAL STATE
    def state186(self, input_str):
        return True, Token(TokenType.CODE_BLOCK_LEFT.value, input_str)

    # CODE BLOCK RIGHT STATE
    def state187(self, input_str):
        input_str <= self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state188(input_str)
        else:
            return False, input_str

    # CODE BLOCK RIGHT FINAL STATE
    def state188(self, input_str):
        return True, Token(TokenType.CODE_BLOCK_RIGHT.value, input_str)

    # LEFT PARENTHESIS STATE
    def state189(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state190(input_str)
        elif self.current_char == ")":
            return self.state191(input_str)
        else:
            return False, input_str

    #  LEFT PARENTHESIS FINAL STATE
    def state190(self, input_str):
        return True, Token(TokenType.LEFT_PAREN.value, input_str)

    # RIGHT PARENTHESIS STATE
    def state191(self, input_str):
        input_str <= self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state192(input_str)
        else:
            return False, input_str

    # RIGHT PARENTHESIS FINAL STATE
    def state193(self, input_str):
        return True, Token(TokenType.RIGHT_PAREN.value, input_str)
    
    
    '''

    IDENTIFIERS

    '''

    # IDENTIFIER STATE
    def state193(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char.isalpha() and self.current_char.islower():
            return self.state194(input_str)
        else:
            return False, input_str

    def state194(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in idt_delim:
            return self.state195(input_str)
        elif self.current_char == "_" or self.current_char.isalnum():
            return self.state196(input_str)
        else:
            return False, input_str

    def state195(self, input_str):
        return True, Token(TokenType.VAR_INIT.value, input_str)

    def state196(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in idt_delim:
            return self.state197(input_str)
        elif self.current_char == "_" or self.current_char.isalnum():
            return self.state198(input_str)
        else:
            return False, input_str

    def state197(self, input_str):
        return True, Token(TokenType.VAR_INIT.value, input_str)

    
    # numericals 
    # STARTING STATE
    def state235(self):
        input_str = ""
        zero_count = 0
        if self.current_char == "0":
            zero_count += 1
            self.advance()

        # Ignore multiple leading zeroes
        while self.current_char == "0" and zero_count == 1:
            self.advance()

        # 00000 = 0; 00000. = 0.
        if (self.current_char == None or self.current_char == ".") and zero_count == 1:
            input_str += "0"
        # 06 = 6
        elif self.current_char != None and self.current_char in digit:
            input_str += self.current_char
            self.advance()

        if self.current_char in num_delim:
            return self.state236(input_str)
        elif self.current_char in num:
            return self.state237(input_str)
        elif self.current_char == ".":
            return self.state207(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state236(self, input_str):
        return True, Token(TokenType.FEINTLIT.value, input_str)

    def state237(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in num_delim:
            return self.state238(input_str)
        elif self.current_char in num:
            return self.state239(input_str)
        elif self.current_char == ".":
            return self.state207(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state238(self, input_str):
        return True, Token(TokenType.FEINTLIT.value, input_str)


def run(text):
    # Create a lexer instance with the input text
    lexer = Lexer(text)
    # Generate tokens and errors by running the lexer
    tokens, errors = lexer.make_tokens()
    # Return the generated tokens and errors
    return tokens, errors

# Example usage:
# text = "your input text here"
# tokens, errors = run(text)
# print(tokens)
# print(errors)

