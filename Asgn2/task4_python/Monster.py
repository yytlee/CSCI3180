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

class Monster():
    def __init__(self, monster_ID = 0, health_capacity = 30):
        self._monster_ID = monster_ID
        self._health_capacity = health_capacity
        self._health = health_capacity
        self._pos = Pos()
        self._drop_item_list = []
        self._hint_list = []

    def add_drop_item(self, key):
        self._drop_item_list.append(key)


    def add_hint(self, monster_ID):
        self._hint_list.append(monster_ID)

    def get_monster_ID(self):
        return self._monster_ID

    def get_pos(self):
        return self._pos

    def set_pos(self, row, column):
        self._pos.set_pos(row, column)

    def get_health_capacity(self):
        return self._health_capacity

    def get_health(self):
        return self._health

    def lose_health(self):
        self._health -= 10
        return self._health <= 0

    def recover(self, healing_power):
        self._health = healing_power

    def action_on_soldier(self, soldier):
        if self._health <= 0:
            self.talk('You had defeated me.\n')
        else:
            if self.require_key(soldier.get_keys()):
                self.fight(soldier)
            else:
                self.display_hints()
        

    def require_key(self, keys):
        return self._monster_ID in keys

    def display_hints(self):
        self.talk("Defeat Monster %s first.\n" %(self._hint_list))

    def fight(self, soldier):
        fight_enabled = True

        while fight_enabled:
            print("       | Monster%d | Soldier |" %(self._monster_ID))
            print("Health | %8d | %7d |\n" %(self._health, soldier.get_health()))

            choice = input('=> What is the next step? (1 = Attack, 2 = Escape, 3 = Use Elixir.) Input: ')

            if choice == '1':
                if self.lose_health():
                    print("=> You defeated Monster%d.\n" %(self._monster_ID))
                    self.drop_items(soldier)
                    fight_enabled = False
                else:
                    if soldier.lose_health():
                        self.recover(self._health_capacity)
                        fight_enabled = False

            elif choice == '2':
                self.recover(self._health_capacity)
                fight_enabled = False
            elif choice == '3':
                if soldier.get_num_elixirs() == 0:
                    print('=> You have run out of elixirs.\n')
                else:
                    soldier.use_elixir()
            else:
                print('=> Illegal choice!\n')

    def drop_items(self, soldier):
        for item in self._drop_item_list:
            soldier.add_key(item)

    def talk(self, text):
        print("Monster%d: %s" %(self._monster_ID, text))

    def display_symbol(self):
        print("M", end = '')