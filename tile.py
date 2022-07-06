class Tile: 
    def __init__(self):
        self.show = False
        self.isBomb = False
        self.isTag = False
        self.size = 50
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

    def setSize(self, size):
        self.size = size