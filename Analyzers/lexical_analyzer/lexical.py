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

            #Reserved Symbols
            elif self.current_char == "=":
                pos_start = self.pos.copy()
                valid, input_str = self.state124()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "+":
                pos_start = self.pos.copy()
                valid, input_str = self.state128()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "-":
                pos_start = self.pos.copy()
                valid, input_str = self.state132()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "*":
                pos_start = self.pos.copy()
                valid, input_str = self.state136()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "/":
                pos_start = self.pos.copy()
                valid, input_str = self.state140()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "%":
                pos_start = self.pos.copy()
                valid, input_str = self.state144()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "!":
                pos_start = self.pos.copy()
                valid, input_str = self.state148()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "<":
                pos_start = self.pos.copy()
                valid, input_str = self.state151()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == ">":
                pos_start = self.pos.copy()
                valid, input_str = self.state155()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "&":
                pos_start = self.pos.copy()
                valid, input_str = self.state159()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "[":
                pos_start = self.pos.copy()
                valid, input_str = self.state161()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "{":
                pos_start = self.pos.copy()
                valid, input_str = self.state165()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "(":
                pos_start = self.pos.copy()
                valid, input_str = self.state169()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())
                    
            elif self.current_char == "@":
                pos_start = self.pos.copy()
                valid, input_str = self.state173()
                if valid:
                    tokens.append(input_str)
                else:
                    errors.append(IllegalCharError(
                        pos_start, self.pos, "'" + input_str + "'").as_string())

"""
States 1 - 12 AND - Announce
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


# STARTING STATE
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

    def state2(self):
        input_str = ""
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

    def state5(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state6(input_str)
            case _:
                return False, input_str
            
    def state6(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "o":
                return self.state7(input_str)
            case _:
                return False, input_str
            
    def state7(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "u":
                return self.state8(input_str)
            case _:
                return False, input_str

    def state8(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state9(input_str)
            case _:
                return False, input_str
            
    def state9(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "c":
                return self.state10(input_str)
            case _:
                return False, input_str

    def state10(self):
        input_str = ""
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
    def state14(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state15(input_str)
            case _:
                return False, input_str
    def state15(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state16(input_str)
            case _:
                return False, input_str
    def state16(self):
        input_str = ""
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
    
    def state19(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "n":
                return self.state20(input_str)
            case _:
                return False, input_str
    def state20(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "s":
                return self.state21(input_str)
            case _:
                return False, input_str
    def state21(self):
        input_str = ""
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
                return self.state31(input_str)
            case "u":
                return self.state39(input_str)
            case _:
                return False, input_str
    def state25(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "f":
                return self.state26(input_str)
            case _:
                return False, input_str
    def state26(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "a":
                return self.state27(input_str)
            case _:
                return False, input_str
    def state27(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "u":
                return self.state28(input_str)
            case _:
                return False, input_str
    def state28(self):
        input_str = ""
        input_str += self.current_char
        self.advance()

        match self.current_char:
            case "l":
                return self.state29(input_str)
            case _:
                return False, input_str
    def state29(self):
        input_str = ""
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
    

def run(fn, text, ln):

    lexer = Lexer(fn, text, ln)
    tokens, errors = lexer.make_tokens()
    return tokens, errors

#thisa a comment