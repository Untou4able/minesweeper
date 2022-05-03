""" Game Class related tests """
import unittest


import minesweeper


class TestGameClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.game = minesweeper.Game()

    def test_game_exists(self) -> None:
        self.assertIsNotNone(self.game)

    def test_game_has_cells(self) -> None:
        self.assertTrue(self.game.cells)

    def test_game_has_mines(self) -> None:
        mines = [c for c in self.game.cells if c.is_mine]
        self.assertTrue(mines)

    def test_geme_returns_cell_by_axis(self) -> None:
        c = self.game.get_cell_by_axis(2, 3)
        self.assertTrue(c._x == 2 and c._y == 3)

    def test_game_out_of_bounds_x(self) -> None:
        c = self.game.get_cell_by_axis(-1, 3)
        self.assertIsNone(c)

    def test_game_out_of_bounds_y(self) -> None:
        c = self.game.get_cell_by_axis(2, minesweeper.settings.GRID_SIZE+1)
        self.assertIsNone(c)

    def test_game_surrounding_cells_count_corner(self) -> None:
        sourroungind_cells = self.game.surrounding_cells(0, 0)
        self.assertEqual(len(sourroungind_cells), 3)

    def test_game_surrounding_cells_count_middle(self) -> None:
        sourroungind_cells = self.game.surrounding_cells(1, 0)
        self.assertEqual(len(sourroungind_cells), 5)

    def test_game_surrounding_cells_count_center(self) -> None:
        sourroungind_cells = self.game.surrounding_cells(1, 1)
        self.assertEqual(len(sourroungind_cells), 8)
