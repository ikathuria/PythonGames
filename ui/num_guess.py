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
                
                QPushButton::disabled { background-color: rgb(0, 0, 0, 0.2);
                                        color: rgb(75, 75, 75); }"""


class Ui_num_guessing(object):

    def setupUi(self, num_guessing):
        # object name
        num_guessing.setObjectName("num_guessing")
        # size
        num_guessing.resize(730, 775)
        num_guessing.setMaximumSize(QtCore.QSize(730, 775))
        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        num_guessing.setFont(font)
        # stylesheet
        num_guessing.setStyleSheet("background-color: rgb(255, 255, 255);")
        # layout
        self.main_layout = QtWidgets.QGridLayout(num_guessing)
        self.main_layout.setObjectName("main_layout")

        # WELCOME ##############################################
        self.welcome = QtWidgets.QLabel(num_guessing)
        # size
        self.welcome.setMinimumSize(QtCore.QSize(700, 0))
        self.welcome.setMaximumSize(QtCore.QSize(700, 100))
        # font
        font.setPointSize(25)
        self.welcome.setFont(font)
        # stylesheet
        self.welcome.setStyleSheet("background-color: rgb(255, 255, 255);"
                                   "border: 1px solid rgb(0, 0, 0);")
        # allignment
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.welcome.setObjectName("welcome")
        # adding to main widget
        self.main_layout.addWidget(self.welcome, 0, 0, 1, 1)

        # DIFFICULTY WIDGET ##################################################
        self.difficulty_widget = QtWidgets.QWidget(num_guessing)
        # size
        self.difficulty_widget.setMinimumSize(QtCore.QSize(700, 100))
        self.difficulty_widget.setMaximumSize(QtCore.QSize(700, 100))
        # font
        self.difficulty_widget.setFont(font)
        # stylesheet
        self.difficulty_widget.setStyleSheet(
            "background-color: rgb(253, 213, 255);")
        # object name
        self.difficulty_widget.setObjectName("difficulty_widget")
        # layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.difficulty_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # DIFFICULTY LABEL #####
        self.difficult = QtWidgets.QLabel(self.difficulty_widget)
        # font
        font.setPointSize(14)
        self.difficult.setFont(font)
        # alignment
        self.difficult.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.difficult.setObjectName("difficult")
        # add to widget
        self.horizontalLayout.addWidget(self.difficult)

        # LEVELS COMBOBOX #####
        self.levels = QtWidgets.QComboBox(self.difficulty_widget)
        # font
        font.setPointSize(14)
        self.levels.setFont(font)
        # stylesheet
        self.levels.setStyleSheet("background-color: rgb(226, 255, 252);")
        # object name
        self.levels.setObjectName("levels")
        # items
        self.levels.addItem("")
        self.levels.addItem("")
        self.levels.addItem("")
        # add to widget
        self.horizontalLayout.addWidget(self.levels)

        # LET"S START BUTTON #####
        self.start = QtWidgets.QPushButton(self.difficulty_widget)
        # # size
        # self.start.setMinimumSize(QtCore.QSize(150, 150))
        # self.start.setMaximumSize(QtCore.QSize(150, 150))
        # font
        font.setPointSize(12)
        self.start.setFont(font)
        # stylesheet
        self.start.setStyleSheet(button_style)
        # object name
        self.start.setObjectName("start")
        # add to widget
        self.horizontalLayout.addWidget(self.start)

        # click click
        self.start.clicked.connect(self.level)

        # add to main widget
        self.main_layout.addWidget(self.difficulty_widget, 1, 0, 1, 1)

        # GUESS WIDGET #################################################
        self.outer_guess_widget = QtWidgets.QWidget(num_guessing)
        # size
        self.outer_guess_widget.setMaximumSize(QtCore.QSize(16777215, 400))
        # font
        self.outer_guess_widget.setFont(font)
        # stylesheet
        self.outer_guess_widget.setStyleSheet(
            "background-color: rgb(255, 252, 165);")
        # object name
        self.outer_guess_widget.setObjectName("outer_guess_widget")
        # layout
        self.gridLayout = QtWidgets.QGridLayout(self.outer_guess_widget)
        self.gridLayout.setObjectName("gridLayout")

        # CHANCES LABEL #####
        self.chances = QtWidgets.QLabel(self.outer_guess_widget)
        # size
        self.chances.setMaximumSize(QtCore.QSize(16777215, 100))
        # font
        font.setPointSize(16)
        self.chances.setFont(font)
        # alignment
        self.chances.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.chances.setObjectName("chances")
        # layout
        self.gridLayout.addWidget(self.chances, 1, 0, 1, 1)

        # MAKE YOUR GUESS LABEL #####
        self.make_your_guess = QtWidgets.QLabel(self.outer_guess_widget)
        # size
        self.make_your_guess.setMaximumSize(QtCore.QSize(16777215, 100))
        # font
        font.setPointSize(26)
        self.make_your_guess.setFont(font)
        # stylesheet
        self.make_your_guess.setStyleSheet("border-radius: 10px;"
                                           "border: 1.5px dashed black;")
        # allignment
        self.make_your_guess.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.make_your_guess.setObjectName("make_your_guess")
        # add to widget
        self.gridLayout.addWidget(self.make_your_guess, 0, 0, 1, 1)

        # inner widget
        self.guess_widget = QtWidgets.QWidget(self.outer_guess_widget)
        # size
        self.guess_widget.setMinimumSize(QtCore.QSize(0, 200))
        # object name
        self.guess_widget.setObjectName("guess_widget")
        # layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.guess_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # SPIN BOX #####
        self.spinBox = QtWidgets.QSpinBox(self.guess_widget)
        # size
        self.spinBox.setMinimumSize(QtCore.QSize(400, 100))
        self.spinBox.setMaximumSize(QtCore.QSize(400, 100))
        # font
        font.setPointSize(14)
        self.spinBox.setFont(font)
        # stylesheet
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        # object name
        self.spinBox.setObjectName("spinBox")
        # add to inner widget
        self.horizontalLayout_2.addWidget(self.spinBox)

        # SUBMIT BUTTON #####
        self.submit_button = QtWidgets.QPushButton(self.guess_widget)
        # size
        self.submit_button.setMinimumSize(QtCore.QSize(150, 150))
        self.submit_button.setMaximumSize(QtCore.QSize(150, 150))
        # font
        font.setPointSize(12)
        self.submit_button.setFont(font)
        # stylesheet
        self.submit_button.setStyleSheet(button_style)
        # object name
        self.submit_button.setObjectName("submit_button")
        # add to widget
        self.horizontalLayout_2.addWidget(self.submit_button)

        # click click
        self.submit_button.clicked.connect(self.submit)

        # add to outer widget
        self.gridLayout.addWidget(self.guess_widget, 2, 0, 1, 1)

        # add to main widget
        self.main_layout.addWidget(self.outer_guess_widget, 2, 0, 1, 1)

        # NEW GAME BUTTON #################################################
        self.new_game = QtWidgets.QPushButton(num_guessing)
        # size
        self.new_game.setMinimumSize(QtCore.QSize(500, 50))
        # font
        font.setPointSize(14)
        self.new_game.setFont(font)
        # stylesheet
        self.new_game.setStyleSheet(button_style)
        # object name
        self.new_game.setObjectName("new_game")
        # layout
        self.main_layout.addWidget(self.new_game, 3, 0, 1, 1)

        # restarting game
        self.new_game.clicked.connect(lambda: self.restart(num_guessing))

        ###################################################################
        self.retranslateUi(num_guessing)
        QtCore.QMetaObject.connectSlotsByName(num_guessing)

    def retranslateUi(self, num_guessing):

        _translate = QtCore.QCoreApplication.translate

        # window title
        num_guessing.setWindowTitle(_translate("num_guessing", "num_guessing"))

        # welcome label
        self.welcome.setText(_translate(
            "TicTacToe", "WELCOME TO NUMBER GUESSING!"))

        # difficulty text
        self.difficult.setText(_translate(
            "num_guessing", "Choose your difficulty level:"))

        # levels items
        # 1
        self.levels.setItemText(0, _translate(
            "num_guessing", "1. Piece of Cake"))
        # 2
        self.levels.setItemText(1, _translate(
            "num_guessing", "2. Let\'s Rock"))
        # 3
        self.levels.setItemText(2, _translate(
            "num_guessing", "3. Damn I\'m Good"))

        # start text
        self.start.setText(_translate("num_guessing", "START!"))

        # chances text
        self.chances.setText(_translate("num_guessing", "CHANCES LEFT: X"))

        # make your guess
        self.make_your_guess.setText(_translate(
            "num_guessing", "Let's start guessing!"))

        # submit text
        self.submit_button.setText(_translate("num_guessing", "Submit Guess"))

        self.spinBox.setEnabled(False)
        self.submit_button.setEnabled(False)

        # new game text
        self.new_game.setText(_translate("num_guessing", "New Game"))

    def restart(self, num_guessing):
        self.levels.setEnabled(True)
        self.start.setEnabled(True)

        self.retranslateUi(num_guessing)
        QtCore.QMetaObject.connectSlotsByName(num_guessing)

    def level(self):
        selection = self.levels.currentText()
        self.levels.setEnabled(False)
        self.start.setEnabled(False)

        if selection.startswith('1'):
            lower_limit = random.randrange(0, 101, 10)
            upper_limit = lower_limit + 10
            self.num_of_guesses = 5

        elif selection.startswith('2'):
            lower_limit = random.randrange(0, 501, 100)
            upper_limit = lower_limit + 50
            self.num_of_guesses = 5

        else:
            lower_limit = random.randrange(0, 501, 100)
            upper_limit = lower_limit + 100
            self.num_of_guesses = 3

        self.ans = random.randint(lower_limit, upper_limit)

        self.spinBox.setMinimum(lower_limit)
        self.spinBox.setMaximum(upper_limit)

        self.spinBox.setEnabled(True)
        self.submit_button.setEnabled(True)

        self.make_your_guess.setText(
            f"Make a guess between {lower_limit} & {upper_limit}")
        self.chances.setText(f"CHANCES LEFT: {self.num_of_guesses}")

    def submit(self):
        self.guess = self.spinBox.value()

        if self.guess == self.ans:
            self.spinBox.setEnabled(False)
            self.submit_button.setEnabled(False)

            self.make_your_guess.setText("YOU GOT IT!")

        elif self.num_of_guesses > 0 and self.guess > self.ans:
            self.num_of_guesses -= 1

            self.chances.setText(f"CHANCES LEFT: {self.num_of_guesses}")
            self.make_your_guess.setText("Try guessing lower")

        elif self.num_of_guesses > 0 and self.guess < self.ans:
            self.num_of_guesses -= 1

            self.chances.setText(f"CHANCES LEFT: {self.num_of_guesses}")
            self.make_your_guess.setText("Try guessing higher")

        if self.num_of_guesses == 0:
            self.spinBox.setEnabled(False)
            self.submit_button.setEnabled(False)

            self.make_your_guess.setText(
                f"YOU LOSE :(\nThe number was {self.ans}")
