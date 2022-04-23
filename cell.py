import tkinter
import random


import settings

class Cell:

    _all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self._cell = None
        self._x = x
        self._y = y

        # Append the object to the Cell.all list
        # i dont argee with this aproach
        # i think it's batter to have Game class responsible for tracking cells
        Cell._all.append(self)

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

    def left_click_action(self, event):
        print(event)
        print('Mine: ', self.is_mine)
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def show_mine(self):
        """ Changes cell color to red """
        self._cell.configure(bg='red')

    def show_cell(self):
        self._cell.configure(text=self.surrounding_mines_counter)

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
        print(event)
        print('right clicked')

    @staticmethod
    def randomize_mines():
        to_be_mines = random.sample(Cell._all, settings.MINES_COUNT)
        for cell in to_be_mines:
            cell.is_mine = True

    def __repr__(self):
        return f'Cell({self._x}, {self._y})'
