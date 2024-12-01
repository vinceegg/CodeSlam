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
Tony Stark - 144 - 167
Jack of All Trades - 168 - 192

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
                             
            # RESERVED  SYMBOLS

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
            # RETURN ERROR
            else:
                pos_start = self.pos.copy()
                errors.append(IllegalCharError(
                    pos_start, self.pos, "'" + self.current_char + "'").as_string())
                self.advance()
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
            case "l":
                return self.state49(input_str)
            case "o":
                return self.state56(input_str)
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
    
    def state49(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "o":
                return self.state50(input_str)
            case _:
                return False, input_str
    
    def state50(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state51(input_str)
            case _:
                return False, input_str
            
    def state51(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state52(input_str)
            case _:
                return False, input_str
            
    def state52(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state53(input_str)
            case _:
                return False, input_str
            
    def state53(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "r":
                return self.state54(input_str)
            case _:
                return False, input_str
            
    def state54(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
                return self.state55(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state55(self, input_str):
        return True, Token(TokenType.FLOATER.value, input_str)
    
    def state56(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "r":
                return self.state57(input_str)
            case _:
                return False, input_str
    
    def state57(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "w":
                return self.state58(input_str)
            case _:
                return False, input_str
            
    def state58(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state59(input_str)
            case _:
                return False, input_str
            
    def state59(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "r":
                return self.state60(input_str)
            case _:
                return False, input_str
            
    def state60(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "d":
                return self.state61(input_str)
            case _:
                return False, input_str
             
    def state61(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
                return self.state62(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state62(self, input_str):
        return True, Token(TokenType.FORWARD.value, input_str)

    def state63(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "e":
                return self.state64(input_str)
            case _:
                return False, input_str

    def state64(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "t":
                return self.state65(input_str)
            case _:
                return False, input_str
        
    def state65(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state66(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state66(self, input_str):
        return True, Token(TokenType.GET.value, input_str)
    
    def state67(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state68(input_str)
            case _:
                return False, input_str

    def state68(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "b":
                return self.state69(input_str)
            case _:
                return False, input_str
            
    def state69(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "o":
                return self.state70(input_str)
            case _:
                return False, input_str
            
    def state70(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "u":
                return self.state71(input_str)
            case _:
                return False, input_str
            
    def state71(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state72(input_str)
            case _:
                return False, input_str
            
    def state72(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "d":
                return self.state73(input_str)
            case _:
                return False, input_str
        
    def state73(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
            return self.state74(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state74(self, input_str):
        return True, Token(TokenType.INBOUND.value, input_str)

    def state75(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "o":
                return self.state76(input_str)
            case _:
                return False, input_str

    def state76(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "s":
                return self.state77(input_str)
            case _:
                return False, input_str
            
    def state77(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "s":
                return self.state78(input_str)
            case _:
                return False, input_str
        
    def state78(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim3:
            return self.state79(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state79(self, input_str):
        return True, Token(TokenType.LOSS.value, input_str)

    def state80(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "O":
                return self.state81(input_str)
            case _:
                return False, input_str

    def state81(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "T":
                return self.state82(input_str)
            case _:
                return False, input_str
        
        
    def state82(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state83(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state83(self, input_str):
        return True, Token(TokenType.NOT_OP.value, input_str)
    
    def state84(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "R":
                return self.state85(input_str)
            case _:
                return False, input_str
        
    def state85(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim6:
            return self.state86(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state86(self, input_str):
        return True, Token(TokenType.OR_OP.value, input_str)

    def state87(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state88(input_str)
            case "l":
                return self.state92(input_str)
            case _:
                return False, input_str

    def state88(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "s":
                return self.state89(input_str)
            case _:
                return False, input_str
            
    def state89(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "s":
                return self.state90(input_str)
            case _:
                return False, input_str
        
    def state90(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
            return self.state91(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state91(self, input_str):
        return True, Token(TokenType.PASS.value, input_str)

    def state92(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state93(input_str)
            case _:
                return False, input_str
            
    def state93(self, input_str):
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "y":
                return self.state94(input_str)
            case _:
                return False, input_str

    def state94(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim1:
                return self.state95(input_str)
        else:
            return False, input_str
            
    # FINAL STATE
    def state95(self, input_str):
        return True, Token(TokenType.PLAY.value, input_str)

    '''
    RESERVED SYMBOLS
    =, ==
    +, +=
    =, -=
    *, *=

    
    '''

    def state144(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim5:
            return self.state145(input_str)
        elif self.current_char == "=":
            return self.state146(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state145(self, input_str):
        return True, Token(TokenType.ASSIGN.value, input_str)

    def state146(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state147(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state147(self, input_str):
        return True, Token(TokenType.EQUAL.value, input_str)

    def state148(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state149(input_str)
        elif self.current_char == "=":
            return self.state150(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state149(self, input_str):
        return True, Token(TokenType.ADD.value, input_str)

    def state150(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state151(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state151(self, input_str):
        return True, Token(TokenType.ADD_ASSIGN.value, input_str)
    
    def state152(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state153(input_str)
        elif self.current_char == "=":
            return self.state154(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state153(self, input_str):
        return True, Token(TokenType.SUB.value, input_str)

    def state154(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state155(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state155(self, input_str):
        return True, Token(TokenType.SUB_ASSIGN.value, input_str)

    def state156(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state157(input_str)
        elif self.current_char == "=":
            return self.state158(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state157(self, input_str):
        return True, Token(TokenType.MUL.value, input_str)

    def state158(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state159(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state159(self, input_str):
        return True, Token(TokenType.MUL_ASSIGN.value, input_str)
    
    def state160(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state161(input_str)
        elif self.current_char == "=":
            return self.state162(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state161(self, input_str):
        return True, Token(TokenType.DIV.value, input_str)

    def state162(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state163(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state163(self, input_str):
        return True, Token(TokenType.DIV_ASSIGN.value, input_str)

    def state164(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state165(input_str)
        elif self.current_char == "=":
            return self.state166(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state165(self, input_str):
        return True, Token(TokenType.MOD.value, input_str)

    def state166(self, input_str):
        input_str += self.current_char
        self.advance()

        if self.current_char in delim4:
            return self.state167(input_str)
        else:
            return False, input_str

    # FINAL STATE
    def state167(self, input_str):
        return True, Token(TokenType.MOD_ASSIGN.value, input_str)
    
    '''

    IDENTIFIERS

    '''

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

