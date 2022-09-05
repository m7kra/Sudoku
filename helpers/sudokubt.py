class SudokuBT:
    '''
    Solves a Sudoku grid using backtracking.
    '''

    def __init__(self, grid, cells):
        '''
        Sets the value of `self.grid` and `self.cells`. Note that cells will be
        an array of `Cell` objects, these already come with some constraints,
        which reduce the amount of errors in the backtracking, making the
        algorithm much faster.
        '''
        
        # The grid to solve
        self.grid = grid
        # The cells that don't have a number assigned yet.
        self.cells = cells
    
    def solve(self):
        '''
        Picks one of the cells and, for each number, checks if it fits on that
        cell. If it does, calls itself recursively. If it doesn't, tries the
        next number. If all the numbers are tested and none fits, returns
        `False`. If the end of `cells` is reached, returns `True`.
        '''
        
        # If no cells are left, the grid is solved.
        if len(self.cells) == 0: return True
        
        cell = self.cells.pop()

        possibilities = cell.possibilities
        position = cell.cell

        for number in possibilities:
            if self.check(position, number):
                self.grid[position[0]][position[1]] = number
                if self.solve(): return True

        # Revert the changes made, because they were not valid
        self.cells.append(cell)
        self.grid[position[0]][position[1]] = 0
        return False
    
    def check(self, cell, number):
        '''
        Checks if `number` can be placed in `cell`. Returns `True` if it can,
        `False` otherwise.
        '''
        
        # Check if the number is already in the row
        if number in self.grid[cell[0]]: return False
        
        # Check if the number is already in the column
        for row in self.grid:
            if row[cell[1]] == number: return False
        
        # Check if the number is already in the box
        box = self.get_box(cell)
        for row in box:
            for cell in row:
                if cell == number: return False
        
        return True

    def get_box(self, cell):
        '''
        Returns the box that contains `cell`.
        '''
        
        box = []
        row = (cell[0] // 3) * 3
        column = (cell[1] // 3) * 3
        for i in range(3):
            box.append(self.grid[row + i][column:column + 3])
        return box

    def get_grid(self):
        '''
        Returns grid.
        '''
        
        return self.grid