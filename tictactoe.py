#-----------Global Variables------------#
#Game board
board = ['-','-','-',
        '-','-','-',
        '-','-','-']

#if game is still going
game_still_going = True

#who won? or tie
winner = None

#current player
current_player = 'X'

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def play_game():

    #diaplay initial board
    display_board()

    while game_still_going:
        
        #while the game is still going
        handle_turn(current_player)

        #check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()
    
    #the game has ended
    if winner =='X' or winner =='O':
        print(winner + ' Won.')
    elif winner==None:
        print('Tie.')

#handle the single turn of the player
def handle_turn(player):

    print(player +"'s turn.")
    #position of the x's and 0's
    
    position = input('choose a postion from 1-9: ')

    valid = True
    while valid:
        
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('Choose a position from 1-9: ') 
        
        position = int(position)-1

        if board[position]=='-':
            valid = False
        else:
            print("You can't go there, Go again.")

        #display_board()

    board[position]= player

    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    #global variables
    global winner
    
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    #global variable
    global game_still_going
    #check if the rows have all the same value
    row_1 = board[0] == board[1] == board[2] !='-'
    row_2 = board[3] == board[4] == board[5] !='-'
    row_3 = board[6] == board[7] == board[8] !='-'
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
    global game_still_going
    #check if the rows have all the same value
    column_1 = board[0] == board[3] == board[6] !='-'
    column_2 = board[1] == board[4] == board[7] !='-'
    column_3 = board[2] == board[5] == board[8] !='-'
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

def check_diagonal():
    global game_still_going
    #check if the rows have all the same value
    diagonal_1 = board[0] == board[4] == board[8] !='-'
    diagonal_2 = board[2] == board[4] == board[6] !='-'
    if diagonal_1 or diagonal_2 :
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None

def check_if_tie():
    #we need global variable here as well
    global game_still_going
    #giving the condition for the Tie
    if '-' not in board:
        game_still_going = False
    return

def flip_player():
    # we need global variables here
    global current_player
    # if the current player was x then change it to O
    if current_player =='X':
        current_player ='O'
    #if the current player was O then change it to X
    elif current_player =='O':
        current_player ='X'
    return

play_game()