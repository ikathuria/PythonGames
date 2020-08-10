"""This is a program to simulate the card game known as "BlackJack" using python.

This program uses the 'random' module to shuffle the "Deck of Cards", which is
made using classes.
"""

import random

# SUIT, RANK, VALUES
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')

VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

#CARD CLASS
class Card:
    """This is a class for storing suit, rank and values of Cards in the Deck.

    Attributes:
        suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        rank (str): The rank of the card('Two', 'Three', 'Four', 'Five', 'Six',
        'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    """
    def __init__(self, suit, rank):
        """The constructor for Card class.

        Parameters:
           suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades', 'Clubs')
           rank (str): The rank of the card('Two', 'Three', 'Four', 'Five', 'Six',
          'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        """
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        """The function to return the value of card.

        Returns:
            Value of card: The rank and suit (for eg. Jack of Spades)
        """
        return self.rank + " of " + self.suit

#DECK CLASS
class Deck:
    """This is a class for creating, shufling and dealing the Cards in the Deck."""
    def __init__(self):
        """The constructor for Deck class."""
        self.deck = []

        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        """To shuffle the cards."""

        random.shuffle(self.deck)

    def deal(self):
        """To deal the cards and remove them from the deck."""

        return self.deck.pop()

    def __str__(self):
        """The function to return the value of card.

        Returns:
            Value of card: The rank and suit (for eg. Jack of Spades)
        """

        temp = ''
        for card in self.deck:
            temp += '\n ' + card.__str__()
        return 'The Deck has:\n' + temp

#PLAYER CLASS
class Player:
    """This is a class for creating, shufling and dealing the Cards in the Deck."""
    def __init__(self, name):
        """The constructor for Player class.

        Parameters:
           name (str): The name of the player
           chips (int): The number of chips with the player
        """
        self.name = name
        self.deck = []

    def remove_one(self):
        """To remove the top card from the player's pile."""

        return self.deck.pop(0)

    def add_cards(self, new_cards):
        """Add cards to the bottom of the player's pile.

        Parameters:
           new_cards (str): The cards added
        """

        if isinstance(new_cards, list):
            self.deck.extend(new_cards) #For multiple cards
        else:
            self.deck.append(new_cards) #For single card

    def __str__(self):
        """To add cards to the player's pile."""

        return f"{self.name} has {len(self.deck)} cards."

#CHIPS CLASS
class Chips:
    
    def __init__(self,total,bet):
        self.total = 1000  #Default value
        self.bet = 0
        
    def win_bet(self):
        self.total += 100
    
    def lose_bet(self):
        self.total -= 100

# INITIALIZING
PLAYER_ONE = Player("One")

# CARDS
NEW_DECK = Deck()
NEW_DECK.shuffle()

# GAME ON
GAME_ON = True

# GAME LOOP
#while GAME_ON:

    # Bet does not exceed their available chips

    # Deal two cards to the Dealer and two cards to the Player

    # Show only one of the Dealer's cards, the other remains hidden
    # Show both of the Player's cards

    #Ask the Player if they wish to Hit, and take another card
    #If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.

# =============================================================================
#     #If a Player Stands, play the Dealer's hand. The dealer will always Hit
#     until the Dealer's value meets or exceeds 17
# =============================================================================

    #Determine the winner and adjust the Player's chips accordingly

    #Ask the Player if they'd like to play again


    #pass






















