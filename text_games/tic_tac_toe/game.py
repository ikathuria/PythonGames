"""The game of Tic Tac Toe (also known as Noughts and Crosses) made using python.

Tic tac toe is a paper-and-pencil game for two players, X and O, who take turns
marking the spaces in a 3×3 grid.  The player who succeeds in placing three of
their marks in a horizontal, vertical, or diagonal row is the winner. If no player
succeeds in achieving such a pattern and the grib has no empty spaces left, there
is a draw.

There is a one player option where the user gets to play against the computer
and a two player option when the user wants to play with a friend.

This program uses the minmax algorithm to implement the one player mode.

"""

from time import sleep
from player import HumanPlayer, GeniusComputerPlayer


class TicTacToe:
    """This is a class for the game.

    Attributes:
        board (list): The game board, initially filled with empty spaces.
        current_winner (str): Initially set to None. Changed to X or O accordingly.

    """

    def __init__(self):
        """Constructor for TicTacToe class."""

        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        """Prints the game board."""

        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """Prints the format of the game board with the numbers."""

        # 0 1 2
        # 3 4 5
        # 6 7 8
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        print()
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print()

    def available_moves(self):
        """Returns a list of all available moves."""

        return [i for i, space in enumerate(self.board) if space == ' ']

    def empty_spaces(self):
        """Returns True if there is an empty space available on the board."""

        return ' ' in self.board

    def num_empty_spaces(self):
        """Returns the number of empty spaces."""

        return self.board.count(' ')

    def make_move(self, square, marker):
        """Places marker on the position chosen."""

        if self.board[square] == ' ':
            self.board[square] = marker
            if self.winner(square, marker):
                self.current_winner = marker
            return True
        return False

    def winner(self, square, marker):
        """Checks if any winning conditions are satisfied."""

        # rows
        row_index = square // 3
        row = self.board[row_index*3:(row_index+1)*3]

        if all([space == marker for space in row]):
            return True

        # columns
        column_index = square % 3
        column = [self.board[column_index + i*3] for i in range(3)]
        if all([space == marker for space in column]):
            return True

        # diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([space == marker for space in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([space == marker for space in diagonal2]):
                return True

        # if no winner
        return False


def play(game, x_player, o_player, time=0.5, print_game=True):
    """Function that contains the main gameplay.

    Attributes:
        game (TicTacToe): An object of the TicTacToe class.
        x_player (Player): An object of the Player class.
        o_player (Player): An object of the Player class.
        time (int): How many seconds to wait before switching to other player, default set to 0.5.
        print_game (bool): If True, all moves are printed. Default is set to True.

    """

    if print_game:
        game.print_board_nums()

    marker = 'X'
    while game.empty_spaces():
        if marker == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, marker):
            if print_game:
                print(marker + f" makes a move to square {square}")
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(marker + ' WINS!')
                return marker

            marker = 'O' if marker == 'X' else 'X'

        sleep(time)

    if print_game:
        print("It's a TIE.")


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


if __name__ == '__main__':
    PLAY_GAME = input("\nReady to play? Enter Yes or No: ")
    # Game on set to true if player is ready
    GAME_ON = bool(PLAY_GAME.lower()[0] == 'y')

    if not GAME_ON:
        print("Goodbye!")

    while GAME_ON:
        first_player = HumanPlayer('X')

        NUM_OF_PLAYERS = who_is_playing()
        if NUM_OF_PLAYERS == 1:
            second_player = GeniusComputerPlayer('O')
        else:
            second_player = HumanPlayer('O')

        t = TicTacToe()
        t.board = [' ' for _ in range(9)]
        t.current_winner = None

        play(t, first_player, second_player)

        # asking the user if they want to play again
        GAME_ON = replay()
