import os
import sys
import re
import ast
import tokenize
import io
from collections import Counter, defaultdict

# Helper function to check if a node is inside a class definition
def is_in_class(tree, node):
    """Check if a node is inside a class definition"""
    for potential_parent in ast.walk(tree):
        if isinstance(potential_parent, ast.ClassDef):
            for child in ast.walk(potential_parent):
                if child == node and child is not potential_parent:
                    return True
    return False

class CodeAnalyzer:
    def __init__(self):
        self.lines_of_code = 0
        self.imports = []
        self.classes = []
        self.functions = []
        self.variables = []
        self.comments = []
        self.codeslam_keywords = set([
            "Team", "Wilt", "Feint", "Floater", "Chant", "Stat", "Forward", 
            "Play", "Run", "Switch", "Get", "Default", "Dribble", "Pass", 
            "Shoot", "Rebound", "Announce", "Inbound", "Zone", "Const"
        ])

    def analyze_python_file(self, file_path):
        """Analyze a Python file and extract key metrics and information"""
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        self.lines_of_code = len(content.splitlines())
        
        # Find all imports
        import_pattern = re.compile(r'^import\s+(\w+).*$|^from\s+(\w+).*$', re.MULTILINE)
        for match in import_pattern.finditer(content):
            if match.group(1):
                self.imports.append(match.group(1))
            elif match.group(2):
                self.imports.append(match.group(2))
        
        # Extract comments
        try:
            for toktype, tokval, _, _, _ in tokenize.tokenize(io.BytesIO(content.encode('utf-8')).readline):
                if toktype == tokenize.COMMENT:
                    self.comments.append(tokval)
        except tokenize.TokenError:
            pass  # Handle any tokenize errors gracefully
        
        # Parse AST for deeper analysis
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    self.classes.append(node.name)
                    
                    # Extract class methods
                    methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                    self.functions.extend([f"{node.name}.{method}" for method in methods])
                
                elif isinstance(node, ast.FunctionDef) and not is_in_class(tree, node):
                    self.functions.append(node.name)
                
                elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                self.variables.append(target.id)
                    else:  # AnnAssign
                        if isinstance(node.target, ast.Name):
                            self.variables.append(node.target.id)
        except SyntaxError:
            print("Could not parse the file as valid Python AST")

    def analyze_codeslam_file(self, file_path):
        """Analyze a CodeSlam language file"""
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        self.lines_of_code = len(content.splitlines())
        
        # Extract comments (CodeSlam uses # for comments)
        comment_pattern = re.compile(r'#.*$', re.MULTILINE)
        self.comments = comment_pattern.findall(content)
        
        # Find variable declarations
        var_pattern = re.compile(r'(Feint|Floater|Chant|Stat)\s+(@\w+)')
        self.variables = [match.group(2) for match in var_pattern.finditer(content)]
        
        # Find function declarations
        func_pattern = re.compile(r'Wilt\s+\w+\s+(@\w+)\(')
        self.functions = [match.group(1) for match in func_pattern.finditer(content)]
        
        # Count keywords
        self.keyword_count = {}
        for keyword in self.codeslam_keywords:
            pattern = re.compile(r'\b' + keyword + r'\b')
            count = len(pattern.findall(content))
            if count > 0:
                self.keyword_count[keyword] = count

    def get_summary(self):
        """Return a summary of the analysis"""
        summary = {
            "lines_of_code": self.lines_of_code,
            "num_imports": len(self.imports),
            "num_classes": len(self.classes),
            "num_functions": len(self.functions),
            "num_variables": len(self.variables),
            "num_comments": len(self.comments),
            "imports": self.imports,
            "classes": self.classes,
            "functions": self.functions[:10],  # Limit to first 10 functions
            "variables": self.variables[:10],  # Limit to first 10 variables
            "keyword_count": getattr(self, "keyword_count", {})
        }
        return summary

def analyze_code_editor():
    """Analyze the code_editor_v2.py file and print the results"""
    analyzer = CodeAnalyzer()
    
    # Get the absolute path to the code_editor_v2.py file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    code_editor_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'CodeEditor', 'code_editor_v2.py'))
    
    if os.path.exists(code_editor_path):
        analyzer.analyze_python_file(code_editor_path)
        summary = analyzer.get_summary()
        
        print("=" * 50)
        print(f"CodeSlam Code Editor Analysis")
        print("=" * 50)
        print(f"📊 Lines of Code: {summary['lines_of_code']}")
        print(f"📦 Number of Imports: {summary['num_imports']}")
        print(f"🏗️ Classes: {len(summary['classes'])}")
        print(f"⚙️ Functions: {summary['num_functions']}")
        print(f"🔠 Variables: {summary['num_variables']}")
        print(f"💬 Comments: {summary['num_comments']}")
        
        print("\n📚 Top Imports:")
        for imp in summary['imports'][:15]:
            print(f"   - {imp}")
            
        print("\n🏗️ Classes:")
        for cls in summary['classes']:
            print(f"   - {cls}")
            
        print("\n⚙️ Sample Functions:")
        for func in summary['functions']:
            print(f"   - {func}")
            
        print("\n🔠 Sample Variables:")
        for var in summary['variables']:
            print(f"   - {var}")
            
        # Find class relationships
        print("\n📊 Class Inheritance Structure:")
        for cls in summary['classes']:
            if cls.startswith("CTk") or cls.startswith("Tk"):
                print(f"   - {cls}: derived from tkinter")
            elif cls == "App":
                print(f"   - {cls}: main application class (derived from customtkinter.CTk)")
            elif cls == "LineNumbers":
                print(f"   - {cls}: derived from tk.Text")
            elif cls == "SyntaxHighlighter":
                print(f"   - {cls}: standalone class")
            elif cls == "ModernCodeEditor": 
                print(f"   - {cls}: derived from tk.Frame")
            else:
                print(f"   - {cls}")
                
        # Analyze the CodeSlam sample code
        print("\n=" * 50)
        print("CodeSlam Sample Program Analysis")
        print("=" * 50)
        
        sample_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'CodeSlam sample programs', 'codeslam_sample.txt'))
        if os.path.exists(sample_path):
            analyzer = CodeAnalyzer()  # Create a fresh analyzer
            analyzer.analyze_codeslam_file(sample_path)
            slam_summary = analyzer.get_summary()
            
            print(f"📊 Lines of Code: {slam_summary['lines_of_code']}")
            print(f"⚙️ Functions: {slam_summary['num_functions']}")
            print(f"🔠 Variables: {slam_summary['num_variables']}")
            print(f"💬 Comments: {slam_summary['num_comments']}")
            
            print("\n⚙️ Functions:")
            for func in slam_summary['functions']:
                print(f"   - {func}")
                
            print("\n🔠 Sample Variables:")
            for var in slam_summary['variables'][:10]:
                print(f"   - {var}")
                
            print("\n🔑 Keyword Usage:")
            for keyword, count in slam_summary.get('keyword_count', {}).items():
                print(f"   - {keyword}: {count} occurrences")
    else:
        print(f"Error: Could not find code_editor_v2.py at {code_editor_path}")

if __name__ == "__main__":
    analyze_code_editor() 