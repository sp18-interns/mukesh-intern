#

#board
# display board
# play game
# handle
# checkwin
# check rows
# check columns
# check daigonals
# check tie
# flip player

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#display_board()
def play_game():

    
    #display initial board
    display_board()

    handle_turn()
#     play_game()
def handle_turn():
    position = input("Choose a position from 1-9:")
    position = int(position) - 1

    board[position] = "X"
    display_board()


play_game()