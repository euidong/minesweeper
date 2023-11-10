import tkinter as tk
from model import Board

TITLE = "Minesweeper"
BTN_WIDTH = 30
BTN_HEIGHT = 30
BORDER_SIZE = 2
OUTTER_PADDING_SIZE = 10
BACKGROUND_COLOR = "#DCDCDC"


class App(tk.Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        master.title(TITLE)
        self.board = Board()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
