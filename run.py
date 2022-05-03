""" Minesweeper Game """

import tkinter


import minesweeper


# Main window configuration
root = tkinter.Tk()
root.configure(bg='black')
root.geometry(f'{minesweeper.settings.WIDTH}x{minesweeper.settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)

top_frame = tkinter.Frame(
    root,
    bg='black',
    width=minesweeper.settings.WIDTH,
    height=minesweeper.utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = tkinter.Frame(
    root,
    bg='black',
    width=minesweeper.utils.width_prct(25),
    height=minesweeper.utils.height_prct(75)
)
left_frame.place(x=0, y=minesweeper.utils.height_prct(25))

center_frame = tkinter.Frame(
    root,
    bg='black',
    width=minesweeper.utils.width_prct(75),
    height=minesweeper.utils.height_prct(75)
)
center_frame.place(
    x=minesweeper.utils.width_prct(25),
    y=minesweeper.utils.height_prct(25)
)

game = minesweeper.Game()
cells = game.cells

for y in range(minesweeper.settings.GRID_SIZE):
    for x in range(minesweeper.settings.GRID_SIZE):
        c = cells[y * minesweeper.settings.GRID_SIZE + x]
        tk_cell = minesweeper.cell.TkCell(c, game)
        tk_cell.create_btn_object(center_frame)
        tk_cell._cell.grid(column=x, row=y)

#minesweeper.cell.Cell.create_cell_count_label(left_frame)
#minesweeper.cell.Cell._cell_count_label.place(x=0, y=0)

game_title = tkinter.Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 36)
)

game_title.place(x=minesweeper.utils.width_prct(25), y=0)

# Start application
root.mainloop()
