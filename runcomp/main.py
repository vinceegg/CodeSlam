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

def run_compiler(code, input_func=None):
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
            # Pass the input function to the compiler
            compiler.input_func = input_func
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
Feint @score;
Floater @scaledScore;
Stat @isValid = Loss;

Run {
Inbound("Enter a test score (0-100): ", @score);

Dribble ((@score >= 0) AND (@score <= 100)) {
@isValid = Win;
} Shoot {
Announce("Invalid score. Please enter a value between 0 and 100.\n");
}

} Play (@isValid == Loss);

@scaledScore = Floater(@score) / 100.0;

Dribble ((@score >= 90 AND @score <= 100) OR (@score >= 75 AND @score < 80)) {
Announce("Excellent or Fairly Good Score!\n");
} Shoot {
Announce("Average or Needs Improvement.\n");
}

Announce("Your scaled score is: " & @scaledScore);
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
