from lexical_analyzer.lexer import build_lexer
from syntax_analyzer.parser import pg
from semantic_analyzer.compiler import Compiler
from rply import ParserGenerator

def main():
    code = '''
Team() {
    Feint @i = 1;
    Feint @j = 1;
    Feint @rows = 5;
    Feint @cols = 8;

    Forward (@i = 1; @i <= @rows; @i++) {
        @j = 1;
        Forward (@j = 1; @j <= @cols; @j++) {
            Announce("* ");
        }
        Announce("\n");
    }
}

 '''

    # Build lexer and tokenize input
    lexer = build_lexer()
    tokens = lexer.lex(code)

    # Build parser and parse tokens into AST
    parser = pg.build()
    try:
        ast = parser.parse(tokens)
        print("\nPARSE SUCCESSFUL!")
        print("AST Output:\n", ast)
        # --- Evaluate ---
        print("\nEVALUATION RESULT:")
        compiler = Compiler()
        compiler.eval(ast)
    except Exception as e:
        print("\nPARSE ERROR!")
        print(e)

if __name__ == "__main__":
    main()
