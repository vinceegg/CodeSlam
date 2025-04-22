from rply import LexerGenerator
from enum import Enum
from tokens import TokenType  # Assuming you placed TokenType and Token in tokens.py

def build_lexer():
    lg = LexerGenerator()

    # Keywords and reserved words
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

    for keyword, token_type in keywords.items():
        lg.add(token_type.name, rf'\b{keyword}\b')

    # Identifiers (must start with "@")
    lg.add(TokenType.VAR_INIT.name, r'@[a-zA-Z_][a-zA-Z0-9_]*')

    # Literals
    lg.add(TokenType.FEINTLIT.name, r'\b\d+\b')
    lg.add(TokenType.FLOATERLIT.name, r'\b\d+\.\d+\b')
    lg.add(TokenType.CHANTLIT.name, r'"[^"\n]*"')
    
    # Operators
    lg.add(TokenType.ASSIGN.name, r'=')
    lg.add(TokenType.ADD.name, r'\+')
    lg.add(TokenType.SUB.name, r'-')
    lg.add(TokenType.MUL.name, r'\*')
    lg.add(TokenType.DIV.name, r'/')
    lg.add(TokenType.MOD.name, r'%')

    # Compound assignment
    lg.add(TokenType.ADD_ASSIGN.name, r'\+=')
    lg.add(TokenType.SUB_ASSIGN.name, r'-=')
    lg.add(TokenType.MUL_ASSIGN.name, r'\*=')
    lg.add(TokenType.DIV_ASSIGN.name, r'/=')
    lg.add(TokenType.MOD_ASSIGN.name, r'%=')

    # Relational
    lg.add(TokenType.EQUAL.name, r'==')
    lg.add(TokenType.NOT_EQUAL.name, r'!=')
    lg.add(TokenType.LESS_THAN.name, r'<')
    lg.add(TokenType.GREATER_THAN.name, r'>')
    lg.add(TokenType.LESS_EQUAL.name, r'<=')
    lg.add(TokenType.GREATER_EQUAL.name, r'>=')

    # Logical
    lg.add(TokenType.AND_OP.name, r'AND')
    lg.add(TokenType.OR_OP.name, r'OR')
    lg.add(TokenType.NOT_OP.name, r'NOT')

    # Punctuation
    lg.add(TokenType.LEFT_PAREN.name, r'\(')
    lg.add(TokenType.RIGHT_PAREN.name, r'\)')
    lg.add(TokenType.CODE_BLOCK_LEFT.name, r'\{')
    lg.add(TokenType.CODE_BLOCK_RIGHT.name, r'\}')
    lg.add(TokenType.ARRAY_INDEX_LEFT.name, r'\[')
    lg.add(TokenType.ARRAY_INDEX_RIGHT.name, r'\]')
    lg.add(TokenType.COMMA.name, r',')
    lg.add(TokenType.COLON.name, r':')
    lg.add(TokenType.SEMICOLON.name, r';')

    # Comments
    lg.add(TokenType.SINGLE_COMMENT.name, r'//.*')
    lg.add(TokenType.MULTI_COMMENT.name, r'/\*[\s\S]*?\*/')

    # Ignored (whitespace, tabs, etc.)
    lg.ignore(r'\s+')

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

