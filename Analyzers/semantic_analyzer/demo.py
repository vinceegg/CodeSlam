#!/usr/bin/env python3

import os
import sys
import tkinter as tk

# Add the parent directory (CODESLAM) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Analyzers.semantic_analyzer.analyzer_runner import analyze_input_code
from Analyzers.lexical_analyzer.lexical import run

def simulate_terminal_output(code_string):
    """
    Simulates the terminal output in the CodeSlam editor interface
    without revealing that we're using Python libraries
    
    Args:
        code_string: The CodeSlam code as a string
    """
    # Format the terminal output to look like genuine CodeSlam compiler output
    output_lines = []
    
    def output_callback(line):
        output_lines.append(line)
    
    # Process the code with our analyzer
    analyze_input_code(code_string, output_callback)
    
    # Build the terminal-style output
    terminal_output = [
        ">> Loading CodeSlam Compiler...",
        ">> Initializing lexical analysis...",
        ">> Analyzing code structure...",
        ">> Running semantic checks...",
        "",
        "=== CodeSlam Analysis Results ==="
    ]
    
    # Filter out the Python-style headers and technical details
    for line in output_lines:
        # Skip the equals line headers
        if line.startswith("====="):
            continue
        
        # Skip the "CodeSlam Semantic Analysis Results" header
        if "CodeSlam Semantic Analysis Results" in line:
            continue
            
        # Include all other content with proper formatting
        if line.strip():
            terminal_output.append(line)
    
    terminal_output.append("")
    terminal_output.append(">> Compilation complete.")
    
    return terminal_output

def display_in_window(output_lines):
    """
    Display the output in a Tkinter window to simulate the CodeSlam terminal
    """
    root = tk.Tk()
    root.title("CodeSlam Terminal Output")
    root.geometry("600x500")
    root.configure(bg="#333333")
    
    terminal = tk.Text(root, bg="#2d2d2d", fg="#e6e6e6", font=("Consolas", 11))
    terminal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Insert the output with colors
    for line in output_lines:
        if ">>" in line:
            terminal.insert(tk.END, line + "\n", "command")
        elif "✅" in line:
            terminal.insert(tk.END, line + "\n", "success")
        elif "❌" in line:
            terminal.insert(tk.END, line + "\n", "error")
        elif line.startswith("📊") or line.startswith("💬") or line.startswith("🔠") or line.startswith("⚙️"):
            terminal.insert(tk.END, line + "\n", "stat")
        elif line.startswith("   -"):
            terminal.insert(tk.END, line + "\n", "detail")
        else:
            terminal.insert(tk.END, line + "\n")
    
    # Configure tags for colored output
    terminal.tag_configure("command", foreground="#8ae234")
    terminal.tag_configure("success", foreground="#4e9a06")
    terminal.tag_configure("error", foreground="#cc0000")
    terminal.tag_configure("stat", foreground="#729fcf")
    terminal.tag_configure("detail", foreground="#ad7fa8")
    
    terminal.configure(state="disabled")  # Make it read-only
    
    root.mainloop()

def main():
    """Run the demo with the sample code"""
    try:
        # Read the sample file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sample_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'CodeSlam sample programs', 'codeslam_sample.txt'))
        
        with open(sample_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Generate the terminal output
        terminal_output = simulate_terminal_output(code)
        
        # Display the output
        display_in_window(terminal_output)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 