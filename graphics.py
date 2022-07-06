'''
    Assumes mat is not empty
    resizable 
'''

import tkinter as tk
from tkinter import ttk

from numpy import column_stack
class App(tk.Tk):
    def __init__(self, mat):
        super().__init__()

        tileSize = mat.mat[0][0].size
        wScreen = tileSize*mat.width
        self.title('Minesweeper')
        self.resizable(False, False)

        content = ttk.Frame(self, padding=(5,5))   
        topFrame = ttk.Frame(content, borderwidth=2, relief="groove", width=wScreen, height=tileSize*2)
        gameFrame = ttk.Frame(content, borderwidth=2, relief="sunken", width=wScreen, height=tileSize*mat.height)
        tileFrame = []
        
        for i in range(mat.height):
            r = []
            for j in range(mat.width):
                r.append(ttk.Frame(gameFrame, borderwidth=1, relief="solid", width=tileSize, height=tileSize))
            tileFrame.append(r)

        content.grid(column=0, row=0)
        topFrame.grid(column=0, row=0, columnspan=1, rowspan=1)
        gameFrame.grid(column=0, row=1, columnspan=1, rowspan=1)
        for i in range(mat.height):
            for j in range(mat.width):
                tileFrame[i][j].grid(column=i, row=j, columnspan=1, rowspan=1)

# app = App()
# app.mainloop()