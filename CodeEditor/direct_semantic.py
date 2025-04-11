#!/usr/bin/env python3
"""
Simple standalone script to analyze CodeSlam code semantically.
This can be run directly from the command line or imported and used in other scripts.
"""

import os
import sys
import re

# Add the parent directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def analyze_code(code_text, output_func=print):
    """
    Analyze CodeSlam code and send output to the provided function
    
    Args:
        code_text: The CodeSlam code as a string
        output_func: Function to call with output messages (defaults to print)
    
    Returns:
        None
    """
    try:
        # Print introduction
        output_func(">> Loading CodeSlam Compiler...")
        output_func(">> Initializing lexical analysis...")
        output_func(">> Analyzing code structure...")
        output_func(">> Running semantic checks...")
        output_func("")
        output_func("=== CodeSlam Analysis Results ===")
        
        # Import analyzer (done here to avoid circular imports)
        from Analyzers.semantic_analyzer.analyzer_runner import analyze_input_code
        
        # Run analyzer with the output function
        analyze_input_code(code_text, output_func)
        
        # Show completion
        output_func("")
        output_func(">> Compilation complete.")
        
        return None  # Success
        
    except Exception as e:
        error_msg = f"Semantic Error: {str(e)}"
        output_func(error_msg)
        
        # Try to extract line and column from the error
        error_text = str(e)
        match = re.search(r"line (\d+), column (\d+)", error_text)
        if match:
            line_num = int(match.group(1))
            col_num = int(match.group(2))
            return (line_num, col_num)  # Return error location for highlighting
        
        return error_msg  # Return error message

def main():
    """Command line entry point"""
    if len(sys.argv) > 1:
        # Read code from file
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            
            print(f"Analyzing file: {filename}")
            analyze_code(code)
            
        except Exception as e:
            print(f"Error: {str(e)}")
    else:
        print("Usage: python direct_semantic.py <filename>")
        print("Provide a CodeSlam source file to analyze")

if __name__ == "__main__":
    main() 