import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import sys
import os
# Add the parent directory (CODESLAM) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Analyzers.lexical_analyzer.tokens import Token
from Analyzers.lexical_analyzer.lexical import run  # Import run function from lexical.py
from tkinter import END

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
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CodeSlam", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # create sidebar buttons
        self.sideBtnLexical = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_lexical)
        self.sideBtnLexical.grid(row=1, column=0, padx=20, pady=10)
        self.sideBtnSyntax = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_syntax)
        self.sideBtnSyntax.grid(row=2, column=0, padx=20, pady=10)
        self.sideBtnSemantic = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_semantic)
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

        # create textbox for code editor
        self.codebox = customtkinter.CTkTextbox(self, width=250)
        self.codebox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        # Placeholder text
        self.codebox_placeholder = "Enter your code here..."
        self.codebox.insert("0.0", self.codebox_placeholder)
        self.codebox.bind("<FocusIn>", self.clear_placeholder)
        self.codebox.bind("<FocusOut>", self.add_placeholder)

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Lexical Analyzer", width=300)
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

    def clear_placeholder(self, event):
        if self.codebox.get("1.0", "end-1c") == self.codebox_placeholder:
            self.codebox.delete("1.0", "end")

    def add_placeholder(self, event):
        if not self.codebox.get("1.0", "end-1c"):
            self.codebox.insert("1.0", self.codebox_placeholder)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_lexical(self):
        """Trigger lexical analysis for the entered code."""
        # Clear the scrollable frame for fresh results
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Retrieve the code input from the editor
        code_text = self.codebox.get("1.0", "end-1c").strip()

        # Ensure code is entered before processing
        if code_text == self.codebox_placeholder or not code_text:
            self.append_terminal_output("No code entered. Please enter code before running lexical analysis.")
            return

        try:
            # Split the code into lines (to handle multi-line input)
            code_lines = code_text.splitlines()

            # Store the results from the lexical analysis
            analysis_results = []

            # Call the run function for each line of code
            for line_number, line_content in enumerate(code_lines, start=1):
                line_results = run("<stdin>", line_content, line_number)
                analysis_results.extend(line_results)  # Combine results from all lines

            # Check if any tokens were found
            if not analysis_results:
                self.append_terminal_output("No lexemes or tokens were detected.")
                return

            # Add column headers
            headers = customtkinter.CTkLabel(
                self.scrollable_frame,
                text=f"{'Lexeme':<15}{'Tokens':<15}",
                font=("Arial", 10, "bold"),
                anchor="w"
            )
            headers.pack(fill="x", padx=10, pady=5)

            # Add a line separator
            separator = customtkinter.CTkLabel(
                self.scrollable_frame,
                text="-" * 30,
                anchor="w"
            )
            separator.pack(fill="x", padx=10, pady=2)

            # Display each lexeme and token pair in the scrollable frame
            for result in analysis_results:
                # Handle tuple format (success_flag, Token object)
                if isinstance(result, tuple) and len(result) == 2:
                    success, token_obj = result
                    if success and isinstance(token_obj, Token):
                        lexeme = getattr(token_obj, "lexeme", "N/A")
                        token = getattr(token_obj, "token_type", "N/A")
                    else:
                        lexeme, token = "Invalid", "Invalid"
                else:
                    lexeme, token = "Invalid", "Invalid"

                # Add the lexeme-token row
                result_label = customtkinter.CTkLabel(
                    self.scrollable_frame,
                    text=f"{lexeme:<15}{token:<15}",
                    anchor="w"
                )
                result_label.pack(fill="x", padx=10, pady=5)

        except Exception as e:
            self.append_terminal_output(f"Error during lexical analysis:\n{e}")

    def sidebar_button_syntax(self):
        self.append_terminal_output("Syntax Button Clicked!")
    
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

if __name__ == "__main__":
    app = App()
    app.mainloop()