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
