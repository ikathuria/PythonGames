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

from PyQt5 import QtCore, QtGui, QtWidgets
import random

# for stylesheet
button_style = """QPushButton { background-color: rgb(0, 0, 0);
                                 color: rgb(255, 255, 255);
                                 border-radius: 10px; }
                
                QPushButton::pressed { background-color: rgb(255, 255, 255);
                                    color: rgb(0, 0, 0);
                                    border: 1px solid rgb(0, 0, 0);
                                    border-radius: 10px; }
                
                QPushButton::disabled { background-color: rgba(0, 0, 0, 0.2);
                                        color: rgb(75, 75, 75); }"""

hs_style = """QPushButton { background-color: rgb(255, 255, 255);
                                 color: rgb(0, 0, 0);
                                 border-radius: 10px; }
                
                QPushButton::pressed { background-color: rgb(0, 0, 0);
                                    color: rgb(255, 255, 255);
                                    border: 1px solid rgb(0, 0, 0);
                                    border-radius: 10px; }
                
                QPushButton::disabled { background-color: rgba(0, 0, 0, 0.2);
                                        color: rgb(75, 75, 75); }"""


SUITS = ('C', 'D', 'H', 'S')

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
        return self.rank + self.suit


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


class Ui_blackjack(object):
    """Ui Class."""

    def setupUi(self, blackjack):
        """setup ui."""

        self.blackjack = blackjack

        blackjack.setObjectName("blackjack")

        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        blackjack.setFont(font)

        # size
        blackjack.resize(530, 530)
        blackjack.setMinimumSize(QtCore.QSize(530, 530))

        # stylesheet
        blackjack.setStyleSheet("background-color: rgb(255, 255, 255);")

        # main layout
        self.main_layout = QtWidgets.QGridLayout(blackjack)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(5)
        self.main_layout.setObjectName("main_layout")

        # WELCOME #############################################################
        self.welcome = QtWidgets.QLabel(blackjack)
        # font
        font.setPointSize(18)
        self.welcome.setFont(font)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHeightForWidth(
            self.welcome.sizePolicy().hasHeightForWidth())
        self.welcome.setSizePolicy(sizePolicy)
        self.welcome.setMinimumSize(QtCore.QSize(510, 50))
        self.welcome.setMaximumSize(QtCore.QSize(16777215, 100))
        # stylesheet
        self.welcome.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # allignment
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.welcome.setObjectName("welcome")

        # adding to main layout
        self.main_layout.addWidget(self.welcome, 0, 0, 1, 2)

        # GAME BOX ###################################################################
        self.game_box = QtWidgets.QWidget(blackjack)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.game_box.sizePolicy().hasHeightForWidth())
        self.game_box.setSizePolicy(sizePolicy)
        self.game_box.setMinimumSize(QtCore.QSize(510, 360))
        # stylesheet
        self.game_box.setStyleSheet("background-color: rgb(217, 221, 255)")
        # object name
        self.game_box.setObjectName("game_box")

        # layout
        self.game_box__layout = QtWidgets.QGridLayout(self.game_box)
        self.game_box__layout.setContentsMargins(10, 10, 10, 10)
        self.game_box__layout.setSpacing(5)
        self.game_box__layout.setObjectName("game_box__layout")

        # PLAYER ####################################################
        self.player = QtWidgets.QScrollArea(self.game_box)
        self.player.setMinimumSize(QtCore.QSize(230, 280))
        self.player.setObjectName("player")

        # cards
        self.player_widget = QtWidgets.QWidget()
        self.player_widget.setGeometry(QtCore.QRect(0, 0, 220, 670))
        self.player_widget.setObjectName("player_widget")

        # layout
        self.player_layout = QtWidgets.QVBoxLayout(self.player_widget)
        self.player_layout.setContentsMargins(10, 10, 10, 10)
        self.player_layout.setSpacing(5)
        self.player_layout.setObjectName("player_layout")

        # value label
        self.player_value = QtWidgets.QLabel(self.player_widget)
        self.player_value.setMinimumSize(QtCore.QSize(0, 40))
        self.player_value.setAlignment(QtCore.Qt.AlignCenter)
        self.player_value.setObjectName("player_value")
        self.player_layout.addWidget(self.player_value)

        # card 1
        self.player_card_1 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_1.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_1.setScaledContents(True)
        # allignment
        self.player_card_1.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_1.setObjectName("player_card_1")

        self.player_layout.addWidget(self.player_card_1)

        # card 2
        self.player_card_2 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_2.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_2.setScaledContents(True)
        # allignment
        self.player_card_2.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_2.setObjectName("player_card_2")

        self.player_layout.addWidget(self.player_card_2)

        # card 3
        self.player_card_3 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_3.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_3.setScaledContents(True)
        # allignment
        self.player_card_3.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_3.setObjectName("player_card_3")

        self.player_layout.addWidget(self.player_card_3)

        # card 4
        self.player_card_4 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_4.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_4.setScaledContents(True)
        # allignment
        self.player_card_4.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_4.setObjectName("player_card_4")

        self.player_layout.addWidget(self.player_card_4)

        # card 5
        self.player_card_5 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_5.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_5.setScaledContents(True)
        # allignment
        self.player_card_5.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_5.setObjectName("player_card_5")

        self.player_layout.addWidget(self.player_card_5)

        # card 6
        self.player_card_6 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_6.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_6.setScaledContents(True)
        # allignment
        self.player_card_6.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_6.setObjectName("player_card_6")

        self.player_layout.addWidget(self.player_card_6)

        # card 7
        self.player_card_7 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_7.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_7.setScaledContents(True)
        # allignment
        self.player_card_7.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_7.setObjectName("player_card_7")

        self.player_layout.addWidget(self.player_card_7)

        # card 8
        self.player_card_8 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_8.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_8.setScaledContents(True)
        # allignment
        self.player_card_8.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_8.setObjectName("player_card_8")

        self.player_layout.addWidget(self.player_card_8)

        # card 9
        self.player_card_9 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_9.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_9.setScaledContents(True)
        # allignment
        self.player_card_9.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_9.setObjectName("player_card_9")

        self.player_layout.addWidget(self.player_card_9)

        # card 10
        self.player_card_10 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_10.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_10.setScaledContents(True)
        # allignment
        self.player_card_10.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_10.setObjectName("player_card_10")

        self.player_layout.addWidget(self.player_card_10)

        # card 11
        self.player_card_11 = QtWidgets.QLabel(self.player_widget)
        # size
        self.player_card_11.setMinimumSize(QtCore.QSize(200, 300))
        self.player_card_11.setScaledContents(True)
        # allignment
        self.player_card_11.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_card_11.setObjectName("player_card_11")

        self.player_layout.addWidget(self.player_card_11)

        # adding to player scroll area
        self.player.setWidget(self.player_widget)

        # adding to layout
        self.game_box__layout.addWidget(self.player, 0, 0, 1, 1)

        # DEALER ##################################
        self.dealer = QtWidgets.QScrollArea(self.game_box)
        self.dealer.setMinimumSize(QtCore.QSize(230, 280))
        self.dealer.setObjectName("dealer")

        # cards
        self.dealer_widget = QtWidgets.QWidget()
        self.dealer_widget.setGeometry(QtCore.QRect(0, -220, 220, 670))
        self.dealer_widget.setObjectName("dealer_widget")

        # layout
        self.dealer_layout = QtWidgets.QVBoxLayout(self.dealer_widget)
        self.dealer_layout.setContentsMargins(10, 10, 10, 10)
        self.dealer_layout.setSpacing(5)
        self.dealer_layout.setObjectName("dealer_layout")

        # dealer value
        self.dealer_value = QtWidgets.QLabel(self.dealer_widget)
        self.dealer_value.setMinimumSize(QtCore.QSize(0, 40))
        self.dealer_value.setAlignment(QtCore.Qt.AlignCenter)
        self.dealer_value.setObjectName("dealer_value")
        self.dealer_layout.addWidget(self.dealer_value)

        # card 1
        self.dealer_card_1 = QtWidgets.QLabel(self.dealer_widget)
        # size
        self.dealer_card_1.setMinimumSize(QtCore.QSize(200, 300))
        self.dealer_card_1.setScaledContents(True)
        # allignment
        self.dealer_card_1.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.dealer_card_1.setObjectName("dealer_card_1")

        self.dealer_layout.addWidget(self.dealer_card_1)

        # card 2
        self.dealer_card_2 = QtWidgets.QLabel(self.dealer_widget)
        # size
        self.dealer_card_2.setMinimumSize(QtCore.QSize(200, 300))
        self.dealer_card_2.setScaledContents(True)
        # allignment
        self.dealer_card_2.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.dealer_card_2.setObjectName("dealer_card_2")

        self.dealer_layout.addWidget(self.dealer_card_2)

        # card 3
        self.dealer_card_3 = QtWidgets.QLabel(self.dealer_widget)
        # size
        self.dealer_card_3.setMinimumSize(QtCore.QSize(200, 300))
        self.dealer_card_3.setScaledContents(True)
        # allignment
        self.dealer_card_3.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.dealer_card_3.setObjectName("dealer_card_3")

        self.dealer_layout.addWidget(self.dealer_card_3)

        # card 4
        self.dealer_card_4 = QtWidgets.QLabel(self.dealer_widget)
        # size
        self.dealer_card_4.setMinimumSize(QtCore.QSize(200, 300))
        self.dealer_card_4.setScaledContents(True)
        # allignment
        self.dealer_card_4.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.dealer_card_4.setObjectName("dealer_card_4")

        self.dealer_layout.addWidget(self.dealer_card_4)

        # card 5
        self.dealer_card_5 = QtWidgets.QLabel(self.dealer_widget)
        # size
        self.dealer_card_5.setMinimumSize(QtCore.QSize(200, 300))
        self.dealer_card_5.setScaledContents(True)
        # allignment
        self.dealer_card_5.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.dealer_card_5.setObjectName("dealer_card_5")

        self.dealer_layout.addWidget(self.dealer_card_5)

        # card 6
        self.dealer_card_6 = QtWidgets.QLabel(self.dealer_widget)
        # size
        self.dealer_card_6.setMinimumSize(QtCore.QSize(200, 300))
        self.dealer_card_6.setScaledContents(True)
        # allignment
        self.dealer_card_6.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.dealer_card_6.setObjectName("dealer_card_6")

        self.dealer_layout.addWidget(self.dealer_card_6)

        # card 7
        self.dealer_card_7 = QtWidgets.QLabel(self.dealer_widget)
        # size
        self.dealer_card_7.setMinimumSize(QtCore.QSize(200, 300))
        self.dealer_card_7.setScaledContents(True)
        # allignment
        self.dealer_card_7.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.dealer_card_7.setObjectName("dealer_card_7")

        self.dealer_layout.addWidget(self.dealer_card_7)

        # card 8
        self.dealer_card_8 = QtWidgets.QLabel(self.dealer_widget)
        # size
        self.dealer_card_8.setMinimumSize(QtCore.QSize(200, 300))
        self.dealer_card_8.setScaledContents(True)
        # allignment
        self.dealer_card_8.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.dealer_card_8.setObjectName("dealer_card_8")

        self.dealer_layout.addWidget(self.dealer_card_8)

        # card 9
        self.dealer_card_9 = QtWidgets.QLabel(self.dealer_widget)
        # size
        self.dealer_card_9.setMinimumSize(QtCore.QSize(200, 300))
        self.dealer_card_9.setScaledContents(True)
        # allignment
        self.dealer_card_9.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.dealer_card_9.setObjectName("dealer_card_9")

        self.dealer_layout.addWidget(self.dealer_card_9)

        # adding to dealer scroll area
        self.dealer.setWidget(self.dealer_widget)

        # adding to layout
        self.game_box__layout.addWidget(self.dealer, 0, 1, 1, 1)

        # HIT BUTTON ########################################
        self.hit = QtWidgets.QPushButton(self.game_box)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.hit.sizePolicy().hasHeightForWidth())
        self.hit.setSizePolicy(sizePolicy)
        self.hit.setMinimumSize(QtCore.QSize(0, 50))
        self.hit.setMaximumSize(QtCore.QSize(16777215, 50))
        # stylesheet
        self.hit.setStyleSheet(hs_style)
        # object name
        self.hit.setObjectName("hit")

        # adding to layout
        self.game_box__layout.addWidget(self.hit, 1, 0, 1, 1)

        # click click
        self.hit.clicked.connect(self.click_hit)

        # STAND BUTTON ########################################
        self.stand = QtWidgets.QPushButton(self.game_box)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.stand.sizePolicy().hasHeightForWidth())
        self.stand.setSizePolicy(sizePolicy)
        self.stand.setMinimumSize(QtCore.QSize(0, 50))
        self.stand.setMaximumSize(QtCore.QSize(16777215, 50))
        # stylesheet
        self.stand.setStyleSheet(hs_style)
        # object name
        self.stand.setObjectName("stand")

        # adding to layout
        self.game_box__layout.addWidget(self.stand, 1, 1, 1, 1)

        # click click
        self.stand.clicked.connect(self.click_stand)

        # adding to main layout
        self.main_layout.addWidget(self.game_box, 1, 0, 1, 2)

        # TEXT ############################################################################
        self.text = QtWidgets.QLabel(blackjack)
        # font
        font.setPointSize(12)
        self.text.setFont(font)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHeightForWidth(
            self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setMinimumSize(QtCore.QSize(300, 75))
        self.text.setMaximumSize(QtCore.QSize(16777215, 200))
        # stylesheet
        self.text.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # allignment
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.text.setObjectName("text")

        # adding to main layout
        self.main_layout.addWidget(self.text, 2, 0, 1, 1)

        # NEW GAME BUTTON ################################################################
        self.new_game = QtWidgets.QPushButton(blackjack)
        # font
        font.setPointSize(14)
        self.new_game.setFont(font)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.new_game.sizePolicy().hasHeightForWidth())
        self.new_game.setSizePolicy(sizePolicy)
        self.new_game.setMinimumSize(QtCore.QSize(0, 50))
        self.new_game.setMaximumSize(QtCore.QSize(16777215, 100))
        # stylesheet
        self.new_game.setStyleSheet(button_style)
        # object name
        self.new_game.setObjectName("new_game")

        # adding to main layout
        self.main_layout.addWidget(self.new_game, 2, 1, 1, 1)

        # restarting game
        self.new_game.clicked.connect(lambda: self.restart(blackjack))

        # OTHER VARIABLES ###################################################################
        self.player_cards = [self.player_card_1, self.player_card_2, self.player_card_3, self.player_card_4, self.player_card_5,
                             self.player_card_6, self.player_card_7, self.player_card_8, self.player_card_9, self.player_card_10, self.player_card_11]

        self.dealer_cards = [self.dealer_card_1, self.dealer_card_2, self.dealer_card_3, self.dealer_card_4,
                             self.dealer_card_5, self.dealer_card_6, self.dealer_card_7, self.dealer_card_8, self.dealer_card_9]

        self.new_deck = Deck()  # initalizing deck
        self.new_deck.shuffle()  # shuffling deck

        # player hand
        self.player_hand = Hand()
        self.player_hand.add_card(self.new_deck.deal())
        self.player_hand.add_card(self.new_deck.deal())

        # dealer hand
        self.dealer_hand = Hand()
        self.dealer_hand.add_card(self.new_deck.deal())
        self.dealer_hand.add_card(self.new_deck.deal())

        #####################################################################################
        self.retranslateUi(blackjack)
        QtCore.QMetaObject.connectSlotsByName(blackjack)

    def retranslateUi(self, blackjack):
        """retransalate."""

        _translate = QtCore.QCoreApplication.translate
        # WINDOW TITLE
        blackjack.setWindowTitle(_translate("blackjack", "blackjack"))

        # WELCOME TEXT
        self.welcome.setText(_translate("blackjack", "WELCOME TO BLACKJACK!"))

        # PLAYER VALUE
        self.player_value.setText(_translate("blackjack", "Player Value: 0"))

        # DEALER VALUE
        self.dealer_value.setText(_translate("blackjack", "Dealer Value: ?"))

        # HIT BUTTON
        self.hit.setText(_translate("blackjack", "HIT"))

        # STAND BUTTON
        self.stand.setText(_translate("blackjack", "STAND"))

        # TEXT TEXT
        self.text.setText(_translate(
            "blackjack", "Do you want to hit or stand?"))

        # NEW GAME BUTTON
        self.new_game.setText(_translate("blackjack", "New Game"))

        for card in self.player_cards:
            card.setHidden(True)

        for card in self.dealer_cards:
            card.setHidden(True)

        self.show_some_cards()

    def restart(self, blackjack):
        """Resets the game for the user."""

        self.new_deck = Deck()  # initalizing deck
        self.new_deck.shuffle()  # shuffling deck

        # player hand
        self.player_hand = Hand()
        self.player_hand.add_card(self.new_deck.deal())
        self.player_hand.add_card(self.new_deck.deal())

        # dealer hand
        self.dealer_hand = Hand()
        self.dealer_hand.add_card(self.new_deck.deal())
        self.dealer_hand.add_card(self.new_deck.deal())

        self.hit.setEnabled(True)
        self.stand.setEnabled(True)

        self.retranslateUi(blackjack)
        QtCore.QMetaObject.connectSlotsByName(blackjack)

    def show_some_cards(self):
        """Some cards shown before dealer's turn."""

        # PLAYER CARDS
        for i in range(len(self.player_hand.cards)):
            card = f"ui_games/images/blackjack/{self.player_hand.cards[i]}.png"

            self.player_cards[i].setPixmap(QtGui.QPixmap(card))
            self.player_cards[i].setHidden(False)

        self.player_value.setText(f"Player Value: {self.player_hand.value}")

        # DEALER CARDS
        self.dealer_card_1.setPixmap(QtGui.QPixmap(
            f"ui_games/images/blackjack/{self.dealer_hand.cards[0]}.png"))
        self.dealer_card_1.setHidden(False)

        self.dealer_card_2.setPixmap(QtGui.QPixmap(
            "ui_games/images/blackjack/gray_back.png"))
        self.dealer_card_2.setHidden(False)

        if self.player_hand.value == 21:
            self.hit.setEnabled(False)
            self.stand.setEnabled(False)

            self.text.setText("Player WINS!")

    def show_all_cards(self):
        """All cards shown at the end of the game."""

        # PLAYER CARDS
        for i in range(len(self.player_hand.cards)):
            card = f"ui_games/images/blackjack/{self.player_hand.cards[i]}.png"

            self.player_cards[i].setPixmap(QtGui.QPixmap(card))
            self.player_cards[i].setHidden(False)

        self.player_value.setText(f"Player Value: {self.player_hand.value}")

        # DEALER CARDS
        for i in range(len(self.dealer_hand.cards)):
            card = f"ui_games/images/blackjack/{self.dealer_hand.cards[i]}.png"

            self.dealer_cards[i].setPixmap(QtGui.QPixmap(card))
            self.dealer_cards[i].setHidden(False)

        self.dealer_value.setText(f"Dealer Value: {self.dealer_hand.value}")

        if self.dealer_hand.value > 21:
            self.text.setText("Dealer BUSTS! Player WINS!")

        elif self.dealer_hand.value > self.player_hand.value:
            self.text.setText("Dealer WINS!")
        
        elif self.dealer_hand.value < self.player_hand.value:
            self.text.setText("Player WINS!")
        
        else:
            self.text.setText("PUSH! It is a tie!")
        
        self.hit.setEnabled(False)
        self.stand.setEnabled(False)

    def click_hit(self):
        """Player chooses to hit."""

        card = self.new_deck.deal()

        self.player_hand.add_card(card)
        self.player_hand.ace_adjust()

        self.show_some_cards()

        if self.player_hand.value > 21:
            self.hit.setEnabled(False)
            self.stand.setEnabled(False)

            self.text.setText("Player BUSTS! Dealer WINS!")

        elif self.player_hand.value == 21:
            self.hit.setEnabled(False)
            self.stand.setEnabled(False)

            self.text.setText("Player WINS!")

    def click_stand(self):
        """Player chooses to stand."""

        self.hit.setEnabled(False)

        while self.dealer_hand.value < 17:  # hit dealer
            card = self.new_deck.deal()

            self.dealer_hand.add_card(card)
            self.dealer_hand.ace_adjust()

        self.show_all_cards()
