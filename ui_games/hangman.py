"""The game of hangman made using python.

Hangman is a paper and pencil guessing game for two or more players. One player
thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting
letters within 6 guesses.

"""

import os
import sys
from random import choice
from PyQt5 import QtCore, QtGui, QtWidgets


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


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

letter_style = """QPushButton { background-color: rgb(255, 255, 255);
                                 color: rgb(0, 0, 0);
                                 border: 1px solid rgb(0, 0, 0);
                                 border-radius: 5px;
                                 font-size: 36px; }
                
                QPushButton::pressed { background-color: rgb(0, 0, 0);
                                       color: rgb(255, 255, 255); }
                
                QPushButton::disabled { background-color: rgba(0, 0, 0, 0.2);
                                        color: rgb(75, 75, 75); }"""


class Ui_hangman(object):
    """Ui Class."""

    def setupUi(self, hangman):
        """setup ui."""

        self.hangman = hangman

        hangman.setObjectName("hangman")

        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        hangman.setFont(font)

        # size
        hangman.resize(530, 530)
        hangman.setMinimumSize(QtCore.QSize(530, 530))

        # stylesheet
        hangman.setStyleSheet("background-color: rgb(255, 255, 255);")

        # main layout
        self.main_layout = QtWidgets.QGridLayout(hangman)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setHorizontalSpacing(20)
        self.main_layout.setVerticalSpacing(5)
        self.main_layout.setObjectName("main_layout")

        # WELCOME #############################################################
        self.welcome = QtWidgets.QLabel(hangman)
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

        # GAME BOX ##############################################################
        self.game_box = QtWidgets.QWidget(hangman)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.game_box.sizePolicy().hasHeightForWidth())
        self.game_box.setSizePolicy(sizePolicy)
        # object name
        self.game_box.setObjectName("game_box")

        # layout
        self.game_box_layout = QtWidgets.QGridLayout(self.game_box)
        self.game_box_layout.setContentsMargins(10, 10, 10, 10)
        self.game_box_layout.setSpacing(5)
        self.game_box_layout.setObjectName("game_box_layout")

        # IMAGE ##############################################
        self.image = QtWidgets.QLabel(self.game_box)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(True)
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QtCore.QSize(200, 200))
        # allignment
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        # setting image
        self.image.setPixmap(QtGui.QPixmap(resource_path(
            "static/images/hangman/0.png"
        )))
        self.image.setScaledContents(True)
        # object name
        self.image.setObjectName("image")

        self.game_box_layout.addWidget(self.image, 0, 0, 1, 1)

        # LETTERS #############################################
        self.letters = QtWidgets.QScrollArea(self.game_box)
        self.letters.setStyleSheet(letter_style)
        self.letters.setWidgetResizable(True)
        self.letters.setObjectName("letters")

        # LETTER BUTTONS #####
        self.letter_buttons = QtWidgets.QWidget()
        self.letter_buttons.setGeometry(QtCore.QRect(0, 0, 263, 606))
        self.letter_buttons.setObjectName("letter_buttons")

        # layout
        self.letters_layout = QtWidgets.QGridLayout(self.letter_buttons)
        self.letters_layout.setContentsMargins(10, 10, 10, 10)
        self.letters_layout.setSpacing(5)
        self.letters_layout.setObjectName("letters_layout")

        # the letters
        # a
        self.button_a = QtWidgets.QPushButton(self.letter_buttons)
        self.button_a.setMinimumSize(QtCore.QSize(20, 20))
        self.button_a.setObjectName("button_a")
        self.letters_layout.addWidget(self.button_a, 0, 0, 1, 1)

        # b
        self.button_b = QtWidgets.QPushButton(self.letter_buttons)
        self.button_b.setMinimumSize(QtCore.QSize(20, 20))
        self.button_b.setObjectName("button_b")
        self.letters_layout.addWidget(self.button_b, 0, 1, 1, 1)

        # c
        self.button_c = QtWidgets.QPushButton(self.letter_buttons)
        self.button_c.setMinimumSize(QtCore.QSize(20, 20))
        self.button_c.setObjectName("button_c")
        self.letters_layout.addWidget(self.button_c, 0, 2, 1, 1)

        # d
        self.button_d = QtWidgets.QPushButton(self.letter_buttons)
        self.button_d.setMinimumSize(QtCore.QSize(20, 20))
        self.button_d.setObjectName("button_d")
        self.letters_layout.addWidget(self.button_d, 1, 0, 1, 1)

        # e
        self.button_e = QtWidgets.QPushButton(self.letter_buttons)
        self.button_e.setMinimumSize(QtCore.QSize(20, 20))
        self.button_e.setObjectName("button_e")
        self.letters_layout.addWidget(self.button_e, 1, 1, 1, 1)

        # f
        self.button_f = QtWidgets.QPushButton(self.letter_buttons)
        self.button_f.setMinimumSize(QtCore.QSize(20, 20))
        self.button_f.setObjectName("button_f")
        self.letters_layout.addWidget(self.button_f, 1, 2, 1, 1)

        # g
        self.button_g = QtWidgets.QPushButton(self.letter_buttons)
        self.button_g.setMinimumSize(QtCore.QSize(20, 20))
        self.button_g.setObjectName("button_g")
        self.letters_layout.addWidget(self.button_g, 2, 0, 1, 1)

        # h
        self.button_h = QtWidgets.QPushButton(self.letter_buttons)
        self.button_h.setMinimumSize(QtCore.QSize(20, 20))
        self.button_h.setObjectName("button_h")
        self.letters_layout.addWidget(self.button_h, 2, 1, 1, 1)

        # i
        self.button_i = QtWidgets.QPushButton(self.letter_buttons)
        self.button_i.setMinimumSize(QtCore.QSize(20, 20))
        self.button_i.setObjectName("button_i")
        self.letters_layout.addWidget(self.button_i, 2, 2, 1, 1)

        # j
        self.button_j = QtWidgets.QPushButton(self.letter_buttons)
        self.button_j.setMinimumSize(QtCore.QSize(20, 20))
        self.button_j.setObjectName("button_j")
        self.letters_layout.addWidget(self.button_j, 3, 0, 1, 1)

        # k
        self.button_k = QtWidgets.QPushButton(self.letter_buttons)
        self.button_k.setMinimumSize(QtCore.QSize(20, 20))
        self.button_k.setObjectName("button_k")
        self.letters_layout.addWidget(self.button_k, 3, 1, 1, 1)

        # l
        self.button_l = QtWidgets.QPushButton(self.letter_buttons)
        self.button_l.setMinimumSize(QtCore.QSize(20, 20))
        self.button_l.setObjectName("button_l")
        self.letters_layout.addWidget(self.button_l, 3, 2, 1, 1)

        # m
        self.button_m = QtWidgets.QPushButton(self.letter_buttons)
        self.button_m.setMinimumSize(QtCore.QSize(20, 20))
        self.button_m.setObjectName("button_m")
        self.letters_layout.addWidget(self.button_m, 4, 0, 1, 1)

        # n
        self.button_n = QtWidgets.QPushButton(self.letter_buttons)
        self.button_n.setMinimumSize(QtCore.QSize(20, 20))
        self.button_n.setObjectName("button_n")
        self.letters_layout.addWidget(self.button_n, 4, 1, 1, 1)

        # o
        self.button_o = QtWidgets.QPushButton(self.letter_buttons)
        self.button_o.setMinimumSize(QtCore.QSize(20, 20))
        self.button_o.setObjectName("button_o")
        self.letters_layout.addWidget(self.button_o, 4, 2, 1, 1)

        # p
        self.button_p = QtWidgets.QPushButton(self.letter_buttons)
        self.button_p.setMinimumSize(QtCore.QSize(20, 20))
        self.button_p.setObjectName("button_p")
        self.letters_layout.addWidget(self.button_p, 5, 0, 1, 1)

        # q
        self.button_q = QtWidgets.QPushButton(self.letter_buttons)
        self.button_q.setMinimumSize(QtCore.QSize(20, 20))
        self.button_q.setObjectName("button_q")
        self.letters_layout.addWidget(self.button_q, 5, 1, 1, 1)

        # r
        self.button_r = QtWidgets.QPushButton(self.letter_buttons)
        self.button_r.setMinimumSize(QtCore.QSize(20, 20))
        self.button_r.setObjectName("button_r")
        self.letters_layout.addWidget(self.button_r, 5, 2, 1, 1)

        # s
        self.button_s = QtWidgets.QPushButton(self.letter_buttons)
        self.button_s.setMinimumSize(QtCore.QSize(20, 20))
        self.button_s.setObjectName("button_s")
        self.letters_layout.addWidget(self.button_s, 6, 0, 1, 1)

        # t
        self.button_t = QtWidgets.QPushButton(self.letter_buttons)
        self.button_t.setMinimumSize(QtCore.QSize(20, 20))
        self.button_t.setObjectName("button_t")
        self.letters_layout.addWidget(self.button_t, 6, 1, 1, 1)

        # u
        self.button_u = QtWidgets.QPushButton(self.letter_buttons)
        self.button_u.setMinimumSize(QtCore.QSize(20, 20))
        self.button_u.setObjectName("button_u")
        self.letters_layout.addWidget(self.button_u, 6, 2, 1, 1)

        # v
        self.button_v = QtWidgets.QPushButton(self.letter_buttons)
        self.button_v.setMinimumSize(QtCore.QSize(20, 20))
        self.button_v.setObjectName("button_v")
        self.letters_layout.addWidget(self.button_v, 7, 0, 1, 1)

        # w
        self.button_w = QtWidgets.QPushButton(self.letter_buttons)
        self.button_w.setMinimumSize(QtCore.QSize(20, 20))
        self.button_w.setObjectName("button_w")
        self.letters_layout.addWidget(self.button_w, 7, 1, 1, 1)

        # x
        self.button_x = QtWidgets.QPushButton(self.letter_buttons)
        self.button_x.setMinimumSize(QtCore.QSize(20, 20))
        self.button_x.setObjectName("button_x")
        self.letters_layout.addWidget(self.button_x, 7, 2, 1, 1)

        # y
        self.button_y = QtWidgets.QPushButton(self.letter_buttons)
        self.button_y.setMinimumSize(QtCore.QSize(20, 20))
        self.button_y.setObjectName("button_y")
        self.letters_layout.addWidget(self.button_y, 8, 0, 1, 1)

        # z
        self.button_z = QtWidgets.QPushButton(self.letter_buttons)
        self.button_z.setMinimumSize(QtCore.QSize(20, 20))
        self.button_z.setObjectName("button_z")
        self.letters_layout.addWidget(self.button_z, 8, 1, 1, 1)
        self.letters.setWidget(self.letter_buttons)

        self.game_box_layout.addWidget(self.letters, 0, 1, 1, 1)

        # adding to main layout
        self.main_layout.addWidget(self.game_box, 1, 0, 1, 2)

        # click click
        for button in self.letter_buttons.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.guess_letter)

        # THE WORD #####################################################################
        self.text = QtWidgets.QLabel(hangman)
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

        # NEW GAME BUTTON ######################################################
        self.new_game = QtWidgets.QPushButton(hangman)
        # font
        font.setPointSize(14)
        self.new_game.setFont(font)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
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
        self.new_game.clicked.connect(lambda: self.restart(hangman))

        # OTHER VARIABLES ##########################################################
        self.the_words = ['python', 'hangman', 'games', 'rainbow', 'phoenix', 'rhythm',
                          'dragon', 'dog', 'cat', 'paint', 'rock', 'paper', 'scissors',
                          'chocolate', 'pizza', 'burger', 'egg', 'chicken', 'cheese',
                          'mathematics', 'morning', 'afternoon', 'night', 'disney',
                          'netflix', 'microsoft', 'google']

        self.all_guesses = []

        self.word = choice(self.the_words)
        self.length = len(self.word)

        self.count = 0

        ###########################################################################
        self.retranslateUi(hangman)
        QtCore.QMetaObject.connectSlotsByName(hangman)

    def retranslateUi(self, hangman):
        """retransalate."""

        _translate = QtCore.QCoreApplication.translate
        # WINDOW TITLE
        hangman.setWindowTitle(_translate("hangman", "hangman"))

        # WELCOME
        self.welcome.setText(_translate("hangman", "WELCOME TO HANGMAN!"))

        # LETTERS
        self.button_a.setText(_translate("hangman", "A"))
        self.button_b.setText(_translate("hangman", "B"))
        self.button_c.setText(_translate("hangman", "C"))
        self.button_d.setText(_translate("hangman", "D"))
        self.button_e.setText(_translate("hangman", "E"))
        self.button_f.setText(_translate("hangman", "F"))
        self.button_g.setText(_translate("hangman", "G"))
        self.button_h.setText(_translate("hangman", "H"))
        self.button_i.setText(_translate("hangman", "I"))
        self.button_j.setText(_translate("hangman", "J"))
        self.button_k.setText(_translate("hangman", "K"))
        self.button_l.setText(_translate("hangman", "L"))
        self.button_m.setText(_translate("hangman", "M"))
        self.button_n.setText(_translate("hangman", "N"))
        self.button_o.setText(_translate("hangman", "O"))
        self.button_p.setText(_translate("hangman", "P"))
        self.button_q.setText(_translate("hangman", "Q"))
        self.button_r.setText(_translate("hangman", "R"))
        self.button_s.setText(_translate("hangman", "S"))
        self.button_t.setText(_translate("hangman", "T"))
        self.button_u.setText(_translate("hangman", "U"))
        self.button_v.setText(_translate("hangman", "V"))
        self.button_w.setText(_translate("hangman", "W"))
        self.button_x.setText(_translate("hangman", "X"))
        self.button_y.setText(_translate("hangman", "Y"))
        self.button_z.setText(_translate("hangman", "Z"))

        # THE WORD
        self.text.setFont(QtGui.QFont("Microsoft JhengHei UI", 16))
        self.text.setText(_translate("hangman", "_ "*self.length))

        # NEW GAME BUTTON
        self.new_game.setText(_translate("hangman", "New Game"))

    def restart(self, hangman):
        """Resets the game for the user."""

        # enabling buttons
        for button in self.letter_buttons.findChildren(QtWidgets.QPushButton):
            button.setEnabled(True)

        # setting image
        self.image.setPixmap(QtGui.QPixmap(resource_path(
            "static/images/hangman/0.png"
        )))
        self.image.setScaledContents(True)

        # setting new word
        self.word = choice(self.the_words)
        self.length = len(self.word)

        # resetting guesses
        self.all_guesses = []

        # resetting count
        self.count = 0

        self.retranslateUi(hangman)
        QtCore.QMetaObject.connectSlotsByName(hangman)

    def guess_letter(self):
        """Matches the letter guessed by user to the word."""

        self.hangman.sender().setEnabled(False)

        guess = self.hangman.sender().text().lower()
        self.all_guesses.append(guess)

        current = ''

        if guess not in self.word:
            self.count += 1
            self.image.setPixmap(QtGui.QPixmap(resource_path(
                f"static/images/hangman/{self.count}.png"
            )))
            self.image.setScaledContents(True)

        for letter in self.word:
            if letter in self.all_guesses:
                current += letter
            else:
                current += '_'

            current += ' '

        self.text.setText(current)

        if '_' not in current:
            self.text.setFont(QtGui.QFont("Microsoft JhengHei UI", 14))
            self.text.setText(f"YOU GOT IT!\nThe word was {self.word}")

        if self.count == 6:
            self.text.setText("Game Over")
            for button in self.letter_buttons.findChildren(QtWidgets.QPushButton):
                button.setEnabled(False)
