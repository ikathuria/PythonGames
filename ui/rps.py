"""Rock Paper Scissors."""

# imports
from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice

the_choices = ['Rock', 'Paper', 'Scissors']

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


class Ui_RockPaperScissors(object):
    """Main widget class."""

    def setupUi(self, RockPaperScissors):
        """Setting up."""

        # object name
        RockPaperScissors.setObjectName("RockPaperScissors")
        # size
        RockPaperScissors.resize(730, 775)
        RockPaperScissors.setMaximumSize(QtCore.QSize(730, 775))
        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        RockPaperScissors.setFont(font)
        # stylesheet
        RockPaperScissors.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # layout
        self.main_layout = QtWidgets.QGridLayout(RockPaperScissors)
        self.main_layout.setObjectName("main_layout")

        # WELCOME ##############################################################
        self.welcome = QtWidgets.QLabel(RockPaperScissors)
        # size
        self.welcome.setMinimumSize(QtCore.QSize(700, 0))
        # font
        font.setPointSize(23)
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

        # PLAYERS OUTER WIDGET ##############################################
        self.players_widget = QtWidgets.QWidget(RockPaperScissors)
        # size
        self.players_widget.setMinimumSize(QtCore.QSize(700, 500))
        self.players_widget.setMaximumSize(QtCore.QSize(700, 500))
        # font
        font.setPointSize(20)
        self.players_widget.setFont(font)
        # object name
        self.players_widget.setObjectName("players_widget")
        # layout
        self.players_layout = QtWidgets.QGridLayout(self.players_widget)
        self.players_layout.setContentsMargins(15, 0, 15, 0)
        self.players_layout.setSpacing(10)
        self.players_layout.setObjectName("players_layout")

        # PLAYER ##########################################################
        # CHOICE IMAGE #####
        self.player_image = QtWidgets.QLabel(self.players_widget)
        # size
        self.player_image.setMinimumSize(QtCore.QSize(230, 230))
        self.player_image.setMaximumSize(QtCore.QSize(230, 230))
        # stylesheet
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.player_image.setGraphicsEffect(shadow)
        self.player_image.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # image
        self.player_image.setPixmap(QtGui.QPixmap("ui/images/rock.png"))
        self.player_image.setScaledContents(True)
        # allignment
        self.player_image.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.player_image.setObjectName("player_image")

        # adding widget 1 to outer widget
        self.players_layout.addWidget(self.player_image, 0, 0, 1, 1)

        # VS. LABEL inside players_widget ##########################
        self.vs_label = QtWidgets.QLabel(self.players_widget)
        # size
        self.vs_label.setMinimumSize(QtCore.QSize(175, 0))
        self.vs_label.setMaximumSize(QtCore.QSize(175, 230))
        # font
        font.setPointSize(28)
        self.vs_label.setFont(font)
        # allignment
        self.vs_label.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.vs_label.setObjectName("vs_label")
        # layout
        self.players_layout.addWidget(self.vs_label, 0, 1, 1, 1)

        # COMPUTER #################################################
        # CHOICE IMAGE #####
        self.computer_image = QtWidgets.QLabel(self.players_widget)
        # size
        self.computer_image.setMinimumSize(QtCore.QSize(230, 230))
        self.computer_image.setMaximumSize(QtCore.QSize(230, 230))
        # stylesheet
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.computer_image.setGraphicsEffect(shadow)
        self.computer_image.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # image
        self.computer_image.setPixmap(QtGui.QPixmap("ui/images/rock.png"))
        self.computer_image.setScaledContents(True)
        # allignment
        self.computer_image.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.computer_image.setObjectName("computer_image")

        # adding widget 2 to outer widget
        self.players_layout.addWidget(self.computer_image, 0, 2, 1, 1)

        # BUTTONS ################################################
        self.choices_widget = QtWidgets.QWidget(self.players_widget)
        # size
        self.choices_widget.setMinimumSize(QtCore.QSize(700, 0))
        # object name
        self.choices_widget.setObjectName("choices_widget")
        # layout
        self.choices_layout = QtWidgets.QGridLayout(self.choices_widget)
        self.choices_layout.setObjectName("choices_layout")

        # ROCK #####
        self.rock = QtWidgets.QPushButton(self.choices_widget)
        # size
        self.rock.setMinimumSize(QtCore.QSize(100, 100))
        self.rock.setMaximumSize(QtCore.QSize(200, 100))
        # font
        font.setPointSize(20)
        self.rock.setFont(font)
        # stylesheet
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.rock.setGraphicsEffect(shadow)
        self.rock.setStyleSheet(button_style)
        # object name
        self.rock.setObjectName("rock")
        # layout
        self.choices_layout.addWidget(self.rock, 0, 0, 1, 1)

        # PAPER #####
        self.paper = QtWidgets.QPushButton(self.choices_widget)
        # size
        self.paper.setMinimumSize(QtCore.QSize(150, 100))
        self.paper.setMaximumSize(QtCore.QSize(200, 100))
        # font
        font.setPointSize(20)
        self.paper.setFont(font)
        # stylesheet
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.paper.setGraphicsEffect(shadow)
        self.paper.setStyleSheet(button_style)
        # object name
        self.paper.setObjectName("paper")
        # layout
        self.choices_layout.addWidget(self.paper, 0, 1, 1, 1)

        # SCISSORS #####
        self.scissors = QtWidgets.QPushButton(self.choices_widget)
        # size
        self.scissors.setMinimumSize(QtCore.QSize(150, 100))
        self.scissors.setMaximumSize(QtCore.QSize(200, 100))
        # font
        font.setPointSize(20)
        self.scissors.setFont(font)
        # stylesheet
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.scissors.setGraphicsEffect(shadow)
        self.scissors.setStyleSheet(button_style)
        # object name
        self.scissors.setObjectName("scissors")
        # layout
        self.choices_layout.addWidget(self.scissors, 0, 2, 1, 1)

        self.players_layout.addWidget(self.choices_widget, 1, 0, 1, 1)

        # adding players_widget to main widget
        self.main_layout.addWidget(self.players_widget, 1, 0, 1, 1)

        # click click
        self.rock.clicked.connect(lambda: self.choose_option('Rock'))
        self.paper.clicked.connect(lambda: self.choose_option('Paper'))
        self.scissors.clicked.connect(lambda: self.choose_option('Scissors'))

        # TEXT #########################################################
        self.text = QtWidgets.QLabel(RockPaperScissors)
        # size
        self.text.setMinimumSize(QtCore.QSize(500, 0))
        # font
        font.setPointSize(18)
        self.text.setFont(font)
        # stylesheet
        self.text.setStyleSheet("background-color: #759FBC;"
                                "border-radius: 10px;"
                                "border: 1.5px dashed black;")
        # allignment
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.text.setObjectName("text")
        # adding to grid layout 4
        self.main_layout.addWidget(self.text, 2, 0, 1, 1)

        # NEW GAME BUTTON ##############################################
        self.new_game = QtWidgets.QPushButton(RockPaperScissors)
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
        self.new_game.clicked.connect(lambda: self.restart(RockPaperScissors))

        ###################################################################
        self.retranslateUi(RockPaperScissors)
        QtCore.QMetaObject.connectSlotsByName(RockPaperScissors)

    def retranslateUi(self, RockPaperScissors):
        """retransalateUi."""

        _translate = QtCore.QCoreApplication.translate
        # set window title
        RockPaperScissors.setWindowTitle(_translate(
            "RockPaperScissors", "RockPaperScissors"))

        # welcome label
        self.welcome.setText(_translate(
            "TicTacToe", "WELCOME TO ROCK PAPER SCISSORS!"))

        # vs text
        self.vs_label.setText(_translate("RockPaperScissors", "Vs."))

        # player 1 text
        # rock
        self.rock.setText(_translate("RockPaperScissors", "ROCK"))
        # paper
        self.paper.setText(_translate("RockPaperScissors", "PAPER"))
        # scissors
        self.scissors.setText(_translate("RockPaperScissors", "SCISSORS"))

        # text text
        self.text.setText(_translate("RockPaperScissors", "LET'S START!"))

        # new game text
        self.new_game.setText(_translate("RockPaperScissors", "New Game"))

    def restart(self, RockPaperScissors):
        self.rock.setEnabled(True)
        self.paper.setEnabled(True)
        self.scissors.setEnabled(True)

        self.retranslateUi(RockPaperScissors)
        QtCore.QMetaObject.connectSlotsByName(RockPaperScissors)

    def win_check(self):
        """Check Winner."""

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

    def choose_option(self, option):
        self.computer_choice = choice(the_choices)

        self.player_choice = option

        self.player_image.setPixmap(QtGui.QPixmap(
            f"ui/images/{self.player_choice.lower()}.png"))
        self.player_image.setScaledContents(True)

        self.computer_image.setPixmap(
            QtGui.QPixmap(f"ui/images/{self.computer_choice.lower()}.png"))
        self.computer_image.setScaledContents(True)

        self.win_check()
