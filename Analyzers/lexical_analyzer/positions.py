# positions.py

class Position:
    """
    Represents a position in the source code.
    
    Methods:
    - advance(): Moves to the next character and updates line and column as needed.
    """

    def __init__(self, idx, line, col, ftxt):
        self.idx = idx # is the current index in the text, indicating the position of the character within the entire string.
        self.line = line  # is the current line number in the text, starting from 0.
        self.col = col # is the current column number within the line, indicating the position of the character within the line.
        self.ftxt = ftxt #  is the full text being processed

    def advance(self, current_char):
        '''
        Updates the position based on the current character.
        '''
        self.idx += 1
        self.col += 1

        if current_char == "\n":
            self.line += 1
            self.col = 0

        return self

    def copy(self):
        '''
        Creates a copy of the current Position object.
        '''
        return Position(self.idx, self.line, self.col, self.ftxt)

    def reset(self):
        '''
        Resets the position to its initial state by setting the character index and column number to 0.
        '''
        self.idx = 0
        self.line = 0
        self.col = 0