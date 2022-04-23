import tkinter


class Cell:

    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self._cell = None

    def create_btn_object(self, location):
        btn = tkinter.Button(
            location,
            text='Text'
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self._cell = btn

    def left_click_action(self, event):
        print(event)
        print('left clicked')

    def right_click_action(self, event):
        print(event)
        print('right clicked')
