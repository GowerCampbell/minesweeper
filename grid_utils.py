# grid_utils.py
import random

def create_random_grid(rows, cols, mine_probability=0.2):
    """
    Creates a random Minesweeper grid with mines and mine-free spots.
    """
    grid = []
    for _ in range(rows):
        row = ["#" if random.random() < mine_probability else "-" for _ in range(cols)]
        grid.append(row)
    return grid

def count_adjacent_mines(grid, row, col):
    """
    Counts the number of mines adjacent to a specific cell in the grid.
    """
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] == "#":
                count += 1
    return count

def reveal_cell(grid, visible_grid, row, col):
    """
    Reveals a cell in the grid and updates the visible grid.
    """
    if grid[row][col] == "#":
        visible_grid[row][col] = "#"
        return True
    else:
        visible_grid[row][col] = str(count_adjacent_mines(grid, row, col))
        return False

def mark_mines(grid, visible_grid):
    """
    Marks the locations of mines on the visible grid.
    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                visible_grid[row][col] = "#"