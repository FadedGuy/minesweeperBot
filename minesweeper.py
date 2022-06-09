'''
    >0 nb bombas rodeadas
    0 no bomb
    -1 bomb
    -2 abierto
    -3 flagged

    check nbBombs <= height*width
'''

import numpy as np
import random

height = 4
width = 4
nbBombs = 5

class Matrix:
    def __init__(self, width, height, nbBombs):
        self.width = width
        self.height = height
        self.nbBombs = nbBombs
        self.setup_matrix()

    def setup_matrix(self):
        self.mat = np.zeros((height, width))

        for i in range(self.nbBombs):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)        
            while(self.mat[x][y] == -1):
                x = random.randint(0, self.width-1)
                y = random.randint(0, self.height-1)

            self.mat[x][y] = -1

        self.calculate_nearby()

    def calculate_nearby(self):
        for i in range(self.height):
            for j in range(self.width):
                n = 0

                if self.mat[i][j] != -1:
                    if(i > 0 and self.mat[i-1][j] == -1):  
                        n+=1
                    if(i < self.height-1 and self.mat[i+1][j] == -1):  
                        n+=1
                    if(i > 0 and j > 0 and self.mat[i-1][j-1] == -1):  
                        n+=1
                    if(i < self.height-1 and j > 0 and self.mat[i+1][j-1] == -1):  
                        n+=1
                    if(i > 0 and j < width-1 and self.mat[i-1][j+1] == -1):  
                        n+=1
                    if(i < self.height-1 and j < width-1 and self.mat[i+1][j+1] == -1):  
                        n+=1
                    if(j < width-1 and self.mat[i][j+1] == -1):  
                        n+=1
                    if(j > 0 and self.mat[i][j-1] == -1):  
                        n+=1

                    self.mat[i][j] = n

    # Returns true if case is a bomb, false if it's not a bomb or if it's marked, later raise exception for not a bomb or marked
    def check_bomb(self, x, y):
        # Check if it's equal to bomb char or number used later
        return True if self.mat[x][y] == -1 else False

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.mat[i][j] > 0:
                    print(f"{self.mat[i][j]:.0f}", end=' ')
                elif self.mat[i][j] == 0:
                    print(f"{self.mat[i][j]:.0f}", end=' ')
                elif self.mat[i][j] == -1:
                    print("B", end=' ')
                elif self.mat[i][j] == -2:
                    print("X", end=' ')
                elif self.mat[i][j] == -3:
                    print("F", end=' ')
                
            print()

if __name__ == "__main__":
    mat = Matrix(height, width, nbBombs)
    mat.print()