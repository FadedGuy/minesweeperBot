'''
    >0 nb bombs around
    0 no bombs around
    -1 bomb

    check nbBombs <= height*width
'''
from matrix import Matrix
from graphics import App

# Globals used for init
width = 5
height = 5
nbBombs = 3

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
    
    coord[1], coord[0] = int(coord[0]), int(coord[1])

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
            tile.setShow()
            movesRem = movesRem - 1
        elif tile.isBomb:
            tile.setShow()
            gameOver = True

    mat.print()
    if not gameOver:
        print("WIN")
    else:
        print("LOSE")

if __name__ == "__main__":
    mat = Matrix(width, height, nbBombs)
    # game(mat)

    app = App(mat)
    app.mainloop()