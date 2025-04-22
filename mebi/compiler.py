from lexical_analyzer.lexer import build_lexer
from syntax_analyzer.parser import pg
from semantic_analyzer.compiler import Compiler
from rply import ParserGenerator

def main():
    code = '''
Team() {
    Feint @x = 4;
    Feint @y = 2;
    Feint @z = 3;
    Feint @result;

    Inbound("enter", @result);
    Announce("Final value: " & (@x + @y * 2 - (8 / 4) + 10 % 3) * @result);
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
