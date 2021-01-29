"""The game of Tic Tac Toe (also known as Noughts and Crosses) made using python.

Tic tac toe is a paper-and-pencil game for two players, X and O, who take turns
marking the spaces in a 3×3 grid.  The player who succeeds in placing three of
their marks in a horizontal, vertical, or diagonal row is the winner. If no player
succeeds in achieving such a pattern and the grib has no empty spaces left, there
is a draw.

There is a one player option where the user gets to play against the computer
and a two player option when the user wants to play with a friend.

"""

import math
import random


class Player:
    """This is a class for the players.

    Attributes:
        marker (str): The marker of the player, either `X` or `O`.

    """

    def __init__(self, marker):
        """Constructor for Player class."""

        self.marker = marker  # x or o


class HumanPlayer(Player):
    """This is a class for the human player.

    Attributes:
        marker (str): The marker of the player, either `X` or `O`.

    """

    def get_move(self, game):
        """Method to get the player's move.

        Attributes:
            game (TicTacToe): An object of the TicTacToe class.

        Returns:
            position (int): The selected space on the game board.

        """

        valid_square = False
        position = None
        while not valid_square:
            square = input(self.marker + '\'s turn. Choose your spot (0-8): ')
            try:
                position = int(square)
                if position not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid input! Try Again!")

        return position


class GeniusComputerPlayer(Player):
    """This is a class for the minimax algorithm player.

    Attributes:
        marker (str): The marker of the player, either `X` or `O`.

    """

    def get_move(self, game):
        """Method to get the player's move.

        Attributes:
            game (TicTacToe): An object of the TicTacToe class.

        Returns:
            position (int): The selected space on the game board.

        """

        if len(game.available_moves()) == 9:
            position = random.choice(game.available_moves())
        else:
            position = self.minimax(game, self.marker)['position']

        return position

    def minimax(self, state, player):
        """Method to get the player's move.

        Attributes:
            state (TicTacToe): An object of the TicTacToe class.
            player (str): The player's marker, either `X` or `O`.

        Returns:
            best (dict): A dictionary of the best possible move.

        """

        max_player = self.marker
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            if other_player == max_player:
                score = 1 * (state.num_empty_spaces() + 1)
            else:
                score = -1 * (state.num_empty_spaces() + 1)
            return {'position': None, 'score': score}

        elif not state.empty_spaces():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update the dictionary if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score

            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
