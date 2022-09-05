from sudokuai import SudokuAI
from sudokubt import SudokuBT


def solve(grid):
    '''
    Solves a sudoku grid
    '''

    # Try to use the constraint-based approach first
    ai = SudokuAI(grid)
    if ai.solve(): return ai.grid

    # If it fails, use backtracking
    cells = list(filter(lambda cell: cell.solved == False, ai.cells))
    bt = SudokuBT(ai.grid, cells)
    if bt.solve(): return bt.grid
    else: return False

def print_grid(grid):
    '''
    Prints the grid in a readable format.
    '''
    
    for row in grid:
        print(row)

board = [
    [0, 0, 3, 7, 0, 1, 6, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 0, 2, 0, 0],
    [0, 3, 0, 2, 0, 8, 0, 4, 0],
    [0, 0, 8, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 1, 3, 0, 2, 7, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 6, 0]
]
'''
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
'''

if __name__ == '__main__':

    print('Original grid:')
    print_grid(board)
    print()

    print('Solved grid:')
    print_grid(solve(board))
    print()

    print('Done.')