class Pos():
    def __init__(self):
        self.row = 0
        self.colume = 0

    def setPos(self, row, column):
        self.row = row
        self.column = column
    

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column