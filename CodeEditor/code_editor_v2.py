import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import sys
import os
# Add the parent directory (CODESLAM) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Add the mebi directory to the Python path
mebi_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mebi'))
sys.path.append(mebi_path)
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
        
        # Configure the line numbers appearance based on mode
        self.update_colors()
        
        # Configure the line numbers appearance
        self.configure(width=4)
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

    def update_colors(self):
        """Update colors based on appearance mode"""
        if customtkinter.get_appearance_mode() == "Light":
            self.configure(background='#f0f0f0')  # Light background
            self.configure(foreground='#666666')  # Darker line numbers for light mode
        else:
            self.configure(background='#2b2b2b')  # Dark background
            self.configure(foreground='#606366')  # Grayish line numbers for dark mode

class SyntaxHighlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.update_colors()
        
    def update_colors(self):
        """Update syntax highlighting colors based on appearance mode"""
        is_light = customtkinter.get_appearance_mode() == "Light"
        
        # Define color schemes for light and dark modes
        self.color_scheme = {
            'keyword': '#0033B3' if is_light else '#4ADADF',  # Blue for light, Light blue for dark
            'number': '#1750EB' if is_light else '#E71D56',   # Blue for light, Pink for dark
            'string': '#067D17' if is_light else '#9CD1BB',   # Green for light, Light green for dark
            'comment': '#8C8C8C' if is_light else '#808080',  # Gray for both
            'variable': '#871094' if is_light else '#EAF2F1', # Purple for light, Light gray for dark
            'operator': '#E75C1D' if is_light else '#FFB27D', # Orange for both
            'brackets': '#000000' if is_light else '#a9b7c6'  # Black for light, Light gray for dark
        }
        
        # Define syntax highlighting patterns
        self.patterns = [
            # Keywords
            (r'\b(Team|Wilt|Feint|Floater|Chant|Stat|Forward|Play|Run|Switch|Get|Default|Dribble|Pass|Shoot|Rebound|Announce|Inbound)\b', 
             self.color_scheme['keyword']),
            # Numbers
            (r'\b\d+(\.\d+)?\b', self.color_scheme['number']),
            # Strings
            (r'"[^"]*"', self.color_scheme['string']),
            # Comments
            (r'//.*$', self.color_scheme['comment']),
            # Variables with @ prefix
            (r'@\w+', self.color_scheme['variable']),
            # Operators
            (r'[+\-*/=<>!&|]', self.color_scheme['operator']),
            # Parentheses and brackets
            (r'[\(\)\[\]\{\}]', self.color_scheme['brackets'])
        ]
        
        # Update existing tags with new colors
        for pattern, color in self.patterns:
            self.text_widget.tag_configure(pattern, foreground=color)
        
        # Reapply highlighting
        self.highlight()

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
        self.update_colors()
        self.create_widgets()
        
    def update_colors(self):
        """Update colors based on appearance mode"""
        if customtkinter.get_appearance_mode() == "Light":
            self.configure(background='#ffffff')  # White background for light mode
            self.editor_bg = '#ffffff'
            self.editor_fg = '#000000'
            self.select_bg = '#add6ff'  # Light blue selection
            self.select_fg = '#000000'
        else:
            self.configure(background='#2b2b2b')  # Dark background
            self.editor_bg = '#2b2b2b'
            self.editor_fg = '#a9b7c6'
            self.select_bg = '#214283'
            self.select_fg = '#a9b7c6'
        
    def create_widgets(self):
        # Create main editor frame with grid
        self.grid(row=0, column=0, sticky="nsew") 
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create text widget with dynamic colors
        editor_font = font.Font(family='Consolas', size=11)
        self.text = ScrolledText(
            self,
            wrap=tk.NONE,
            font=editor_font,
            background=self.editor_bg,
            foreground=self.editor_fg,
            insertbackground=self.editor_fg,  # Cursor color matches text
            selectbackground=self.select_bg,
            selectforeground=self.select_fg,
            spacing1=4,
            spacing2=0,
            spacing3=4,
            padx=8,
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
        # self.text.bind('<Tab>', self.handle_tab)
        
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
        
    # def handle_tab(self, event):
    #     # Insert spaces instead of tab
    #     self.text.insert("insert", "    ")
    #     return "break"
        
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

    def update_theme(self):
        """Update all colors when theme changes"""
        self.update_colors()
        self.text.configure(
            background=self.editor_bg,
            foreground=self.editor_fg,
            insertbackground=self.editor_fg,
            selectbackground=self.select_bg,
            selectforeground=self.select_fg
        )
        self.line_numbers.update_colors()
        self.highlighter.update_colors()  # Update syntax highlighting colors
        self.update_error_colors()  # Update error highlighting colors

    def update_error_colors(self):
        """Update error highlighting colors based on appearance mode"""
        is_light = customtkinter.get_appearance_mode() == "Light"
        
        error_bg = "#FFE8E8" if is_light else "#4B1515"  # Light red for light mode, Dark red for dark mode
        error_highlight = "#FFCCCC" if is_light else "#662222"  # Brighter red for both modes
        
        self.text.tag_configure("error_line", background=error_bg)
        self.text.tag_configure("error_highlight", background=error_highlight)

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
            fg_color="#E5E5E5" if customtkinter.get_appearance_mode() == "Light" else "#2B2B2B",  # Light/Dark background when disabled
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
            fg_color="#E5E5E5" if customtkinter.get_appearance_mode() == "Light" else "#2B2B2B",  # Light/Dark background when disabled
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

        # Command input field (entry widget)
        self.command_input = customtkinter.CTkEntry(self, placeholder_text="Enter your input here...")
        self.command_input.grid(row=2, column=1, padx=(20, 0), pady=(10, 20), sticky="ew")
        self.command_input.bind("<Return>", self.process_command_input)

        # Variables for input handling
        self.waiting_for_input = False
        self.input_processed = tkinter.BooleanVar(value=False)
        self.last_input = None

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
        # Update editor colors when appearance mode changes
        self.editor_frame.update_theme()
        # Update button colors
        self.update_button_colors()
        # Update scrollable frame colors
        self.update_lexical_table_colors()

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

        # Create styled table headers with light/dark mode awareness
        header_frame = customtkinter.CTkFrame(self.scrollable_frame)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=1)

        is_light = customtkinter.get_appearance_mode() == "Light"
        header_bg = "#F0F0F0" if is_light else "#3B3B3B"
        content_bg = "#FFFFFF" if is_light else "#2b2b2b"
        alt_content_bg = "#F5F5F5" if is_light else "#323232"
        text_color = "black" if is_light else "white"

        header_lexeme = customtkinter.CTkLabel(
            header_frame, 
            text="Lexeme",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            fg_color=header_bg,
            text_color=text_color,
            corner_radius=6
        )
        header_lexeme.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        header_token = customtkinter.CTkLabel(
            header_frame, 
            text="Token",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            fg_color=header_bg,
            text_color=text_color,
            corner_radius=6
        )
        header_token.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Use the Lexer
        tokens, errors = run(codebox_content)

        # Create table content with alternating row colors
        for i, token in enumerate(tokens):
            row_frame = customtkinter.CTkFrame(
                self.scrollable_frame,
                fg_color=content_bg if i % 2 == 0 else alt_content_bg
            )
            row_frame.grid(row=i+1, column=0, columnspan=2, sticky="ew", padx=5, pady=2)
            row_frame.grid_columnconfigure(0, weight=1)
            row_frame.grid_columnconfigure(1, weight=1)

            lexeme_label = customtkinter.CTkLabel(
                row_frame, 
                text=token.value,
                font=customtkinter.CTkFont(size=12),
                text_color=text_color,
                anchor="center"
            )
            lexeme_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

            token_label = customtkinter.CTkLabel(
                row_frame, 
                text=token.type,
                font=customtkinter.CTkFont(size=12),
                text_color=text_color,
                anchor="center"
            )
            token_label.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Handle errors and button states
        if errors:
            self.append_terminal_output("Lexical Errors:", text_color="red")
            for error in errors:
                self.append_terminal_output(str(error), text_color="red")
                if hasattr(error, 'line_number'):
                    self.editor_frame.highlight_error(error.line_number, error.column)
            # Disable syntax button when there are lexical errors
            self.sideBtnSyntax.configure(
                state="disabled",
                fg_color="#2B2B2B"  # Dark background when disabled
            )
            self.sideBtnSemantic.configure(
                state="disabled",
                fg_color="#2B2B2B"  # Dark background when disabled
            )
        else:
            self.append_terminal_output("No Lexical Error/s", text_color="green")
            # Enable syntax button only when there are no lexical errors
            self.sideBtnSyntax.configure(
                state="normal",
                fg_color="#1f538d"  # Blue background when enabled
            )

    def sidebar_button_syntax(self):
        self.clear_terminal_output()
        self.editor_frame.clear_error_highlights()
        
        # Get the tokens from the lexical analyzer table
        tokens = []
        for widget in self.scrollable_frame.winfo_children():
            if isinstance(widget, customtkinter.CTkFrame) and widget.grid_info()['row'] > 0:
                lexeme_label = widget.winfo_children()[0]
                token_label = widget.winfo_children()[1]
                
                lexeme = lexeme_label.cget("text")
                token_type = token_label.cget("text")
                
                token = Token(TokenType[token_type], token_type)
                tokens.append(token)
        
        if not tokens:
            self.append_terminal_output("No tokens to analyze. Run lexical analysis first.", text_color="red")
            return
        
        try:
            result = parse(tokens)
            if result:
                self.append_terminal_output("No Syntax Error/s", text_color="green")
                self.sideBtnSemantic.configure(
                    state="normal",
                    fg_color="#1f538d"
                )
        except SyntaxError as e:
            if e.token == "EOF":
                error_msg = f"Syntax Error at line {e.line_number}, column {e.column}: Expected Token: {{{e.expected}}}"
            else:
                error_msg = f"Syntax Error at line {e.line_number}, column {e.column}: Unexpected Token: {e.token}\nExpected Token: {{{e.expected}}}"
            self.append_terminal_output(error_msg, text_color="red")
            
            if hasattr(e, 'line_number') and hasattr(e, 'column'):
                self.editor_frame.highlight_error(e.line_number, e.column)
                
            self.sideBtnSemantic.configure(
                state="disabled",
                fg_color="#2B2B2B"
            )

    def sidebar_button_semantic(self):
        """Run semantic analysis using the mebi compiler"""
        self.clear_terminal_output()
        self.editor_frame.clear_error_highlights()
        
        # Get code from editor
        code = self.codebox.get("1.0", "end-1c")
        
        try:
            from mebi.main import run_compiler
            
            # Define a custom input function that uses our command input box
            def get_terminal_input(prompt):
                self.terminal_output.configure(state="normal")
                # Show the prompt in terminal
                self.terminal_output.insert(END, prompt)
                self.terminal_output.see(END)
                self.terminal_output.configure(state="disabled")
                
                # Reset input flags
                self.input_processed.set(False)
                self.waiting_for_input = True
                
                # Enable and focus the input box
                self.command_input.configure(state="normal")
                self.command_input.focus_set()
                
                # Wait for input to be processed
                self.wait_variable(self.input_processed)
                
                return self.last_input
            
            # Run the compiler with our custom input function
            output = run_compiler(code, input_func=get_terminal_input)
            
            # Display the output directly in the terminal
            if output:
                self.terminal_output.configure(state="normal")
                # Process the output to handle escape sequences
                processed_output = bytes(output, "utf-8").decode("unicode_escape")
                self.terminal_output.insert(END, processed_output)
                self.terminal_output.see(END)
                self.terminal_output.configure(state="disabled")
                    
        except ImportError as e:
            self.append_terminal_output("Error importing mebi compiler:", text_color="red")
            self.append_terminal_output(str(e), text_color="red")

    def process_command_input(self, event):
        """Process input from the command input box."""
        user_input = self.command_input.get()
        
        if self.waiting_for_input:
            # Add the input to terminal with newline
            self.terminal_output.configure(state="normal")
            self.terminal_output.insert(END, user_input + "\n")
            self.terminal_output.configure(state="disabled")
            self.terminal_output.see(END)
            
            # Store the input and signal it's processed
            self.last_input = user_input
            self.input_processed.set(True)
            self.waiting_for_input = False
            
            # Clear the input box
            self.command_input.delete(0, END)
            # Disable the input box until next input request
            self.command_input.configure(state="disabled")
        
        return "break"

    def update_button_colors(self):
        """Update button colors based on appearance mode"""
        disabled_color = "#E5E5E5" if customtkinter.get_appearance_mode() == "Light" else "#2B2B2B"
        
        if self.sideBtnSyntax.cget("state") == "disabled":
            self.sideBtnSyntax.configure(fg_color=disabled_color)
        if self.sideBtnSemantic.cget("state") == "disabled":
            self.sideBtnSemantic.configure(fg_color=disabled_color)

    def update_lexical_table_colors(self):
        """Update lexical analyzer table colors based on appearance mode"""
        is_light = customtkinter.get_appearance_mode() == "Light"
        
        # Update the scrollable frame background
        self.scrollable_frame.configure(
            fg_color="#FFFFFF" if is_light else "#2B2B2B"
        )
        
        # Update header colors
        for widget in self.scrollable_frame.winfo_children():
            if isinstance(widget, customtkinter.CTkFrame):
                if widget.grid_info()['row'] == 0:  # Header frame
                    for header in widget.winfo_children():
                        header.configure(
                            fg_color="#F0F0F0" if is_light else "#3B3B3B"
                        )
                else:  # Content rows
                    widget.configure(
                        fg_color="#FFFFFF" if is_light else "#2b2b2b" 
                        if widget.grid_info()['row'] % 2 == 0 
                        else "#F5F5F5" if is_light else "#323232"
                    )
                    
    def clear_terminal_output(self):
        """Clear the terminal output."""
        self.terminal_output.configure(state="normal")
        self.terminal_output.delete("1.0", END)
        self.terminal_output.insert("0.0", "Terminal Output:\n\n")
        self.terminal_output.configure(state="disabled")
        # Reset input state
        self.waiting_for_input = False
        self.command_input.configure(state="disabled")

    def append_terminal_output(self, text, text_color="white"):
        """Append text to the terminal output with specified color"""
        self.terminal_output.configure(state="normal")  # Make it editable temporarily
        
        # Determine color based on message type
        if "Error" in text or "error" in text.lower():
            text_color = "red"
        elif "No" in text and ("Error" in text or "error" in text.lower()):
            text_color = "green"
            
        # Add the text with newline and color
        self.terminal_output.insert(END, text + "\n", text_color)
        self.terminal_output.configure(state="disabled")  # Make it read-only again
        self.terminal_output.see(END)  # Auto-scroll to the end

if __name__ == "__main__":
    app = App()
    app.mainloop()