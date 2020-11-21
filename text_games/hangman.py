"""The game of hangman made using python.

Hangman is a paper and pencil guessing game for two or more players. One player
thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting
letters within a certain number of guesses.

"""
VOWELS = ['a', 'e', 'i', 'o', 'u']


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


if __name__ == "__main__":
    PLAY_GAME = input("\nReady to play? Enter Yes or No: ")
    # Game on set to true if player is ready
    GAME_ON = bool(PLAY_GAME.lower()[0] == 'y')

    if not GAME_ON:
        print("Goodbye!")

    while GAME_ON:
        NUM_OF_GUESSES = 6

        # asking the user if they want to play again
        GAME_ON = replay()
