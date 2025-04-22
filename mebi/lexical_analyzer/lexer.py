from rply import LexerGenerator
from lexical_analyzer.tokens import TokenType 


def build_lexer():
    lg = LexerGenerator()

    # --- Reserved Keywords ---
    keywords = {
        "FEINT": TokenType.FEINT,
        "CHANT": TokenType.CHANT,
        "FLOATER": TokenType.FLOATER,
        "STAT": TokenType.STAT,
        "CONST": TokenType.CONST,
        "INBOUND": TokenType.INBOUND,
        "ANNOUNCE": TokenType.ANNOUNCE,
        "DRIBBLE": TokenType.DRIBBLE,
        "SHOOT": TokenType.SHOOT,
        "PASS": TokenType.PASS,
        "DEFAULT": TokenType.DEFAULT,
        "SWITCH": TokenType.SWITCH,
        "GET": TokenType.GET,
        "FORWARD": TokenType.FORWARD,
        "PLAY": TokenType.PLAY,
        "TIMEOUT": TokenType.TIMEOUT,
        "RESUME": TokenType.RESUME,
        "RUN": TokenType.RUN,
        "REBOUND": TokenType.REBOUND,
        "WIN": TokenType.WIN,
        "LOSS": TokenType.LOSS,
        "TEAM": TokenType.TEAM,
        "DUNK": TokenType.DUNK,
        "WILT": TokenType.WILT,
        "ZONE": TokenType.ZONE
    }

    for word, token in keywords.items():
        lg.add(token.name, rf"\b{word}\b")

    # --- Identifiers ---
    lg.add(TokenType.VAR_INIT.name, r"@[a-zA-Z_][a-zA-Z0-9_]*")

    # --- Literals ---
    lg.add(TokenType.NEGAFLOATER.name, r"-\d+\.\d+")
    lg.add(TokenType.FLOATERLIT.name, r"\d+\.\d+")
    lg.add(TokenType.NEGAFEINT.name, r"-\d+")
    lg.add(TokenType.FEINTLIT.name, r"\d+")
    lg.add(TokenType.CHANTLIT.name, r'"([^"\\]|\\.)*"')

    # --- Arithmetic Operators ---
    lg.add(TokenType.ADD.name, r"\+")
    lg.add(TokenType.SUB.name, r"-")
    lg.add(TokenType.MUL.name, r"\*")
    lg.add(TokenType.DIV.name, r"/")
    lg.add(TokenType.MOD.name, r"%")

    # --- Assignment Operators ---
    lg.add(TokenType.ADD_ASSIGN.name, r"\+=")
    lg.add(TokenType.SUB_ASSIGN.name, r"-=")
    lg.add(TokenType.MUL_ASSIGN.name, r"\*=")
    lg.add(TokenType.DIV_ASSIGN.name, r"/=")
    lg.add(TokenType.MOD_ASSIGN.name, r"%=")
    lg.add(TokenType.ASSIGN.name, r"=")

    # --- Relational Operators ---
    lg.add(TokenType.EQUAL.name, r"==")
    lg.add(TokenType.NOT_EQUAL.name, r"!=")
    lg.add(TokenType.LESS_EQUAL.name, r"<=")
    lg.add(TokenType.GREATER_EQUAL.name, r">=")
    lg.add(TokenType.LESS_THAN.name, r"<")
    lg.add(TokenType.GREATER_THAN.name, r">")

    # --- Logical Operators ---
    lg.add(TokenType.AND_OP.name, r"\bAND\b")
    lg.add(TokenType.OR_OP.name, r"\bOR\b")
    lg.add(TokenType.NOT_OP.name, r"\bNOT\b")

    # --- Structural Symbols ---
    lg.add(TokenType.LEFT_PAREN.name, r"\(")
    lg.add(TokenType.RIGHT_PAREN.name, r"\)")
    lg.add(TokenType.CODE_BLOCK_LEFT.name, r"\{")
    lg.add(TokenType.CODE_BLOCK_RIGHT.name, r"\}")
    lg.add(TokenType.ARRAY_INDEX_LEFT.name, r"\[")
    lg.add(TokenType.ARRAY_INDEX_RIGHT.name, r"\]")

    # --- Other Symbols ---
    lg.add(TokenType.COMMA.name, r",")
    lg.add(TokenType.COLON.name, r":")
    lg.add(TokenType.SEMICOLON.name, r";")
    lg.add(TokenType.QUOTE.name, r'"')
    lg.add(TokenType.UNDERSCORE.name, r"_")
    lg.add(TokenType.BACKSLASH.name, r"\\")
    lg.add(TokenType.INCREMENT.name, r"\+\+")
    lg.add(TokenType.DECREMENT.name, r"--")

    # --- Commenting ---
    lg.add(TokenType.SINGLE_COMMENT.name, r"//[^\n]*")
    lg.add(TokenType.MULTI_COMMENT.name, r"/\*[\s\S]*?\*/")

    # --- Escape Sequences ---
    lg.add(TokenType.BACKSLASH_AND.name, r"\\&")
    lg.add(TokenType.BACKSLASH_AT.name, r"\\@")
    lg.add(TokenType.ESCAPE_SEQUENCE.name, r"\\[ntr\"\\]")

    # --- Whitespace and Control Characters (ignored) ---
    lg.ignore(r"[ \t\r\f\v]+")
    lg.ignore(r"\n")  # Optional: Handle newline tracking separately if needed

    return lg.build()


if __name__ == "__main__":
    lexer = build_lexer()
    code = '''
    TEAM {
        FEINT @score = 10;
        ANNOUNCE "Welcome!";
    }
    '''
    for token in lexer.lex(code):
        print(token)

