class Group:
    '''
    Represents a group of cells in Sudoku's grid
    '''

    def __init__(self, number, cells, moves):
        '''
        Sets the value of `self.number`, `self.cells` and `self.moves`.
        '''
        
        # The number of the group (1 to 9)
        self.number = number
        # A list of cells in the group
        self.cells = cells
        # SudokuAI's list of safe moves, to which the group can add.
        self.moves = moves
        # Whether the number has been assigned to a cell or not.
        self.solved = False
    
    def register_move(self, move):
        '''
        If `cell` is in `self.cells` and `number` is different from `self.number`,
        removes `cell` from possibilities. If the number is the same,
        `self.possibilities` should be filtered so that no cells share the same row,
        column or box. If a single cell is left, this is the solution and should be
        added to `moves`. If `number == self.number` and `cell in self.cells`, `solved`
        is set to `True`.
        '''

        # Prevent unnecessary work
        if self.solved: return
        
        cell, number = move

        if number == self.number:
            if cell in self.cells:
                self.solved = True
                return
            else:
                self.cells = list(filter(lambda x:
                    x[0] != cell[0] and x[1] != cell[1] and x[2] != cell[2],
                    self.cells
                ))
        elif cell in self.cells: self.cells.remove(cell)

        if len(self.cells) == 1:
            self.solved = True
            self.moves.append((self.cells.pop(), self.number))
            return