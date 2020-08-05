"""This is a program to simulate the card game known as "War" using python.

This program uses the 'random' module to shuffle the "Deck of Cards", which is
made using classes.
"""

import random


# SUIT, RANK, VALUES
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#CARD CLASS
class Card:
    """This is a class for storing values Cards in a Deck.

    Longer class information....
    Longer class information....

    Attributes:
        suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        rank (str): The rank of the card('Two', 'Three', 'Four', 'Five', 'Six',
        'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    """
    def __init__(self, suit, rank):
        """
        The constructor for Card class.

        Parameters:
           suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades', 'Clubs')
           rank (str): The rank of the card('Two', 'Three', 'Four', 'Five', 'Six',
          'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        """
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        """
        The function to return the value of card.

        Returns:
            Value of card: The rank and suit (for eg. Jack of Spades)
        """
        return self.rank + " of " + self.suit

#DECK CLASS
class Deck:
    """
    This is a class for storing values Cards in a Deck.

    Attributes:
        suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        rank (str): The rank of the card('Two', 'Three', 'Four', 'Five', 'Six',
        'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    """
    def __init__(self):
        """
        The constructor for Card class.

        Parameters:
           suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades', 'Clubs')
           rank (str): The rank of the card('Two', 'Three', 'Four', 'Five', 'Six',
          'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        """
        self.all_cards = []

        for suit in SUITS:
            for rank in RANKS:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        """
        The constructor for Card class.

        Parameters:
           suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades', 'Clubs')
           rank (str): The rank of the card('Two', 'Three', 'Four', 'Five', 'Six',
          'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        """

        random.shuffle(self.all_cards)

    def deal(self):
        """
        The constructor for Card class.

        Parameters:
           suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades', 'Clubs')
           rank (str): The rank of the card('Two', 'Three', 'Four', 'Five', 'Six',
          'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        """

        return self.all_cards.pop()

NEW_DECK = Deck()
