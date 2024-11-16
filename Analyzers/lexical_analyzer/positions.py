# positions.py

class Position:
    """
    Represents a position in the source code.

    Attributes:
    - text: The source text being processed.
    - pos: The current character index in the source text.
    - line: The current line number in the text.
    - column: The current column number in the text.
    - current_char: The current character at the `pos` index, or None if at the end.
    
    Methods:
    - advance(): Moves to the next character and updates line and column as needed.
    - peek(): Returns the next character without changing position.
    """

    def __init__(self, text):
        self.text = text
        self.pos = 0  # Current position in the text
        self.line = 1
        self.column = 1
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        """Advance the `pos` pointer and update `current_char`, line, and column."""
        if self.current_char == '\n':
            self.line += 1
            self.column = 0
        self.pos += 1
        self.column += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None  # Indicates end of input

    def peek(self):
        """Peek at the next character without advancing the position."""
        peek_pos = self.pos + 1
        if peek_pos < len(self.text):
            return self.text[peek_pos]
        else:
            return None

    def reset(self):
        """Reset the position to the beginning of the text."""
        self.pos = 0
        self.line = 1
        self.column = 1
        self.current_char = self.text[self.pos] if self.text else None

    def copy(self):
        """Create a copy of the current position."""
        new_position = Position(self.text)
        new_position.pos = self.pos
        new_position.line = self.line
        new_position.column = self.column
        new_position.current_char = self.current_char
        return new_position
