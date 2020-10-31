import os
import time
import BlackJack
import Hangman
import NumberGuessing
import RockPaperScissors
import TicTacToe
import War


def clearScreen():
    time.sleep(1.5)

    # for mac and linux
    if os.name == 'posix':
        _ = os.system('clear')

    # for windows platfrom
    else:
        _ = os.system('cls')


def rules(nameOfGame):

    needHelp = input("Do you want to see the rules for the game: ")
    if needHelp.lower().startswith('y'):
        print(nameOfGame.__doc__)


while (1):
    wel = 'WELCOME TO PYTHON GAMES'
    print('\n', *wel)
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
            else:
                raise ValueError

        except ValueError:
            print("Invalid input! Try again!")

    # blackjack
    if choice == 1:
        rules(BlackJack)
        os.system("python games_package//BlackJack.py")

    # hangman
    elif choice == 2:
        rules(Hangman)
        os.system("python games_package//Hangman.py")

    # number guessing game
    elif choice == 3:
        rules(NumberGuessing)
        os.system("python games_package//NumberGuessing.py")

    # rock paper scissors
    elif choice == 4:
        rules(RockPaperScissors)
        os.system("python games_package//RockPaperScissors.py")

    # nuer tic tac toe
    elif choice == 5:
        rules(TicTacToe)
        os.system("python games_package//TicTacToe.py")

    # war
    elif choice == 6:
        rules(War)

        print("Starting in 10 seconds")
        for i in range(1, 11):
            print(i)
            time.sleep(1)

        os.system("python games_package//War.py")

        print("Closing in 10 seconds")
        for i in range(1, 11):
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

    clearScreen()
