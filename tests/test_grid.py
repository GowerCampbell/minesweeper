# tests/test_grid.py
import unittest
from grid_utils import create_random_grid, count_adjacent_mines

class TestGridUtils(unittest.TestCase):
    def test_create_random_grid(self):
        grid = create_random_grid(3, 3, 1.0)  # 100% mine probability
        self.assertTrue(all(cell == "#" for row in grid for cell in row))

    def test_count_adjacent_mines(self):
        grid = [["#", "-", "#"], ["-", "-", "-"], ["#", "-", "-"]]
        self.assertEqual(count_adjacent_mines(grid, 1, 1), 3)

if __name__ == "__main__":
    unittest.main()