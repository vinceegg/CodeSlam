# Using the CodeSlam Semantic Analyzer

This guide shows how to use the semantic analyzer with the CodeSlam IDE.

## Quick Start

1. The integration has already been applied to `code_editor_v2.py`.

2. Run the CodeSlam IDE:
   ```
   python CodeEditor/code_editor_v2.py
   ```

3. Load or write CodeSlam code in the editor.

4. Click the "Semantic" button in the sidebar to run the semantic analysis.

5. View the results in the terminal output panel at the bottom of the IDE.

## How It Works

When you click the "Semantic" button, the IDE will:

1. Get the code from the editor
2. Pass it to our semantic analyzer
3. Display the analysis results in the terminal output

The analysis will appear to be performed by a native CodeSlam compiler, but it's actually using our Python-based semantic analyzer behind the scenes.

## Understanding the Output

The output includes:

- **Code Metrics**: Line count, variables, functions, and comments
- **Variable Analysis**: List of variables with their types
- **Function Analysis**: List of functions with return types and parameters
- **Control Structure Analysis**: Usage of control structures like loops and conditionals
- **Keyword Usage**: Statistics about language keyword usage
- **Semantic Errors**: Any detected semantic issues in the code

## Example Usage

1. Open the CodeSlam IDE
2. Load the sample code from `CodeSlam sample programs/codeslam_sample.txt`
3. Click "Semantic" in the sidebar
4. Observe the analysis results in the terminal
5. Try modifying the code and run the analysis again to see updated results

## Troubleshooting

If the semantic analyzer doesn't work:

1. Ensure you have all required Python libraries installed
2. Check if the integration was applied correctly
3. Try running the standalone demo:
   ```
   python Analyzers/semantic_analyzer/editor_integration.py
   ```

## Creating Test Cases

You can create your own test cases by:

1. Creating a new CodeSlam file with specific code structures
2. Running the semantic analysis on it
3. Checking if the analyzer correctly identifies the structures

For example, try creating functions without return statements to test error detection.

## Additional Information

For more technical details about the implementation, see the README.md file in the semantic_analyzer directory.

If you need to reapply the integration, run:
```
python Analyzers/semantic_analyzer/apply_integration.py 