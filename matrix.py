import random 
from tile import Tile

class Matrix:
    def __init__(self, width, height, nbBombs):
        self.tilesUI = []
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
                    if(i > 0 and j < self.width-1 and self.mat[i-1][j+1].isBomb):  
                        n+=1
                    if(i < self.height-1 and j < self.width-1 and self.mat[i+1][j+1].isBomb):  
                        n+=1
                    if(j < self.width-1 and self.mat[i][j+1].isBomb):  
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
