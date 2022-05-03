import random
import itertools


from typing import List, Tuple, Optional


from . import settings
from .cell import Cell


class Game:
    """ Game Class resposible for holding game state, cells """
    _cell_count = settings.CELL_COUNT

    def __init__(self, *args, **kwargs) -> None:
        self.new_game()

    @property
    def cells(self) -> Tuple[Cell]:
        return tuple(self._cells)

    def surrounding_mines_counter(self, x: int, y: int) -> int:
        return sum([cell.is_mine for cell in self.surrounding_cells(x, y)])

    def surrounding_cells(self, x: int, y: int) -> List[Cell]:
        x_range = range(x-1, x+2)
        y_range = range(y-1, y+2)
        surrounding_cells = []
        for sy, sx in itertools.product(y_range, x_range):
            if not (sy, sx) == (y, x):
                cell = self.get_cell_by_axis(sx, sy)
                if cell:
                    surrounding_cells.append(cell)
        return surrounding_cells

    def new_game(self) -> None:
        self._generate_cells()
        self._set_mines()

    def _generate_cells(self) -> None:
        #if not self._cells:
        self._cells = []
        for y, x in itertools.product(range(settings.GRID_SIZE), range(settings.GRID_SIZE)):
            c = Cell(x, y)
            self._cells.append(c)

    def _set_mines(self) -> None:
        to_be_mines = random.sample(self._cells, settings.MINES_COUNT)
        for cell in to_be_mines:
            cell.is_mine = True

    def get_cell_by_axis(self, x: int, y: int) -> Optional[Cell]:
        if self._is_out_of_bounds(x, y):
            return
        return self._cells[settings.GRID_SIZE * y + x]

    def _is_out_of_bounds(self, x: int, y: int) -> bool:
        return not (x >= 0 and x < settings.GRID_SIZE and y >= 0 and y < settings.GRID_SIZE )
