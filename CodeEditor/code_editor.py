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
        
        # Configure the line numbers appearance
        self.configure(width=4)
        self.configure(background='#2b2b2b')  # Dark background
        self.configure(foreground='#606366')  # Grayish line numbers
        self.configure(borderwidth=0)
        self.configure(highlightthickness=0)
        self.configure(state='disabled')  # Make it read-only
        self.configure(padx=8)  # Add padding to align numbers better
        
        # Match the font and spacing of the main editor
        self.configure(font=text_widget.cget("font"))
        self.configure(spacing1=text_widget.cget("spacing1"))
        self.configure(spacing2=text_widget.cget("spacing2"))
        self.configure(spacing3=text_widget.cget("spacing3"))
        
        # Bind text widget scroll events
        self.text_widget.bind('<MouseWheel>', self._on_mousewheel)
        self.text_widget.bind('<Button-4>', self._on_mousewheel)
        self.text_widget.bind('<Button-5>', self._on_mousewheel)
        self.text_widget.bind('<Key>', self._on_key_event)
        
        # Bind the text widget's vertical scrollbar
        if hasattr(self.text_widget, 'yview'):
            text_scroll = self.text_widget.vbar  # Get ScrolledText's scrollbar
            text_scroll.configure(command=self._on_text_scroll)
            self.text_widget.configure(yscrollcommand=self._on_text_yview)
        
    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        if event.num == 4:  # Linux scroll up
            self.yview_scroll(-1, "units")
            self.text_widget.yview_scroll(-1, "units")
        elif event.num == 5:  # Linux scroll down
            self.yview_scroll(1, "units")
            self.text_widget.yview_scroll(1, "units")
        else:  # Windows/MacOS
            delta = -1 * (event.delta // 120)
            self.yview_scroll(delta, "units")
            self.text_widget.yview_scroll(delta, "units")
        return "break"
        
    def _on_text_scroll(self, *args):
        """Handle scrollbar movement"""
        self.yview(*args)
        self.text_widget.yview(*args)
        
    def _on_text_yview(self, *args):
        """Sync line numbers when text widget is scrolled"""
        self.yview_moveto(args[0])
        return args
        
    def _on_key_event(self, event=None):
        """Update line numbers on key events"""
        self.update_line_numbers()
        
    def update_line_numbers(self):
        """Update the line numbers"""
        self.configure(state='normal')
        self.delete('1.0', tk.END)
        
        # Get the total number of lines
        text_content = self.text_widget.get('1.0', tk.END)
        line_count = text_content.count('\n') + (not text_content.endswith('\n'))
        
        # Generate line numbers with proper padding
        line_numbers = '\n'.join(str(i).rjust(3) for i in range(1, line_count + 1))
        self.insert('1.0', line_numbers)
        
        # Sync scroll position
        if hasattr(self.text_widget, 'yview'):
            self.yview_moveto(self.text_widget.yview()[0])
        self.configure(state='disabled')

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
        self.configure(background='#2b2b2b')
        self.create_widgets()
        
    def create_widgets(self):
        # Create main editor frame with grid
        self.grid(row=0, column=0, sticky="nsew") 
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create text widget with custom font and colors
        editor_font = font.Font(family='Consolas', size=11)
        self.text = ScrolledText(
            self,
            wrap=tk.NONE,
            font=editor_font,
            background='#2b2b2b',
            foreground='#a9b7c6',
            insertbackground='white',
            selectbackground='#214283',
            selectforeground='#a9b7c6',
            spacing1=4,  # Adjusted spacing
            spacing2=0,
            spacing3=4,
            padx=8,  # Added padding
            pady=4
        )
        
        # Create line numbers with matching style
        self.line_numbers = LineNumbers(
            self, 
            self.text,
            font=editor_font,
            padx=8,
            pady=4,
            width=4,
            spacing1=4,  # Match text widget spacing
            spacing2=0,
            spacing3=4
        )
        
        # Grid layout for better control
        self.line_numbers.grid(row=0, column=0, sticky="nsew")
        self.text.grid(row=0, column=1, sticky="nsew")
        
        # Initialize syntax highlighter
        self.highlighter = SyntaxHighlighter(self.text)
        self.text.bind('<KeyRelease>', self._on_text_change)
        
        # Add auto-indentation
        self.text.bind('<Return>', self.auto_indent)
        self.text.bind('<Tab>', self.handle_tab)
        
        # Add bracket matching
        self.text.bind('<KeyRelease-bracketleft>', self.insert_matching_bracket)
        self.text.bind('<KeyRelease-parenleft>', self.insert_matching_bracket)
        self.text.bind('<KeyRelease-braceleft>', self.insert_matching_bracket)
        
        # Initial line numbers
        self.line_numbers.update_line_numbers()
        
        # Add binding for any modifications to reset buttons
        self.text.bind('<<Modified>>', self._on_modify)
        self.text.bind('<KeyPress>', self._on_modify)
        
        # Create error highlight tag
        self.text.tag_configure("error_line", background="#4B1515")  # Dark red background
        self.text.tag_configure("error_highlight", background="#662222")  # Brighter red for specific error
        
    def _on_text_change(self, event=None):
        """Handle text changes"""
        self.highlighter.highlight()
        self.line_numbers.update_line_numbers()
        
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
        self.line_numbers.update_line_numbers()

    def _on_modify(self, event=None):
        """Handle any modifications to the text"""
        if hasattr(self, 'master') and hasattr(self.master, 'reset_analyzer_buttons'):
            self.master.reset_analyzer_buttons()
        self.clear_error_highlights()
        
        # Reset the modified flag
        if event and event.widget.edit_modified():
            event.widget.edit_modified(False)
            
    def clear_error_highlights(self):
        """Clear all error highlights"""
        self.text.tag_remove("error_line", "1.0", "end")
        self.text.tag_remove("error_highlight", "1.0", "end")
        
    def highlight_error(self, line_num, column=None):
        """Highlight the error line and specific position"""
        # Clear previous highlights
        self.clear_error_highlights()
        
        # Highlight the entire line
        line_start = f"{line_num}.0"
        line_end = f"{line_num}.end"
        self.text.tag_add("error_line", line_start, line_end)
        
        # Highlight specific error position if column is provided
        if column is not None:
            error_start = f"{line_num}.{column}"
            error_end = f"{line_num}.{column + 1}"
            self.text.tag_add("error_highlight", error_start, error_end)
        
        # Ensure the error is visible
        self.text.see(line_start)

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

        
        # create sidebar buttons with improved styling
        button_font = customtkinter.CTkFont(size=13)
        
        self.sideBtnLexical = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Lexical",
            command=self.sidebar_button_lexical,
            font=button_font,
            fg_color="#1f538d",  # Blue background
            hover_color="#366BA3",  # Lighter blue on hover
            corner_radius=6
        )
        self.sideBtnLexical.grid(row=1, column=0, padx=20, pady=10)
        
        self.sideBtnSyntax = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Syntax",
            command=self.sidebar_button_syntax,
            state="disabled",
            font=button_font,
            fg_color="#2B2B2B",  # Dark background when disabled
            hover_color="#366BA3",  # Lighter blue on hover when enabled
            corner_radius=6
        )
        self.sideBtnSyntax.grid(row=2, column=0, padx=20, pady=10)
        
        self.sideBtnSemantic = customtkinter.CTkButton(
            self.sidebar_frame,
            text="Semantic",
            command=self.sidebar_button_semantic,
            state="disabled",
            font=button_font,
            fg_color="#2B2B2B",  # Dark background when disabled
            hover_color="#366BA3",  # Lighter blue on hover when enabled
            corner_radius=6
        )
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
        self.editor_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=1)  # Changed rowspan to 1
        self.grid_rowconfigure(0, weight=3)  # Give more weight to editor row
        self.grid_rowconfigure(1, weight=1)  # Give less weight to terminal row
        self.grid_rowconfigure(2, weight=0)  # Minimal weight for input row
        
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

    def reset_analyzer_buttons(self):
        """Reset all analyzer buttons to initial state"""
        self.sideBtnSyntax.configure(
            state="disabled",
            fg_color="#2B2B2B"  # Reset to dark background
        )
        self.sideBtnSemantic.configure(
            state="disabled",
            fg_color="#2B2B2B"  # Reset to dark background
        )
        
        # Clear the lexical analysis table
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        # Clear any error highlights
        self.editor_frame.clear_error_highlights()
        
        # Clear terminal output
        self.clear_terminal_output()
        
    def sidebar_button_lexical(self):
        self.clear_terminal_output()
        self.editor_frame.clear_error_highlights()
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
            self.append_terminal_output("Lexical Errors:", text_color="red")
            for error in errors:
                self.append_terminal_output(str(error), text_color="red")
                # Highlight the error line
                if hasattr(error, 'line_number'):
                    self.editor_frame.highlight_error(error.line_number, error.column)
            self.sideBtnSyntax.configure(
                state="disabled",
                fg_color="#2B2B2B"  # Dark background when disabled
            )
        else:
            self.append_terminal_output("No Lexical Errors", text_color="green")
            self.sideBtnSyntax.configure(
                state="normal",
                fg_color="#1f538d"  # Blue background when enabled
            )

    def sidebar_button_syntax(self):
        self.clear_terminal_output()
        self.editor_frame.clear_error_highlights()
        codebox_content = self.codebox.get("1.0", "end-1c")
        
        # First do lexical analysis
        tokens, lexical_errors = run(codebox_content)
        
        if lexical_errors:
            self.append_terminal_output("Cannot perform syntax analysis due to lexical errors:", text_color="red")
            for error in lexical_errors:
                self.append_terminal_output(str(error), text_color="red")
                if hasattr(error, 'line_number'):
                    self.editor_frame.highlight_error(error.line_number, error.column)
            self.sideBtnSemantic.configure(
                state="disabled",
                fg_color="#2B2B2B"  # Dark background when disabled
            )
            return

        # If no lexical errors, proceed with syntax analysis
        syntax_result = parse(tokens)
        
        if isinstance(syntax_result, SyntaxError):
            self.append_terminal_output(str(syntax_result), text_color="red")
            self.editor_frame.highlight_error(syntax_result.line_number, syntax_result.column)
            self.sideBtnSemantic.configure(
                state="disabled",
                fg_color="#2B2B2B"  # Dark background when disabled
            )
        else:
            self.append_terminal_output("No Syntax Errors", text_color="green")
            self.sideBtnSemantic.configure(
                state="normal",
                fg_color="#1f538d"  # Blue background when enabled
            )

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