import sys
import os
import io

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from lexical_analyzer.lexer import build_lexer
from syntax_analyzer.parser import pg
from semantic_analyzer.compiler import Compiler
from rply import ParserGenerator

def run_compiler(code):
    # Create StringIO to capture output
    output = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = output
    
    try:
        # Build lexer and tokenize input
        lexer = build_lexer()
        tokens = lexer.lex(code)

        # Build parser and parse tokens into AST
        parser = pg.build()
        try:
            ast = parser.parse(tokens)
            compiler = Compiler()
            compiler.eval(ast)  # This will write to our StringIO
            return output.getvalue()  # Return the captured output
            
        except Exception as e:
            return str(e)
            
    finally:
        sys.stdout = old_stdout
        output.close()

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
    print(run_compiler(code))

if __name__ == "__main__":
    main()
