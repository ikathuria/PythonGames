# ---------------------------------------------------------------------------------------
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# DISPLAY BOARD -------------------------------------------------------------------------
def display_board(board):
    print()
    print(" "+board[7]+" "+"|"+" "+board[8]+" "+"|"+" "+board[9]+" ")
    print("-"+"-"+"-"+"|"+"-"+"-"+"-"+"|"+"-"+"-"+"-")
    print(" "+board[4]+" "+"|"+" "+board[5]+" "+"|"+" "+board[6]+" ")
    print("-"+"-"+"-"+"|"+"-"+"-"+"-"+"|"+"-"+"-"+"-")
    print(" "+board[1]+" "+"|"+" "+board[2]+" "+"|"+" "+board[3]+" ")

# WIN CHECK -----------------------------------------------------------------------------
def win_check(board,mark):    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # TOP
            (board[4] == mark and board[5] == mark and board[6] == mark) or # MIDDLE
            (board[1] == mark and board[2] == mark and board[3] == mark) or # BOTTOM
            (board[7] == mark and board[4] == mark and board[1] == mark) or # LEFT
            (board[8] == mark and board[5] == mark and board[2] == mark) or # MIDDLE
            (board[9] == mark and board[6] == mark and board[3] == mark) or # RIGHT
            (board[7] == mark and board[5] == mark and board[3] == mark) or # DIAGONAL
            (board[9] == mark and board[5] == mark and board[1] == mark)) # DIAGONAL

# PLAYER INPUT --------------------------------------------------------------------------
def marker():
    while True:
        try:
            marker = input("Player 1, do you want to be X or O? ")        
            marker = marker.lower()
            if marker == 'x':
                return ('X', 'O')
            elif marker == 'o':
                return ('O', 'X')
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Try Again!")

# SPACE CHECK ---------------------------------------------------------------------------
def space_check(board, position):
        return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# POSITION ------------------------------------------------------------------------------
def position(board):
    position = 0
    while True:
        try:
            position = int(input("Enter position (1-9): "))
            if position in range(1,10):
                if space_check(board, position):
                    return position
                else:
                    print("Position already filled, choose another space!")
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Try Again!")

# PLACING THE MARKER --------------------------------------------------------------------
def place_marker(board, marker, pos):
    board[pos] = marker

# MAIN GAME -----------------------------------------------------------------------------
while True:
    #GAME DISPLAY
    theKey = ['0','1','2','3','4','5','6','7','8','9']
    gameDisplay = ['0',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    print("How the position system works:")
    display_board(theKey)
    
    #GAME START
    play_game = input("Ready player one? Y or N: ")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    #TURN
    turn = "Player 1"
    
    #GMAE ON
    while game_on:
        #markers
        player1, player2 = marker()
        
        if turn == "Player 1":
            # PLAYER 1 TURN
            
            display_board(gameDisplay)
            pos = position(gameDisplay)
            place_marker(gameDisplay, player1, pos)

            if win_check(gameDisplay, player1):
                display_board(gameDisplay)
                print("\nPlayer 1 is the winner!")
                game_on = False
            else:
                if full_board_check(gameDisplay):
                    display_board(gameDisplay)
                    print("\nThe game is a draw!")
                    break
                else:
                    turn = "Player 2"

        else:
            # PLAYER 2 TURN
            
            display_board(gameDisplay)
            pos = position(gameDisplay)
            place_marker(gameDisplay, player2, pos)

            if win_check(gameDisplay, player2):
                display_board(gameDisplay)
                print("\nPlayer 2 has won!")
                game_on = False
            else:
                if full_board_check(gameDisplay):
                    display_board(gameDisplay)
                    print("\nThe game is a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break