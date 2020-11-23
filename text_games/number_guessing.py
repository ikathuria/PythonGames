"""A simple number guessing game made using python.

This is a number guessing game where the system chooses a random number that the
user has to attempt to guess. It has 3 levels of difficulty.
    1. Piece of Cake: The simplest mode, with a 10 digit range and a maximum of 5 guesses.
    2. Let's Rock: The in-between mode, with a 50 digit range and a maximum of 5 guesses.
    3. Damn I'm Good: The hardcore mode, with a 100 digit range and a maximum of 3 guesses.

This program uses the `random` module to generate random ranges and answers.

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


if __name__ == "__main__":
    PLAY_GAME = input("\nReady to play? Enter Yes or No: ")
    # Game on set to true if player is ready
    GAME_ON = bool(PLAY_GAME.lower()[0] == 'y')

    if not GAME_ON:
        print("Goodbye!")

    while GAME_ON:
        # the 3 difficulty levels
        print("1. Piece of Cake")
        print("2. Let's Rock")
        print("3. Damn I'm Good")

        # a loop is set to get the correct input for difficulty level
        while True:
            try:
                difficulty = int(input("Choose your difficulty level: "))
                if difficulty in range(1, 4):
                    break
                raise ValueError

            except ValueError:
                print("Invalid input!")
                print("Choose a number between 1-3")

        # setting up game according to difficulty
        if difficulty == 1:
            # selecting random lower limit
            lowerLimit = random.randrange(0, 101, 10)
            upperLimit = lowerLimit + 10  # setting upper limit
            NUM_OF_GUESSES = 5  # setting number of guesses

        elif difficulty == 2:
            # selecting random lower limit
            lowerLimit = random.randrange(0, 501, 100)
            upperLimit = lowerLimit + 50  # setting upper limit
            NUM_OF_GUESSES = 5  # setting number of guesses

        else:
            # selecting random lower limit
            lowerLimit = random.randrange(0, 501, 100)
            upperLimit = lowerLimit + 100  # setting upper limit
            NUM_OF_GUESSES = 3  # setting number of guesses

        # corrent answer is selcted within the range
        ans = random.randint(lowerLimit, upperLimit)

        print(
            f"\nYour range for guessing will be {lowerLimit} to {upperLimit}")
        print(f"You will get {NUM_OF_GUESSES} guesses")

        COUNT = 1
        while COUNT <= NUM_OF_GUESSES:

            # input for user's guess
            while True:
                print(f"\nGUESS NUMBER {COUNT}")
                try:
                    guess = int(input("Make your guess: "))
                    if guess in range(lowerLimit, upperLimit+1):
                        break
                    raise ValueError

                except ValueError:
                    print("Invalid input!")
                    print(
                        f"Choose a number between {lowerLimit} and {upperLimit}")

            # if guess is less than answer, user is told to guess higher
            # elif guess is greater than answer, user is told to guess lower
            # else user has guessed the answer and loop is broken

            if guess < ans:
                print("Try guessing higher!")
                COUNT += 1

            elif guess > ans:
                print("Try guessing lower!")
                COUNT += 1

            else:
                break

        if guess == ans:
            print(f"\nYou got it in {COUNT} guesses!")

        else:
            print("\nBetter luck next time!")
            print("The correct number was", ans)

        # asking the user if they want to play again
        GAME_ON = replay()
