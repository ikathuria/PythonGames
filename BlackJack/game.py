"""A program to simulate the card game known as "BlackJack" using python.

This program uses the 'random' module to shuffle the "Deck of Cards", which is
made using classes.
"""

import random

# SUIT, RANK, VALUES
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')

VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
          'King': 10, 'Ace': 11}


# CARD CLASS
class Card:
    """
    This is a class for storing suit, rank and values of Cards in the Deck.
    """

    def __init__(self, suit, rank):
        """The constructor for Card class.

        Parameters:
           suit (str): The suit of a card ('Hearts', 'Diamonds', 'Spades',
           'Clubs')
           rank (str): The rank of the card('Two', 'Three', 'Four', 'Five',
           'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',
           'Ace')
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


# DECK CLASS
class Deck:
    """Class for creating, shufling and dealing the Cards in the Deck."""

    def __init__(self):
        """The constructor for Deck class."""
        self.deck = list()

        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        """The function to return the value of card.

        Returns:
            Value of card: The rank and suit (for eg. Jack of Spades)
        """

        temp = ''
        for card in self.deck:
            temp += '\n' + card.__str__()
        return 'The Deck:\n' + temp

    def shuffle(self):
        """To shuffle the cards."""

        random.shuffle(self.deck)

    def deal(self):
        """To deal the cards and remove them from the deck."""

        card = self.deck.pop()
        return card


# CARD IN HAND CLASS
class Hand:
    """Class for represeting which cards the player has in hand."""

    def __init__(self):
        """The constructor for Hand class.

        Parameters:
           card (list): List of cards in player's hand
           ace (int): Ace card
           value (int): Value of the cards in hand
        """

        self.cards = []
        self.ace = 0
        self.value = 0

    def add_card(self, card):
        """Adds card to player's hand when they select 'hit'.

        Parameters:
           card (str): The card added from deck
        """

        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.ace += 1

    def ace_adjust(self):
        """To adjust the calue of ace according to the player's need."""

        while self.value > 21 and self.ace:

            self.value -= 10
            self.ace -= 1


# CHIPS CLASS
class Chips:
    """Class for keeping track of the player's chips."""

    def __init__(self, total=1000):
        """The constructor for Chips class.

        Parameters:
           total (int): The total chips with the player
           bet (int): The player's bet
        """
        self.total = total
        self.bet = 0

    def win_bet(self):
        """The function to add chips upon winning bet."""

        self.total += 2*self.bet

    def lose_bet(self):
        """The function to remove chips upon losing bet."""

        self.total -= self.bet


# CHIPS AND BET
def bet(chips):
    """Function to take bet."""

    while True:
        try:
            chips.bet = int(input("Make a bet: "))
            if isinstance(chips.bet, int):
                if chips.bet > chips.total:
                    print(f"Not enough chips! You have {chips.total} left!")
                else:
                    return chips.bet
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Try Again!")


# SHOW CARDS
def show_some_cards(player_hand, dealer_hand):
    print("\nDealer's Hand: ")
    print("<card hidden>")
    print(dealer_hand.cards[1])
    print("\nPlayer's Hand:")
    for card in player_hand.cards:
        print(card)
    print("Player's Hand = ", player_hand.value)


def show_all_cards(player_hand, dealer_hand):
    print("\nDealer's Hand:")
    for card in dealer_hand.cards:
        print(card)
    print("Dealer's Hand =", dealer_hand.value)

    print("\nPlayer's Hand:")
    for card in player_hand.cards:
        print(card)
    print("Player's Hand = ", player_hand.value)


# HIT AND STAND
def hit(deck, hand):
    """Function for when the player chooses 'hit'."""

    card = deck.deal()

    hand.add_card(card)
    hand.ace_adjust()


# PLAYING
playing = True


def hit_or_stand(deck, hand):
    """Function for player to choose 'hit' or 'stand'."""

    while True:
        try:
            choice = input("Do you want to hit or stand? ")
            choice = choice.lower()

            if player_hand.value < 21:
                if choice.startswith('h'):
                    hit(deck, player_hand)
                    show_some_cards(player_hand, dealer_hand)
                elif choice.startswith('s'):
                    print("Dealer's turn!")
                    playing = False
                    break
                else:
                    raise ValueError

            elif player_hand.value == 21:
                playing = False
                break

            else:
                player_busts(player_hand, dealer_hand, player_chips)
                playing = False
                break

        except ValueError:
            print("Invalid input! Try again!")


# WINNING SCENARIOS
def player_wins(player, dealer, chips):  # player wins
    """Function for when player wins."""

    print("Player WINS!")

    player_chips.win_bet()


def player_busts(player, dealer, chips):  # player busts
    """Function for when player loses."""

    print("Player BUSTS!")

    player_chips.lose_bet()


def dealer_wins(player, dealer, chips):  # delaer wins
    """Function for when dealer wins."""

    print("Dealer WINS!")

    player_chips.lose_bet()


def dealer_busts(player, dealer, chips):  # player wins
    """Function for when dealer loses."""

    print("Dealer BUSTS! Player WINS!")

    player_chips.win_bet()


def tie(player, dealer):  # tie
    """Function for when player and dealer tie."""

    print("PUSH! Dealer and player tie!")


# GAME LOOP
while True:

    # START
    wel = "WELCOME TO BALCKJACK"
    print(*wel)
    print()

    # CARDS
    deck = Deck()
    deck.shuffle()

    # DEALING CARDS
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # CHIPS AND BET
    while True:
        try:
            total = int(input("Enter total starting chips: "))
            if isinstance(total, int):
                player_chips = Chips(total)
                bet(player_chips)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Try Again!")

    # SHOWING CARDS
    show_some_cards(player_hand, dealer_hand)

    while playing:

        # HIT OR STAND
        hit_or_stand(deck, player_hand)

        # SHOWING CARDS
        show_some_cards(player_hand, dealer_hand)

        # CHECK FOR PLAYER BUST
        if player_hand.value > 21:

            player_busts(player_hand, dealer_hand, player_chips)
            break

        if player_hand.value <= 21:

            while dealer_hand.value < 17:  # hit dealer
                hit(deck, dealer_hand)

            show_all_cards(player_hand, dealer_hand)  # show all cards

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                tie(player_hand, dealer_hand)

        # PLAYER'S TOTAL CHIPS
        print(f"\nPlayer's total chips: {player_chips.total}")

        # PLAY AGAIN
    try:
        replay = input("Would you like to play again? Yes or No: ")
        if replay.lower().startswith('y'):
            playing = True
            continue
        elif replay.lower().startswith('n'):
            print("Thank you for playing!")
            playing = False
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid input! Try again!")
