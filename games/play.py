"""File combining all the games made.

"""

import os
import time

rule_book = {'blackjack': """Blackjack is a comparing card game between one or more players
and a dealer, where each player in turn competes against the dealer. Player and dealer are dealt
2 cards each. One of the dealer's card remains hidden until the player's turn is over. A hand's
value is the sum of the card values. The value of cards two through ten are 2-10. Face cards
(Jack, Queen, and King) are all worth 10. Aces can be worth 1 or 11 depending on the player's
need. Players are allowed to draw additional cards ("hit") to improve their hands till
they reach a value of 21 or they can end their turn ("stand").
    
The conditions for winning and losing are as follows:
    
    1. If the player exceeds a sum of 21 ("busts"), the player loses, even if the dealer also exceeds 21.

    2. If the dealer exceeds 21 ("busts") and the player does not, the player wins.

    3. If the player attains a final sum higher than the dealer and does not bust, the player wins.

    4. If both dealer and player receive a blackjack (a value of 21) or any other hands with the same sum
    called a "push", no one wins.""",

             'hangman': """test""",

             'number_guessing': """This is a number guessing game where the system chooses a random
number that the user has to attempt to guess. It has 3 levels of difficulty.

1. Piece of Cake: The simplest mode, with a 10 digit range and a maximum of 5 guesses.
2. Let's Rock: The in-between mode, with a 50 digit range and a maximum of 5 guesses.
3. Damn I'm Good: The hardcore mode, with a 100 digit range and a maximum of 3 guesses.""",

             'rock_paper_scissors': """Rock Paper Scissors is a hand game usually played between 2 people, in which each
player simultaneously forming one of the three shapes which are rock, paper and scissors.
There are two outcomes for the game, either a draw or one of the players winning.

Rock beats scissors, scissors beats paper and paper beats rock.
There is a one player option where the user gets to play against the computer and a two player
option when the user wants to play with a friend.""",

             'tic_tac_toe': """Tic tac toe is a paper-and-pencil game for two players, X and O, who take turns
marking the spaces in a 3×3 grid. The player who succeeds in placing three of their
marks in a horizontal, vertical, or diagonal row is the winner. If no player succeeds
in achieving such a pattern and the grib has no empty spaces left, there is a draw.

There is a one player option where the user gets to play against the computer and a
two player option when the user wants to play with a friend.""",

             'war': """War is a simple card game, typically played by two players using a standard
playing card deck. The objective of the game is to win all of the cards. The deck is
divided evenly among the players, giving each a down stack. In unison, each player
reveals the top card of their deck — this is called a "battle" — and the player with
the higher card takes both of the cards played and moves them to their stack. If the
two cards played are of equal value, then there is a "war". Both players place the
next card of their pile face down and then another card face-up. The owner of the
higher face-up card wins the war.

This program is not user interactive. The game is set to advance in a loop till an
outcome is reached."""}


def clear_screen():
    """Clears screen using the `os` module."""

    time.sleep(1.5)

    if os.name == 'posix':  # for mac and linux
        _ = os.system('clear')

    else:  # for windows
        _ = os.system('cls')


def rules(name_of_game):
    """Shows the rulebook for the game selected by user.

    Args:
        name_of_game (str): Name of the game for which rules are needed.

    """

    need_help = input(
        "Do you want to see the rules for the game? Enter Yes or No: ")

    if need_help.lower().startswith('y'):
        print()
        print(rule_book[name_of_game])


while True:
    WEL = 'WELCOME TO PYTHON GAMES'
    print('\n', *WEL)
    print("\n1. BlackJack")
    print("2. Hangman")
    print("3. Number Guessing Game")
    print("4. Rock Paper Scissors")
    print("5. Tic Tac Toe")
    print("6. War")
    print("7. Exit")

    while True:
        try:
            choice = int(input("\nWhich game do you want to play? (1-7): "))
            if choice in range(1, 8):
                break
            raise ValueError

        except ValueError:
            print("Invalid input! Try again!")

    # blackjack
    if choice == 1:
        rules('blackjack')
        os.system("python games//blackjack.py")

    # hangman
    elif choice == 2:
        rules('hangman')
        os.system("python games//hangman.py")

    # number guessing game
    elif choice == 3:
        rules('number_guessing')
        os.system("python games//number_guessing.py")

    # rock paper scissors
    elif choice == 4:
        rules('rock_paper_scissors')
        os.system("python games//rock_paper_scissors.py")

    # nuer tic tac toe
    elif choice == 5:
        rules('tic_tac_toe')
        os.system("python games//tic_tac_toe.py")

    # war
    elif choice == 6:
        rules('war')
        os.system("python games//war.py")

        print("Closing in 5 seconds")
        for i in range(1, 6):
            print(i)
            time.sleep(1)

    # exit
    elif choice == 7:
        print("\nThank You for playing!")
        print("Goodbye!")
        break

    # invalid option
    else:
        print("Invalid option! Try again!")

    clear_screen()
