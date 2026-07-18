from ui.board import Board
from players.player_logic import Player1, Player2

player1 = Player1()
player2 = Player2()

def run():
    board = Board()
    board.display()

    print('\n', "Player 1's turn:", '\n')
    player1.get_move(board)
    board.display()

    print('\n', "Player 2's turn:", '\n')
    player2.get_move(board)
    board.display()


