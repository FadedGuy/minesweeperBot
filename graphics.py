'''
    Assumes mat is not empty
    resizable 
    ['text'] to change text value on widget
'''

import tkinter as tk
from tkinter import ttk
from functools import partial
from turtle import update

from matplotlib import widgets

from numpy import tile

class App(tk.Tk):
    def __init__(self, mat):
        super().__init__()
        mat.print_nude()

        tileSize = mat.mat[0][0].size
        wScreen = tileSize*mat.width
        self.title('Minesweeper')
        self.resizable(False, False)
        self.flagMode = False

        content = ttk.Frame(self, padding=(5,5))   
        topFrame = ttk.Frame(content, borderwidth=2, relief="groove", width=wScreen, height=tileSize*2)
        
        bombsLabel = ttk.Label(topFrame, text=f"{mat.nbBombs}", width=6)
        resetButton = ttk.Button(topFrame, text=":D", width=6, command=lambda: print("Reset"))
        flagModeCb = ttk.Checkbutton(topFrame, text="Flag Mode", command=partial(self.toggleFlagMode))

        gameFrame = ttk.Frame(content, borderwidth=2, relief="sunken", width=wScreen, height=tileSize*mat.height)
        for i in range(mat.height):
            r = []
            for j in range(mat.width):
                r.append(ttk.Button(gameFrame, text=mat.mat[i][j].getTextValue(), width=6, command=partial(self.click_box, i, j, mat)))
            mat.tilesUI.append(r)
        self.update_UI(mat)

        content.grid(column=0, row=0)
        topFrame.grid(column=0, row=0, columnspan=2, rowspan=1)
        bombsLabel.grid(column=0, row=0, columnspan=1, rowspan=1)
        resetButton.grid(column=1, row=0, columnspan=1, rowspan=1, sticky="nwes")
        flagModeCb.grid(column=2, row=0, columnspan=1, rowspan=1)

        gameFrame.grid(column=0, row=1, columnspan=1, rowspan=1)

        for i in range(mat.height):
            for j in range(mat.width):
                mat.tilesUI[i][j].grid(column=j, row=i, columnspan=1, rowspan=1)

        
    def update_UI(self, mat):
        for i in range(mat.height):
            for j in range(mat.width):
                tile = mat.mat[i][j]
                if tile.show:
                    mat.tilesUI[i][j]['text'] = tile.getTextValue()
                else:
                    mat.tilesUI[i][j]['text'] = " "

    def click_box(self, i, j, mat):
        mat.mat[i][j].setShow()
        self.update_UI(mat)

    def toggleFlagMode(self):
        self.flagMode = not self.flagMode
        print(self.flagMode)
        
# app = App()
# app.mainloop()