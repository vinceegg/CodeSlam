import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import sys
import os
# Add the parent directory (CODESLAM) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Analyzers.lexical_analyzer.lexical import *  # Import all function from lexical.py
from Analyzers.syntax_analyzer import parse  # Import the parser
from tkinter import END

from customtkinter import CTkImage
from PIL import Image
from Analyzers.syntax_analyzer.errors import SyntaxError

import tkinter as tk
from tkinter import ttk, font
from tkinter.scrolledtext import ScrolledText
import re

# Load the image
image_path = "assets/icons/CodeSLAM-LOGO.png"
image = Image.open(image_path)

# Create CTkImage with a specified size
logo_image = CTkImage(image, size=(100, 100))  # Set desired width and height here

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")

class LineNumbers(tk.Text):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
        self.text_widget = text_widget
        self.text_widget.bind('<KeyPress>', self._on_key_press)
        self.text_widget.bind('<KeyRelease>', self._on_key_release)
        
        # Configure the line numbers appearance
        self.configure(width=4)
        self.configure(background='#2b2b2b')  # Dark background
        self.configure(foreground='#606366')  # Grayish line numbers
        self.configure(borderwidth=0)
        self.configure(highlightthickness=0)
        
    def _on_key_press(self, event=None):
        self.redraw()
        
    def _on_key_release(self, event=None):
        self.redraw()
        
    def redraw(self):
        self.delete('1.0', tk.END)
        line_count = self.text_widget.get('1.0', tk.END).count('\n')
        for line in range(1, line_count + 1):
            self.insert(tk.END, f"{line:3d}\n")
        self.configure(state='disabled')  # Make line numbers read-only

class SyntaxHighlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        
        # Define syntax highlighting patterns
        self.patterns = [
            # Keywords
            (r'\b(Team|Wilt|Feint|Floater|Chant|Stat|Forward|Play|Run|Switch|Get|Default|Dribble|Pass|Shoot|Rebound|Announce|Inbound)\b', '#4ADADF'),  # Light Blue
            # Numbers
            (r'\b\d+(\.\d+)?\b', '#E71D56'),  
            # Strings
            (r'"[^"]*"', '#9CD1BB'), 
            # Comments
            (r'//.*$', '#808080'),  
            # Variables with @ prefix
            (r'@\w+', '#EAF2F1'),  
            # Operators
            (r'[+\-*/=<>!&|]', '#FFB27D'),  
            # Parentheses and brackets
            (r'[\(\)\[\]\{\}]', '#a9b7c6'), 
        ]
        
        # Create tags for each pattern
        for pattern, color in self.patterns:
            self.text_widget.tag_configure(pattern, foreground=color)
            
    def highlight(self, event=None):
        # Remove existing tags
        for pattern, _ in self.patterns:
            self.text_widget.tag_remove(pattern, '1.0', tk.END)
            
        # Apply highlighting
        content = self.text_widget.get('1.0', tk.END)
        for pattern, color in self.patterns:
            for match in re.finditer(pattern, content, re.MULTILINE):
                start = f"1.0+{match.start()}c"
                end = f"1.0+{match.end()}c"
                self.text_widget.tag_add(pattern, start, end)

class ModernCodeEditor(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background='#2b2b2b')  # Dark theme background
        self.create_widgets()
        
    def create_widgets(self):
        # Create main editor frame
        editor_frame = tk.Frame(self, background='#2b2b2b')
        editor_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create text widget with custom font and colors
        editor_font = font.Font(family='Consolas', size=11)
        self.text = ScrolledText(
            editor_frame,
            wrap=tk.NONE,
            font=editor_font,
            background='#2b2b2b',  # Dark background
            foreground='#a9b7c6',  # Light text
            insertbackground='white',  # White cursor
            selectbackground='#214283',  # Selection color
            selectforeground='#a9b7c6',
            spacing1=2,  # Add some line spacing
            spacing2=2,
            spacing3=2
        )
        
        # Create line numbers
        self.line_numbers = LineNumbers(
            editor_frame, 
            self.text,
            font=editor_font,
            padx=5,
            pady=4
        )
        
        # Pack widgets
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Initialize syntax highlighter
        self.highlighter = SyntaxHighlighter(self.text)
        self.text.bind('<KeyRelease>', self.on_key_release)
        
        # Add auto-indentation
        self.text.bind('<Return>', self.auto_indent)
        self.text.bind('<Tab>', self.handle_tab)
        
        # Add bracket matching
        self.text.bind('<KeyRelease-bracketleft>', self.insert_matching_bracket)
        self.text.bind('<KeyRelease-parenleft>', self.insert_matching_bracket)
        self.text.bind('<KeyRelease-braceleft>', self.insert_matching_bracket)
        
    def on_key_release(self, event):
        self.highlighter.highlight()
        self.line_numbers.redraw()
        
    def auto_indent(self, event):
        # Get current line's indentation
        current_line = self.text.get("insert linestart", "insert")
        match = re.match(r'^(\s+)', current_line)
        if match:
            self.text.insert("insert", f"\n{match.group(1)}")
            return "break"
        return None
        
    def handle_tab(self, event):
        # Insert spaces instead of tab
        self.text.insert("insert", "    ")
        return "break"
        
    def insert_matching_bracket(self, event):
        # Define matching brackets
        brackets = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        
        # Get the typed bracket
        char = event.char
        if char in brackets:
            # Insert matching bracket and move cursor back
            self.text.insert("insert", brackets[char])
            self.text.mark_set("insert", "insert-1c")
            
    def get_text(self):
        return self.text.get('1.0', tk.END)
        
    def set_text(self, text):
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', text)
        self.highlighter.highlight()
        self.line_numbers.redraw()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CodeSlam Compiler")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # Replace the "CodeSlam" text with the image
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, image=logo_image, text="")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        
        # create sidebar buttons
        self.sideBtnLexical = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_lexical)
        self.sideBtnLexical.grid(row=1, column=0, padx=20, pady=10)
        self.sideBtnSyntax = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_syntax, state="disabled")
        self.sideBtnSyntax.grid(row=2, column=0, padx=20, pady=10)
        self.sideBtnSemantic = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_semantic, state="disabled")
        self.sideBtnSemantic.grid(row=3, column=0, padx=20, pady=10)
        
        # create sidebar widgets
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Replace the old editor frame setup with ModernCodeEditor
        self.editor_frame = ModernCodeEditor(self)
        self.editor_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        # Use the ModernCodeEditor's text widget for code access
        self.codebox = self.editor_frame.text
        
        # Create styled table frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Lexical Analyzer", width=400)
        self.scrollable_frame.grid(row=0, column=2, rowspan=2, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)  # Make both columns expand equally

        # Style the table headers
        self.style = ttk.Style()
        self.style.configure("Header.TLabel", font=('Helvetica', 12, 'bold'))
        
        # Terminal (text widget) to display output
        self.terminal_output = customtkinter.CTkTextbox(self, width=250, height=150)
        self.terminal_output.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.terminal_output.insert("0.0", "Terminal Output:\n\n")
        self.terminal_output.configure(state="disabled")  # Make terminal output read-only

        # Command input field (entry widget)
        self.command_input = customtkinter.CTkEntry(self)
        self.command_input.grid(row=2, column=1, padx=(20, 0), pady=(10, 20), sticky="ew")
        self.command_input.bind("<Return>", self.execute_command)  # Bind Enter key to run the command

        # set default values
        self.sideBtnLexical.configure(text="Lexical")
        self.sideBtnSyntax.configure(text="Syntax")
        self.sideBtnSemantic.configure(text="Semantic")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def insert_tab(self, event):
        self.codebox.insert("insert", "\t")  # Insert a tab character
        return "break"  # Prevent the default behavior of the Tab key

    def clear_placeholder(self, event):
        if self.codebox.get("1.0", "end-1c") == self.codebox_placeholder:
            self.codebox.delete("1.0", "end")

    def add_placeholder(self, event):
        if not self.codebox.get("1.0", "end-1c"):
            self.codebox.insert("1.0", self.codebox_placeholder)

    def sync_scroll(self, *args):
        """Synchronize scrolling between widgets"""
        # Update scrollbar
        self.scrollbar.set(*args)
        # Sync the line numbers with code editor
        self.line_numbers.yview_moveto(args[0])
        
    def scroll_both(self, *args):
        """Scroll both text widgets when scrollbar is moved"""
        self.codebox.yview(*args)
        self.line_numbers.yview(*args)
        
    def on_modified(self, event=None):
        """Handle text modifications"""
        self.codebox.edit_modified(False)  # Reset modified flag
        self.update_line_numbers()
        
    def update_line_numbers(self, event=None):
        """Update line numbers and keep scroll position"""
        current_scroll = self.codebox.yview()[0]  # Save current scroll position
        line_count = int(self.codebox.index('end-1c').split('.')[0])
        line_numbers_string = "\n".join(str(i) for i in range(1, line_count + 1))
        self.line_numbers.configure(state="normal")
        self.line_numbers.delete("1.0", "end")
        self.line_numbers.insert("1.0", line_numbers_string)
        self.line_numbers.configure(state="disabled")
        # Restore scroll position
        self.line_numbers.yview_moveto(current_scroll)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def on_code_change(self, event=None):
        
        """Handle code changes and reset button states"""
        self.update_line_numbers()  # Keep existing line number update
        
        # Reset buttons to initial state
        self.sideBtnSyntax.configure(state="disabled")
        self.sideBtnSemantic.configure(state="disabled")
        
        # Clear the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        # Reset terminal if it's not empty
        if self.terminal_output.get("1.0", END).strip() != "Terminal Output:":
            self.clear_terminal_output()

    def sidebar_button_lexical(self):
        self.clear_terminal_output()
        codebox_content = self.codebox.get("1.0", "end-1c")

        # Clear existing content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Create styled table headers
        header_frame = customtkinter.CTkFrame(self.scrollable_frame)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=1)

        header_lexeme = customtkinter.CTkLabel(
            header_frame, 
            text="Lexeme",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            fg_color="#3B3B3B",  # Darker blue background
            corner_radius=6
        )
        header_lexeme.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        header_token = customtkinter.CTkLabel(
            header_frame, 
            text="Token",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            fg_color="#3B3B3B",  # Darker blue background
            corner_radius=6
        )
        header_token.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Use the Lexer
        tokens, errors = run(codebox_content)

        # Create table content with alternating row colors
        for i, token in enumerate(tokens):
            row_frame = customtkinter.CTkFrame(
                self.scrollable_frame,
                fg_color="#2b2b2b" if i % 2 == 0 else "#323232"
            )
            row_frame.grid(row=i+1, column=0, columnspan=2, sticky="ew", padx=5, pady=2)
            row_frame.grid_columnconfigure(0, weight=1)
            row_frame.grid_columnconfigure(1, weight=1)

            lexeme_label = customtkinter.CTkLabel(
                row_frame, 
                text=token.value,
                font=customtkinter.CTkFont(size=12),
                anchor="center"
            )
            lexeme_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

            token_label = customtkinter.CTkLabel(
                row_frame, 
                text=token.type,
                font=customtkinter.CTkFont(size=12),
                anchor="center"
            )
            token_label.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        if errors:
            self.append_terminal_output("Errors:", text_color="red")
            for error in errors:
                self.append_terminal_output(str(error), text_color="red")
            self.sideBtnSyntax.configure(state="disabled")
        else:
            self.append_terminal_output("No Lexical/s Error", text_color="green")
            self.sideBtnSyntax.configure(state="normal")

    def sidebar_button_syntax(self):
        self.clear_terminal_output()  # Clear the terminal output first
        codebox_content = self.codebox.get("1.0", "end-1c")  # Get the content of the codebox
        
        # First do lexical analysis
        tokens, lexical_errors = run(codebox_content)
        
        if lexical_errors:
            self.append_terminal_output("Cannot perform syntax analysis due to lexical errors:", text_color="red")
            for error in lexical_errors:
                self.append_terminal_output(str(error), text_color="red")
            self.sideBtnSemantic.configure(state="disabled")
            return

        # If no lexical errors, proceed with syntax analysis
        syntax_result = parse(tokens)
        
        if isinstance(syntax_result, SyntaxError):
            self.append_terminal_output(str(syntax_result), text_color="red")
            # Highlight the error in the code editor
            self.highlight_error(syntax_result.line_number, syntax_result.column)
            self.sideBtnSemantic.configure(state="disabled")
        else:
            self.append_terminal_output("No Syntax Errors", text_color="green")
            self.sideBtnSemantic.configure(state="normal")

    def highlight_error(self, line_num, column):
        """Highlight the error location in the code editor"""
        # Remove any existing highlights
        self.codebox.tag_remove("error", "1.0", "end")
        
        # Create a tag for error highlighting
        self.codebox.tag_config("error", background="red", foreground="white")
        
        # Calculate the position to highlight
        start_pos = f"{line_num}.{column}"
        end_pos = f"{line_num}.{column + 1}"
        
        # Apply the highlight
        self.codebox.tag_add("error", start_pos, end_pos)
        
        # Scroll to the error position
        self.codebox.see(start_pos)

    def sidebar_button_semantic(self):
        self.append_terminal_output("Semantic Button Clicked!")

    def append_terminal_output(self, text):
        """Append text to the terminal output."""
        self.terminal_output.configure(state="normal")  # Make it editable temporarily
        self.terminal_output.insert(END, f"{text}\n")
        self.terminal_output.configure(state="disabled")  # Make it read-only again

    def execute_command(self, event=None):
        """Execute the command entered in the command input field."""
        command = self.command_input.get()
        if command.strip():
            self.append_terminal_output(f"Executing: {command}")
            subprocess.run(command, shell=True, stdout=sys.stdout, stderr=sys.stderr)

    def clear_terminal_output(self):
        """Clear the terminal output."""
        self.terminal_output.configure(state="normal")  # Make it editable temporarily
        self.terminal_output.delete("1.0", END)  # Clear all text
        self.terminal_output.insert("0.0", "Terminal Output:\n\n")  # Add initial text
        self.terminal_output.configure(state="disabled")  # Make it read-only again

    def append_terminal_output(self, text, text_color=None):
        """Append text to the terminal output."""
        self.terminal_output.configure(state="normal")
        # self.terminal_output.insert(END, text + "\n")
        # self.terminal_output.configure(state="disabled")     
        if text_color:
            self.terminal_output.insert(END, text + "\n", text_color)
            self.terminal_output.tag_config(text_color, foreground=text_color)  # Configure the color
        else:
            self.terminal_output.insert(END, text + "\n")
        
        self.terminal_output.configure(state="disabled")
            
    def on_configure(self, event):
        """Update line numbers when code editor is configured/resized"""
        self.update_line_numbers()
        self.line_numbers.yview_moveto(self.codebox.yview()[0])

if __name__ == "__main__":
    app = App()
    app.mainloop()