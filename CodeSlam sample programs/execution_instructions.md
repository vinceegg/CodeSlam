# Instructions for Executing CodeSlam Activity Examples

## Overview

This document provides step-by-step instructions for executing the CodeSlam language examples from the activity.txt file. To make it easier to execute and see the results, we've split the examples into several smaller files.

## Files

1. **mdas_example.txt** - Contains the basic and complex MDAS (Multiplication, Division, Addition, Subtraction) operations
2. **other_examples.txt** - Contains area, perimeter, odd/even, and leap year examples
3. **shapes_examples.txt** - Contains the shape drawing examples
4. **function_call_example.txt** - Contains the function call examples

## Execution Instructions

### Method 1: Using the CodeSlam Editor (Recommended)

1. Launch the CodeSlam editor:
   ```
   python CodeEditor/code_editor_v2.py
   ```

2. Open one of the example files listed above using the editor

3. Run the analysis in order:
   - Click the "Lexical" button in the sidebar
   - If no lexical errors, click the "Syntax" button
   - If no syntax errors, click the "Semantic" button

4. After clicking the "Semantic" button, the code will be executed automatically if there are no errors, and the results will appear in the terminal output area at the bottom of the editor.

5. Repeat steps 2-4 for each example file to see all the results.

### Method 2: Looking at Expected Results

For a quick reference of what results to expect from each example, see the `activity_results.txt` file which contains the expected output for all examples.

## Notes on Specific Examples

### MDAS Operations
The basic and complex MDAS operations demonstrate arithmetic operations in CodeSlam. The results show how expressions are evaluated following normal operator precedence rules.

### Function Call
The function call example shows how to define and call functions in CodeSlam, with conditional branching based on the parameter value.

### Shape Drawing
These examples demonstrate how to use loops to create different shapes. When executed, they will print characters to form visual patterns.

### Other Examples
These examples show how to perform calculations and use conditional statements in CodeSlam.

## Verification

To verify your execution results, compare the terminal output with the expected results in `activity_results.txt`.

## Troubleshooting

If you encounter errors:
- Make sure you're clicking the buttons in the correct order (Lexical → Syntax → Semantic)
- Check for syntax errors in your code against the original examples
- Restart the CodeSlam editor if you encounter unexpected behavior 