"""The card game, BlackJack, made using python.

Blackjack is a comparing card game between one or more players and a dealer,
where each player in turn competes against the dealer.

Player and dealer are dealt 2 cards each. One of the dealer's card remains hidden
until the player's turn is over. A hand's value is the sum of the card values.
The value of cards two through ten are 2-10. Face cards (Jack, Queen, and King)
are all worth 10. Aces can be worth 1 or 11 depending on the player's need. Players
are allowed to draw additional cards ("hit") to improve their hands till they reach
a value of 21 or they can end their turn ("stand").

The conditions for winning and losing are as follows:
    1. If the player exceeds a sum of 21 ("busts"), the player loses, even if the
    dealer also exceeds 21.

    2. If the dealer exceeds 21 ("busts") and the player does not, the player wins.

    3. If the player attains a final sum higher than the dealer and does not bust, the
    player wins.

    4. If both dealer and player receive a blackjack (a value of 21) or any other
    hands with the same sum called a "push", no one wins.

This program uses the 'random' module to shuffle the "Deck of Cards", which is
made using classes.

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
                "\nDo you want to continue playing? Enter Yes or No: ")

            if not play_again.isdigit():
                if play_again.lower().startswith('y'):
                    return True
                print("Thank you for playing!")
                return False

            raise ValueError

        except ValueError:
            print("Invalid input! Try again!")


SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')

VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
          'King': 10, 'Ace': 11}


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
    """Class for creating, shufling and dealing the Cards in the Deck."""

    def __init__(self):
        """The constructor for Deck class.

        Parameters:
           deck (list): List of cards in deck.

        """

        self.deck = list()

        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        temp = ''
        for card in self.deck:
            temp += '\n' + card.__str__()
        return 'The Deck:\n' + temp

    def shuffle(self):
        """Method to shuffle the cards with the `random` module."""

        random.shuffle(self.deck)

    def deal(self):
        """To deal the cards and remove them from the deck."""

        card = self.deck.pop()
        return card


class Hand:
    """Class for represeting which cards the player has in hand."""

    def __init__(self):
        """The constructor for Hand class.

        Parameters:
           card (list): List of cards in player's hand.
           ace (int): Ace card.
           value (int): Value of the cards in hand.

        """

        self.cards = []
        self.ace = 0
        self.value = 0

    def add_card(self, card):
        """Adds card to player's hand when they select 'hit'.

        Parameters:
           card (str): The card added from deck.

        """

        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.ace += 1

    def ace_adjust(self):
        """To adjust the value of ace according to the player's need."""

        while self.value > 21 and self.ace:

            self.value -= 10
            self.ace -= 1


class Chips:
    """Class for keeping track of the player's chips.

    Attributes:
        total (int): Player's total chips.

    """

    def __init__(self):
        """The constructor for Chips class.

        Parameters:
           total (int): The total chips with the player.
           bet (int): The player's bet.

        """

        self.total = 100
        self.bet = 0

    def win_bet(self):
        """The function to add chips upon winning bet."""

        self.total += self.bet

    def lose_bet(self):
        """The function to remove chips upon losing bet."""

        self.total -= self.bet


def bet(chips):
    """Function to take bet.

    Returns:
        chips.bet if enough chips are available.

    """

    while True:
        try:
            chips.bet = int(input("Make a bet: "))

            if chips.bet in range(1, chips.total+1):
                return chips.bet
            print(f"Not enough chips! You have {chips.total} left!")

        except ValueError:
            print("Invalid input! Try Again!")


def show_some_cards(player_cards, dealer_cards):
    """Function to print the value of cards in player and dealer's hand.

    One of the dealer's card will be hidden till the player chooses to stand.

    Args:
        player_cards (list): Cards in player's hand at the current time.
        dealer_cards (list): Cards in dealer's hand at the current time.

    """

    print("\nDealer's Hand: ")
    print("<card hidden>")
    print(dealer_cards.cards[1])

    print("\nPlayer's Hand:")
    for card in player_cards.cards:
        print(card)
    print("Player's Hand = ", player_cards.value)


def show_all_cards(player_cards, dealer_cards):
    """Function to print the value of all cards in player and dealer's hand.

    Args:
        player_cards (list): Cards in player's hand at the current time.
        dealer_cards (list): Cards in dealer's hand at the current time.

    """

    print("\nDealer's Hand:")
    for card in dealer_cards.cards:
        print(card)
    print("Dealer's Hand =", dealer_cards.value)

    print("\nPlayer's Hand:")
    for card in player_cards.cards:
        print(card)
    print("Player's Hand = ", player_cards.value)


def hit(deck, hand):
    """Adds card to player's hand when they choose to 'hit'.

    Args:
        deck (list): List of cards in deck.
        hand (list): List of cards in player's hand.

    """

    card = deck.deal()

    hand.add_card(card)
    hand.ace_adjust()


def hit_or_stand(deck, hand):
    """Function for player to choose 'hit' or 'stand'.

    Args:
        deck (list): List of cards in deck.
        hand:

    Raises:
        ValueError: Invalid input! Try again!

    """

    while True:
        try:
            if hand.value < 21:
                choice = input(
                    "\nWhat would you like to do? Enter hit or stand: ")

                if choice.lower().startswith('h'):
                    hit(deck, hand)
                    show_some_cards(hand, dealer_hand)

                elif choice.lower().startswith('s'):
                    return False

                else:
                    raise ValueError

            elif hand.value >= 21:
                return False

        except ValueError:
            print("Invalid input! Try again!")


def player_wins(change_chips):  # player wins
    """Player wins.

    Args:
        change_chips: Players' chips which will be incremented according to the bet.

    """

    print("\nPlayer WINS!")

    change_chips.win_bet()


def player_busts(change_chips):  # player busts
    """Player busts.

    Args:
        change_chips: Players' chips which will be decremented according to the bet.

    """

    print("\nPlayer BUSTS!")

    change_chips.lose_bet()


def dealer_wins(change_chips):  # dealer wins
    """Dealer wins.

    Args:
        change_chips: Players' chips which will be decremented according to the bet.

    """

    print("\nDealer WINS!")

    change_chips.lose_bet()


def dealer_busts(change_chips):  # dealer loses
    """Dealer loses.

    Args:
        change_chips: Players' chips which will be incremented according to the bet.

    """

    print("\nDealer BUSTS! Player WINS!")

    change_chips.win_bet()


def tie():  # tie
    """Player and dealer tie."""

    print("\nPUSH! Dealer and player tie!")


if __name__ == "__main__":
    PLAY_GAME = input("\nReady to play? Enter Yes or No: ")
    # Game on set to true is player is ready
    GAME_ON = bool(PLAY_GAME.lower()[0] == 'y')

    player_chips = Chips()  # setting up player's chips

    if not GAME_ON:
        print("Goodbye!")

    while GAME_ON:
        new_deck = Deck()  # initalizing deck
        new_deck.shuffle()  # shuffling deck

        player_hand = Hand()  # creating player hand object

        # dealing 2 cards
        player_hand.add_card(new_deck.deal())
        player_hand.add_card(new_deck.deal())

        dealer_hand = Hand()  # creating dealer hand object

        # dealing 2 cards
        dealer_hand.add_card(new_deck.deal())
        dealer_hand.add_card(new_deck.deal())

        print(f"\nPlayer's total chips: {player_chips.total}")
        bet(player_chips)  # taking bet

        show_some_cards(player_hand, dealer_hand)  # showing some cards

        PLAYER_TURN = True  # player_turn set to true

        while PLAYER_TURN:
            # does the player want to hit or stand
            PLAYER_TURN = hit_or_stand(new_deck, player_hand)

        if player_hand.value > 21:  # player busts
            player_busts(player_chips)

        if player_hand.value == 21:  # player wins
            player_wins(player_chips)

        elif player_hand.value < 21:  # dealer's turn
            print("\nDealer's turn!")

            while dealer_hand.value < 17:  # hit dealer
                hit(new_deck, dealer_hand)

            show_all_cards(player_hand, dealer_hand)  # show all cards

            if dealer_hand.value > 21:
                dealer_busts(player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)

            else:
                tie()

        # displaying final chips
        print(f"\nPlayer's total chips: {player_chips.total}")

        if player_chips.total > 0:
            # asking the user if they want to play again
            GAME_ON = replay()
        else:
            print("You lost all your chips! Game Over!")
            print("Thank you for playing!")
            GAME_ON = False
