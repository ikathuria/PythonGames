"""The game of Rock Paper Scissors made using python.

Rock Paper Scissors is a hand game usually played between 2 people, in
which each player simultaneously forming one of the three shapes which are
rock, paper and scissors. There are two outcomes for the game, either a draw
or one of the players winning.

Rock beats scissors, scissors beats paper and paper beats rock.

There is a one player option where the user gets to play against the computer
and a two player option when the user wants to play with a friend.

This program uses the `random` module for the one player mode.

"""

import random


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


options = ['Rock', 'Paper', 'Scissors']


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


def option():
    """Takes input of user's choice of rock, paper or scissors.

    Returns:
        0th index from the list of options if user chooses rock.
        1st index from the list of options if user chooses paper.
        2nd index from the list of options if user chooses scissors.

    Raises:
        ValueError: Invalid input! Try Again!

    """

    while True:
        try:
            choice = input(
                "\nWhat would you like to choose? Rock, Paper or Scissors: ")
            choice = choice.lower()

            if choice.startswith('r'):  # user chooses rock
                return options[0]

            if choice.startswith('p'):  # user chooses paper
                return options[1]

            if choice.startswith('s'):  # user chooses scissors
                return options[2]

            raise ValueError

        except ValueError:
            print("Invalid input! Try Again!")


def win_check(first_choice, second_choice, playing):
    """Checks to see which player has won and prints win or tie statement.

    Args:
        first_choice (str): First player's choice.
        second_choice (str): Second player's choice.
        playing (int): The number of players.

    """

    if playing == 1:  # one player
        player_one_wins = "You win"
        player_two_wins = "Computer wins"
    else:  # two players
        player_one_wins = "Player 1 wins"
        player_two_wins = "Player 2 wins"

    # tie
    if first_choice == second_choice:
        print("Tie!")

    # rock
    elif first_choice == "Rock":

        if second_choice == "Paper":
            print(f"{player_two_wins} {second_choice} covers {first_choice}")

        else:
            print(f"{player_one_wins} {first_choice} smashes {second_choice}")

    # paper
    elif first_choice == "Paper":

        if second_choice == "Scissors":
            print(f"{player_two_wins} {second_choice} cuts {first_choice}")

        else:
            print(f"{player_one_wins} {first_choice} covers {second_choice}")

    # scissors
    elif first_choice == "Scissors":

        if second_choice == "Rock":
            print(f"{player_two_wins} {second_choice} smashes {first_choice}")

        else:
            print(f"{player_one_wins} {first_choice} cuts {second_choice}")


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
            print("You will be playing against the computer!")

            PLAYER_ONE_CHOICE = option()
            COMPUTER_CHOICE = options[random.randint(0, 2)]
            PLAYER_TWO_CHOICE = "not playing"

            win_check(PLAYER_ONE_CHOICE, COMPUTER_CHOICE, NUM_OF_PLAYERS)

        elif NUM_OF_PLAYERS == 2:
            PLAYER_ONE_CHOICE = option()
            PLAYER_TWO_CHOICE = option()
            COMPUTER_CHOICE = "not playing"

            win_check(PLAYER_ONE_CHOICE, PLAYER_TWO_CHOICE, NUM_OF_PLAYERS)

        # asking the user if they want to play again
        GAME_ON = replay()
