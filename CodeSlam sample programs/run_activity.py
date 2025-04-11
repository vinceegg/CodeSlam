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
        # Handle direct variable references
        if isinstance(expr, str) and expr.strip().startswith('@') and expr.strip() in variables:
            return variables[expr.strip()]

        # Replace variables with their values
        processed_expr = expr.strip()
        
        # Sort variables by length in reverse order to avoid partial replacements
        var_names = sorted(variables.keys(), key=len, reverse=True)
        
        # Replace all variable references with their values
        for var_name in var_names:
            if var_name in processed_expr:
                processed_expr = processed_expr.replace(var_name, str(variables[var_name]))
        
        # Handle parentheses recursively
        while '(' in processed_expr:
            # Find innermost parentheses
            start = processed_expr.rindex('(')
            end = processed_expr.find(')', start)
            if end == -1:
                raise ValueError("Mismatched parentheses")
            
            # Evaluate the expression inside parentheses
            inner_result = evaluate_expression(processed_expr[start + 1:end], variables)
            
            # Replace the parenthetical expression with its result
            processed_expr = processed_expr[:start] + str(inner_result) + processed_expr[end + 1:]
        
        # Handle numeric literals
        if processed_expr.isdigit():
            return int(processed_expr)
        
        if processed_expr.replace('.', '', 1).isdigit() and processed_expr.count('.') == 1:
            return float(processed_expr)
            
        # Split the expression into tokens, preserving operators
        tokens = []
        current_num = ''
        i = 0
        while i < len(processed_expr):
            char = processed_expr[i]
            if char.isdigit() or char == '.':
                current_num += char
            elif char in '+-*/%':
                if current_num:
                    tokens.append(float(current_num))
                    current_num = ''
                tokens.append(char)
            elif not char.isspace():
                if current_num:
                    tokens.append(float(current_num))
                    current_num = ''
            i += 1
        
        if current_num:
            tokens.append(float(current_num))

        # Handle empty expression
        if not tokens:
            return None

        # Single number
        if len(tokens) == 1:
            return int(tokens[0]) if tokens[0].is_integer() else tokens[0]

        # Handle multiplication, division, and modulo first
        i = 0
        while i < len(tokens):
            if isinstance(tokens[i], str) and tokens[i] in '*/%':
                left = float(tokens[i-1])
                right = float(tokens[i+1])
                if tokens[i] == '*':
                    result = left * right
                elif tokens[i] == '/':
                    if right == 0:
                        raise ValueError("Division by zero")
                    result = left / right
                elif tokens[i] == '%':
                    if right == 0:
                        raise ValueError("Modulo by zero")
                    # Ensure operands are integers for modulo
                    left_int = int(left)
                    right_int = int(right)
                    result = left_int % right_int
                tokens[i-1:i+2] = [result]
                i -= 1
            i += 1

        # Handle addition and subtraction
        result = float(tokens[0])
        i = 1
        while i < len(tokens):
            if tokens[i] == '+':
                result += float(tokens[i+1])
            elif tokens[i] == '-':
                result -= float(tokens[i+1])
            i += 2

        # Convert to int if the result is a whole number
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result
            
    except Exception as e:
        print(f"Expression evaluation error: {str(e)}")
        return None

def evaluate_condition(condition, variables):
    """Evaluate a conditional expression"""
    try:
        # Handle logical operators
        if ' OR ' in condition:
            parts = condition.split(' OR ')
            return any(evaluate_condition(part.strip(), variables) for part in parts)
        elif ' AND ' in condition:
            parts = condition.split(' AND ')
            return all(evaluate_condition(part.strip(), variables) for part in parts)
            
        # Handle comparison operators
        if '<=' in condition:
            left, right = condition.split('<=')
            left_val = evaluate_expression(left.strip(), variables)
            right_val = evaluate_expression(right.strip(), variables)
            return left_val <= right_val if left_val is not None and right_val is not None else False
        elif '>=' in condition:
            left, right = condition.split('>=')
            left_val = evaluate_expression(left.strip(), variables)
            right_val = evaluate_expression(right.strip(), variables)
            return left_val >= right_val if left_val is not None and right_val is not None else False
        elif '<' in condition:
            left, right = condition.split('<')
            left_val = evaluate_expression(left.strip(), variables)
            right_val = evaluate_expression(right.strip(), variables)
            return left_val < right_val if left_val is not None and right_val is not None else False
        elif '>' in condition:
            left, right = condition.split('>')
            left_val = evaluate_expression(left.strip(), variables)
            right_val = evaluate_expression(right.strip(), variables)
            return left_val > right_val if left_val is not None and right_val is not None else False
        elif '==' in condition:
            left, right = condition.split('==')
            left_val = evaluate_expression(left.strip(), variables)
            right_val = evaluate_expression(right.strip(), variables)
            return left_val == right_val if left_val is not None and right_val is not None else False
        elif '!=' in condition:
            left, right = condition.split('!=')
            left_val = evaluate_expression(left.strip(), variables)
            right_val = evaluate_expression(right.strip(), variables)
            return left_val != right_val if left_val is not None and right_val is not None else False
        
        # If no comparison operator, evaluate as boolean
        value = evaluate_expression(condition, variables)
        return bool(value) if value is not None else False
            
    except Exception as e:
        print(f"Condition evaluation error: {str(e)}")
        return False

def execute_block(block_lines, variables, output_list):
    """Execute a block of code with its own variable scope"""
    # Create a new scope
    local_vars = variables.copy()
    
    # Execute each line in the block
    for line in block_lines:
        line = line.strip()
        if not line or line.startswith('//') or line.startswith('#'):
            continue
            
        # Handle Announce statements
        announce_match = re.search(r'Announce\s*\(([^)]+)\)\s*;', line)
        if announce_match:
            announcement = announce_match.group(1)
            parts = re.split(r'\s*&\s*', announcement)
            processed_parts = []
            
            for part in parts:
                part = part.strip()
                if part.startswith('"') and part.endswith('"'):
                    processed_parts.append(part[1:-1])
                elif part.startswith('@'):
                    if part in local_vars:
                        processed_parts.append(str(local_vars[part]))
                    else:
                        var_value = evaluate_expression(part, local_vars)
                        processed_parts.append(str(var_value) if var_value is not None else part)
                else:
                    expr_value = evaluate_expression(part, local_vars)
                    processed_parts.append(str(expr_value) if expr_value is not None else part)
            
            output_list.append("".join(processed_parts))
            
    return local_vars

def execute_team_function(code, output_list=None, parent_vars=None):
    """Execute a single Team() function code block and capture output"""
    if output_list is None:
        output_list = []
    
    # Initialize the variable store with parent variables if provided
    variables = parent_vars.copy() if parent_vars is not None else {}
    
    # Split code into lines and process each line
    lines = code.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        
        # Skip empty lines, comments, and structural lines
        if not line or line.startswith('//') or line.startswith('#') or line.startswith('Team') or line in ['{', '}']:
            continue
        
        # Feint (integer) variable declarations
        feint_match = re.search(r'Feint\s+(@\w+)\s*=\s*([^;]+);', line)
        if feint_match:
            var_name = feint_match.group(1)
            value_expr = feint_match.group(2).strip()
            value = evaluate_expression(value_expr, variables)
            variables[var_name] = int(value) if value is not None else 0
            continue
        
        # Handle conditional blocks (Dribble/Pass/Shoot)
        dribble_match = re.search(r'Dribble\s*\(([^)]+)\)\s*{', line)
        if dribble_match:
            # Extract the condition and evaluate it
            condition = dribble_match.group(1).strip()
            condition_result = evaluate_condition(condition, variables)
            
            # Find the end of the Dribble block
            dribble_block = []
            brace_count = 1
            dribble_end = i
            
            while dribble_end < len(lines) and brace_count > 0:
                curr_line = lines[dribble_end].strip()
                if curr_line.endswith('{'):
                    brace_count += 1
                elif curr_line == '}' or curr_line.startswith('} '):
                    brace_count -= 1
                if brace_count > 0:
                    dribble_block.append(lines[dribble_end])
                dribble_end += 1
            
            # Find any Pass/Shoot blocks
            pass_blocks = []  # List of (condition, block) tuples
            shoot_block = None
            curr_pos = dribble_end
            
            while curr_pos < len(lines):
                curr_line = lines[curr_pos].strip()
                
                # Check for Pass (else if)
                pass_match = re.search(r'Pass\s*\(([^)]+)\)\s*{', curr_line)
                if pass_match:
                    pass_condition = pass_match.group(1).strip()
                    pass_lines = []
                    curr_pos += 1
                    brace_count = 1
                    
                    while curr_pos < len(lines) and brace_count > 0:
                        curr_line = lines[curr_pos].strip()
                        if curr_line.endswith('{'):
                            brace_count += 1
                        elif curr_line == '}' or curr_line.startswith('} '):
                            brace_count -= 1
                        if brace_count > 0:
                            pass_lines.append(lines[curr_pos])
                        curr_pos += 1
                    
                    pass_blocks.append((pass_condition, pass_lines))
                    continue
                
                # Check for Shoot (else)
                shoot_match = re.search(r'Shoot\s*{', curr_line)
                if shoot_match:
                    shoot_lines = []
                    curr_pos += 1
                    brace_count = 1
                    
                    while curr_pos < len(lines) and brace_count > 0:
                        curr_line = lines[curr_pos].strip()
                        if curr_line.endswith('{'):
                            brace_count += 1
                        elif curr_line == '}' or curr_line.startswith('} '):
                            brace_count -= 1
                        if brace_count > 0:
                            shoot_lines.append(lines[curr_pos])
                        curr_pos += 1
                    
                    shoot_block = shoot_lines
                    break
                
                curr_pos += 1
            
            # Execute the appropriate block based on conditions
            block_executed = False
            
            # Try Dribble block
            if condition_result:
                block_executed = True
                block_vars = variables.copy()
                execute_team_function('\n'.join(dribble_block), output_list, block_vars)
                variables.update(block_vars)
            
            # Try Pass blocks
            if not block_executed:
                for pass_condition, pass_lines in pass_blocks:
                    if evaluate_condition(pass_condition, variables):
                        block_executed = True
                        block_vars = variables.copy()
                        execute_team_function('\n'.join(pass_lines), output_list, block_vars)
                        variables.update(block_vars)
                        break
            
            # Try Shoot block
            if not block_executed and shoot_block:
                block_vars = variables.copy()
                execute_team_function('\n'.join(shoot_block), output_list, block_vars)
                variables.update(block_vars)
            
            # Skip to the end of the entire conditional structure
            i = curr_pos if curr_pos > dribble_end else dribble_end
            continue
        
        # Handle Announce statements
        announce_match = re.search(r'Announce\s*\(([^)]+)\)\s*;', line)
        if announce_match:
            announcement = announce_match.group(1)
            parts = re.split(r'\s*&\s*', announcement)
            processed_parts = []
            
            for part in parts:
                part = part.strip()
                if part.startswith('"') and part.endswith('"'):
                    processed_parts.append(part[1:-1])
                elif part.startswith('@'):
                    if part in variables:
                        processed_parts.append(str(variables[part]))
                    else:
                        var_value = evaluate_expression(part, variables)
                        processed_parts.append(str(var_value) if var_value is not None else part)
                else:
                    expr_value = evaluate_expression(part, variables)
                    processed_parts.append(str(expr_value) if expr_value is not None else part)
            
            output_list.append("".join(processed_parts))
            continue
        
        # Handle variable assignments
        assignment_match = re.search(r'(@\w+)\s*=\s*([^;]+);', line)
        if assignment_match:
            var_name = assignment_match.group(1)
            value_expr = assignment_match.group(2).strip()
            value = evaluate_expression(value_expr, variables)
            variables[var_name] = value
            continue
    
    return variables

def execute_line(line, variables, output_list):
    """Execute a single line of code"""
    # Handle Announce statements
    announce_match = re.search(r'Announce\s*\(([^)]+)\)\s*;', line)
    if announce_match:
        announcement = announce_match.group(1)
        parts = re.split(r'\s*&\s*', announcement)
        processed_parts = []
        
        for part in parts:
            part = part.strip()
            if part.startswith('"') and part.endswith('"'):
                processed_parts.append(part[1:-1])
            elif part.startswith('@'):
                if part in variables:
                    processed_parts.append(str(variables[part]))
                else:
                    var_value = evaluate_expression(part, variables)
                    processed_parts.append(str(var_value) if var_value is not None else part)
            else:
                expr_value = evaluate_expression(part, variables)
                processed_parts.append(str(expr_value) if expr_value is not None else part)
        
        output_list.append("".join(processed_parts))
        return
    
    # Handle variable assignments
    assignment_match = re.search(r'(@\w+)\s*=\s*([^;]+);', line)
    if assignment_match:
        var_name = assignment_match.group(1)
        value_expr = assignment_match.group(2).strip()
        value = evaluate_expression(value_expr, variables)
        variables[var_name] = value
        return

def main():
    """Main function to run the interpreter"""
    # Get input file from command line argument or use default
    input_file = sys.argv[1] if len(sys.argv) > 1 else "activity.txt"
    
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            code = file.read()
            
        # Execute the code
        output = []
        execute_team_function(code, output)
        
        # Print the output
        for line in output:
            print(line)
            
    except FileNotFoundError:
        print(f"Error: Could not find file {input_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 