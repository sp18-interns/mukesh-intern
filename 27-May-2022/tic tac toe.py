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

#------Global variables---------------

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

    # If game is still going
game_still_going = True

#who won? or tie?
winner = None 

#whos turn is it
current_player = "X"



def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#display_board()
def play_game():

#display initial board
    display_board()
    while game_still_going:


        handle_turn(current_player)


        check_if_game_over()
      # flip to the other player
        flip_player()

    # The game has ended
    if winner =="X" or winnner == "0":
        print(winner +"won.")
    elif winner == None:
        print("Tie.")
#     play_game()
def handle_turn(player):
    position = input("Choose a position from 1-9:")
    position = int(position) - 1

    board[position] = "X"
    display_board()


play_game()

def check_if_game_over():
    
    check_if_win()
    check_if_tie()
