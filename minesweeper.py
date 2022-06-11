'''
    >0 nb bombas rodeadas
    0 no bomb
    -1 bomb
    -2 abierto
    -3 flagged

    check nbBombs <= height*width
'''

from multiprocessing.sharedctypes import Value
import numpy as np
import random

width = 5
height = 5
nbBombs = 5
class Tile: 
    def __init__(self):
        self.show = False
        self.isBomb = False
        self.value = 0
    
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

            self.mat[y][x].value = -1
            self.mat[y][x].isBomb = True
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

                    self.mat[i][j].value = n

    def check_input(self, coord):
        if self.check_bomb(x, y):
            return 

    # Returns true if case is a bomb, false if it's not a bomb or if it's marked, later raise exception for not a bomb or marked
    def check_bomb(self, x, y):
        # Check if it's equal to bomb char or number used later
        return True if self.mat[x][y] == -1 else False

    def print_nude(self):
        for row in self.mat:
            for tile in row:
                if tile.value > 0:
                    print(f"{tile.value:.0f}", end=' ')
                elif tile.value == 0:
                    print(f"{tile.value:.0f}", end=' ')
                elif tile.value == -1:
                    print("B", end=' ')
                elif tile.value == -2:
                    print("X", end=' ')
                elif tile.value == -3:
                    print("F", end=' ')
            print()
    
    def print(self):
        for row in self.mat:
            for tile in row:
                if tile.value >= -1:
                    print("■", end=' ')
                elif tile.value == -2:
                    print(f"{tile.value:.0f}", end=' ')
                elif tile.value == -3:
                    print("Ø", end=' ')
            print()


def game(mat, nbBombs):
    bombsRem = nbBombs

    while(bombsRem > 0):
        coord  = input("x,y: ")
        coord = [a for a in coord.split(",")]
        
        valid = True
        for pos in coord:
                try: 
                    int(pos)
                except ValueError:
                    valid = False
                    print(f"{pos} is not an int!")
                    continue

        if valid:
            for i in range(len(coord)):
                coord[i] = int(coord[i])

        print(coord)
        bombsRem = bombsRem-1
    
    print("Game over")

if __name__ == "__main__":
    mat = Matrix(height, width, nbBombs)
    game(mat, nbBombs)