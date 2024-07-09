import random

SIZE = 4
WIN_CONDITION = 2048

# this function creates a 4x4 grid filled with zeros and places two '2' tiles randomly on the grid by calling add_random_two twice
def initialize_grid():
    grid = [[0] * SIZE for _ in range(SIZE)]
    add_random_two(grid)
    add_random_two(grid)
    return grid

# This function finds all empty cells in the grid, selects one randomly, and places a '2' in it.
def add_random_two(grid):
    empty_cells = [(i, j) for i in range(SIZE) for j in range(SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2

# This function moves all tiles to the left, combines tiles with the same value, and fills empty spaces with zeros.
def move_left(grid):
    new_grid = []
    for row in grid:
        new_row = [num for num in row if num != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [num for num in new_row if num != 0]
        new_row.extend([0] * (SIZE - len(new_row)))
        new_grid.append(new_row)
    return new_grid
# This function reverses each row, uses move_left to perform the move, and then reverses the rows back to achieve a right move.
def move_right(grid):
    reversed_grid = [row[::-1] for row in grid]
    new_grid = move_left(reversed_grid)
    return [row[::-1] for row in new_grid]

# This function transposes the grid (swaps rows and columns), uses move_left, and then transposes it back to achieve an up move.
def move_up(grid):
    transposed_grid = [list(row) for row in zip(*grid)]
    new_grid = move_left(transposed_grid)
    return [list(row) for row in zip(*new_grid)]

# This function transposes the grid, uses move_right, and then transposes it back to achieve a down move.
def move_down(grid):
    transposed_grid = [list(row) for row in zip(*grid)]
    new_grid = move_right(transposed_grid)
    return [list(row) for row in zip(*new_grid)]

# This function checks if any cell in the grid has the winning value
def check_win(grid):
    return any(cell == WIN_CONDITION for row in grid for cell in row)

# This function checks if there are no more valid moves left. 
# It first checks if there are any empty cells and then checks if there are any adjacent cells with the same value.
def check_game_over(grid):
    if any(cell == 0 for row in grid for cell in row):
        return False
    for i in range(SIZE):
        for j in range(SIZE):
            if i + 1 < SIZE and grid[i][j] == grid[i + 1][j]:
                return False
            if j + 1 < SIZE and grid[i][j] == grid[i][j + 1]:
                return False
    return True

# This function prints the grid in a readable format.
def print_grid(grid):
    for row in grid:
        print('\t'.join(map(str, row)))
    print()
