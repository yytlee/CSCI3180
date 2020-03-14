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
from Map import Map
from Soldier import Soldier
from Monster import Monster
from Spring import Spring
import random

class SaveTheTribine():
    def __init__(self):
        self._map = Map()
        self._soldier = Soldier()
        self._spring = Spring()
        self._monsters = [Monster() for i in range(7)]
        self._game_enabled = True

    def initialize(self):
        # We use the integer 1-7 to represent the keys for corresponding caves, and the integer -1 to represent the artifact. 

        self._monsters[0] = Monster(1, random.randint(3, 7) * 10)
        self._monsters[0].set_pos(4, 1)
        self._monsters[0].add_drop_item(2)
        self._monsters[0].add_drop_item(3)
    
        self._monsters[1] = Monster(2, random.randint(3, 7) * 10)
        self._monsters[1].set_pos(3, 3)
        self._monsters[1].add_drop_item(3)
        self._monsters[1].add_drop_item(6)
        self._monsters[1].add_hint(1)
        self._monsters[1].add_hint(5)

        self._monsters[2] = Monster(3, random.randint(3, 7) * 10)
        self._monsters[2].set_pos(5, 3)
        self._monsters[2].add_drop_item(4)
        self._monsters[2].add_hint(1)
        self._monsters[2].add_hint(2)

        self._monsters[3] = Monster(4, random.randint(3, 7) * 10)
        self._monsters[3].set_pos(5, 5)
        self._monsters[3].add_hint(3)
        self._monsters[3].add_hint(6)

        self._monsters[4] = Monster(5, random.randint(3, 7) * 10)
        self._monsters[4].set_pos(1, 4)
        self._monsters[4].add_drop_item(2)
        self._monsters[4].add_drop_item(6)

        self._monsters[5] = Monster(6, random.randint(3, 7) * 10)
        self._monsters[5].set_pos(3, 5)
        self._monsters[5].add_drop_item(4)
        self._monsters[5].add_drop_item(7)
        self._monsters[5].add_hint(2)
        self._monsters[5].add_hint(5)

        self._monsters[6] = Monster(7, random.randint(3, 7) * 10)
        self._monsters[6].set_pos(4, 7)
        self._monsters[6].add_drop_item(-1)
        self._monsters[6].add_hint(6)

        for i in range(7):
            self._map.add_object(self._monsters[i])

        self._soldier.set_pos(1, 1)
        self._soldier.add_key(1)
        self._soldier.add_key(5)

        self._map.add_object(self._soldier)

        self._spring.set_pos(7, 4)

        self._map.add_object(self._spring)

    def start(self):
        print('=> Welcome to the desert!')
        print('=> Now you have to defeat the monsters and find the artifact to save the tribe.')

        while self._game_enabled:
            self._map.display_map()
            self._soldier.display_information()
            
            move = input('\n=> What is the next step? (W = Up, S = Down, A = Left, D = Light.) Input: ').upper()

            pos = self._soldier.get_pos()

            new_row = old_row = pos.get_row()
            new_column = old_column = pos.get_column()

            if move == 'W':
                new_row = old_row - 1
            elif move == 'S':
                new_row = old_row + 1
            elif move == 'A':
                new_column = old_column - 1
            elif move == 'D':
                new_column = old_column + 1
            else:
                print('=> Illegal move!')
                continue

            if self._map.check_move(new_row, new_column):
                occupied_object = self._map.get_occupied_object(new_row, new_column)

                if occupied_object != None:
                    occupied_object.action_on_soldier(self._soldier)
                else:
                    self._soldier.move(new_row, new_column)
                    self._map.update(self._soldier, old_row, old_column, new_row, new_column)
                    print()
            else:
                print('=> Illegal move!')

            if self._soldier.get_health() <= 0:
                print('=> You died.')
                print('=> Game over.\n')
                self._game_enabled = False

            # Check if the soldier has received the artifact. 
            if -1 in self._soldier.get_keys():
                print('=> You found the artifact.')
                print('=> Game over.\n')
                self._game_enabled = False


if __name__ == '__main__':
    game = SaveTheTribine()
    game.initialize()
    game.start()