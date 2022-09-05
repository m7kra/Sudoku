from helpers.cell import Cell
from helpers.group import Group

class SudokuAI:
    '''
    Solves a Sudoku grid using a constraint based approach.
    '''

    def __init__(self, grid):
        '''
        Prepares to solve the grid: sets the value of `self.grid` to all zero
        (zero is used to represent an empty cell), creates the cells and groups.
        Also inserts each of numbers in the given `grid`.
        '''
        
        # The grid to solve
        self.grid = [[0 for i in range(9)] for j in range(9)]
        # The cells of the grid (81 - 9x9)
        self.cells = []
        # The different groups of the grid (243 - 3x9x9)
        self.groups = []
        # A list of moves known to be safe, in the form `(cell, value)`
        self.moves = []

        # A temporary list of cells, not the same as `self.cells`, which are a
        # list of cell objects
        cells = []

        # Create the cells
        for row in range(9):
            for column in range(9):
                # The box is calculated by dividing the row and column by 3 and
                # multiplying the result by 3
                box = (row // 3) * 3 + (column // 3)
                cell = (row, column, box)
                cells.append(cell)
                self.cells.append(Cell(cell, self.moves))
        
        # Create the groups
        for i in range(3):
            for j in range(9):
                # The groups are the rows, the columns and the boxes
                group = [cell for cell in cells if cell[i] == j]
                for k in range(1, 10):
                    self.groups.append(Group(k, group, self.moves))

        # Insert the numbers in the grid
        for row in range(9):
            for column in range(9):
                if grid[row][column]:
                    self.moves.append(((row, column, (row // 3) * 3 + (column // 3)), grid[row][column]))
    
    def solve(self):
        '''
        Repeatedly calls `make_move` until the grid is solved or no more moves
        can be made. Returns the solved grid or `None` if the grid cannot be
        solved.
        '''
        
        while self.make_move():
            pass
        
        if self.solved(): return True
        else: return False
    
    def make_move(self):
        '''
        Chooses one move of `self.moves` and makes it. If there are no moves,
        returns `False`. If there are moves, returns `True`.
        '''
        if len(self.moves) == 0: return False

        move = self.moves.pop()
        cell, number = move
        self.grid[cell[0]][cell[1]] = number

        for cell in self.cells:
            cell.register_move(move)
        for group in self.groups:
            group.register_move(move)
        
        return True
    
    def solved(self):
        '''
        Checks if the grid is solved. Returns `True` if it is, `False` otherwise.
        '''
        
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    return False
        return True
    
    def get_grid(self):
        '''
        Returns the grid.
        '''

        return self.grid
    
    def get_cells(self):
        '''
        Returns the cells that were not solved
        '''

        return list(filter(lambda cell: cell.solved == False, self.cells))


"""
##### `grid(self)`:

Returns the grid.

##### `cells(self)`:

Returns the cells that were not solved.
"""
