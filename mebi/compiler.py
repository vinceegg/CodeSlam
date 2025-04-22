


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
