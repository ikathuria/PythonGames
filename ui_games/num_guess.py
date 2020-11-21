"""A simple number guessing game made using python.

This is a number guessing game where the system chooses a random number that the
user has to attempt to guess. It has 3 levels of difficulty.
    1. Piece of Cake: The simplest mode, with a 10 digit range and a maximum of 5 guesses.
    2. Let's Rock: The in-between mode, with a 50 digit range and a maximum of 5 guesses.
    3. Damn I'm Good: The hardcore mode, with a 100 digit range and a maximum of 3 guesses.

This program uses the `random` module to generate random ranges and answers.

"""

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randrange, randint

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

level_style = """QCommandLinkButton { background-color: rgb(184, 110, 255); }

                 QCommandLinkButton::pressed { background-color: rgb(255, 110, 181); }

                 QCommandLinkButton::disabled { background-color: rgba(255, 110, 181, 0.2); }"""


class Ui_num_guess(object):
    """Ui Class."""

    def setupUi(self, num_guess):
        """setup ui."""

        self.num_guess = num_guess

        num_guess.setObjectName("num_guess")

        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        num_guess.setFont(font)

        # size
        num_guess.resize(530, 530)
        num_guess.setMinimumSize(QtCore.QSize(530, 530))

        # stylesheet
        num_guess.setStyleSheet("background-color: rgb(255, 255, 255);")

        # main layout
        self.main_layout = QtWidgets.QGridLayout(num_guess)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(5)
        self.main_layout.setObjectName("main_layout")

        # WELCOME #####################################################################
        self.welcome = QtWidgets.QLabel(num_guess)
        # font
        font.setPointSize(18)
        self.welcome.setFont(font)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHeightForWidth(
            self.welcome.sizePolicy().hasHeightForWidth())
        self.welcome.setSizePolicy(sizePolicy)
        self.welcome.setMinimumSize(QtCore.QSize(510, 0))
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
        self.game_box = QtWidgets.QWidget(num_guess)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.game_box.sizePolicy().hasHeightForWidth())
        self.game_box.setSizePolicy(sizePolicy)
        self.game_box.setMinimumSize(QtCore.QSize(510, 300))
        # object name
        self.game_box.setObjectName("game_box")

        # layout
        self.game_box_layout = QtWidgets.QGridLayout(self.game_box)
        self.game_box_layout.setContentsMargins(10, 10, 10, 10)
        self.game_box_layout.setHorizontalSpacing(10)
        self.game_box_layout.setVerticalSpacing(5)
        self.game_box_layout.setObjectName("game_box_layout")

        # TEXT ############################################
        self.text = QtWidgets.QLabel(self.game_box)
        # font
        font.setPointSize(14)
        self.text.setFont(font)
        # size
        self.text.setMinimumSize(QtCore.QSize(275, 0))
        self.text.setMaximumSize(QtCore.QSize(16777215, 600))
        # stylesheet
        self.text.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # allignment
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.text.setObjectName("text")
        # adding to layout
        self.game_box_layout.addWidget(self.text, 0, 0, 3, 1)

        # LEVEL 1 #########################################
        self.level_1 = QtWidgets.QCommandLinkButton(self.game_box)
        # size
        self.level_1.setMaximumSize(QtCore.QSize(16777215, 150))
        # stylesheet
        self.level_1.setStyleSheet(level_style)
        # object name
        self.level_1.setObjectName("level_1")

        self.game_box_layout.addWidget(self.level_1, 0, 1, 1, 2)

        # LEVEL 2 #########################################
        self.level_2 = QtWidgets.QCommandLinkButton(self.game_box)
        # size
        self.level_2.setMaximumSize(QtCore.QSize(16777215, 150))
        # stylesheet
        self.level_2.setStyleSheet(level_style)
        # object name
        self.level_2.setObjectName("level_2")

        self.game_box_layout.addWidget(self.level_2, 1, 1, 1, 2)

        # LEVEL 3 #########################################
        self.level_3 = QtWidgets.QCommandLinkButton(self.game_box)
        # size
        self.level_3.setMaximumSize(QtCore.QSize(16777215, 150))
        # stylesheet
        self.level_3.setStyleSheet(level_style)
        # object name
        self.level_3.setObjectName("level_3")

        self.game_box_layout.addWidget(self.level_3, 2, 1, 1, 2)

        # selecting level
        self.level_1.clicked.connect(self.select_level)
        self.level_2.clicked.connect(self.select_level)
        self.level_3.clicked.connect(self.select_level)

        # SPIN BOX ########################################
        self.spinBox = QtWidgets.QSpinBox(self.game_box)
        # size
        self.spinBox.setMinimumSize(QtCore.QSize(300, 100))
        # object name
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setEnabled(False)

        self.game_box_layout.addWidget(self.spinBox, 3, 0, 1, 2)

        # SUBMIT BUTTON ####################################
        self.submit = QtWidgets.QPushButton(self.game_box)
        # size
        self.submit.setMinimumSize(QtCore.QSize(100, 100))
        # stylesheet
        self.submit.setStyleSheet(button_style)
        # object name
        self.submit.setObjectName("submit")
        self.submit.setEnabled(False)

        self.game_box_layout.addWidget(self.submit, 3, 2, 1, 1)

        # adding to main layout
        self.main_layout.addWidget(self.game_box, 1, 0, 1, 2)

        self.submit.clicked.connect(self.submit_guess)

        # NEW GAME BUTTON ###########################################################
        self.new_game = QtWidgets.QPushButton(num_guess)
        # font
        font.setPointSize(14)
        self.new_game.setFont(font)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.new_game.sizePolicy().hasHeightForWidth())
        self.new_game.setSizePolicy(sizePolicy)
        self.new_game.setMinimumSize(QtCore.QSize(0, 50))
        self.new_game.setMaximumSize(QtCore.QSize(16777215, 50))
        # stylesheet
        self.new_game.setStyleSheet(button_style)
        # object name
        self.new_game.setObjectName("new_game")

        # adding to main layout
        self.main_layout.addWidget(self.new_game, 2, 0, 1, 1)

        # restarting game
        self.new_game.clicked.connect(lambda: self.restart(num_guess))

        ##############################################################################
        self.retranslateUi(num_guess)
        QtCore.QMetaObject.connectSlotsByName(num_guess)

    def retranslateUi(self, num_guess):
        """retransalate."""

        _translate = QtCore.QCoreApplication.translate
        # WINDOW TITLE
        num_guess.setWindowTitle(_translate("num_guess", "num_guess"))

        # WELCOME TEXT
        self.welcome.setText(_translate(
            "num_guess", "WELCOME TO NUMBER GUESSING!"))

        # TEXT TEXT
        self.text.setText(_translate("num_guess", "Choose your level"))

        # LEVELS
        # level 1
        self.level_1.setText(_translate("num_guess", "1. Piece of Cake"))
        # level 2
        self.level_2.setText(_translate("num_guess", "2. Let's Rock!"))
        # level 3
        self.level_3.setText(_translate("num_guess", "3. Damn I'm Good"))

        # SUBMIT TEXT
        self.submit.setText(_translate("num_guess", "Submit"))

        # NEW GAME BUTTON
        self.new_game.setText(_translate("num_guess", "New Game"))

    def restart(self, num_guess):
        """Resets the game for the user."""

        self.level_1.setEnabled(True)
        self.level_2.setEnabled(True)
        self.level_3.setEnabled(True)

        self.retranslateUi(num_guess)
        QtCore.QMetaObject.connectSlotsByName(num_guess)

    def select_level(self):
        """Sets level conditions based on user choice."""

        self.level_1.setEnabled(False)
        self.level_2.setEnabled(False)
        self.level_3.setEnabled(False)

        self.spinBox.setEnabled(True)
        self.submit.setEnabled(True)

        selection = self.num_guess.sender()

        if '1' in selection.text():
            lower_limit = randrange(0, 101, 10)
            upper_limit = lower_limit + 10
            self.num_of_guesses = 5

        elif '2' in selection.text():
            lower_limit = randrange(0, 501, 100)
            upper_limit = lower_limit + 50
            self.num_of_guesses = 5

        else:
            lower_limit = randrange(0, 501, 100)
            upper_limit = lower_limit + 100
            self.num_of_guesses = 3

        self.ans = randint(lower_limit, upper_limit)

        self.spinBox.setMinimum(lower_limit)
        self.spinBox.setMaximum(upper_limit)

        self.text.setText(
            f"Make a guess between\n{lower_limit} & {upper_limit}\nCHANCES LEFT: {self.num_of_guesses}")

    def submit_guess(self):
        """Submits the user's guess and checks answer."""

        self.guess = self.spinBox.value()

        if self.guess == self.ans:
            self.spinBox.setEnabled(False)
            self.submit.setEnabled(False)

            self.text.setText(f"YOU GOT IT!\nThe number was {self.ans}")

        elif self.num_of_guesses > 0 and self.guess > self.ans:
            self.num_of_guesses -= 1

            self.text.setText(
                f"CHANCES LEFT: {self.num_of_guesses}\nTry guessing lower")

        elif self.num_of_guesses > 0 and self.guess < self.ans:
            self.num_of_guesses -= 1

            self.text.setText(
                f"CHANCES LEFT: {self.num_of_guesses}\nTry guessing higher")

        if self.num_of_guesses == 0:
            self.spinBox.setEnabled(False)
            self.submit.setEnabled(False)

            self.text.setText(
                f"YOU LOSE :(\nThe number was {self.ans}")
