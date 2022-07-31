# Sudoku solver

## Logic

Representing a Sudoku grid and solving it may be a tricky challenge: columns, rows and boxes, each with their own layout, stick in your way. However, with a bit of abstraction, one can depict it in a bunch of overlapping containers, composed of nine cells.

Despite having different geometries, containers follow the same basic rules. They should map each number to a set of possible cells and detect if any number only has a single possible cell.  Therefore, one can use a single class for all containers.

## Structure

### SudokuAI

Class that solves a Sudoku game.

| Property     | Description                                                                |
| ------------ | -------------------------------------------------------------------------- |
| `grid`       | Two-dimensional array representing the Sudoku grid.                        |
| `containers` | List of containers (27 in all, 9 for rows, 9 for columns and 9 for boxes). |
| `moves`      | Set of known positions in the grid.                                        |

| Method          | Description                                                                                                                         | Arguments      | Return Value |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------- |:--------------:|:------------:|
| `__init__`      | Sets up `containers` and registers the values in `initial_grid`.                                                                    | `initial_grid` | -            |
| `solve`         | Solves the whole puzzle, returning `None` if no solution was found. Raises an error if the initial grid leads to an illegal result. | -              | `board`      |
| `make_move`     | Adds a number into `grid` if there is a sure one. Returns `None` if there is not and raises an error if move was illegal.           | -              | `move`       |
| `register_move` | Updates all the `containers`.                                                                                                       | `move`         | -            |

### Container

Class that represents a row, column or box. Each number is mapped to a set of possible cells.

| Property    | Description                                                                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cells`     | Set of cells in the container. Each cell is a tuple where `tuple[0]`, `tuple[1]` and `tuple[2]` are the indexes of the row, column and box of the cell. |
| `positions` | Dictionary that maps each number to its possible locations                                                                                              |
| `moves`     | Stores the owner's set of certain moves, in order to add the newly discovered ones.                                                                     |

| Method                | Description                                                                                                                                                                                                                                                                                                           | Arguments        | Return Value          |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:----------------:|:---------------------:|
| `__init__`            | Initializes the container, settings its `cells` and `moves` to the given arguments. Also initializes `positions`, mapping each number to `cells`.                                                                                                                                                                     | `cells`, `moves` | -                     |
| `register_move`       | Updates `positions`, according to the following rules: <br/>- If `cell` belongs to `cells`, it should be taken of all `positions` and the number should be removed.<br/>- Raise an error if the move is illegal<br/>- If `cell` doesn't belong to `positions`, remove all the cells from the same row, column or box. | `cell`, `number` | -                     |
| `add_move`            | Adds a move to `moves`                                                                                                                                                                                                                                                                                                | `move`           | -                     |
| `highest_probability` | Finds the `move` with the highest probability of being true.                                                                                                                                                                                                                                                          | -                | `(move, probability)` |
