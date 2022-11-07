from helpers.sudokuai import SudokuAI
from helpers.sudokubt import SudokuBT


def solve(grid):
    '''
    Solves a sudoku grid
    '''

    # Try to use the constraint-based approach first
    ai = SudokuAI(grid)
    if ai.solve(): return ai.grid()

    # If it fails, use backtracking
    grid = ai.get_grid()
    cells = ai.get_cells()
    bt = SudokuBT(grid, cells)
    if bt.solve(): return bt.get_grid()
    else: return False

def print_grid(grid):
    '''
    Prints the grid in a readable format.
    '''
    
    print('-' * 19)
    for row in grid:
        print(str(row)
            .replace(',', '')
            .replace('[', '|')
            .replace(']', '|')
            .replace('0', ' ')
        )
    print('-' * 19)

'''
Zeroes represent empty cells. Replace them with your own grid.
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

if __name__ == '__main__':

    print('\nOriginal grid:')
    print_grid(board)
    print()

    print('Solved grid:')
    print_grid(solve(board))
    print()