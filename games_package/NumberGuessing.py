"""A simple number guessing game made using python.

"""

import random

if __name__ == "__main__":
    # GAME ON
    gameOn = True

    while gameOn:

        # welcome
        wel = "WELCOME TO NUMBER-GUESSING-GAME"
        print('\n', *wel)
        print()

        # select difficulty level
        print("1. Piece of Cake")
        print("2. Let's Rock")
        print("3. Damn I'm Good")

        while True:
            try:
                difficulty = int(input("Choose your difficulty level: "))
                if difficulty in range(1, 4):
                    break
                else:
                    raise ValueError

            except ValueError:
                print("Invalid input!")
                print("Choose a number between 1-3")

        # selecting random lower limit
        lowerLimit = random.randrange(0, 501, 100)

        # setting upper limit and number of guesses according to difficulty
        if difficulty == 1:
            upperLimit = lowerLimit + 10
            numOfGuesses = 5

        elif difficulty == 2:
            upperLimit = lowerLimit + 50
            numOfGuesses = 5

        else:
            upperLimit = lowerLimit + 100
            numOfGuesses = 3

        ans = random.randint(lowerLimit, upperLimit)

        print(f"\nYour range for guessing will be {lowerLimit} to {upperLimit}")
        print(f"You will get {numOfGuesses} guesses")

        count = 1
        while count <= numOfGuesses:

            # guessing
            while True:
                print(f"\nGUESS NUMBER {count}")
                try:
                    guess = int(input("Make your guess: "))
                    if guess in range(lowerLimit, upperLimit+1):
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print("Invalid input!")
                    print(f"Choose a number between {lowerLimit} and {upperLimit}")

            if guess < ans:
                print("Try guessing higher!")
                count += 1

            elif guess > ans:
                print("Try guessing lower!")
                count += 1

            else:
                break

        if guess == ans:
            print(f"\nYou got it in {count} guesses!")

        else:
            print(f"\nBetter luck next time!")
            print("The correct number was", ans)

        while True:
            try:
                replay = input("\nDo you want to play again? Enter Yes or No: ")
                if replay.lower().startswith('y'):
                    gameOn = True
                    break
                elif replay.lower().startswith('n'):
                    print("\nThank you for playing!")
                    gameOn = False
                    break
                else:
                    raise ValueError

            except ValueError:
                print("Invalid input! Try again!")
