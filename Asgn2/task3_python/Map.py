# /*
#  * CSCI3180 Principles of Programming Languages
#  *
#  * --- Declaration ---
#  *
#  * I declare that the assignment here submitted is original except for source
#  * material explicitly acknowledged. I also acknowledge that I am aware of
#  * University policy and regulations on honesty in academic work, and of the
#  * disciplinary guidelines and procedures applicable to breaches of such policy
#  * and regulations, as contained in the website
#  * http://www.cuhk.edu.hk/policy/academichonesty/
#  *
#  * Assignment 2
#  * Name : Lee Tsz Yan
#  * Student ID : 1155110177
#  * Email Addr : tylee8@cse.cuhk.edu.hk
#  */
from Cell import Cell
from Pos import Pos

class Map():
    def __init__(self):
        self.cells = [[Cell() for i in range(7)] for j in range(7)]


    def addObject(self, object):
        pos = object.getPos()
        if pos != None:
            self.cells[pos.getRow() - 1][pos.getColumn() - 1].setOccupiedObject(object)

    # Print the game map in console.
    def displayMap(self):
        print('   | 1 | 2 | 3 | 4 | 5 | 6 | 7 |')
        print('--------------------------------')
        for i in range(7):
            print(" %d |" %(i + 1), end = '')
            for j in range(7):
                occupiedObject = self.cells[i][j].getOccupiedObject()
                if occupiedObject != None:
                    print(' ', end = '')
                    occupiedObject.displaySymbol()
                    print(' |', end = '')
                else:
                    print('   |', end = '')
            print('')
            print('--------------------------------')
        print('')


    def getOccupiedObject(self, row, column):
        return self.cells[row - 1][column - 1].getOccupiedObject()

    def checkMove(self, row, column):
        return ((row >= 1 and row <= 7) and (column >= 1 and column <= 7))

    def update(self, soldier, oldRow, oldColumn, newRow, newColumn):
        self.cells[oldRow - 1][oldColumn - 1].setOccupiedObject(None)
        self.cells[newRow - 1][newColumn - 1].setOccupiedObject(soldier)