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

# Load the image
image_path = "assets/icons/CodeSLAM-LOGO.png"
image = Image.open(image_path)

# Create CTkImage with a specified size
logo_image = CTkImage(image, size=(100, 100))  # Set desired width and height here

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")

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

        # create frame for code editor and line numbers
        self.editor_frame = customtkinter.CTkFrame(self)
        self.editor_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.editor_frame.grid_columnconfigure(1, weight=1)
        self.editor_frame.grid_rowconfigure(0, weight=1)

        # Create scrollbar first
        self.scrollbar = customtkinter.CTkScrollbar(self.editor_frame)
        self.scrollbar.grid(row=0, column=2, sticky="ns")

        # create line number widget
        self.line_numbers = customtkinter.CTkTextbox(self.editor_frame, width=40, corner_radius=0, yscrollcommand=self.sync_scroll)
        self.line_numbers.grid(row=0, column=0, sticky="ns")
        self.line_numbers.configure(state="disabled")

        # create textbox for code editor
        self.codebox = customtkinter.CTkTextbox(self.editor_frame, width=250, corner_radius=0, yscrollcommand=self.sync_scroll)
        self.codebox.grid(row=0, column=1, sticky="nsew")

        # Configure scrollbar to work with both text widgets
        self.scrollbar.configure(command=self.scroll_both)

        # Bind all scroll events
        self.codebox.bind("<Key>", self.on_code_change)
        self.codebox.bind("<KeyRelease>", self.on_code_change)
        self.codebox.bind("<<Modified>>", self.on_modified)
        self.codebox.bind("<Configure>", self.on_configure)

        # Placeholder text
        self.codebox_placeholder = "Enter your code here..."
        self.codebox.insert("0.0", self.codebox_placeholder)
        self.codebox.bind("<FocusIn>", self.clear_placeholder)
        self.codebox.bind("<FocusOut>", self.add_placeholder)

        # Set tab width to 1 character
        self.codebox.configure(tabs=("1c"))

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Lexical Analyzer", width=400)
        self.scrollable_frame.grid(row=0, column=2, rowspan=2, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

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
        self.clear_terminal_output()  # Clear the terminal output first
        codebox_content = self.codebox.get("1.0", "end-1c")  # Get the content of the codebox

        # Clear the existing content in the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Create table headers
        header_lexeme = customtkinter.CTkLabel(self.scrollable_frame, text="Lexeme", 
            font=customtkinter.CTkFont(size=12, weight="bold"))
        header_lexeme.grid(row=0, column=0, padx=(20, 10), pady=5)
        header_token = customtkinter.CTkLabel(self.scrollable_frame, text="Token", 
            font=customtkinter.CTkFont(size=12, weight="bold"), anchor="center")
        header_token.grid(row=0, column=1, padx=10, pady=5)

        # Use the Lexer to tokenize the codebox content
        tokens, errors = run(codebox_content)

        # Populate the table with tokens
        for i, token in enumerate(tokens):
            lexeme_label = customtkinter.CTkLabel(self.scrollable_frame, text=token.value, anchor="center")
            lexeme_label.grid(row=i+1, column=0, padx=10, pady=10)
            token_label = customtkinter.CTkLabel(self.scrollable_frame, text=token.type, anchor="center")
            token_label.grid(row=i+1, column=1, padx=10, pady=10)

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