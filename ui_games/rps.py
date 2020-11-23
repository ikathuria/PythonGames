"""The game of Rock Paper Scissors made using python.

Rock Paper Scissors is a hand game usually played between 2 people, in
which each player simultaneously forming one of the three shapes which are
rock, paper and scissors. There are two outcomes for the game, either a draw
or one of the players winning.

Rock beats scissors, scissors beats paper and paper beats rock.

There is a one player option where the user gets to play against the computer
and a two player option when the user wants to play with a friend.

This program uses the `random` module for the one player mode.

"""

from random import choice
from PyQt5 import QtCore, QtGui, QtWidgets

the_choices = ['Rock', 'Paper', 'Scissors']

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


class Ui_rps(object):
    """Ui Class."""

    def setupUi(self, rps):
        """setup ui."""

        self.rps = rps

        rps.setObjectName("rps")

        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        rps.setFont(font)

        # size
        rps.resize(530, 530)
        rps.setMinimumSize(QtCore.QSize(530, 530))

        # stylesheet
        rps.setStyleSheet("background-color: rgb(255, 255, 255);")

        # main layout
        self.main_layout = QtWidgets.QGridLayout(rps)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setHorizontalSpacing(20)
        self.main_layout.setVerticalSpacing(5)
        self.main_layout.setObjectName("main_layout")

        # WELCOME ##################################################################
        self.welcome = QtWidgets.QLabel(rps)
        # font
        font.setPointSize(16)
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

        # CHOICE WIDGET #################################################################
        self.choice_widget = QtWidgets.QWidget(rps)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.choice_widget.sizePolicy().hasHeightForWidth())
        self.choice_widget.setSizePolicy(sizePolicy)
        # object name
        self.choice_widget.setObjectName("choice_widget")

        # layout
        self.choices_layout = QtWidgets.QGridLayout(self.choice_widget)
        self.choices_layout.setContentsMargins(10, 10, 10, 10)
        self.choices_layout.setSpacing(5)
        self.choices_layout.setObjectName("choices_layout")

        # PLAYER CHOICE ###############################################
        self.player = QtWidgets.QLabel(self.choice_widget)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(True)
        self.player.setSizePolicy(sizePolicy)
        self.player.setMinimumSize(QtCore.QSize(210, 210))
        # stylesheet
        self.player.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # allignment
        self.player.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player.setObjectName("player")

        self.choices_layout.addWidget(self.player, 0, 0, 1, 1)

        # VS LABEL #####################################################
        self.vs_label = QtWidgets.QLabel(self.choice_widget)
        # font
        font.setPointSize(12)
        self.vs_label.setFont(font)
        # allignment
        self.vs_label.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.vs_label.setObjectName("vs_label")

        self.choices_layout.addWidget(self.vs_label, 0, 1, 1, 1)

        # COMPUTER CHOICE #############################################
        self.computer = QtWidgets.QLabel(self.choice_widget)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(True)
        self.computer.setSizePolicy(sizePolicy)
        self.computer.setMinimumSize(QtCore.QSize(210, 210))
        # stylesheet
        self.computer.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # allignment
        self.computer.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.computer.setObjectName("computer")

        self.choices_layout.addWidget(self.computer, 0, 2, 1, 1)

        # adding to main layout
        self.main_layout.addWidget(self.choice_widget, 1, 0, 1, 2)

        # BUTTONS ##############################################################################
        self.buttons = QtWidgets.QWidget(rps)
        # font
        font.setPointSize(12)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setMinimumSize(QtCore.QSize(510, 0))
        # stylesheet
        self.buttons.setStyleSheet(button_style)
        # object name
        self.buttons.setObjectName("buttons")

        # layout
        self.buttons_layout = QtWidgets.QGridLayout(self.buttons)
        self.buttons_layout.setContentsMargins(10, 10, 10, 10)
        self.buttons_layout.setSpacing(10)
        self.buttons_layout.setObjectName("buttons_layout")

        # ROCK #####
        self.rock = QtWidgets.QPushButton(self.buttons)
        self.rock.setFont(font)
        self.rock.setMinimumSize(QtCore.QSize(0, 60))
        self.rock.setObjectName("rock")

        self.buttons_layout.addWidget(self.rock, 0, 0, 1, 1)

        # PAPER #####
        self.paper = QtWidgets.QPushButton(self.buttons)
        self.paper.setFont(font)
        self.paper.setMinimumSize(QtCore.QSize(0, 60))
        self.paper.setObjectName("paper")

        self.buttons_layout.addWidget(self.paper, 0, 1, 1, 1)

        # SCISSORS #####
        self.scissors = QtWidgets.QPushButton(self.buttons)
        self.scissors.setFont(font)
        self.scissors.setMinimumSize(QtCore.QSize(0, 60))
        self.scissors.setObjectName("scissors")

        self.buttons_layout.addWidget(self.scissors, 0, 2, 1, 1)

        # adding to main layout
        self.main_layout.addWidget(
            self.buttons, 2, 0, 1, 2, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        # click click
        self.rock.clicked.connect(self.choose_option)
        self.paper.clicked.connect(self.choose_option)
        self.scissors.clicked.connect(self.choose_option)

        # TEXT ##########################################################################
        self.text = QtWidgets.QLabel(rps)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(
            self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setMinimumSize(QtCore.QSize(300, 75))
        # stylesheet
        self.text.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # styleheet
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.text.setObjectName("text")

        # adding to main layout
        self.main_layout.addWidget(self.text, 3, 0, 1, 1)

        # NEW GAME BUTTON ####################################################################
        self.new_game = QtWidgets.QPushButton(rps)
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
        self.main_layout.addWidget(self.new_game, 3, 1, 1, 1)

        # restarting game
        self.new_game.clicked.connect(lambda: self.restart(rps))

        ####################################################################################
        self.retranslateUi(rps)
        QtCore.QMetaObject.connectSlotsByName(rps)

    def retranslateUi(self, rps):
        """retransalate."""

        _translate = QtCore.QCoreApplication.translate
        # WINDOW TITLE
        rps.setWindowTitle(_translate("rps", "rps"))

        # WELCOME
        self.welcome.setText(_translate(
            "rps", "WELCOME TO ROCK-PAPER-SCISSORS!"))

        # PLAYER CHOICE
        self.player.setText(_translate("rps", "Player"))

        # VS LABEL
        self.vs_label.setText(_translate("rps", "Vs."))

        # COMPUTER CHOICE
        self.computer.setText(_translate("rps", "Computer"))

        # BUTTONS
        # rock
        self.rock.setText(_translate("rps", "Rock"))
        # paper
        self.paper.setText(_translate("rps", "Paper"))
        # scissors
        self.scissors.setText(_translate("rps", "Scissors"))

        # TEXT
        self.text.setText(_translate("rps", "Make your choice"))

        # NEW GAME BUTTON
        self.new_game.setText(_translate("rps", "New Game"))

    def restart(self, rps):
        """Resets the game for the user."""

        self.rock.setEnabled(True)
        self.paper.setEnabled(True)
        self.scissors.setEnabled(True)

        self.retranslateUi(rps)
        QtCore.QMetaObject.connectSlotsByName(rps)
    
    def win_check(self):
        """Check winning conditions."""

        player_wins = "Player WINS!"
        computer_wins = "Computer WINS!"

        if self.player_choice == self.computer_choice:
            self.text.setText("TIE!")

        # rock
        elif self.player_choice == "Rock":

            if self.computer_choice == "Paper":
                self.text.setText(
                    f"{computer_wins} {self.computer_choice} covers {self.player_choice}")

            else:
                self.text.setText(
                    f"{player_wins} {self.player_choice} smashes {self.computer_choice}")

        # paper
        elif self.player_choice == "Paper":

            if self.computer_choice == "Scissors":
                self.text.setText(
                    f"{computer_wins} {self.computer_choice} cuts {self.player_choice}")

            else:
                self.text.setText(
                    f"{player_wins} {self.player_choice} covers {self.computer_choice}")

        # scissors
        elif self.player_choice == "Scissors":

            if self.computer_choice == "Rock":
                self.text.setText(
                    f"{computer_wins} {self.computer_choice} smashes {self.player_choice}")

            else:
                self.text.setText(
                    f"{player_wins} {self.player_choice} cuts {self.computer_choice}")

        self.rock.setEnabled(False)
        self.paper.setEnabled(False)
        self.scissors.setEnabled(False)
    
    def choose_option(self):
        self.computer_choice = choice(the_choices)

        self.player_choice = self.rps.sender().text()

        self.player.setPixmap(QtGui.QPixmap(
            f"ui_games/images/rps/{self.player_choice.lower()}.png"))
        self.player.setScaledContents(True)

        self.computer.setPixmap(
            QtGui.QPixmap(f"ui_games/images/rps/{self.computer_choice.lower()}.png"))
        self.computer.setScaledContents(True)

        self.win_check()
