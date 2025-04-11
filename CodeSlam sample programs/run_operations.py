import re

def execute_and_print_result(code, operation_name):
    """Execute a simple CodeSlam operation and show the result"""
    print(f"\n--- {operation_name} ---")
    print("Code:")
    print(code)
    
    # Extract variables
    variables = {}
    
    # Process line by line
    lines = code.split('\n')
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and Team declarations
        if not line or line.startswith('Team') or line == '{' or line == '}' or line.startswith('#'):
            continue
            
        # Extract Feint variables
        feint_match = re.search(r'Feint\s+(@\w+)\s*=\s*(\d+);', line)
        if feint_match:
            var_name = feint_match.group(1)
            var_value = int(feint_match.group(2))
            variables[var_name] = var_value
            continue
            
        # Extract Floater variables
        floater_match = re.search(r'Floater\s+(@\w+)\s*=\s*(\d+\.\d+);', line)
        if floater_match:
            var_name = floater_match.group(1)
            var_value = float(floater_match.group(2))
            variables[var_name] = var_value
            continue
            
        # Handle result calculations
        result_match = re.search(r'@(\w+)\s*=\s*([^;]+);', line)
        if result_match:
            var_name = '@' + result_match.group(1)
            expr = result_match.group(2)
            
            # Replace variables with their values
            for v_name, value in variables.items():
                expr = expr.replace(v_name, str(value))
                
            # Evaluate the expression
            result = eval(expr)
            variables[var_name] = result
            continue
            
        # Handle announce statements
        announce_match = re.search(r'Announce\s*\(([^)]+)\)\s*;', line)
        if announce_match:
            announcement = announce_match.group(1)
            
            # Process string parts and variables in the announcement
            parts = re.split(r'\s*&\s*', announcement)
            result_text = ""
            
            for part in parts:
                part = part.strip()
                if part.startswith('"') and part.endswith('"'):
                    # String literal
                    result_text += part[1:-1]
                elif part.startswith('@'):
                    # Variable reference
                    if part in variables:
                        result_text += str(variables[part])
                    else:
                        result_text += f"[unknown var: {part}]"
            
            print(f"Output: {result_text}")
            continue
    
    print()  # Add empty line

# 1. Addition
addition_code = """Team() {
   Feint @x = 5;         
   Feint @y = 10;        
   @result = @x + @y;  
    
   Announce("The result is: " & @result);
}"""

# 2. Subtraction
subtraction_code = """Team() {
   Feint @y = 20;         
   Feint @z = 6;        
   @result = @y - @z;  
    
   Announce("The result is: " & @result);
}"""

# 3. Multiplication
multiplication_code = """Team() {
   Feint @x = 4;         
   Feint @z = 10;        
   @result = @x * @z;  
    
   Announce("The result is: " & @result);
}"""

# 4. Division
division_code = """Team() {
   Feint @m = 50;         
   Feint @n = 8;        
   @result = @m / @n; 
    
   Announce("The result is: " & @result);
}"""

# 5. Complex addition
complex_addition = """Team() {
    Feint @z = 3;          
    Feint @x = 5;          
    Feint @y = 10;         
    
    @result = (@z + @x) + @y + (@x + @z);  
    
    Announce("The result is: " & @result);    
}"""

# 6. Complex subtraction
complex_subtraction = """Team() {
    Feint @y = 10;         
    Feint @z = 3;          
    Feint @x = 5;         
    
    @result = (@y - @z) - @x - (@z - @x);  
    
    Announce("The result is: " & @result);    
}"""

# 7. Complex multiplication
complex_multiplication = """Team() {
    Feint @x = 2;         
    Feint @z = 3;         
    Feint @y = 4;          
    
    @result = (@x * @z) * @y * (@z * @y);  
    
   Announce("The result is: " & @result);    
}"""

# 8. Complex division
complex_division = """Team() {
    Floater @x = 2.0;       
    Floater @y = 10.0;
    Floater @z = 4.0;
    
    @result = (@y / @z) / @x / (@x / @y);  
    
   Announce("The division result is: " & @result);
}"""

# 9. Mixed operations 1
mixed_operations1 = """Team() {
    Floater @x = 3.0;
    Floater @y = 8.0;
    Floater @z = 2.0;
   
    @result = @y + (@z * @x) / (@y - @z);
    
   Announce("The computed result is: " & @result);
}"""

# 10. Mixed operations 2
mixed_operations2 = """Team() {
    Floater @x = 12.0;
    Floater @y = 5.0;   
    Floater @z = 3.0;
    
    @result = @z + @y * (@x / @z);
    
   Announce("The result is: " & @result);
}"""

# 11. Mixed operations 3
mixed_operations3 = """Team() {
    Feint @x = 4;   
    Feint @y = 7;
    Feint @z = 3;
    
    @result = @x * (@y - @z) + (@z / @x);
    
   Announce("The result is: " & @result); 
}"""

# 12. Mixed operations 4
mixed_operations4 = """Team() {
    Feint @x = 10;
    Feint @y = 3;
    Feint @z = 5;
    
    @result = (@x / @y) * @z - (@y + @x);
    
   Announce("The result is: " & @result);  
}"""

# 17. Area of a square
square_area = """Team() {
    Floater @side = 5.0;
    Floater @area;

    # Calculate area
    @area = @side * @side;

    # Output the result
    Announce("The area of the square with side " & @side & " is: " & @area);
}"""

# 18. Perimeter of a triangle
triangle_perimeter = """Team() {
    Floater @side1 = 3.0;
    Floater @side2 = 4.0;
    Floater @side3 = 5.0;
    Floater @perimeter;

    # Calculate perimeter
    @perimeter = @side1 + @side2 + @side3;

    # Output the result
    Announce("The perimeter of the triangle is: " & @perimeter);
}"""

# 19. Even or odd checker
even_odd = """Team() {
    Feint @number = 10;  

    # Check even or odd
    Dribble (@number % 2 == 0) {
        Announce("The number " & @number & " is even.");
    } Shoot {
        Announce("The number " & @number & " is odd.");
    }
}"""

# 20. Leap year checker
leap_year = """Team() {
    Feint @year = 2024;  

    # Check for leap year
    Dribble ((@year % 4 == 0 AND @year % 100 != 0) OR (@year % 400 == 0)) {
        Announce(@year & " is a leap year.");
    } Shoot {
        Announce(@year & " is not a leap year.");
    }
}"""

# Execute all examples
print("===== CodeSlam Activity Results =====")
print("SAMPLE 1: Basic Operations")
execute_and_print_result(addition_code, "Addition")
execute_and_print_result(subtraction_code, "Subtraction")
execute_and_print_result(multiplication_code, "Multiplication")
execute_and_print_result(division_code, "Division")

print("\nSAMPLE 2: Complex Operations with Same Operation Type")
execute_and_print_result(complex_addition, "Complex Addition")
execute_and_print_result(complex_subtraction, "Complex Subtraction")
execute_and_print_result(complex_multiplication, "Complex Multiplication")
execute_and_print_result(complex_division, "Complex Division")

print("\nSAMPLE 3: Mixed Operations")
execute_and_print_result(mixed_operations1, "Mixed Operations 1")
execute_and_print_result(mixed_operations2, "Mixed Operations 2")
execute_and_print_result(mixed_operations3, "Mixed Operations 3")
execute_and_print_result(mixed_operations4, "Mixed Operations 4")

print("\nOTHER PROGRAMS")
execute_and_print_result(square_area, "Area of a Square")
execute_and_print_result(triangle_perimeter, "Perimeter of a Triangle") 