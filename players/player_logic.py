# separate algorithms for both players

# initial algorithms for player 1 and 2 is to add 1 to a column, will refine with RL later

import random


class Player:
    def __init__(self, player_number):
        self.player_number = player_number

    def get_move(self, board, inputNumber):
        while board.grid[0][inputNumber] != 0:
            inputNumber = int(input('Enter a number: '))
        rowPos = -1
        while board.grid[rowPos][inputNumber] != 0:
            rowPos -= 1

        board.grid[rowPos][inputNumber] = self.player_number
        return board

    def algorithm(self, board):
        valid_columns = [col for col in range(7) if board.grid[0][col] == 0]
        return random.choice(valid_columns)

def win_condition(board, player):
    # Check for horizontal win
    for row in range(6):
        for col in range(4):
            if all(board.grid[row][col + i] == player for i in range(4)):
                return True

    # Check for vertical win
    for row in range(3):
        for col in range(7):
            if all(board.grid[row + i][col] == player for i in range(4)):
                return True

    # Check for diagonal win (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if all(board.grid[row + i][col + i] == player for i in range(4)):
                return True

    # Check for diagonal win (top-right to bottom-left)
    for row in range(3):
        for col in range(3, 7):
            if all(board.grid[row + i][col - i] == player for i in range(4)):
                return True

    return False

def draw_condition(board):
    return all(board.grid[0][col] != 0 for col in range(7))