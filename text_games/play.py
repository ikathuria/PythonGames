"""File combining all the games made."""

import os
import time

# my module
import rulebook


def clear_screen():
    """Clears screen using the `os` module."""

    print("\nCLOSING IN 5 SECONDS")
    time.sleep(5)

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
        print(rulebook.rule_book(name_of_game))


while True:
    WEL = "\nWELCOME TO PYTHON GAMES"  # welcome to python games
    print(*WEL, end="\n\n")

    # the game choices
    print("1. BlackJack")
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
        WEL = "\nWELCOME TO BALCKJACK"
        print(*WEL, end="\n\n")

        rules('blackjack')
        os.system("python text_games//blackjack.py")

    # hangman
    elif choice == 2:
        WEL = "\nWELCOME TO HANGMAN"
        print(*WEL, end="\n\n")

        rules('hangman')
        os.system("python text_games//hangman.py")

    # number guessing game
    elif choice == 3:
        WEL = "\nWELCOME TO NUMBER-GUESSING-GAME"
        print(*WEL, end="\n\n")

        rules('number_guessing')
        os.system("python text_games//number_guessing.py")

    # rock paper scissors
    elif choice == 4:
        WEL = "\nWELCOME TO ROCK-PAPER-SCISSORS"
        print(*WEL, end="\n\n")

        rules('rock_paper_scissors')
        os.system("python text_games//rock_paper_scissors.py")

    # nuer tic tac toe
    elif choice == 5:
        WEL = "\nWELCOME TO TIC-TAC-TOE"
        print(*WEL, end="\n\n")

        rules('tic_tac_toe')
        os.system("python text_games//tic_tac_toe.py")

    # war
    elif choice == 6:
        WEL = "\nWELCOME TO WAR"
        print(*WEL, end="\n\n")

        rules('war')
        os.system("python text_games//war.py")

    # exit
    elif choice == 7:
        print("\nThank You for playing!")
        print("Goodbye!")
        break

    # invalid option
    else:
        print("Invalid option! Try again!")

    clear_screen()
