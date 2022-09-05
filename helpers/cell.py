class Cell:
    '''
    Represents a single cell in Sudoku's grid
    '''

    def __init__(self, cell, moves):
        '''
        Sets the value of `self.cell`, `possibilities`, `solved` and `moves`.
        '''
        
        # A tupple containing the cells coordinates `(row, column, box)`.
        self.cell = cell
        # A list of possible values for the cell (ranging from 1 to 9 in the
        # beginning).
        self.possibilities = [i for i in range(1, 10)]
        # Whether a number has been assigned to the cell or not.
        self.solved = False
        # SudokuAI's list of safe moves, to which the cell can add.
        self.moves = moves
    
    def register_move(self, move):
        '''
        If `cell` is in `self.cells` and `number` is different from
        `self.number`, removes `cell` from possibilities. If the number is the
        same, `self.possibilities` should be filtered so that no cells share the
        same row, column or box. If a single cell is left, this is the solution
        and should be added to `moves`. If `number == self.number` and `cell in
        self.cells`, `solved` is set to `True`.
        '''

        # Prevent unnecessary work
        if self.solved: return
        
        cell, number = move

        if cell == self.cell:
            self.solved = True
            return

        if cell[0] == self.cell[0] or cell[1] == self.cell[1] or cell[2] == self.cell[2]:
            if number in self.possibilities:
                self.possibilities.remove(number)
                if len(self.possibilities) == 1:
                    self.moves.append((self.cell, self.possibilities[0]))