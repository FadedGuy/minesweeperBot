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
    
    def setShow(self):
        self.show = True

    def IsBomb(self):
        return self.isBomb

    def setSize(self, size):
        self.size = size

    def getTextValue(self):
        if self.isTag:
            return "Ø"
        elif self.isBomb:
            return "B"
        else:
            return f"{self.value}"