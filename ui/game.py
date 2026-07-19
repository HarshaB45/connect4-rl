from ui.board import Board
from players.player_logic import Player1, Player2, win_condition

player1 = Player1()
player2 = Player2()
 
import random
def run():
    board = Board()
    board.display()

    print('\n')
    print("Player 1's turn:", '\n')
    column = int(input('Enter a number: '))
    player1.get_move(board, column)
    board.display()

    print('\n')
    print("Player 2's turn:", '\n')
    column = int(input('Enter a number: '))
    player2.get_move(board, column)
    board.display()

    print('\n')
    print("Player 1's turn:", '\n')
    column = int(input('Enter a number: '))
    player1.get_move(board, column)
    board.display()

    print('\n')
    print("Player 2's turn:", '\n')
    column = int(input('Enter a number: '))
    player2.get_move(board, column)
    board.display()

    print('\n')
    print("Player 1's turn:", '\n')
    column = int(input('Enter a number: '))
    player1.get_move(board, column)
    board.display()

    print('\n')
    print("Player 2's turn:", '\n')
    column = int(input('Enter a number: '))
    player2.get_move(board, column)
    board.display()

    print('\n')
    print("Player 1's turn:", '\n')
    column = int(input('Enter a number: '))
    player1.get_move(board, column)
    board.display()

    print('\n')
    print("Player 2's turn:", '\n')
    column = int(input('Enter a number: '))
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

    while win_condition(board, 1) == False and win_condition(board, 2) == False:
        print('\n')
        column = random.randint(0, 6)
        player1.get_move(board, column)
        board.display()
        
        if win_condition(board, 1):
            print("Player 1 wins!")
            break
        
        print('\n')
        column = random.randint(0, 6)
        player2.get_move(board, column)
        board.display()
        
        if win_condition(board, 2):
            print("Player 2 wins!")
            break
    


