''' Tic Tac Toe Game
'''
import time
import random
from IPython.display import clear_output

class TicTacToe():
    '''
    Tic Tac Toe board class
    '''
    def __init__(self):
        ''' Define Tic Tac Toe board
        '''
        self.board = dict()
        for i in range(1, 10):
            self.board[i] = ' '
    def display_board(self):
        ''' Display tic tac toe board
        '''
        clear_output()
        print("\t|\t|\t\n    {}   |   {}   |    {}    \n\t|\t|\t\n--------+-------+--------".format(self.board[1], self.board[2], self.board[3]))
        print("\t|\t|\t\n    {}   |   {}   |    {}    \n\t|\t|\t\n--------+-------+--------".format(self.board[4], self.board[5], self.board[6]))
        print("\t|\t|\t\n    {}   |   {}   |    {}    \n\t|\t|\t".format(self.board[7], self.board[8], self.board[9]))
        print('_'*100)
    def player_marker(self):
        ''' assign player and computer with 'X' and 'O'
        '''
        while True:
            player1 = input("select you marker- either 'X' or 'O' \n").upper()
            if player1 == 'X':
                player2 = 'O'
                return (player1, player2)
            elif player1 == 'O':
                player2 = 'X'
                return (player1, player2)
    def enter_position(self, player1, player2):
        ''' assign values to board position
        '''
        if player1 != player2:
            position = int(input(' Player {} enter available position from 1-9\n'.format(player1)))
            while(self.board[position] == 'X' or self.board[position] == 'O'):
                position = int(input(' Player {}, {} position already occupied please enter another\n'.format(player1, position)))
            self.board[position] = player
        else:
            positions = [i for i in self.board.keys() if self.board[i] == ' ']
            position = random.choice(positions)
            self.board[position] = player2
        self.display_board()
    def game_win(self):
        ''' Check for game completionn and return winner
        '''
        if self.board[1] == self.board[2] == self.board[3] != ' ':
            return self.board[1]
        elif self.board[4] == self.board[5] == self.board[6] != ' ':
            return self.board[4]
        elif self.board[7] == self.board[8] == self.board[9] != ' ':
            return self.board[7]
        elif self.board[1] == self.board[4] == self.board[7] != ' ':
            return self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] != ' ':
            return self.board[2]
        elif self.board[3] == self.board[6] == self.board[9] != ' ':
            return self.board[3]
        elif self.board[1] == self.board[5] == self.board[9] != ' ':
            return self.board[1]
        elif self.board[3] == self.board[5] == self.board[7] != ' ':
            return self.board[3]
        else:
            return None
    def check_board(self):
        '''Return True if values left in board else false
        '''
        return ' ' in self.board.values()
if __name__ == '__main__':

    game = TicTacToe()
    player, computer = game.player_marker()
    game.display_board()
    if player == 'X':
        print("You will go first")
        TURN = player
    else:
        print("computer will go first")
        TURN = computer
    while True:
        if TURN == player:
            game.enter_position(player, computer)
            TURN = computer
        else:
            game.enter_position(computer, computer)
            TURN = player
        winner = game.game_win()
        if winner is not None:
            print('{} Wins!!!!!'.format(winner))
            break
        else:
            empty = game.check_board()
            if empty is not True:
                win = game.game_win()
                if win is None:
                    print('Match draws - No one Wins')
                    break
    time.sleep(5)
    clear_output()
