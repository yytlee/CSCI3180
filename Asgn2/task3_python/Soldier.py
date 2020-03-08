from Pos import Pos
import random

class Soldier():
    def __init__(self):
        self.health = 100
        self.numElixirs = 2
        self.pos = Pos()
        self.keys = set()

    
    def getHealth(self):
        return self.health

    def loseHealth(self):
        self.health -= 10
        return self.health <= 0

    def recover(self, healingPower):
        ## Soldier's health cannot exceed capacity.
        totalHealth = healingPower + self.health
        self.health = 100 if totalHealth >= 100 else totalHealth

    def getPos(self):
        return self.pos

    def setPos(self, row, column):
        self.pos.setPos(row, column)

    def move(self, row, column):
        self.setPos(row, column)

    def getKeys(self):
        return self.keys

    def addKey(self, key):
        self.keys.add(key)

    def getNumElixirs(self):
        return self.numElixirs

    def addElixir(self):
        self.numElixirs += 1

    def useElixir(self):
        self.recover(random.randint(15, 20))
        self.numElixirs -= 1

    def displayInformation(self):
        print("Health: %d." %(self.health))
        print("Position (row, column): (%d, %d)." %(self.pos.getRow(), self.pos.getColumn()))
        print('Keys: [', end = '')
        print(*self.keys, sep = ', ', end = '].\n')
        print("Elixirs: %d." %(self.numElixirs))

    def displaySymbol(self):
        print('S', end = '')