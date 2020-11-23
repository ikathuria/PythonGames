"""The card game, War, made using python.

War is a simple card game, typically played by two players using a standard
playing card deck.

The objective of the game is to win all of the cards. The deck is divided evenly
among the players, giving each a down stack. In unison, each player reveals the
top card of their deck — this is called a "battle" — and the player with the
higher card takes both of the cards played and moves them to their stack. If the
two cards played are of equal value, then there is a "war". Both players place the
next card of their pile face down and then another card face-up. The owner of the
higher face-up card wins the war.

This program is not user interactive. The game is set to advance in a loop till an
outcome is reached.

This program uses the 'random' module to shuffle the "Deck of Cards".

"""

import random

# SUIT, RANK, VALUES
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """This is a class for storing suit, rank and values of Cards in the Deck.

    Attributes:
        suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        rank (str): The rank of the card('Two', 'Three', 'Four', 'Five', 'Six',
        'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    """

    def __init__(self, suit, rank):
        """The constructor for Card class."""

        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """This is a class for creating, shufling and dealing the Cards in the Deck."""

    def __init__(self):
        """The constructor for Deck class.

        Parameters:
           all_cards (list): List of cards in deck.

        """

        self.all_cards = []

        for suit in SUITS:
            for rank in RANKS:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        """Method to shuffle the cards with the `random` module."""

        random.shuffle(self.all_cards)

    def deal(self):
        """To deal the cards and remove them from the deck."""

        return self.all_cards.pop()


class Player:
    """This is a class for storing Player names and adding/removing their cards.

    Attributes:
        name (str): String storing player's name.

    """

    def __init__(self, name):
        """The constructor for Player class."""

        self.name = name
        self.all_cards = []

    def remove_one(self):
        """To remove the top card from the player's pile."""

        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """Add cards to the bottom of the player's pile.

        Args:
            new_cards (str or list): The card which will be added to the player's pile.

        """

        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)  # For multiple cards

        else:
            self.all_cards.append(new_cards)  # For single card

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards."


if __name__ == "__main__":
    # naming the players
    PLAYER_ONE = Player("One")
    PLAYER_TWO = Player("Two")

    NEW_DECK = Deck()  # initalizing deck
    NEW_DECK.shuffle()  # shuffling deck

    # dealing card to both players
    for x in range(26):
        PLAYER_ONE.add_cards(NEW_DECK.deal())
        PLAYER_TWO.add_cards(NEW_DECK.deal())

    PLAY_GAME = input("\nReady to play? Enter Yes or No: ")
    # Game on set to true if player is ready
    GAME_ON = bool(PLAY_GAME.lower()[0] == 'y')

    if not GAME_ON:
        print("Goodbye!")

    while GAME_ON:
        # NUMBER OF ROUNDS
        ROUND_NUM = 0

        while True:
            ROUND_NUM += 1
            print(f"Round number: {ROUND_NUM}")

            if len(PLAYER_ONE.all_cards) == 0:
                print("Player 1 has no cards left :(\nPlayer 2 WINS!!")
                GAME_ON = False
                break

            if len(PLAYER_TWO.all_cards) == 0:
                print("Player 2 has no cards left :(\nPlayer 1 WINS!!")
                GAME_ON = False
                break

            # new round
            PLAYER_ONE_CARDS = []
            PLAYER_ONE_CARDS.append(PLAYER_ONE.remove_one())

            PLAYER_TWO_CARDS = []
            PLAYER_TWO_CARDS.append(PLAYER_TWO.remove_one())

            AT_WAR = True
            while AT_WAR:

                try:
                    if PLAYER_ONE_CARDS[-1].value > PLAYER_TWO_CARDS[-1].value:

                        PLAYER_ONE.add_cards(PLAYER_ONE_CARDS)
                        PLAYER_ONE.add_cards(PLAYER_TWO_CARDS)
                        AT_WAR = False

                    elif PLAYER_ONE_CARDS[-1].value < PLAYER_TWO_CARDS[-1].value:

                        PLAYER_TWO.add_cards(PLAYER_TWO_CARDS)
                        PLAYER_TWO.add_cards(PLAYER_ONE_CARDS)
                        AT_WAR = False
                        break

                    else:
                        print("YOU ARE AT WAR!")

                        if len(PLAYER_ONE.all_cards) <= 5:
                            print("Player 2 WINS!")
                            AT_WAR = False
                            GAME_ON = False

                        elif len(PLAYER_TWO.all_cards) <= 5:
                            print("Player 1 WINS!")
                            GAME_ON = False
                            break

                        else:
                            for num in range(5):
                                PLAYER_ONE_CARDS.append(PLAYER_ONE.remove_one)
                                PLAYER_TWO_CARDS.append(PLAYER_TWO.remove_one)
                except AttributeError:
                    AT_WAR = False
