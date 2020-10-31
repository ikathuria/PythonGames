"""This is a program to simulate the game of "Rock-Paper-Scissors" using python.

This program uses the 'random' module when the player wants to play against the computer.
"""
import random

options = ['Rock', 'Paper', 'Scissors']


# PLAYERS
def players():
    """Gives the user the otion to choose number of players."""

    while True:
        try:
            players = int(input("\nHow many players? 1 or 2: "))
            if isinstance(players, int):
                if players == 1:
                    return 1
                elif players == 2:
                    return 2
                else:
                    print("Choose 1 or 2!")
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Try Again!")


def option():
    """Takes input of user's choice (rock, paper or scissors)."""

    while True:
        try:
            choice = input(
                "\nWhat would you like to choose? Rock, Paper or Scissors: ")
            choice = choice.lower()
            if choice.startswith('r'):
                return options[0]
            elif choice.startswith('p'):
                return options[1]
            elif choice.startswith('s'):
                return options[2]
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Try Again!")


# WIN CHECK
def win_check(player1_choice, player2_choice):
    """Checks to see which player has won."""

    # tie
    if player1_choice == player2_choice:
        print("Tie!")

    # rock
    elif player1_choice == "Rock":

        if player2_choice == "Paper":
            print("Player 2 wins!", player2_choice, "covers", player1_choice)

        else:
            print("Player 1 wins!", player1_choice, "smashes", player2_choice)

    # paper
    elif player1_choice == "Paper":

        if player2_choice == "Scissors":
            print("Player 2 wins!", player2_choice, "cut", player1_choice)

        else:
            print("Player 1 wins!", player1_choice, "covers", player2_choice)

    # scissors
    elif player1_choice == "Scissors":

        if player2_choice == "Rock":
            print("Player 2 wins!", player2_choice, "smashes", player1_choice)

        else:
            print("Player 1 wins!", player1_choice, "cut", player2_choice)

    else:
        pass



if __name__ == "__main__":
    # GAME ON
    GAME_ON = True

    while GAME_ON:

        # welcome
        wel = "WELCOME TO ROCK-PAPER-SCISSORS"
        print('\n', *wel)
        print()

        # game start
        choice = players()

        if choice == 1:
            print("You will be playing against the computer!")

            player1_choice = option()
            computer_choice = options[random.randint(0, 2)]
            player2_choice = "not playing"

            win_check(player1_choice, computer_choice)

        elif choice == 2:
            player1_choice = option()
            player2_choice = option()
            computer_choice = "not playing"

            win_check(player1_choice, player2_choice)

        else:
            pass

        while True:
            try:
                replay = input("\nDo you want to play again? Enter Yes or No: ")
                if isinstance(replay, str):
                    if replay.lower().startswith('y'):
                        GAME_ON = True
                        break
                    elif replay.lower().startswith('n'):
                        print("\nThank you for playing!")
                        GAME_ON = False
                        break
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input! Try again!")
