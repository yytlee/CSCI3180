"""
Name: XXX
Student ID: XXX
"""

"""Please refer to the specification of Task 1 for more
details about this game.
"""

"""Warning: Apart from completing these member functions (TODO marks), 
Do Not change any other parts of our provided source code. 
"""

"""Tips: Debug the code by inserting `from IPython import embed; embed()'
"""

import random; random.seed(0)

from utils import *
from Board import Board
from Human import Human
from Player import Player
from Computer import Computer

class SixMensMorris():
    def __init__(self):
        self.board = Board()
        self.players = []
        self.num_play = 0 
        
    def next_player(self):
        self.num_play += 1
        return self.players[ 1 - self.num_play % 2 ]

    def opponent(self, player):
        return self.players[ self.num_play % 2 ]

    def check_win(self, player):
        if_win = False
        if self.board.check_win(player, self.opponent(player)):
            print('Congratulation to the winner: {}!'.format( 
                g('Player 1') if player.get_id() == 1 else b('Player 2') 
            ))
            if_win = True
        return if_win

    def start_game(self):
        # Choose the player type for both players
        print('Please choose Player 1:')
        print('1. Human Player')
        print('2. Computer Player')
        x = input('Your choice is: ')
        if x == '1':
            self.players.append(Human(1, self.board))
            print('Player 1 is a human.')
        elif x == '2':
            self.players.append(Computer(1, self.board))
            print('Player 1 is a computer.')

        ### TODO (Choose the type for player 2)

        # Start the game
        self.board.print_board()
        end = False
        while not end:
            player = self.next_player()

            if self.num_play <= 12:
                # Phase 1
                x = player.next_put()
            else:
                # Phase 2
                x = player.next_move()
            self.board.print_board()

            if ### TODO:
                end = True
            else:
                if self.board.form_mill(x, player):
                    print('You form a mill!')
                    
                    ### TODO
                    
                    self.board.print_board()
                
                if ### TODO:
                    end = True

if __name__ == '__main__':
    game = SixMensMorris()
    game.start_game()


