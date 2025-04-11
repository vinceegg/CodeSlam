#!/usr/bin/env python3

import os
import sys

# Add the parent directory (CODESLAM) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Analyzers.semantic_analyzer.semantic_analyzer import analyze_code_editor

def main():
    """Run the code analyzer and print results to the terminal"""
    print("Running CodeSlam Code Editor Analyzer...")
    analyze_code_editor()

if __name__ == "__main__":
    main() 