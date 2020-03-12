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
from Pos import Pos

class Merchant():
    def __init__(self, elixirPrice, shieldPrice):

        # TODO: Initialization.
        self.elixirPrice = elixirPrice
        self.shieldPrice = shieldPrice
        self.pos = Pos()

    def actionOnSoldier(self, soldier):
        self.talk('Do you want to buy something? (1. Elixir, 2. Shield) Input: ')

        # TODO: Main logic.
        choice = input()

        if choice == '1':
            if soldier.getNumCoin() >= self.elixirPrice:
                soldier.useCoin(self.elixirPrice)
                soldier.addElixir()
                print("You have %d coin(s) left.", soldier.getNumCoin())
            else:
                self.talk("Poor guy, you don't have enough coins.")
        elif choice == '2':
            if soldier.getNumCoin() >= self.shieldPrice:
                soldier.useCoin(self.shieldPrice)
                soldier.addShield()
                print("You have %d coin(s) left.", soldier.getNumCoin())
            else:
                self.talk("Poor guy, you don't have enough coins.")
        else:
            print('=> Illegal move!\n')

    def talk(self, text):
        print('Merchant$: ' + text, end = '')

    # TODO: Other functions.

    def getPos(self):
        return self.pos

    def setPos(self, row, column):
        self.pos.setPos(row, column)

    def displaySymbol(self):
        print('$', end = '')