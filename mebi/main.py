from lexical_analyzer.lexer import build_lexer
from syntax_analyzer.parser import pg
from semantic_analyzer.compiler import Compiler
from rply import ParserGenerator

def main():
    code = '''
Team() {
    Feint @year = 2024;  

    # Check for leap year
    Dribble ((@year % 4 == 0 AND @year % 100 != 0) OR (@year % 400 == 0)) {
        Announce(@year & " is a leap year.");
    } Shoot {
        Announce(@year & " is not a leap year.");
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
