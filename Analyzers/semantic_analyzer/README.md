# CodeSlam Semantic Analyzer

This directory contains a semantic analyzer for the CodeSlam programming language.

## Overview

The semantic analyzer examines CodeSlam source code and provides feedback about its structure, variables, functions, and potential issues. The analysis is displayed in the CodeSlam IDE's terminal output in a way that appears native to the language.

## Files

- `semantic_analyzer.py`: The main analyzer for Python files and CodeSlam code
- `analyzer_runner.py`: Utility to process and analyze CodeSlam code
- `editor_integration.py`: Integration code for the CodeSlam IDE
- `apply_integration.py`: Script to automatically apply integration to the IDE
- `demo.py`: Demonstration script showing the analyzer in action
- `run_analyzer.py`: Simple script to run the analyzer on the code editor

## Integration with CodeSlam Editor

The integration is designed to hide the fact that Python libraries are being used for analysis. When users click the "Semantic" button in the CodeSlam IDE, they will see native-looking compiler output in the terminal.

### How to Integrate

1. Run the automatic integration script:
   ```
   python apply_integration.py
   ```

2. The script will:
   - Back up your original code_editor_v2.py file
   - Add the necessary import
   - Replace the sidebar_button_semantic method with the integrated version

3. Launch the CodeSlam editor and test the semantic analyzer with CodeSlam code

### Manual Integration

If the automatic script doesn't work, you can manually integrate:

1. Add this import to code_editor_v2.py:
   ```python
   from Analyzers.semantic_analyzer.editor_integration import SemanticIntegration
   ```

2. Replace the sidebar_button_semantic method with:
   ```python
   def sidebar_button_semantic(self):
       self.clear_terminal_output()
       self.editor_frame.clear_error_highlights()
       
       # Get the code from the editor
       code = self.codebox.get("1.0", "end-1c")
       
       # Use our semantic integration class to analyze the code
       # and display the output in the terminal
       SemanticIntegration.run_analysis(code, self.append_terminal_output)
   ```

## Testing the Integration

You can test the integration before applying it to the editor by running:

```
python editor_integration.py
```

This will show example output as it would appear in the CodeSlam IDE's terminal.

## Features

The semantic analyzer provides:

- Line count and code metrics
- Variable identification and typing
- Function detection with parameter and return type analysis
- Control structure analysis
- Keyword usage statistics
- Simple semantic error detection (e.g., missing return statements)

## Example Output

```
>> Loading CodeSlam Compiler...
>> Initializing lexical analysis...
>> Analyzing code structure...
>> Running semantic checks...

=== CodeSlam Analysis Results ===
📊 Lines of Code: 157
💬 Comments: 31  
🔠 Variables: 26
⚙️ Functions: 4

🔠 Variables:
   - @score (Feint)
   - @percentageAccuracy (Floater)
   - @playerName (Chant)
   - @isAllStar (Stat)
   - @maxPoints (Feint)
   - @teamName (Chant)
   - @points (Feint)
   - @teamMembers (Chant)
   - @seasonStats (Feint)
   - @totalScore (Feint)

⚙️ Functions:
   - @calculateTotalPoints (Feint) with parameters: @points1, @points2
   - @displayPlayerInfo (Dunk) with parameters: @name, @age, @height
   - @isEligible (Stat) with parameters: Feint @age, Feint @experience
   - @formatName (Chant) with parameters: Chant @firstName, Chant @lastName

🔄 Control Structures:
   - Dribble: 6 occurrences
   - Pass: 1 occurrences
   - Shoot: 3 occurrences
   - Forward: 4 occurrences
   - Play: 2 occurrences
   - Run: 1 occurrences
   - Switch: 1 occurrences

🔑 Keyword Usage:
   - Announce: 26 occurrences
   - Feint: 14 occurrences
   - Chant: 8 occurrences
   - Dribble: 6 occurrences
   - Forward: 4 occurrences
   - Rebound: 4 occurrences
   - Wilt: 4 occurrences
   - Shoot: 3 occurrences
   - Floater: 3 occurrences
   - Stat: 3 occurrences

✅ No semantic errors detected

>> Compilation complete. 