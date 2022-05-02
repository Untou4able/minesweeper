import random


from typing import Tuple


from . import settings
from .cell import Cell


class Game:
    """ Game Class resposible for holding game state, cells """
    _cell_count = settings.CELL_COUNT

    def __init__(self, *args, **kwargs) -> None:
        self._cells = []
        self.new_game()

    @property
    def cells(self) -> Tuple[Cell]:
        return tuple(self._cells)

    def new_game(self) -> None:
        self._generate_cells()
        self._set_mines()

    def _generate_cells(self) -> None:
        if not self._cells:
            for x in range(settings.GRID_SIZE):
                for y in range(settings.GRID_SIZE):
                    c = Cell(x, y)
                    self._cells.append(c)

    def _set_mines(self):
        to_be_mines = random.sample(self._cells, settings.MINES_COUNT)
        for cell in to_be_mines:
            cell.is_mine = True
