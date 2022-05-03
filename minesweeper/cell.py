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

    def __repr__(self):
        return f'Cell({self._x}, {self._y})'

class TkCell:

    def __init__(self, game_cell, game):
        self._game_cell = game_cell
        self._game = game

    def create_btn_object(self, location):
        btn = tkinter.Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self._cell = btn

    #@staticmethod
    #def create_cell_count_label(location):
    #    label = tkinter.Label(
    #        location,
    #        width=12,
    #        height=4,
    #        font=("", 24),
    #        text=f'Cells Left:{settings.CELL_COUNT}'
    #    )
    #    Cell._cell_count_label = label

    def left_click_action(self, event):
        if self._game_cell._is_marked:
            return
        if self._game_cell.is_mine:
            self.show_mine()
        else:
            if self._game.surrounding_mines_counter(self._game_cell._x, self._game_cell._y) == 0:
                for cell in self._game.surrounding_cells(self._game_cell._x, self._game_cell._y):
                    cell.show_cell()
            self.show_cell()
            if self._game._cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'You\'ve won', 'Game over', 0)
                sys.exit()
        #self._cell.unbind_all()

    def show_mine(self):
        """ Changes cell color to red """
        self._cell.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You\'ve lost', 'Game over', 0)
        sys.exit()

    def show_cell(self):
        if not self._game_cell._is_open:
            self._game._cell_count -= 1
            self._cell.configure(text=self._game.surrounding_mines_counter(self._game_cell._x, self._game_cell._y))
            #Cell._cell_count_label.configure(text=f'Cells Left:{self._game._cell_count}')
        self._game_cell._is_open = True

    def right_click_action(self, event):
        if self._game_cell._is_open:
            return
        if not self._game_cell._is_marked:
            self._cell.configure(bg='orange')
            self._game_cell._is_marked = True
        else:
            self._cell.configure(bg='SystemButtonFace')
            self._game_cell._is_marked = False
