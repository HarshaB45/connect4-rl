# separate algorithms for both players

# initial algorithms for player 1 and 2 is to add 1 to a column, will refine with RL later

import random
from ui.board import Board

board = Board()

# this
class Player1:
    def __init__(self):
        pass
    
    def get_move(self, board, inputNumber):
        rowPos = -1
        while board.grid[rowPos][inputNumber] != 0:
            rowPos -= 1

        board.grid[rowPos][inputNumber] = 1
        return board
    
class Player2:
    def __init__(self):
        pass

    def get_move(self, board, inputNumber):
        rowPos = -1
        while board.grid[rowPos][inputNumber] != 0:
            rowPos -= 1

        board.grid[rowPos][inputNumber] = 2
        return board