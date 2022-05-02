import ctypes
import sys
import tkinter


from . import settings

class Cell:

    _cell_count_label = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self._cell = None
        self._is_marked = False
        self._x = x
        self._y = y
        self._is_open = False

    def create_btn_object(self, location):
        """
        It's shouldn't be a thing: game object creates specific button
        of specific UI framework. UI mixed up with logic is bad
        """
        btn = tkinter.Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self._cell = btn

    @staticmethod
    def create_cell_count_label(location):
        label = tkinter.Label(
            location,
            width=12,
            height=4,
            font=("", 24),
            text=f'Cells Left:{settings.CELL_COUNT}'
        )
        Cell._cell_count_label = label

    def left_click_action(self, event):
        if self._is_marked:
            return
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_mines_counter == 0:
                for cell in self.surrounding_cells:
                    cell.show_cell()
            self.show_cell()
            if Cell._cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'You\'ve won', 'Game over', 0)
                sys.exit()
        #self._cell.unbind_all()

    def show_mine(self):
        """ Changes cell color to red """
        self._cell.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You\'ve lost', 'Game over', 0)
        sys.exit()

    def show_cell(self):
        if not self._is_open:
            Cell._cell_count -= 1
            self._cell.configure(text=self.surrounding_mines_counter)
            Cell._cell_count_label.configure(text=f'Cells Left:{Cell._cell_count}')
        self._is_open = True

    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self._x - 1, self._y - 1),
            self.get_cell_by_axis(self._x - 1, self._y),
            self.get_cell_by_axis(self._x - 1, self._y + 1),
            self.get_cell_by_axis(self._x, self._y - 1),
            self.get_cell_by_axis(self._x + 1, self._y - 1),
            self.get_cell_by_axis(self._x + 1, self._y),
            self.get_cell_by_axis(self._x + 1, self._y + 1),
            self.get_cell_by_axis(self._x, self._y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_mines_counter(self):
        counter = 0
        for cell in self.surrounding_cells:
            counter += cell.is_mine
        return counter

    def get_cell_by_axis(self, x, y):
        """ Bad implementation by iterating over _all list """
        for cell in Cell._all:
            if cell._x == x and cell._y == y:
                return cell

    def right_click_action(self, event):
        if self._is_open:
            return
        if not self._is_marked:
            self._cell.configure(bg='orange')
            self._is_marked = True
        else:
            self._cell.configure(bg='SystemButtonFace')
            self._is_marked = False

    def __repr__(self):
        return f'Cell({self._x}, {self._y})'
