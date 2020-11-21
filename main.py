"""Giving the user the option to play the games in text or gui versions."""

import os
import time


def clear_screen():
    """Clears screen using the `os` module."""

    time.sleep(1)

    if os.name == 'posix':  # for mac and linux
        _ = os.system('clear')

    else:  # for windows
        _ = os.system('cls')


while True:
    WEL = "\nWELCOME TO PYTHON GAMES"  # welcome to python games
    print(*WEL, end="\n\n")

    # the game choices
    print("1. Text Games")
    print("2. Gui Games")
    print("3. Exit")

    while True:
        try:
            choice = int(input("\nWhich format would you like to play the game in? (1-3): "))
            if choice in range(1, 4):
                break
            raise ValueError

        except ValueError:
            print("Invalid input! Try again!")
        
    if choice == 1:
        os.system("python text_games//play.py")
    
    elif choice == 2:
        os.system("python ui_games//gui_games.py")
    
    elif choice == 3:
        print("Goodbye!")
        break

    clear_screen()
