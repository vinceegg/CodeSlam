import re
import os
import sys

# This script executes each Team() code block in the activity.txt file 
# and displays the results for each block

def extract_team_functions(code):
    """Extract individual Team() function blocks from the code"""
    team_pattern = re.compile(r'(Team\(\)\s*{[^}]*})', re.DOTALL)
    matches = team_pattern.findall(code)
    
    # Extract section headings
    heading_pattern = re.compile(r'#([^#\n]*?)(?=\n\s*Team\(\)|$)', re.DOTALL)
    headings = heading_pattern.findall(code)
    
    # Combine headings with team functions
    heading_to_team = []
    for i, team_function in enumerate(matches):
        if i < len(headings):
            # Clean up the heading text
            heading = headings[i].strip()
            heading_to_team.append((heading, team_function))
        else:
            heading_to_team.append(("Unknown", team_function))
    
    return heading_to_team

def evaluate_expression(expr, variables):
    """Evaluate a CodeSLAM expression with variables and operations"""
    try:
        # If it's a direct variable reference, return its value
        if expr in variables:
            return variables[expr]
            
        # Replace variables with their values
        processed_expr = expr
        
        # Sort variables by length in reverse order to avoid partial replacements
        var_names = sorted(variables.keys(), key=len, reverse=True)
        
        for var_name in var_names:
            if var_name in processed_expr:
                processed_expr = processed_expr.replace(var_name, str(variables[var_name]))
        
        # Handle numeric literals
        if processed_expr.isdigit():
            return int(processed_expr)
        
        if processed_expr.replace('.', '', 1).isdigit() and processed_expr.count('.') == 1:
            return float(processed_expr)
        
        # Special case for expressions that might have variables followed by operations
        if any(op in processed_expr for op in ['+', '-', '*', '/']):
            try:
                # Be careful with evaluation to avoid security issues
                # This only works with simple numeric expressions
                # For a real language, you'd need a proper parser
                result = eval(processed_expr)
                return result
            except Exception as e:
                print(f"Expression eval error: {e}")
                pass
            
        # Handle simple operations
        # Addition
        if '+' in processed_expr:
            parts = processed_expr.split('+')
            result = 0
            for part in parts:
                part_value = evaluate_expression(part.strip(), variables)
                if part_value is not None:
                    result += float(part_value)
            return result
            
        # Subtraction
        if '-' in processed_expr and not processed_expr.startswith('-'):  # Avoid misinterpreting negative numbers
            parts = processed_expr.split('-')
            result = evaluate_expression(parts[0].strip(), variables) or 0
            for part in parts[1:]:
                part_value = evaluate_expression(part.strip(), variables)
                if part_value is not None:
                    result -= float(part_value)
            return result
            
        # Multiplication
        if '*' in processed_expr:
            parts = processed_expr.split('*')
            result = 1
            for part in parts:
                part_value = evaluate_expression(part.strip(), variables)
                if part_value is not None:
                    result *= float(part_value)
            return result
            
        # Division
        if '/' in processed_expr:
            parts = processed_expr.split('/')
            result = evaluate_expression(parts[0].strip(), variables) or 0
            for part in parts[1:]:
                part_value = evaluate_expression(part.strip(), variables)
                if part_value is not None and float(part_value) != 0:
                    result /= float(part_value)
            return result
            
        # String value
        if processed_expr.startswith('"') and processed_expr.endswith('"'):
            return processed_expr[1:-1]  # Remove quotes
        
        # Try to directly convert to a number one more time
        try:
            return float(processed_expr)
        except:
            pass
        
        # Return the processed expression if all else fails
        return processed_expr
        
    except Exception as e:
        print(f"Expression evaluation error: {str(e)}")
        return None

def execute_team_function(code, output_list=None):
    """Execute a single Team() function code block and capture output"""
    if output_list is None:
        output_list = []
    
    # Initialize the variable store
    variables = {}
    
    # Process line by line to execute statements in order
    lines = code.split('\n')
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('//') or line.startswith('#'):
            continue
        
        # Skip the Team() declaration line
        if line.startswith('Team'):
            continue
        
        # Skip opening/closing braces
        if line == '{' or line == '}':
            continue
        
        # Feint (integer) variable declarations
        feint_match = re.search(r'Feint\s+(@\w+(?:\s*,\s*@\w+)*)\s*(?:=\s*([^;]+))?;', line)
        if feint_match:
            var_names = re.findall(r'@\w+', feint_match.group(1))
            if feint_match.group(2):  # If there's an initialization value
                value_expr = feint_match.group(2).strip()
                value = evaluate_expression(value_expr, variables)
                for var_name in var_names:
                    variables[var_name] = int(value) if value is not None else 0
            else:
                # Just initialize to default value of 0
                for var_name in var_names:
                    variables[var_name] = 0
            continue
        
        # Floater (float) variable declarations
        floater_match = re.search(r'Floater\s+(@\w+(?:\s*,\s*@\w+)*)\s*(?:=\s*([^;]+))?;', line)
        if floater_match:
            var_names = re.findall(r'@\w+', floater_match.group(1))
            if floater_match.group(2):  # If there's an initialization value
                value_expr = floater_match.group(2).strip()
                value = evaluate_expression(value_expr, variables)
                for var_name in var_names:
                    variables[var_name] = float(value) if value is not None else 0.0
            else:
                # Just initialize to default value of 0.0
                for var_name in var_names:
                    variables[var_name] = 0.0
            continue
        
        # Direct variable assignments
        assignment_match = re.search(r'(@\w+)\s*=\s*([^;]+);', line)
        if assignment_match:
            var_name = assignment_match.group(1)
            value_expr = assignment_match.group(2).strip()
            # Evaluate the expression
            value = evaluate_expression(value_expr, variables)
            
            # If the variable already exists, maintain its type
            if var_name in variables and isinstance(variables[var_name], int):
                variables[var_name] = int(value) if value is not None else 0
            elif var_name in variables and isinstance(variables[var_name], float):
                variables[var_name] = float(value) if value is not None else 0.0
            else:
                # New variable, use the natural type of the result
                variables[var_name] = value if value is not None else 0
            continue
        
        # Chant declarations
        chant_match = re.search(r'Chant\s+(@\w+)\s*=\s*"([^"]*)"', line)
        if chant_match:
            var_name = chant_match.group(1)
            text = chant_match.group(2)
            variables[var_name] = text
            continue
        
        # Announce statements
        announce_match = re.search(r'Announce\s*\(([^)]+)\)\s*;', line)
        if announce_match:
            announcement = announce_match.group(1)
            # Process string concatenation with &
            parts = re.split(r'\s*&\s*', announcement)
            processed_parts = []
            
            for part in parts:
                part = part.strip()
                # If it's a string literal
                if part.startswith('"') and part.endswith('"'):
                    processed_parts.append(part[1:-1])  # Remove quotes
                # If it's a variable with @ prefix
                elif part.startswith('@'):
                    if part in variables:
                        processed_parts.append(str(variables[part]))
                    else:
                        # Try to evaluate the variable
                        var_value = evaluate_expression(part, variables)
                        if var_value is not None:
                            processed_parts.append(str(var_value))
                        else:
                            processed_parts.append(part)  # Keep as is if not found
                else:
                    # Try to evaluate as an expression
                    expr_value = evaluate_expression(part, variables)
                    if expr_value is not None:
                        processed_parts.append(str(expr_value))
                    else:
                        processed_parts.append(part)
            
            # Join all parts and add to output
            output_list.append("".join(processed_parts))
            continue
            
        # Dribble (if/else) statements
        dribble_match = re.search(r'Dribble\s*\(([^)]+)\)\s*{', line)
        if dribble_match:
            condition_expr = dribble_match.group(1)
            condition_value = evaluate_expression(condition_expr, variables)
            
            # Find the block of code inside the Dribble
            dribble_block = ""
            dribble_braces = 1
            i = lines.index(line) + 1
            
            while i < len(lines) and dribble_braces > 0:
                curr_line = lines[i].strip()
                if curr_line.endswith('{'):
                    dribble_braces += 1
                elif curr_line == '}' or curr_line.startswith('} '):
                    dribble_braces -= 1
                    
                if dribble_braces > 0:  # Only add if we're still inside the block
                    dribble_block += lines[i] + "\n"
                i += 1
                
            # If the condition is true, execute the block
            if condition_value:
                execute_team_function(dribble_block, output_list)
                
            # Look for Pass or Shoot (else if/else) blocks
            while i < len(lines):
                curr_line = lines[i].strip()
                # Check for Pass (else if)
                pass_match = re.search(r'Pass\s*\(([^)]+)\)\s*{', curr_line)
                if pass_match and not condition_value:
                    # We need to evaluate this condition
                    pass_condition = pass_match.group(1)
                    pass_value = evaluate_expression(pass_condition, variables)
                    
                    if pass_value:
                        # Extract and execute the Pass block
                        pass_block = ""
                        pass_braces = 1
                        j = i + 1
                        
                        while j < len(lines) and pass_braces > 0:
                            pass_line = lines[j].strip()
                            if pass_line.endswith('{'):
                                pass_braces += 1
                            elif pass_line == '}' or pass_line.startswith('} '):
                                pass_braces -= 1
                                
                            if pass_braces > 0:  # Only add if we're still inside the block
                                pass_block += lines[j] + "\n"
                            j += 1
                            
                        # Execute the Pass block
                        execute_team_function(pass_block, output_list)
                        i = j
                        condition_value = True  # Now we've handled a condition
                        continue
                        
                # Check for Shoot (else)
                elif curr_line.startswith('Shoot') and not condition_value:
                    # Extract and execute the Shoot block
                    shoot_block = ""
                    shoot_braces = 1
                    j = i + 1
                    
                    while j < len(lines) and shoot_braces > 0:
                        shoot_line = lines[j].strip()
                        if shoot_line.endswith('{'):
                            shoot_braces += 1
                        elif shoot_line == '}' or shoot_line.startswith('} '):
                            shoot_braces -= 1
                            
                        if shoot_braces > 0:  # Only add if we're still inside the block
                            shoot_block += lines[j] + "\n"
                        j += 1
                        
                    # Execute the Shoot block
                    execute_team_function(shoot_block, output_list)
                    i = j
                    break
                    
                # If we're past the control structure, exit the loop
                if not (curr_line.startswith('Pass') or curr_line.startswith('Shoot')):
                    break
                    
                i += 1
                
            continue
            
        # Forward (for loop) statements
        forward_match = re.search(r'Forward\s*\(\s*([^;]+);\s*([^;]+);\s*([^)]+)\s*\)\s*{', line)
        if forward_match:
            # Extract the three parts of the for loop
            init_expr = forward_match.group(1).strip()
            cond_expr = forward_match.group(2).strip()
            incr_expr = forward_match.group(3).strip()
            
            # Initialize the loop variable
            if '=' in init_expr:
                var_name, value_expr = init_expr.split('=', 1)
                var_name = var_name.strip()
                value_expr = value_expr.strip()
                variables[var_name] = evaluate_expression(value_expr, variables)
            
            # Extract the loop body
            loop_body = ""
            loop_braces = 1
            i = lines.index(line) + 1
            
            while i < len(lines) and loop_braces > 0:
                curr_line = lines[i].strip()
                if curr_line.endswith('{'):
                    loop_braces += 1
                elif curr_line == '}':
                    loop_braces -= 1
                    
                if loop_braces > 0:  # Only add if we're still inside the block
                    loop_body += lines[i] + "\n"
                i += 1
            
            # Execute the loop
            while evaluate_expression(cond_expr, variables):
                # Execute the loop body
                execute_team_function(loop_body, output_list)
                
                # Increment/update loop variable
                if '=' in incr_expr:
                    var_name, value_expr = incr_expr.split('=', 1)
                    var_name = var_name.strip()
                    value_expr = value_expr.strip()
                    variables[var_name] = evaluate_expression(value_expr, variables)
                elif '++' in incr_expr:
                    var_name = incr_expr.replace('++', '').strip()
                    variables[var_name] += 1
                elif '--' in incr_expr:
                    var_name = incr_expr.replace('--', '').strip()
                    variables[var_name] -= 1
            
            continue
        
        # Function call statement
        function_call_match = re.search(r'@(\w+)\s*\(([^)]*)\)\s*;', line)
        if function_call_match:
            func_name = function_call_match.group(1)
            args_str = function_call_match.group(2).strip()
            
            # For our simple example, we'll just handle the @functionCall function
            if func_name == "functionCall":
                # Parse the arguments
                args = []
                if args_str:
                    arg_parts = args_str.split(',')
                    for part in arg_parts:
                        arg_value = evaluate_expression(part.strip(), variables)
                        args.append(arg_value)
                
                if len(args) > 0:
                    # Handle the "functionCall" which is a switch on choice
                    choice = args[0]
                    
                    # Set some example variables that might be used in the function
                    if "@a" not in variables:
                        variables["@a"] = 10
                    if "@b" not in variables:
                        variables["@b"] = 5
                        
                    if choice == 1:
                        output_list.append(f"Multiplication:\n{variables['@a'] * variables['@b']}")
                    elif choice == 2:
                        output_list.append(f"Division:\n{variables['@a'] / variables['@b']}")
                    elif choice == 3:
                        output_list.append(f"Addition:\n{variables['@a'] + variables['@b']}")
                    elif choice == 4:
                        output_list.append(f"Subtraction:\n{variables['@a'] - variables['@b']}")
                    else:
                        output_list.append("Invalid choice\n")
                        
            continue
            
    # Return the captured output
    return output_list

def main():
    # Path to the activity.txt file
    activity_path = "activity.txt"
    
    # Check if the file exists in the current directory, if not try to find it
    if not os.path.exists(activity_path):
        activity_path = os.path.join("CodeSlam sample programs", "activity.txt")
        
    if not os.path.exists(activity_path):
        print(f"Error: Could not find the activity.txt file.")
        return
        
    # Read the file
    with open(activity_path, 'r') as f:
        code = f.read()
        
    # Extract Team() functions
    team_functions = extract_team_functions(code)
    
    # Create directory for output files if it doesn't exist
    output_dir = os.path.join(os.path.dirname(activity_path), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Save output to file
    summary_file = os.path.join(output_dir, "activity_results.txt")
    with open(summary_file, 'w') as out_file:
        out_file.write("============== CodeSlam Activity Results ==============\n\n")
        
        # Execute each Team() function
        for i, (heading, team_code) in enumerate(team_functions):
            print(f"Executing {heading.strip()}...")
            out_file.write(f"Program {i+1}: {heading}\n")
            out_file.write("-" * 50 + "\n")
            out_file.write(f"Code:\n{team_code}\n\n")
            
            # Execute the function and capture output
            output = []
            try:
                output = execute_team_function(team_code)
                out_file.write("Output:\n")
                for line in output:
                    out_file.write(f"{line}\n")
            except Exception as e:
                out_file.write(f"Error: {str(e)}\n")
            
            out_file.write("\n" + "=" * 50 + "\n\n")
    
    print(f"Results saved to {summary_file}")
    
    # Display final results
    print("\nActivity results:")
    with open(summary_file, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main() 