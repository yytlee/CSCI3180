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

class Spring():
    def __init__(self):
        self._num_chance = 1
        self._healing_power = 100
        self._pos = Pos()


    def set_pos(self, row, column):
        self._pos.set_pos(row, column)

    def get_pos(self):
        return self._pos

    def action_on_soldier(self, soldier):
        self.talk()
        if self._num_chance == 1:
            soldier.recover(self._healing_power)
            self._num_chance -= 1

    def talk(self):
        print('Spring@: You have ' + str(self._num_chance) + ' chance to recover 100 health.\n')

    def display_symbol(self):
        print('@', end = '')