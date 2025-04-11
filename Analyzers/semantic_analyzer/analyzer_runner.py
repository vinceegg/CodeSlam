#!/usr/bin/env python3

import os
import sys
import re
import io
import traceback

# Add the parent directory (CODESLAM) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def analyze_input_code(code_string, output_callback=None):
    """
    Analyze code directly from a string input
    
    Args:
        code_string: The CodeSlam code as a string
        output_callback: Function to call with output messages
    
    Returns:
        None
    """
    try:
        if output_callback:
            output_callback("Starting CodeSlam code analysis...")
        else:
            print("Starting CodeSlam code analysis...", flush=True)
        
        # Count lines of code
        lines = code_string.splitlines()
        line_count = len(lines)
        
        # Keywords to look for
        codeslam_keywords = [
            "Team", "Wilt", "Feint", "Floater", "Chant", "Stat", "Forward", 
            "Play", "Run", "Switch", "Get", "Default", "Dribble", "Pass", 
            "Shoot", "Rebound", "Announce", "Inbound", "Zone", "Const",
            "Timeout", "Resume"
        ]
        
        # Count keyword occurrences
        keyword_counts = {}
        for keyword in codeslam_keywords:
            pattern = re.compile(r'\b' + keyword + r'\b')
            count = len(pattern.findall(code_string))
            if count > 0:
                keyword_counts[keyword] = count
        
        # Extract variables
        var_pattern = re.compile(r'(Feint|Floater|Chant|Stat)\s+(@\w+)')
        variables = [match.group(2) for match in var_pattern.finditer(code_string)]
        var_types = {}
        for match in var_pattern.finditer(code_string):
            var_types[match.group(2)] = match.group(1)
        
        # Extract functions
        func_pattern = re.compile(r'Wilt\s+(Feint|Floater|Chant|Stat|Dunk)\s+(@\w+)\s*\(([^)]*)\)')
        functions = []
        for match in func_pattern.finditer(code_string):
            return_type = match.group(1)
            func_name = match.group(2)
            params = match.group(3).strip()
            functions.append((func_name, return_type, params))
        
        # Count comments
        comment_pattern = re.compile(r'#.*$', re.MULTILINE)
        comments = comment_pattern.findall(code_string)
        
        # Extract control structures
        control_structures = {
            "Dribble": len(re.findall(r'\bDribble\s*\(', code_string)),
            "Pass": len(re.findall(r'\bPass\s*\(', code_string)),
            "Shoot": len(re.findall(r'\bShoot\s*\{', code_string)),
            "Forward": len(re.findall(r'\bForward\s*\(', code_string)),
            "Play": len(re.findall(r'\bPlay\s*\(', code_string)),
            "Run": len(re.findall(r'\bRun\s*\{', code_string)),
            "Switch": len(re.findall(r'\bSwitch\s*\(', code_string))
        }
        
        # Simple semantic check: all functions should return a value unless they're Dunk type
        semantic_errors = []
        for func_name, return_type, _ in functions:
            if return_type != "Dunk":  # Dunk is equivalent to void
                # Check if function has a return (Rebound statement)
                func_body_pattern = re.compile(r'Wilt\s+' + return_type + r'\s+' + 
                                            re.escape(func_name) + r'\s*\([^)]*\)\s*\{(.*?)\}', 
                                            re.DOTALL)
                func_body_match = func_body_pattern.search(code_string)
                if func_body_match:
                    func_body = func_body_match.group(1)
                    if "Rebound" not in func_body:
                        semantic_errors.append(f"Function {func_name} has return type {return_type} but no Rebound statement")
        
        # Output the results
        output = []
        output.append("=" * 50)
        output.append("CodeSlam Semantic Analysis Results")
        output.append("=" * 50)
        output.append(f"📊 Lines of Code: {line_count}")
        output.append(f"💬 Comments: {len(comments)}")
        output.append(f"🔠 Variables: {len(variables)}")
        output.append(f"⚙️ Functions: {len(functions)}")
        
        output.append("\n🔠 Variables:")
        for var in variables[:10]:  # Show first 10 variables
            output.append(f"   - {var} ({var_types.get(var, 'unknown')})")
        
        output.append("\n⚙️ Functions:")
        for func_name, return_type, params in functions[:5]:  # Show first 5 functions
            output.append(f"   - {func_name} ({return_type}) with parameters: {params}")
        
        output.append("\n🔄 Control Structures:")
        for structure, count in control_structures.items():
            if count > 0:
                output.append(f"   - {structure}: {count} occurrences")
        
        output.append("\n🔑 Keyword Usage:")
        for keyword, count in sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
            output.append(f"   - {keyword}: {count} occurrences")
        
        # Output any semantic errors
        if semantic_errors:
            output.append("\n❌ Semantic Errors:")
            for error in semantic_errors:
                output.append(f"   - {error}")
        else:
            output.append("\n✅ No semantic errors detected")
        
        # Send output to callback or print
        if output_callback:
            for line in output:
                output_callback(line)
        else:
            # Print with immediate flush to ensure output appears
            for line in output:
                print(line, flush=True)
        
        # NEW: Execute the code to show Announce outputs
        if "Announce" in keyword_counts and not semantic_errors:
            execute_code(code_string, output_callback)
    
    except Exception as e:
        error_msg = f"Error during analysis: {str(e)}"
        traceback.print_exc()
        if output_callback:
            output_callback(error_msg)
        else:
            print(error_msg, flush=True)

def execute_code(code_string, output_callback=None):
    """
    Simple execution of CodeSlam code to show outputs of Announce statements
    
    Args:
        code_string: The CodeSlam code as a string
        output_callback: Function to call with output messages
    """
    # Define the output function
    def show_output(message):
        if output_callback:
            output_callback(f"\n📢 Program Output: {message}")
        else:
            print(f"\n📢 Program Output: {message}", flush=True)
    
    # Extract and execute Announce statements
    announce_pattern = re.compile(r'Announce\s*\(\s*"([^"]*)"\s*\)')
    announce_matches = announce_pattern.findall(code_string)
    
    # If there are Announce statements, add a header
    if announce_matches:
        if output_callback:
            output_callback("\n🎮 Running program...")
        else:
            print("\n🎮 Running program...", flush=True)
            
        # Show all Announce outputs
        for message in announce_matches:
            show_output(message)

def main():
    """Run the analyzer with test code or file input"""
    try:
        if len(sys.argv) > 1:
            # Read code from file
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                code = f.read()
                print(f"Analyzing file: {sys.argv[1]}", flush=True)
        else:
            # Use sample code
            current_dir = os.path.dirname(os.path.abspath(__file__))
            sample_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'CodeSlam sample programs', 'codeslam_sample.txt'))
            with open(sample_path, 'r', encoding='utf-8') as f:
                code = f.read()
                print(f"Analyzing sample file: {os.path.basename(sample_path)}", flush=True)
        
        # Print some basic information before analysis
        print(f"Code length: {len(code)} characters", flush=True)
        print(f"Lines of code: {len(code.splitlines())}", flush=True)
        
        analyze_input_code(code)
    
    except Exception as e:
        print(f"ERROR: {str(e)}", flush=True)
        traceback.print_exc()

if __name__ == "__main__":
    main() 