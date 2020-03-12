from Pos import Pos

class Monster():
    def __init__(self, monsterID = 0, healthCapacity = 30):
        self.monsterID = monsterID
        self.healthCapacity = healthCapacity
        self.health = healthCapacity
        self.pos = Pos()
        self.dropItemList = []
        self.hintList = []

    def addDropItem(self, key):
        self.dropItemList.append(key)


    def addHint(self, monsterID):
        self.hintList.append(monsterID)

    def getMonsterID(self):
        return self.monsterID

    def getPos(self):
        return self.pos

    def setPos(self, row, column):
        self.pos.setPos(row, column)

    def getHealthCapacity(self):
        return self.healthCapacity

    def getHealth(self):
        return self.health

    def loseHealth(self):
        self.health -= 10
        return self.health <= 0

    def recover(self, healingPower):
        self.health = healingPower

    def actionOnSoldier(self, soldier):
        if self.health <= 0:
            self.talk('You had defeated me.\n')
        else:
            if self.requireKey(soldier.getKeys()):
                self.fight(soldier)
            else:
                self.displayHints()
        

    def requireKey(self, keys):
        return self.monsterID in keys

    def displayHints(self):
        self.talk("Defeat Monster %s first.\n" %(self.hintList))

    def fight(self, soldier):
        fightEnabled = True

        while fightEnabled:
            print("       | Monster%d | Soldier |" %(self.monsterID))
            print("Health | %8d | %7d |\n" %(self.health, soldier.getHealth()))

            choice = input('=> What is the next step? (1 = Attack, 2 = Escape, 3 = Use Elixir.) Input: ')

            if choice == '1':
                if self.loseHealth():
                    print("=> You defeated Monster%d.\n" %(self.monsterID))
                    self.dropItems(soldier)
                    fightEnabled = False
                else:
                    if soldier.loseHealth():
                        self.recover(self.healthCapacity)
                        fightEnabled = False

            elif choice == '2':
                self.recover(self.healthCapacity)
                fightEnabled = False
            elif choice == '3':
                if soldier.getNumElixirs() == 0:
                    print('=> You have run out of elixirs.\n')
                else:
                    soldier.useElixir()
            else:
                print('=> Illegal choice!\n')

    def dropItems(self, soldier):
        for item in self.dropItemList:
            soldier.addKey(item)

    def talk(self, text):
        print("Monster%d: %s" %(self.monsterID, text))

    def displaySymbol(self):
        print("M", end = '')