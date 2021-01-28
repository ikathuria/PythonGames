"""The game of Tic Tac Toe (also known as Noughts and Crosses) made using python.

Tic tac toe is a paper-and-pencil game for two players, X and O, who take turns
marking the spaces in a 3×3 grid.  The player who succeeds in placing three of
their marks in a horizontal, vertical, or diagonal row is the winner. If no player
succeeds in achieving such a pattern and the grib has no empty spaces left, there
is a draw.

"""


def replay():
    """Gives the user the otion to play again.

    Returns:
        True if user wants to play again.
        False if user doesn't want to play again.

    """

    while True:
        try:
            play_again = input(
                "\nDo you want to play again? Enter Yes or No: ")

            if not play_again.isdigit():
                if play_again.lower().startswith('y'):
                    return True
                print("Thank you for playing!")
                return False

            raise ValueError

        except ValueError:
            print("Invalid input! Try again!")


def who_is_playing():
    """Gives the user the otion to choose number of players.

    Returns:
        1 if chosen number of players is one.
        2 if chosen number of players is two.

    Raises:
        ValueError: Invalid input! Try Again!

    """

    while True:
        try:
            players = int(input("\nHow many players? 1 or 2: "))

            if players in range(1, 3):
                if players == 1:
                    return 1
                return 2
            print("Choose 1 or 2!")
            raise ValueError

        except ValueError:
            print("Invalid input! Try Again!")


def display_board(board):
    """Prints the game board.

    Args:
        board (list): The game board.

    """

    print()
    print(" "+board[7]+" "+"|"+" "+board[8]+" "+"|"+" "+board[9]+" ")
    print("-"+"-"+"-"+"|"+"-"+"-"+"-"+"|"+"-"+"-"+"-")
    print(" "+board[4]+" "+"|"+" "+board[5]+" "+"|"+" "+board[6]+" ")
    print("-"+"-"+"-"+"|"+"-"+"-"+"-"+"|"+"-"+"-"+"-")
    print(" "+board[1]+" "+"|"+" "+board[2]+" "+"|"+" "+board[3]+" ")


def win_check(board, mark):
    """Checks to see if any player has won the game.

    Args:
        board (list): The game board.
        mark (str): Player's mark (X or O).

    Returns:
        True if any of the win check conditions are satisfied.

    """

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # middle
            # bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # left
            # middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # right
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choosing_marker():
    """Takes input from player 1 for their choice of marker (X or O).

    Returns:
        Tuple of markers where the first element represents player one's marker
        i.e. (player_one_marker, player_two_marker).

    Raises:
        ValueError: Invalid input! Try Again!

    """

    while True:
        try:
            mark = input("\nPlayer 1, do you want to be X or O? ")
            mark = mark.lower()

            if mark == 'x':
                return ('X', 'O')

            if mark == 'o':
                return ('O', 'X')

            raise ValueError

        except ValueError:
            print("Invalid input! Try Again!")


def position_input(board):
    """Takes input from players for their choice of input position on the board.

    Args:
        board (list): The game board where the marker will be placed.

    Raises:
        ValueError: Invalid input! Try Again!

    """

    position = 0
    while True:
        try:
            position = int(input("Enter position (1-9): "))

            if position in range(1, 10):
                if space_check(board, position):
                    return position

                print("Position already filled, choose another space!")

            else:
                raise ValueError

        except ValueError:
            print("Invalid input! Try Again!")


def space_check(board, position):
    """Checks if the position is free or not.

    Args:
        board (list): The current game board.
        position (int): The selected position.

    Returns:
        True if selected position on the board is empty.

    """

    return board[position] == ' '


def full_board_check(board):
    """Checks if the all the positions have been filled or not.

    Args:
        board (list): The current game board.

    Returns:
        True if board is full.
        False if some position is still empty.

    """

    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def place_marker(board, marker, pos):
    """Places the marker chosen on the position of choice.

    Args:
        board (list): The current game board.
        marker (str): Player's marker.
        pos (int): Selected position.

    """

    board[pos] = marker


if __name__ == "__main__":
    PLAY_GAME = input("\nReady to play? Enter Yes or No: ")
    # Game on set to true if player is ready
    GAME_ON = bool(PLAY_GAME.lower()[0] == 'y')

    if not GAME_ON:
        print("Goodbye!")

    while GAME_ON:
        # game start
        NUM_OF_PLAYERS = who_is_playing()
        if NUM_OF_PLAYERS == 1:
            second_player = "Computer"
        else:
            second_player = "Player 2"

        # starting game display
        THE_KEY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        GAME_DISPLAY = ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        print("How the position system works:")
        display_board(THE_KEY)

        TURN = "Player 1"  # Turn set to player 1

        PLAYER1, PLAYER2 = choosing_marker()  # markers set

        # turns
        while TURN in ("Player 1", second_player):
            if TURN == "Player 1":  # player one's turn

                display_board(GAME_DISPLAY)  # display current board game
                print("\nPlayer 1,", end=" ")
                POS = position_input(GAME_DISPLAY)
                place_marker(GAME_DISPLAY, PLAYER1, POS)

                if win_check(GAME_DISPLAY, PLAYER1):
                    display_board(GAME_DISPLAY)
                    # player one wins, game ends
                    print("\nPlayer 1 is the winner!")
                    TURN = "Finish"

                else:
                    if full_board_check(GAME_DISPLAY):
                        display_board(GAME_DISPLAY)
                        print("\nThe game is a draw!")  # game ends in a draw
                        TURN = "Finish"

                    else:
                        TURN = second_player

            elif TURN == "Player 2":  # player two's turn

                display_board(GAME_DISPLAY)  # display current board game
                print("\nPlayer 2,", end=" ")
                POS = position_input(GAME_DISPLAY)
                place_marker(GAME_DISPLAY, PLAYER2, POS)

                if win_check(GAME_DISPLAY, PLAYER2):
                    display_board(GAME_DISPLAY)
                    print("\nPlayer 2 has won!")  # player two wins, game ends
                    TURN = "Finish"

                else:
                    if full_board_check(GAME_DISPLAY):
                        display_board(GAME_DISPLAY)
                        print("\nThe game is a draw!")  # game ends in a draw
                        TURN = "Finish"

                    else:
                        TURN = "Player 1"

            elif TURN == "Computer":  # computer's turn

                display_board(GAME_DISPLAY)  # display current board game
                print("\nComputer,", end=" ")
                POS = position_input(GAME_DISPLAY)
                place_marker(GAME_DISPLAY, PLAYER2, POS)

                if win_check(GAME_DISPLAY, PLAYER2):
                    display_board(GAME_DISPLAY)
                    print("\nComputer has won!")  # computer wins, game ends
                    TURN = "Finish"

                else:
                    if full_board_check(GAME_DISPLAY):
                        display_board(GAME_DISPLAY)
                        print("\nThe game is a draw!")  # game ends in a draw
                        TURN = "Finish"

                    else:
                        TURN = "Player 1"

        # asking the user if they want to play again
        GAME_ON = replay()
