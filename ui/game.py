from ui.board import Board
from players.player_logic import Player, draw_condition, win_condition

player1 = Player(1)
player2 = Player(2)
 
import random


def prompt_valid_column(board):
    while True:
        try:
            column = int(input('Enter a number: '))
        except ValueError:
            print('Please enter a number from 0 to 6.')
            continue

        if column < 0 or column > 6:
            print('Please enter a number from 0 to 6.')
            continue

        if board.grid[0][column] != 0:
            print('That column is full, please choose another column.')
            continue

        return column


def run():
    board = Board()
    board.display()

    print('\n')
    print("Player 1's turn:", '\n')
    column = prompt_valid_column(board)
    player1.get_move(board, column)
    board.display()

    print('\n')
    print("Player 2's turn:", '\n')
    column = prompt_valid_column(board)
    player2.get_move(board, column)
    board.display()

    print('\n')
    print("Player 1's turn:", '\n')
    column = prompt_valid_column(board)
    player1.get_move(board, column)
    board.display()

    print('\n')
    print("Player 2's turn:", '\n')
    column = prompt_valid_column(board)
    player2.get_move(board, column)
    board.display()

    print('\n')
    print("Player 1's turn:", '\n')
    column = prompt_valid_column(board)
    player1.get_move(board, column)
    board.display()

    print('\n')
    print("Player 2's turn:", '\n')
    column = prompt_valid_column(board)
    player2.get_move(board, column)
    board.display()

    print('\n')
    print("Player 1's turn:", '\n')
    column = prompt_valid_column(board)
    player1.get_move(board, column)
    board.display()

    print('\n')
    print("Player 2's turn:", '\n')
    column = prompt_valid_column(board)
    player2.get_move(board, column)
    board.display()

def bot_run():
    board = Board()
    board.display()
    
    print('\n')
    column = random.randint(0, 6)
    player1.get_move(board, column)
    board.display()
    
    print('\n')
    column = random.randint(0, 6)
    player2.get_move(board, column)
    board.display()

    while win_condition(board, 1) == False and win_condition(board, 2) == False and draw_condition(board) == False:
        print('\n')
        column = player1.algorithm(board)
        player1.get_move(board, column)
        board.display()
        
        if win_condition(board, 1):
            print("Player 1 wins!")
            break
        
        print('\n')
        column = player2.algorithm(board)
        player2.get_move(board, column)
        board.display()
        
        if win_condition(board, 2):
            print("Player 2 wins!")
            break
    
    if draw_condition(board):
        print("It's a draw!")
