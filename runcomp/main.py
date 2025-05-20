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
    # Allow for real-time output via output_callback
    output_callback = None
    # If the caller passes an output_callback as a kwarg, use it
    if hasattr(input_func, "__self__") and hasattr(input_func.__self__, "output_callback"):
        output_callback = input_func.__self__.output_callback
    elif hasattr(input_func, "output_callback"):
        output_callback = input_func.output_callback
    # Or, if the caller passes output_callback directly (for future-proofing)
    if hasattr(run_compiler, "output_callback"):
        output_callback = run_compiler.output_callback

    class CallbackWriter:
        def write(self, s):
            if output_callback:
                output_callback(s)
            else:
                sys.__stdout__.write(s)
            self.flush()
        def flush(self):
            if output_callback:
                output_callback("")  # Trigger GUI update if needed

    old_stdout = sys.stdout
    sys.stdout = CallbackWriter()
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
            # Pass output_callback to the compiler if it supports it
            if hasattr(compiler, 'set_output_callback'):
                compiler.set_output_callback(output_callback)
            compiler.eval(ast)
            return None
        except Exception as e:
            return str(e)
    finally:
        sys.stdout = old_stdout

def main():
    code = '''
Team(){
Feint @x = 42, @z;
Floater @y = 3.14, @q;
Chant @msg = "Hello!";
@z = @y;
@q = @x;
Announce(@x & "\n");
Announce(@z & "\n");
Announce(@msg & "\n");
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
