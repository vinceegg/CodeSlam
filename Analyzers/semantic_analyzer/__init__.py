from .semantic_analyzer import analyze_code_editor
from .analyzer_runner import analyze_input_code

def analyze_and_execute(tokens, output_callback=None, debug=False, list_vars=False):
    """
    Analyze tokens from the CodeSlam language and execute the code
    
    Parameters:
    - tokens: List of tokens from the lexical analyzer
    - output_callback: Function to call with output messages
    - debug: Boolean to enable/disable debug messages
    - list_vars: Boolean to enable/disable variable listing
    
    Returns:
    - None on success, or error message on failure
    """
    try:
        # Convert tokens to CodeSlam source code string format
        # This is a simplified approach - in a real system you'd have proper tokenstream handling
        code = ""
        current_line = ""
        
        for token in tokens:
            if token.type == "NEWLINE":
                code += current_line + "\n"
                current_line = ""
            else:
                # Add spacing around most tokens
                if token.type not in ["WHITESPACE", "COMMA", "SEMICOLON"]:
                    if current_line and not current_line.endswith(" "):
                        current_line += " "
                
                # Add the token value
                current_line += token.value
                
                # Add space after certain tokens
                if token.type not in ["WHITESPACE", "LPAREN", "LBRACE", "LBRACKET"]:
                    current_line += " "
        
        # Add the last line if it exists
        if current_line.strip():
            code += current_line
        
        # Use our more advanced analyzer
        if output_callback:
            output_callback("Starting semantic analysis...")
            
        # Perform the analysis
        analyze_input_code(code, output_callback)
        return None  # Success
        
    except Exception as e:
        error_msg = f"Semantic analysis failed: {str(e)}"
        if output_callback:
            output_callback(error_msg)
        return error_msg  # Return error message on failure
