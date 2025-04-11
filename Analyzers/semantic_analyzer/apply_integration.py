#!/usr/bin/env python3

"""
This script applies the semantic analyzer integration to the
code_editor_v2.py file automatically.

Usage:
    python apply_integration.py

It will:
1. Backup the original code_editor_v2.py file
2. Add the necessary imports
3. Replace the sidebar_button_semantic method
"""

import os
import sys
import re
import shutil
import datetime

# Add the parent directory (CODESLAM) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def apply_integration():
    """Apply the integration to code_editor_v2.py"""
    # Get the path to code_editor_v2.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    code_editor_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'CodeEditor', 'code_editor_v2.py'))
    
    if not os.path.exists(code_editor_path):
        print(f"Error: Could not find code_editor_v2.py at {code_editor_path}")
        return False
    
    # Create a backup
    backup_path = code_editor_path + f".bak.{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    shutil.copy2(code_editor_path, backup_path)
    print(f"Created backup at {backup_path}")
    
    # Read the file
    with open(code_editor_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add the import
    import_statement = "from Analyzers.semantic_analyzer.editor_integration import SemanticIntegration"
    
    # Check if the import already exists
    if import_statement in content:
        print("Import already exists, skipping...")
    else:
        # Find a good spot to add the import (after other imports)
        import_pattern = r'(from .+? import .+?\n)\n'
        match = re.search(import_pattern, content)
        
        if match:
            # Insert after the last import
            new_content = content[:match.end()] + import_statement + "\n\n" + content[match.end():]
            content = new_content
            print("Added import statement")
        else:
            print("Could not find a place to add the import, please add manually:")
            print(import_statement)
    
    # Replace the sidebar_button_semantic method
    semantic_method_pattern = r'def sidebar_button_semantic\(self\):[^}]*?(?=def|\Z)'
    
    new_method = """def sidebar_button_semantic(self):
        self.clear_terminal_output()
        self.editor_frame.clear_error_highlights()
        
        # Get the code from the editor
        code = self.codebox.get("1.0", "end-1c")
        
        # Use our semantic integration class to analyze the code
        # and display the output in the terminal
        result = SemanticIntegration.run_analysis(code, self.append_terminal_output)
        
        # If result contains error location coordinates, highlight the error
        if isinstance(result, tuple) and len(result) == 2:
            line_num, col_num = result
            self.editor_frame.highlight_error(line_num, col_num)

    """
    
    # Check if the method exists and replace it
    if re.search(semantic_method_pattern, content, re.DOTALL):
        content = re.sub(semantic_method_pattern, new_method, content, flags=re.DOTALL)
        print("Replaced sidebar_button_semantic method")
    else:
        print("Could not find sidebar_button_semantic method, please replace manually:")
        print(new_method)
    
    # Write the modified content back to the file
    with open(code_editor_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Integration applied to {code_editor_path}")
    print("Please test the integration by running the CodeSlam editor.")
    return True

def main():
    """Main function"""
    print("CodeSlam Semantic Analyzer Integration")
    print("====================================")
    
    choice = input("Apply integration to code_editor_v2.py? (y/n): ")
    if choice.lower() == 'y':
        success = apply_integration()
        if success:
            print("\nIntegration completed successfully!")
            print("\nNow you can run the CodeSlam editor and use the Semantic button")
            print("in the sidebar to analyze your code without showing that Python")
            print("libraries are being used for analysis.")
    else:
        print("Integration cancelled.")

if __name__ == "__main__":
    main() 