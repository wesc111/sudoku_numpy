
from enum import Enum

# Class suElemT defines the type of a Sudoku element
class suElemT(Enum):
    """This is the documentation for MyClass."""
    UNDEFINED = 0
    FIXED = 1
    SOLVED_SINGLE = 2
    SOLVED_HIDDEN_SINGLE = 3
    GUESS = 4

# The candidate list for a sudoku element
class candidateList():
    row = 0
    col = 0
    block = 0
    list = []
    def print(self):
        print(f"row={self.row}, col={self.col} block={self.block}: {self.list}")