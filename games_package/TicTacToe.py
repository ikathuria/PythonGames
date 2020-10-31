"""This is a program to simulate the game of "Tic-Tac-Toe" also known as "Noughts and Crosses" using python.

"""


# REPLAY
def replay():
    """Gives the user the otion to play again."""
    res = input("Do you want to play again? Enter Yes or No: ")
    return res.lower().startswith('y')


# DISPLAY BOARD
def display_board(board):
    """Prints the game board while updating it as the game is progressing.

    Args:
        board: The game board.
    """
    print()
    print(" "+board[7]+" "+"|"+" "+board[8]+" "+"|"+" "+board[9]+" ")
    print("-"+"-"+"-"+"|"+"-"+"-"+"-"+"|"+"-"+"-"+"-")
    print(" "+board[4]+" "+"|"+" "+board[5]+" "+"|"+" "+board[6]+" ")
    print("-"+"-"+"-"+"|"+"-"+"-"+"-"+"|"+"-"+"-"+"-")
    print(" "+board[1]+" "+"|"+" "+board[2]+" "+"|"+" "+board[3]+" ")

# WIN CHECK


def win_check(board, mark):
    """Checks if any player has won the game."""
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # TOP
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # MIDDLE
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # BOTTOM
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # LEFT
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # MIDDLE
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # RIGHT
            # DIAGONAL
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))  # DIAGONAL

# PLAYER INPUT


def marker():
    """Takes input from player 1 for their choice of marker (X or O)."""
    while True:
        try:
            mark = input("Player 1, do you want to be X or O? ")
            mark = mark.lower()
            if mark == 'x':
                return ('X', 'O')
            elif mark == 'o':
                return ('O', 'X')
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Try Again!")

# POSITION


def position_input(board):
    """Takes input from players for their choice of position on the board."""
    position = 0
    while True:
        try:
            position = int(input("Enter position (1-9): "))
            if position in range(1, 10):
                if space_check(board, position):
                    return position
                else:
                    print("Position already filled, choose another space!")
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Try Again!")

# SPACE CHECK


def space_check(board, position):
    """Checks if the position is free or not."""
    return board[position] == ' '


def full_board_check(board):
    """Checks if the all the positions have been filled or not."""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# PLACING THE MARKER


def place_marker(board, marker, POS):
    """Places the marker chosen on the position of choice."""
    board[POS] = marker


if __name__ == "__main__":
    # MAIN GAME
    while True:
        # welcome
        wel = "WELCOME TO TIC-TAC-TOE"
        print('\n', *wel)
        print()

        # GAME DISPLAY
        THE_KEY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        GAME_DISPLAY = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        print("How the position system works:")
        display_board(THE_KEY)

        # GAME START
        PLAY_GAME = input("\nReady player one? Y or N: ")
        GAME_ON = bool(PLAY_GAME.lower()[0] == 'y')

        # TURN
        TURN = "Player 1"

        # MARKERS
        PLAYER1, PLAYER2 = marker()

        # GAME ON
        while GAME_ON:

            wel = "WELCOME TO TIC-TAC-TOE"
            print('\n', *wel)

            if TURN == "Player 1":
                # PLAYER 1 TURN

                display_board(GAME_DISPLAY)
                print("Player 1,", end=" ")
                POS = position_input(GAME_DISPLAY)
                place_marker(GAME_DISPLAY, PLAYER1, POS)

                if win_check(GAME_DISPLAY, PLAYER1):
                    display_board(GAME_DISPLAY)
                    print("\nPlayer 1 is the winner!")
                    GAME_ON = False
                else:
                    if full_board_check(GAME_DISPLAY):
                        display_board(GAME_DISPLAY)
                        print("\nThe game is a draw!")
                        break
                    else:
                        TURN = "Player 2"

            else:
                # PLAYER 2 TURN

                display_board(GAME_DISPLAY)
                print("Player 2,", end=" ")
                POS = position_input(GAME_DISPLAY)
                place_marker(GAME_DISPLAY, PLAYER2, POS)

                if win_check(GAME_DISPLAY, PLAYER2):
                    display_board(GAME_DISPLAY)
                    print("\nPlayer 2 has won!")
                    GAME_ON = False
                else:
                    if full_board_check(GAME_DISPLAY):
                        display_board(GAME_DISPLAY)
                        print("\nThe game is a draw!")
                        break
                    else:
                        TURN = "Player 1"

        if not replay():
            break
