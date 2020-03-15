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
from Soldier import Soldier
import random

class Task4Soldier(Soldier):
    def __init__(self):
        super(Task4Soldier, self).__init__()
        self._coin = 0
        self._shield = 0

    def get_num_coin(self):
        return self._coin

    def add_coin(self):
        self._coin += 1

    def use_coin(self, n):
        self._coin -= n

    def add_shield(self):
        self._shield += 1

    def lose_health(self):
        h = 0 if self._shield > 2 else (10 - 5 * (self._shield))
        self._health -= h
        return self._health <= 0

    def display_information(self):
        print("Health: %d." %(self._health))
        print("Position (row, column): (%d, %d)." %(self._pos.get_row(), self._pos.get_column()))
        print('Keys: [', end = '')
        print(*self._keys, sep = ', ', end = '].\n')
        print("Elixirs: %d." %(self._num_elixirs))
        print("Defence: %d." %(self._shield))
        print("Coins: %d." %(self._coin))