from Pos import Pos

class Spring():
    def __init__(self, chance = 1, healing = 100):
        self.numChance = chance
        self.healingPower = healing
        self.pos = Pos()


    def setPos(self, row, column):
        self.pos.setPos(row, column)

    def getPos(self):
        return self.pos

    def actionOnSoldier(self, soldier):
        self.talk()
        if self.numChance == 1:
            soldier.recover(self.healingPower)
            self.numChance -= 1

    def talk(self):
        print('Spring@: You have ' + str(self.numChance) + ' chance to recover 100 health.\n')

    def displaySymbol(self):
        print('@', end = '')