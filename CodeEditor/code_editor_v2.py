import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import sys
import os
# Add the parent directory (CODESLAM) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Analyzers.lexical_analyzer.lexical import *  # Import all function from lexical.py
from tkinter import END

from customtkinter import CTkImage
from PIL import Image

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

        # create line number widget
        self.line_numbers = customtkinter.CTkTextbox(self.editor_frame, width=40, corner_radius=0)
        self.line_numbers.grid(row=0, column=0, sticky="ns")
        self.line_numbers.configure(state="disabled")

        # create textbox for code editor
        self.codebox = customtkinter.CTkTextbox(self.editor_frame, width=250, corner_radius=0)
        self.codebox.grid(row=0, column=1, sticky="nsew")
        
        # Placeholder text
        self.codebox_placeholder = "Enter your code here..."
        self.codebox.insert("0.0", self.codebox_placeholder)
        self.codebox.bind("<FocusIn>", self.clear_placeholder)
        self.codebox.bind("<FocusOut>", self.add_placeholder)
        self.codebox.bind("<KeyRelease>", self.update_line_numbers)

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
        
        # Keep track of user input mode (ADDED)
        self.input_mode = False
        self.current_prompt = ">>"
        
        # Bind key events for terminal input
        self.terminal_output.bind("<Key>", self.handle_terminal_key)
        self.terminal_output.bind("<Return>", self.process_terminal_input)

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

    def update_line_numbers(self, event=None):
        line_count = int(self.codebox.index('end-1c').split('.')[0])
        line_numbers_string = "\n".join(str(i) for i in range(1, line_count + 1))
        self.line_numbers.configure(state="normal")
        self.line_numbers.delete("1.0", "end")
        self.line_numbers.insert("1.0", line_numbers_string)
        self.line_numbers.configure(state="disabled")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_lexical(self):
        self.clear_terminal_output()  # Clear the terminal output first
        codebox_content = self.codebox.get("1.0", "end-1c")  # Get the content of the codebox
        # self.append_terminal_output(f"Codebox Content:\n{codebox_content}")
    
        # Clear the existing content in the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
    
        # Create table headers
        header_lexeme = customtkinter.CTkLabel(self.scrollable_frame, text="Lexeme", font=customtkinter.CTkFont(size=12, weight="bold"))
        header_lexeme.grid(row=0, column=0, padx=(20, 10), pady=5)
        header_token = customtkinter.CTkLabel(self.scrollable_frame, text="Token", font=customtkinter.CTkFont(size=12, weight="bold"), anchor="center")
        header_token.grid(row=0, column=1, padx=10, pady=5)
    
        # Use the Lexer to tokenize the codebox content
        tokens, errors = run(codebox_content)
    
        # Populate the table with tokens
        for i, token in enumerate(tokens):
            lexeme_label = customtkinter.CTkLabel(self.scrollable_frame, text=token.value, anchor="center")
            lexeme_label.grid(row=i+1, column=0, padx=10, pady=10)
            token_label = customtkinter.CTkLabel(self.scrollable_frame, text=token.type, anchor="center")
            token_label.grid(row=i+1, column=1, padx=10, pady=10)
            
    
        # Output tokens and errors to the terminal
        # self.append_terminal_output("Tokens:")
        # for token in tokens:
        #     self.append_terminal_output(f"{token.value} -> {token.type}")
    
        if errors:
            self.append_terminal_output("Errors:", text_color="red")
            for error in errors:
                self.append_terminal_output(str(error), text_color="red")
        else:
            self.append_terminal_output("No Lexical Error/s", text_color="green")
            # Enable user input after successful lexical analysis
            self.enable_terminal_input()

    def sidebar_button_syntax(self):
        self.append_terminal_output("Syntax Button Clicked!")
    
    def sidebar_button_semantic(self):
        self.append_terminal_output("Semantic Button Clicked!")

    # MODIFIED
    def append_terminal_output(self, text, text_color=None):
        """Append text to the terminal output."""
        current_pos = self.terminal_output.index(END)  # Get current end position  
        
        if text_color:
            self.terminal_output.insert(END, text + "\n", text_color)
            self.terminal_output.tag_config(text_color, foreground=text_color)  # Configure the color
        else:
            self.terminal_output.insert(END, text + "\n")
        
        self.terminal_output.see(END)  # Auto-scroll to the end

        # REMOVED: self.terminal_output.configure(state="disabled")  # No longer making terminal read-only
            
    # ADDED
    def enable_terminal_input(self):
        """Enable user input in the terminal."""
        self.input_mode = True # Set input mode to True         
        self.terminal_output.insert(END, f"{self.current_prompt}")  # Add the prompt (>>) to the terminal
        self.terminal_output.see(END)  # Auto-scroll to the end  # Auto-scroll to the end
        self.terminal_output.focus_set()  # Set focus to the terminal
        # Get the current end position of the terminal
        self.input_start_pos = self.terminal_output.index(END + "-1c")

    # ADDED
    def handle_terminal_key(self, event):
        """Handle key events in the terminal during input mode."""
        if not self.input_mode:
            return  # Do nothing if not in input mode
        
        # Only allow typing at or after the input position
        current_pos = self.terminal_output.index(tkinter.INSERT)
        if self.terminal_output.compare(current_pos, "<", self.input_start_pos):
            self.terminal_output.mark_set(tkinter.INSERT, END) # Move cursor to end if trying to edit past text
            return "break" # Prevent the key event
            
        # Allow normal typing otherwise
        return None

    # ADDED
    def process_terminal_input(self, event):
        """Process user input when Enter is pressed in the terminal."""
        if not self.input_mode:
            return "break" # Do nothing if not in input mode
            
        # Get the line where the cursor is
        current_line = self.terminal_output.get("insert linestart", "insert lineend")
        
        # Extract just the input part (after the prompt)
        if current_line.startswith(self.current_prompt):
            user_input = current_line[len(self.current_prompt):] # Remove prompt from input
            
            # Reset input mode
            self.input_mode = False
            
            # Add a newline
            self.terminal_output.insert(END, "\n")
            
            # Process the input
            if user_input.strip():
                # Here you would call your semantic analyzer
                self.terminal_output.insert(END, "No semantic analyzer function yet\n")
            
            # Start a new prompt
            self.enable_terminal_input()
            
        return "break"  # Prevent the default Enter behavior

    def execute_command(self, event):
        command = self.command_input.get()
        if command.lower() == "clear":
            self.clear_terminal_output()
        elif command.strip():
            self.append_terminal_output(f"Executing: {command}")
            subprocess.run(command, shell=True, stdout=sys.stdout, stderr=sys.stderr)
        
        # Clear the command input field
        self.command_input.delete(0, END)
        return "break"

    def clear_terminal_output(self):
        """Clear the terminal output."""
        self.terminal_output.delete("1.0", END)  # Clear all text
        self.terminal_output.insert("0.0", "Terminal Output:\n\n")  # Add initial text
        self.input_mode = False  # Reset input mode
            
if __name__ == "__main__":
    app = App()
    app.mainloop()