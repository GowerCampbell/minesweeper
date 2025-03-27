# main.py
from grid_utils import create_random_grid, reveal_cell, mark_mines
from display import print_grid

def play_minesweeper(rows, cols, mine_probability=0.2):
    """
    Playable Minesweeper game.
    """
    grid = create_random_grid(rows, cols, mine_probability)
    visible_grid = [["-" for _ in range(cols)] for _ in range(rows)]
    lives = 3
    game_over = False

    while not game_over:
        print("\nMinesweeper: Will you survive?")
        print(f"\nLives remaining: {lives}")
        print("------------------>")
        print_grid(visible_grid)

        try:
            row = int(input("\nEnter row number: "))
            col = int(input("Enter column number: "))
        except ValueError:
            print("\nInvalid input! Please enter numbers.")
            continue

        if row < 0 or row >= rows or col < 0 or col >= cols:
            print("\nInvalid row or column! Try again.")
            continue

        if reveal_cell(grid, visible_grid, row, col):
            lives -= 1
            print("\nYou hit a mine!")
            if lives == 0:
                print("\nGame Over! You've run out of lives.")
                mark_mines(grid, visible_grid)
                print("\nFinal Grid:")
                print_grid(visible_grid)
                game_over = True
            else:
                print(f"Lives remaining: {lives}")
        else:
            if all(cell != "-" for row in visible_grid for cell in row):
                print("\nCongratulations! You've cleared the grid.")
                mark_mines(grid, visible_grid)
                print("Final Grid:")
                print_grid(visible_grid)
                game_over = True

if __name__ == "__main__":
    rows, cols = 5, 5
    mine_probability = 0.2
    play_minesweeper(rows, cols, mine_probability)