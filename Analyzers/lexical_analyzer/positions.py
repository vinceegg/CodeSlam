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

    def __init__(self, idx, col, ftxt):
        self.idx = idx
        self.col = col
        self.ftxt = ftxt

    def advance(self, current_char):
        '''
        Updates the position based on the current character.
        '''
        self.idx += 1
        self.col += 1

        if current_char == "\n":
            self.col = 0

        return self

    def copy(self):
        '''
        Creates a copy of the current Position object.
        '''
        return Position(self.idx, self.col, self.ftxt)

    def reset(self):
        '''
        Resets the position to its initial state by setting the character index and column number to 0.
        '''
        self.idx = 0
        self.col = 0
