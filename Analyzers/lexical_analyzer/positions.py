# positions.py

class Position:
    """
    Represents a position in the source code.
    
    Methods:
    - advance(): Moves to the next character and updates line and column as needed.
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