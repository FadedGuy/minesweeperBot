import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, mat):
        super().__init__()

        self.geometry("240x100")
        self.title('Minesweeper')
        self.resizable(0, 0)

        content = ttk.Frame(self)
        frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
        namelbl = ttk.Label(content, text="Name")

        content.grid(column=0, row=0)
        frame.grid(column=0, row=0, columnspan=3, rowspan=2)
        namelbl.grid(column=3, row=0, columnspan=2)

# app = App()
# app.mainloop()