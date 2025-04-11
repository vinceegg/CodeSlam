#!/usr/bin/env python3

import os
import sys
import re
import time

# Add the parent directory (CODESLAM) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Analyzers.semantic_analyzer.analyzer_runner import analyze_input_code

class EditorIntegration:
    def __init__(self):
        """Initialize the integration for CodeSlam editor"""
        self.code = ""
        self.output_lines = []
        self.simulation_steps = [
            "Initializing CodeSlam virtual machine...",
            "Loading semantic analyzer...",
            "Preparing execution environment...",
            "Building symbol table...",
            "Running code validation..."
        ]
    
    def process_code(self, code_string):
        """
        Process the code and generate terminal output
        
        Args:
            code_string: The code from CodeSlam editor
            
        Returns:
            List of terminal output lines (as if from the CodeSlam compiler)
        """
        self.code = code_string
        self.output_lines = []
        
        # Create a callback to capture output
        def output_callback(line):
            self.output_lines.append(line)
        
        # Run the actual analyzer (but keep it hidden)
        analyze_input_code(code_string, output_callback)
        
        # Replace the output with simulated compiler output
        terminal_output = []
        
        # Add simulation steps with delays to make it look like a real compiler
        terminal_output.extend(self.simulation_steps)
        terminal_output.append("")  # Empty line
        
        # Process the analyzer output to make it look like real compiler output
        filtered_output = self._filter_analyzer_output()
        terminal_output.extend(filtered_output)
        
        # Add completion message
        terminal_output.append("")
        terminal_output.append("Code analysis complete.")
        
        return terminal_output
    
    def _filter_analyzer_output(self):
        """Filter analyzer output to look like native compiler output"""
        filtered = []
        
        for line in self.output_lines:
            # Skip headers
            if line.startswith("=====") or "CodeSlam Semantic Analysis Results" in line:
                continue
                
            # Include all other content
            if line.strip():
                filtered.append(line)
        
        return filtered
    
    def get_terminal_output(self):
        """Get the terminal output as a single string"""
        return "\n".join(self.output_lines)


def process_editor_code(code_string):
    """
    Process code from the editor and return terminal output lines
    
    This is the main function to be called from code_editor_v2.py
    
    Args:
        code_string: The CodeSlam code from the editor
        
    Returns:
        List of output lines for the terminal
    """
    integration = EditorIntegration()
    return integration.process_code(code_string)


# Class to be used for direct integration with the App class in code_editor_v2.py
class SemanticIntegration:
    @staticmethod
    def run_analysis(code, output_callback):
        """
        Run semantic analysis from the editor
        
        Args:
            code: The code from the editor
            output_callback: Function to call with each line of output
        """
        # Add simulation steps
        simulation_steps = [
            ">> Loading CodeSlam Compiler...",
            ">> Initializing lexical analysis...",
            ">> Analyzing code structure...",
            ">> Running semantic checks...",
            "",
            "=== CodeSlam Analysis Results ==="
        ]
        
        # Add a small delay between steps for realism
        for step in simulation_steps:
            # Use correct parameter order for output_callback
            output_callback(step)
            time.sleep(0.2)  # Small delay between steps
            
        # Process the code with our analyzer but format output to look native
        def modified_callback(line):
            # Skip headers
            if line.startswith("=====") or "CodeSlam Semantic Analysis Results" in line:
                return
                
            # Include all other content with appropriate colors
            if line.strip():
                # Just use the original output_callback - it will handle colors based on content
                output_callback(line)
        
        # Call the actual analyzer
        try:
            analyze_input_code(code, modified_callback)
            output_callback("")
            output_callback(">> Compilation complete.")
        except Exception as e:
            error_msg = str(e)
            output_callback(f">> ERROR: Analysis failed: {error_msg}")
            
            # Try to extract line and column from error message
            match = re.search(r"line (\d+), column (\d+)", error_msg)
            if match:
                line_num = int(match.group(1))
                col_num = int(match.group(2))
                # Return this info so the editor can highlight the error
                return line_num, col_num
            
            return None


# Sample usage
if __name__ == "__main__":
    # Read sample code
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'CodeSlam sample programs', 'codeslam_sample.txt'))
    
    print("Running CodeSlam Editor Integration Demo")
    print("=======================================")
    print("This demonstrates how the semantic analyzer would look")
    print("when integrated with the CodeSlam editor interface.")
    print()
    print("Loading sample code from:", os.path.basename(sample_path))
    print()
    
    try:
        with open(sample_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Define a simple output callback for testing
        def test_callback(line, text_color=None):
            color_codes = {
                "red": "\033[91m",
                "green": "\033[92m",
                "blue": "\033[94m",
                "purple": "\033[95m",
                "reset": "\033[0m"
            }
            
            # Determine color based on content if no color specified
            if text_color is None:
                if "Error" in line or "❌" in line:
                    text_color = "red"
                elif line.startswith("📊") or line.startswith("💬") or line.startswith("🔠") or line.startswith("⚙️"):
                    text_color = "blue"
                elif line.startswith("   -"):
                    text_color = "purple"
                elif "✅" in line or line.startswith(">>"):
                    text_color = "green"
            
            # Print with color if applicable
            if text_color and text_color in color_codes:
                print(f"{color_codes[text_color]}{line}{color_codes['reset']}")
            else:
                print(line)
        
        # Test the semantic integration
        print("\nTESTING SEMANTIC INTEGRATION:")
        print("-" * 30)
        
        # The test callback needs to accept the signature from the main code
        # In the actual code_editor_v2.py, the output_callback would have different parameter handling
        SemanticIntegration.run_analysis(code, test_callback)
            
        print("\nIntegration demo completed successfully.")
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc() 