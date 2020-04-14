import random

random.seed(0) # don't touch!

# you are not allowed to modify Player class!
class Player:
    due = 200
    income = 0
    tax_rate = 0.2
    handling_fee_rate = 0
    prison_rounds = 2

    def __init__(self, name):
        self.name = name
        self.money = 100000
        self.position = 0
        self.num_rounds_in_jail = 0

    def updateAsset(self):
        self.money += Player.income

    def payDue(self):
        self.money += Player.income * (1 - Player.tax_rate)
        self.money -= Player.due * (1 + Player.handling_fee_rate)

    def printAsset(self):
        print("Player %s's money: %d" % (self.name, self.money))

    def putToJail(self):
        self.num_rounds_in_jail = Player.prison_rounds

    def move(self, step):
        if self.num_rounds_in_jail > 0:
            self.num_rounds_in_jail -= 1
        else:
            self.position = (self.position + step) % 36



class Bank:
    def __init__(self):
        pass

    def print(self):
        print("Bank ", end='')

    def stepOn(self):

        # ...
        Player.income = 2000
        Player.tax_rate = 0
        Player.due = 0

        cur_player.payDue()
        print("You received $2000 from the Bank!")

        return

class Jail:
    def __init__(self):
        pass

    def print(self):
        print("Jail ", end='')

    def stepOn(self):

        # ...
        jail = 2
        while(True):
            response = input("Pay $1000 to reduce the prison round to 1? [y/n]\n")
            if response == "y" and cur_player.money < 1100:
                print("You do not have enough money to reduce the prison round!")
                break
            elif response == "y":
                jail = 1
                Player.due = 1000
                Player.handling_fee_rate = 0.1
                Player.income = 0.0
                cur_player.payDue()
                break
            elif response == "n":
                break

        Player.prison_rounds = jail
        
        cur_player.putToJail()


class Land:
    land_price = 1000
    upgrade_fee = [1000, 2000, 5000]
    toll = [500, 1000, 1500, 3000]
    tax_rate = [0.1, 0.15, 0.2, 0.25]

    def __init__(self):
        self.owner = None
        self.level = 0

    def print(self):
        if self.owner is None:
            print("Land ", end='')
        else:
            print("%s:Lv%d" % (self.owner.name, self.level), end="")
    
    def buyLand(self):

        # ...
        if cur_player.money < 1100:
            print("You do not have enough money to buy the land")
            return

        self.owner = cur_player
        Player.due = Land.land_price
        Player.handling_fee_rate = 0.1
        Player.income = 0.0

        cur_player.payDue()
    
    def upgradeLand(self):
        
        # ...
        fee = Land.upgrade_fee[self.level]
        
        Player.due = fee
        Player.handling_fee_rate = 0.1
        Player.income = 0.0

        if cur_player.money < (fee * (1 + Player.handling_fee_rate)):
            print("You do not have enough money to upgrade the land!")
            return
        self.level += 1

        cur_player.payDue()
    
    def chargeToll(self):
        
        # ...
        fee = Land.toll[self.level]
        Player.due = fee
        Player.handling_fee_rate = 0.0
        Player.income = 0.0

        if cur_player.money < fee:
            Player.due = cur_player.money

        cur_player.payDue()

        # ...
        Player.due = 0.0
        Player.income = fee
        Player.tax_rate = Land.tax_rate[self.level]

        self.owner.payDue()

    def stepOn(self):

        # ... 
        if self.owner == None:
            while True:
                response = input("Pay $1000 to buy the land? [y/n]\n")
                if response == "y":
                    self.buyLand()
                    break
                elif response == "n":
                    break
        elif self.owner != cur_player:
            fee = Land.toll[self.level]
            print("You need to pay player " + self.owner.name + " $" + str(fee))
            self.chargeToll()
        elif self.owner == cur_player and self.level != 3:
            fee = Land.upgrade_fee[self.level]
            while True:
                response = input("Pay $" + str(fee) + " to upgrade the land? [y/n]\n")
                if response == "y":
                    self.upgradeLand()
                    break
                elif response == "n":
                    break
        return



players = [Player("A"), Player("B")]
cur_player = players[0]
num_players = len(players)
cur_player_idx = 0
cur_player = players[cur_player_idx]
num_dices = 1
cur_round = 0

game_board = [
    Bank(), Land(), Land(), Land(), Land(), Land(), Land(), Land(), Land(), Jail(),
    Land(), Land(), Land(), Land(), Land(), Land(), Land(), Land(),
    Jail(), Land(), Land(), Land(), Land(), Land(), Land(), Land(), Land(), Jail(),
    Land(), Land(), Land(), Land(), Land(), Land(), Land(), Land()
]
game_board_size = len(game_board)


def printCellPrefix(position):
    occupying = []
    for player in players:
        if player.position == position and player.money > 0:
            occupying.append(player.name)
    print(" " * (num_players - len(occupying)) + "".join(occupying), end='')
    if len(occupying) > 0:
        print("|", end='')
    else:
        print(" ", end='')


def printGameBoard():
    print("-" * (10 * (num_players + 6)))
    for i in range(10):
        printCellPrefix(i)
        game_board[i].print()
    print("\n")
    for i in range(8):
        printCellPrefix(game_board_size - i - 1)
        game_board[-i - 1].print()
        print(" " * (8 * (num_players + 6)), end="")
        printCellPrefix(i + 10)
        game_board[i + 10].print()
        print("\n")
    for i in range(10):
        printCellPrefix(27 - i)
        game_board[27 - i].print()
    print("")
    print("-" * (10 * (num_players + 6)))


def terminationCheck():

    # ...
    for player in players:
        if player.money == 0:
            return False

    return True


def throwDice():
    step = 0
    for i in range(num_dices):
        step += random.randint(1, 6)
    return step


def main():
    global cur_player
    global num_dices
    global cur_round
    global cur_player_idx

    while terminationCheck():
        if cur_player.num_rounds_in_jail == 0:
            printGameBoard()
            for player in players:
                player.printAsset()

    # ...
        Player.due = 200
        Player.tax_rate = 0.0
        Player.income = 0.0
        cur_player.payDue()

        if cur_player.num_rounds_in_jail > 0:
            cur_player.move(0)
            cur_round += 1
            cur_player_idx = cur_round % 2
            cur_player = players[cur_player_idx]
            next

        print("Player " + cur_player.name + "'s turn.")
        while True:
            response = input("Pay $500 to throw two dice? [y/n]\n")
            if response == "n":
                num_dices = 1
                break
            elif response == "y" and cur_player.money < 525:
                print("You do not have enough money to throw two dice!")
                num_dices = 1
                break
            elif response == "y":
                num_dices = 2
                Player.due = 500
                Player.handling_fee_rate = 0.05
                Player.income = 0.0
                cur_player.payDue()
                break
        
        step = throwDice()
        print("Points of dice: " + str(step))
        cur_player.move(step)
        printGameBoard()
        game_board[cur_player.position].stepOn()
        if cur_player.money < 0:
            cur_player.money = 0

        cur_round += 1
        cur_player_idx = cur_round % 2
        cur_player = players[cur_player_idx]

    print("Game over! winner: " + cur_player.name + ".")
    


if __name__ == '__main__':
    main()
