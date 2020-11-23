"""The game of hangman made using python.

Hangman is a paper and pencil guessing game for two or more players. One player
thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting
letters within a certain number of guesses.

"""

import random

the_words = ['python', 'hangman', 'games', 'rainbow', 'phoenix', 'rhythm',
             'dragon', 'dog', 'cat', 'paint', 'rock', 'paper', 'scissors',
             'chocolate', 'pizza', 'burger', 'egg', 'chicken', 'cheese',
             'mathematics', 'morning', 'afternoon', 'night', 'disney',
             'netflix', 'microsoft', 'google']


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
        WIN = False

        all_guesses = []  # all the player guesses
        COUNT = 0  # counter to keep track of player's guesses
        word = random.choice(the_words)  # the word to be guessed

        print(f"Guess the word: {'_ '*len(word)}")

        # guessing
        while COUNT < 6:
            while True:
                guess = input("\nEnter you guess: ").lower()
                if guess not in all_guesses:
                    if guess.isalpha():
                        break
                    print("Not a valid letter! Try again")

                else:
                    print(
                        "Letter already guessed! Choose another letter")

            all_guesses.append(guess)

            CURRENT = ''

            if guess not in word:
                COUNT += 1

            for letter in word:
                if letter in all_guesses:
                    CURRENT += letter
                else:
                    CURRENT += '_'

                CURRENT += ' '

            print(f"\nGUESSES LEFT: {6-COUNT}")
            print(f"Your guesses: {all_guesses}")
            print(f"\nThe word: {CURRENT}")

            if '_' not in CURRENT:
                WIN = True
                break

        if WIN:
            print("\nYOU GOT IT!")
        else:
            print("\nGame Over!")

        print(f"The word was {word}")

        # asking the user if they want to play again
        GAME_ON = replay()
