class SudokuAI:
    '''
    Class that solves a Sudoku game.
    '''

    def __init__(self, initial_grid):
        '''
        Sets up `containers` and registers the values in `initial_grid`.
        '''

        # Two-dimensional array representing the Sudoku grid.
        self.grid = [[None for i in range(9)] for i in range(9)]

        # Set of known positions in the grid.
        self.moves = set()

        # List of containers (27 in all, 9 for rows, 9 for columns and 9 for
        # boxes).
        cells = set()
        for i in range(9):
            for j in range(9):
                box = (i // 3) * 3 + j // 3
                cells.add((i, j, box))
        self.containers = []
        for i in range(3):
            for j in range(9):
                container_cells = set(filter(lambda cell: cell[i] == j, cells))
                self.containers.append(Container(container_cells, self.moves))
        
        # Register values in `initial_grid`
        for i in range(9):
            for j in range(9):
                if initial_grid[i][j]:
                    box = (i // 3) * 3 + j // 3
                    self.register_move(((i, j, box), initial_grid[i][j]))


    
    def solve(self):
        '''
        Solves the whole puzzle, returning `None` if no solution was found.
        '''
        while len(self.moves) > 0:
            self.make_move()
        
        # Check if any cell is missing
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == None:
                    return None
        
        return self.grid
    
    def make_move(self):
        '''
        Adds a number into `grid`, returning `None` if no move is sure.
        '''
        if len(self.moves) == 0: return None

        move = self.moves.pop()
        self.register_move(move)
        return move
    
    def register_move(self, move):
        '''
        Updates all the `containers`.
        '''
        cell, number = move
        self.grid[cell[0]][cell[1]] = number

        for container in self.containers:
            container.register_move(cell, number)

class Container:
    '''
    Class that represents a row, column or box. Each number is mapped to a set
    of possible cells.
    '''

    def __init__(self, cells, moves):
        '''
        Initializes the container, settings its `cells` and `moves` to the given
        arguments. Also initializes `positions`, mapping each number to `cells`.
        '''

        # Set of cells in the container. Each cell is a tuple where
        # `tuple[0]`, `tuple[1]` and `tuple[2]` are the indexes of the row,
        # column and box of the cell.
        self.cells = cells

        # Dictionary that maps each number to its possible locations
        self.positions = {i: cells.copy() for i in range(1, 10)}

        # Stores the owner's list of certain moves, in order to add the newly
        # discovered ones.
        self.moves = moves


    def register_move(self, cell, number):
        '''
        Updates `positions`, according to the following rules:

        - If `cell` belongs to `cells`, it should be taken of all `positions`
          and the number should be removed.
        
        - If `cell` doesn't belong to `positions`, remove all the cells from the
          same row, column or box.
        '''

        if cell in self.cells:
            del self.positions[number]
            for value in self.positions:
                if cell in self.positions[value]:
                    self.positions[value].remove(cell)

        else:
            if number in self.positions:
                self.positions[number] = set(filter(
                    lambda position:
                        position[0] != cell[0] and
                        position[1] != cell[1] and
                        position[2] != cell[2],
                    self.positions[number]
                ))

        # If any number is left with one single option, add it to moves
        for number in self.positions:
            possilibities = self.positions[number]
            if len(possilibities) == 1:
                self.add_move((possilibities.pop(), number))



    def add_move(self, move):
        '''
        Adds a move to `moves`
        '''
        self.moves.add(move)

board = [
    [None, None, None, None, 8, 4, None, None, 6],
    [None, None, None, None, None, None, None, None, 4],
    [4, 8, 6, None, None, None, 9, 7, 5],
    [9, None, 5, 3, None, 7, None, None, None],
    [3, 2, None, None, None, None, None, 5, 9],
    [None, None, None, 5, None, None, 3, 6, None],
    [None, 4, 1, 8, None, None, 5, None, 3],
    [5, 7, None, None, None, 6, None, 4, None],
    [2, None, None, 4, None, None, None, None, None]
]
'''
board = [
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None]
]
'''
ai = SudokuAI(board)
ai.solve()
for row in ai.grid:
    print(row)