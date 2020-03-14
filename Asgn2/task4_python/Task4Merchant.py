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
    def __init__(self, elixir_price, shield_price):

        # TODO: Initialization.
        self._elixir_price = elixir_price
        self._shield_price = shield_price
        self._pos = Pos()

    def action_on_soldier(self, soldier):
        self.talk('Do you want to buy something? (1. Elixir, 2. Shield) Input: ')

        # TODO: Main logic.
        choice = input()

        if choice == '1':
            if soldier.get_num_coin() >= self._elixir_price:
                soldier.use_coin(self._elixir_price)
                soldier.add_elixir()
                print("You have %d coin(s) left.", soldier.get_num_coin())
            else:
                self.talk("Poor guy, you don't have enough coins.")
                print()
        elif choice == '2':
            if soldier.get_num_coin() >= self._shield_price:
                soldier.use_coin(self._shield_price)
                soldier.add_shield()
                print("You have %d coin(s) left.", soldier.get_num_coin())
            else:
                self.talk("Poor guy, you don't have enough coins.")
                print()
        else:
            print('=> Illegal move!\n')

    def talk(self, text):
        print('Merchant$: ' + text, end = '')

    # TODO: Other functions.

    def get_pos(self):
        return self._pos

    def set_pos(self, row, column):
        self._pos.set_pos(row, column)

    def display_symbol(self):
        print('$', end = '')