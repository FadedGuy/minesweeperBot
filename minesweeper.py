'''
    >0 nb bombs around
    0 no bombs around
    -1 bomb

    check nbBombs <= height*width
'''

import numpy as np
import random

width = 4
height = 4
nbBombs = 1
class Tile: 
    def __init__(self):
        self.show = False
        self.isBomb = False
        self.isTag = False
        self.value = 0
    
    def setValue(self, value):
        if value == -1:
            self.isBomb = True
        self.value = value

    def toggleFlag(self):
        self.isTag = not self.isTag
    
    def toggleShow(self):
        self.show = not self.show

    def IsBomb(self):
        return self.isBomb

class Matrix:
    def __init__(self, width, height, nbBombs):
        self.width = width
        self.height = height
        self.nbBombs = nbBombs

        self.mat = []
        for i in range(height):
            r = []
            for j in range(width):
                r.append(Tile())
            self.mat.append(r)

        self.setup_matrix()

    def setup_matrix(self):
        for i in range(self.nbBombs):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            while(self.mat[y][x].isBomb):
                x = random.randint(0, self.width-1)
                y = random.randint(0, self.height-1)

            self.mat[y][x].setValue(-1)
        self.calculate_nearby()

    def calculate_nearby(self):
        for i in range(self.height):
            for j in range(self.width):
                n = 0

                if self.mat[i][j].isBomb is False:
                    if(i > 0 and self.mat[i-1][j].isBomb):  
                        n+=1
                    if(i < self.height-1 and self.mat[i+1][j].isBomb):  
                        n+=1
                    if(i > 0 and j > 0 and self.mat[i-1][j-1].isBomb):  
                        n+=1
                    if(i < self.height-1 and j > 0 and self.mat[i+1][j-1].isBomb):  
                        n+=1
                    if(i > 0 and j < width-1 and self.mat[i-1][j+1].isBomb):  
                        n+=1
                    if(i < self.height-1 and j < width-1 and self.mat[i+1][j+1].isBomb):  
                        n+=1
                    if(j < width-1 and self.mat[i][j+1].isBomb):  
                        n+=1
                    if(j > 0 and self.mat[i][j-1].isBomb):  
                        n+=1

                    self.mat[i][j].setValue(n)

    def print_nude(self):
        for row in self.mat:
            for tile in row:
                if tile.isTag or tile.isBomb:
                    if tile.isTag:
                        print("F", end=' ')
                    else:
                        print("B", end=' ')
                else:
                    print(f"{tile.value:.0f}", end=' ')
            print()
    
    def print(self):
        for row in self.mat:
            for tile in row:
                if tile.isTag:
                    print("Ø", end=' ')
                elif tile.show:
                    print(f"{tile.value:.0f}", end=' ')
                else:
                    print("■", end=' ')
            print()

# Returns None if input coords are not valid, otherwise returns the coords as [x,y]
def get_coords(w, h):
    coord  = input("x,y: ")
    coord = [a for a in coord.split(",")]

    if len(coord) != 2:
        print("Incorrent number of coordinates")
        return None

    for pos in coord:
            try: 
                int(pos)
            except ValueError:
                print(f"{pos} is not an int!")
                return None
    
    coord[0],coord[1] = int(coord[0]), int(coord[1])

    if coord[0] < 0 or coord[0] >= w or coord[1] < 0 or coord[1] >= h:
        print("Invalid coordinates")
        return None

    return [int(coord[0]), int(coord[1])]

def game(mat):
    movesRem = (mat.width*mat.height) - mat.nbBombs
    gameOver = False
    # mat.print_nude()

    while(not gameOver and movesRem > 0):
        mat.print()

        coord = None
        while coord is None:
            coord = get_coords(mat.height, mat.width)

        # Check, bomb, flag, error
        tile = mat.mat[coord[0]][coord[1]]
        if tile.value >= 0 and not tile.isTag and not tile.show:
            tile.toggleShow()
            movesRem = movesRem - 1
        elif tile.isBomb:
            tile.toggleShow()
            gameOver = True

    mat.print()
    if not gameOver:
        print("WIN")
    else:
        print("LOSE")

if __name__ == "__main__":
    mat = Matrix(height, width, nbBombs)
    game(mat)