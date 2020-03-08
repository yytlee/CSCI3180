from Pos import Pos
from Map import Map
from Task4Soldier import Soldier, Task4Soldier
from Task4Monster import Monster
from Spring import Spring
from Task4Merchant import Merchant
import random

class SaveTheTribine():
    def __init__(self):
        self.map = Map()
        self.soldier = Task4Soldier()
        self.spring = Spring()
        self.monsters = [Monster(0, 0) for i in range(7)]
        self.merchant = Merchant(1, 2)
        self.gameEnabled = True

    def initialize(self):
        # We use the integer 1-7 to represent the keys for corresponding caves, and the integer -1 to represent the artifact. 

        self.monsters[0] = Monster(1, random.randint(3, 7) * 10)
        self.monsters[0].setPos(4, 1)
        self.monsters[0].addDropItem(2)
        self.monsters[0].addDropItem(3)
    
        self.monsters[1] = Monster(2, random.randint(3, 7) * 10)
        self.monsters[1].setPos(3, 3)
        self.monsters[1].addDropItem(3)
        self.monsters[1].addDropItem(6)
        self.monsters[1].addHint(1)
        self.monsters[1].addHint(5)

        self.monsters[2] = Monster(3, random.randint(3, 7) * 10)
        self.monsters[2].setPos(5, 3)
        self.monsters[2].addDropItem(4)
        self.monsters[2].addHint(1)
        self.monsters[2].addHint(2)

        self.monsters[3] = Monster(4, random.randint(3, 7) * 10)
        self.monsters[3].setPos(5, 5)
        self.monsters[3].addHint(3)
        self.monsters[3].addHint(6)

        self.monsters[4] = Monster(5, random.randint(3, 7) * 10)
        self.monsters[4].setPos(1, 4)
        self.monsters[4].addDropItem(2)
        self.monsters[4].addDropItem(6)

        self.monsters[5] = Monster(6, random.randint(3, 7) * 10)
        self.monsters[5].setPos(3, 5)
        self.monsters[5].addDropItem(4)
        self.monsters[5].addDropItem(7)
        self.monsters[5].addHint(2)
        self.monsters[5].addHint(5)

        self.monsters[6] = Monster(7, random.randint(3, 7) * 10)
        self.monsters[6].setPos(4, 7)
        self.monsters[6].addDropItem(-1)
        self.monsters[6].addHint(6)

        for i in range(7):
            self.map.addObject(self.monsters[i])

        self.soldier.setPos(1, 1)
        self.soldier.addKey(1)
        self.soldier.addKey(5)

        self.map.addObject(self.soldier)

        self.spring.setPos(7, 4)

        self.map.addObject(self.spring)

        self.merchant.setPos(7, 7)

        self.map.addObject(self.merchant)


    def start(self):
        print('=> Welcome to the desert!')
        print('=> Now you have to defeat the monsters and find the artifact to save the tribe.')

        while self.gameEnabled:
            self.map.displayMap()
            self.soldier.displayInformation()
            
            move = input('\n=> What is the next step? (W = Up, S = Down, A = Left, D = Light.) Input: ').upper()

            pos = self.soldier.getPos()

            newRow = oldRow = pos.getRow()
            newColumn = oldColumn = pos.getColumn()

            if move == 'W':
                newRow = oldRow - 1
            elif move == 'S':
                newRow = oldRow + 1
            elif move == 'A':
                newColumn = oldColumn - 1
            elif move == 'D':
                newColumn = oldColumn + 1
            else:
                print('=> Illegal move!')
                continue

            if self.map.checkMove(newRow, newColumn):
                occupiedObject = self.map.getOccupiedObject(newRow, newColumn)

                if occupiedObject != None:
                    occupiedObject.actionOnSoldier(self.soldier)
                else:
                    self.soldier.move(newRow, newColumn)
                    self.map.update(self.soldier, oldRow, oldColumn, newRow, newColumn)
                    print()
            else:
                print('=> Illegal move!')

            if self.soldier.getHealth() <= 0:
                print('=> You died.')
                print('=> Game over.\n')
                self.gameEnabled = False

            # Check if the soldier has received the artifact. 
            if -1 in self.soldier.getKeys():
                print('=> You found the artifact.')
                print('=> Game over.\n')
                self.gameEnabled = False


if __name__ == '__main__':
    game = SaveTheTribine()
    game.initialize()
    game.start()