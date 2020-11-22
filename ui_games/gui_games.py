"""Different one player games made with python.

The user interface is designed with PyQt5.

"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# personal modules
import rulebook
from blackjack import Ui_blackjack
from hangman import Ui_hangman
from num_guess import Ui_num_guess
from rps import Ui_rps
from ttt import Ui_tic_tac_toe


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


class Ui_PythonGames(object):
    """Ui Class."""

    def setupUi(self, PythonGames):
        """Setting up the User Interface."""

        PythonGames.setObjectName("PythonGames")

        # icon
        PythonGames.setWindowIcon(QtGui.QIcon("ui_games/images/icon.png")) 

        # setting size at 800x600
        PythonGames.resize(800, 600)

        # expanding
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            PythonGames.sizePolicy().hasHeightForWidth())
        PythonGames.setSizePolicy(sizePolicy)

        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        PythonGames.setFont(font)

        # stylesheet
        PythonGames.setStyleSheet("background-color: rgb(255, 255, 255);")

        # CENTRAL WIDGET ########################################################
        self.centralwidget = QtWidgets.QWidget(PythonGames)
        self.centralwidget.setObjectName("centralwidget")

        # the main grid layout
        self.main_layout = QtWidgets.QGridLayout(self.centralwidget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(5)
        self.main_layout.setObjectName("main_layout")

        # GAMES BOX ############################################################
        self.games_box = QtWidgets.QGroupBox(self.centralwidget)
        # size
        self.games_box.setMaximumSize(QtCore.QSize(300, 16777215))
        # stylesheet
        self.games_box.setStyleSheet(button_style)
        # allignment
        self.games_box.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.games_box.setObjectName("games_box")
        # layout
        self.games_box_layout = QtWidgets.QGridLayout(self.games_box)
        self.games_box_layout.setContentsMargins(10, 10, 10, 10)
        self.games_box_layout.setSpacing(5)
        self.games_box_layout.setObjectName("games_box_layout")

        # game buttons #####
        # blackjack
        self.blackjack_button = QtWidgets.QPushButton(self.games_box)
        self.blackjack_button.setMinimumSize(QtCore.QSize(0, 30))
        self.blackjack_button.setObjectName("blackjack_button")
        self.games_box_layout.addWidget(self.blackjack_button, 0, 0, 1, 1)

        # hangman
        self.hangman_button = QtWidgets.QPushButton(self.games_box)
        self.hangman_button.setMinimumSize(QtCore.QSize(0, 30))
        self.hangman_button.setObjectName("hangman_button")
        self.games_box_layout.addWidget(self.hangman_button, 1, 0, 1, 1)

        # number guessing
        self.num_guess_button = QtWidgets.QPushButton(self.games_box)
        self.num_guess_button.setMinimumSize(QtCore.QSize(0, 30))
        self.num_guess_button.setObjectName("num_guess_button")
        self.games_box_layout.addWidget(self.num_guess_button, 2, 0, 1, 1)

        # rock paper scissors
        self.rps_button = QtWidgets.QPushButton(self.games_box)
        self.rps_button.setMinimumSize(QtCore.QSize(0, 30))
        self.rps_button.setObjectName("rps_button")
        self.games_box_layout.addWidget(self.rps_button, 3, 0, 1, 1)

        # tic tac toe
        self.ttt_button = QtWidgets.QPushButton(self.games_box)
        self.ttt_button.setMinimumSize(QtCore.QSize(0, 30))
        self.ttt_button.setObjectName("ttt_button")
        self.games_box_layout.addWidget(self.ttt_button, 4, 0, 1, 1)

        # adding to main layout
        self.main_layout.addWidget(self.games_box, 0, 0, 1, 1)

        # THE RULES ######################################################
        self.rules_scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        # size
        self.rules_scrollArea.setMaximumSize(QtCore.QSize(300, 16777215))
        self.rules_scrollArea.setWidgetResizable(True)
        # stylesheet
        self.rules_scrollArea.setStyleSheet(
            "background-color: rgb(217, 221, 255);")
        # object name
        self.rules_scrollArea.setObjectName("rules_scrollArea")

        # the content
        self.rules_content = QtWidgets.QWidget()
        # geometry
        self.rules_content.setGeometry(QtCore.QRect(0, 0, 222, 674))
        # object name
        self.rules_content.setObjectName("rules_content")
        # layout
        self.rules_layout = QtWidgets.QGridLayout(self.rules_content)
        self.rules_layout.setObjectName("rules_layout")

        # rules label
        self.rules_label = QtWidgets.QLabel(self.rules_content)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.rules_label.sizePolicy().hasHeightForWidth())
        self.rules_label.setSizePolicy(sizePolicy)
        self.rules_label.setMaximumSize(QtCore.QSize(300, 16777215))
        # allignment
        self.rules_label.setAlignment(QtCore.Qt.AlignCenter)
        # word wrap
        self.rules_label.setWordWrap(True)
        # object name
        self.rules_label.setObjectName("rules_label")
        # adding to layout
        self.rules_layout.addWidget(self.rules_label)
        # adding to scroll area
        self.rules_scrollArea.setWidget(self.rules_content)

        # adding to main layout
        self.main_layout.addWidget(self.rules_scrollArea, 1, 0, 1, 1)

        # EXIT BUTTON #########################################################
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        # size
        self.exit_button.setMinimumSize(QtCore.QSize(0, 50))
        # stylesheet
        self.exit_button.setStyleSheet(button_style)
        # object name
        self.exit_button.setObjectName("exit_button")

        # adding to main layout
        self.main_layout.addWidget(self.exit_button, 2, 0, 1, 1)

        # GAMES FRAME ##########################################################
        self.games_frame = QtWidgets.QFrame(self.centralwidget)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.games_frame.setSizePolicy(sizePolicy)
        self.games_frame.setMinimumSize(QtCore.QSize(530, 530))
        # stylesheet
        self.games_frame.setStyleSheet("background-color: rgb(217, 221, 255);")
        # object name
        self.games_frame.setObjectName("games_frame")
        # layout
        self.games_frame_layout = QtWidgets.QGridLayout(self.games_frame)
        self.games_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.games_frame_layout.setObjectName("games_frame_layout")

        # adding to main layout
        self.main_layout.addWidget(self.games_frame, 0, 1, 3, 1)

        # setting centralwidget
        PythonGames.setCentralWidget(self.centralwidget)

        # MENUBAR ###############################################################
        self.menubar = QtWidgets.QMenuBar(PythonGames)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        PythonGames.setMenuBar(self.menubar)

        # STATUSBAR ############################################################
        self.statusbar = QtWidgets.QStatusBar(PythonGames)
        self.statusbar.setObjectName("statusbar")
        PythonGames.setStatusBar(self.statusbar)

        #########################################################################
        self.retranslateUi(PythonGames)
        QtCore.QMetaObject.connectSlotsByName(PythonGames)

    def retranslateUi(self, PythonGames):
        _translate = QtCore.QCoreApplication.translate
        # WINDOW TITLE
        PythonGames.setWindowTitle(_translate("PythonGames", "Python Games"))

        # GAMES BOX TITLE
        self.games_box.setTitle(_translate("PythonGames", "The Games"))

        # GAME BUTTONS
        # blackjack
        self.blackjack_button.setText(_translate("PythonGames", "Blackjack"))
        # rules
        self.blackjack_button.clicked.connect(
            lambda: self.show_rules('Blackjack'))
        # game
        self.blackjack_button.clicked.connect(
            lambda: self.start_game('Blackjack'))

        # hangman
        self.hangman_button.setText(_translate("PythonGames", "Hangman"))
        # rules
        self.hangman_button.clicked.connect(lambda: self.show_rules('Hangman'))
        # game
        self.hangman_button.clicked.connect(lambda: self.start_game('Hangman'))

        # number guessing
        self.num_guess_button.setText(
            _translate("PythonGames", "Number Guessing"))
        # rules
        self.num_guess_button.clicked.connect(
            lambda: self.show_rules('Number guessing'))
        # game
        self.num_guess_button.clicked.connect(
            lambda: self.start_game('Number guessing'))

        # rock paper scissors
        self.rps_button.setText(_translate(
            "PythonGames", "Rock Paper Scissors"))
        # rules
        self.rps_button.clicked.connect(
            lambda: self.show_rules('Rock Paper Scissors'))
        # game
        self.rps_button.clicked.connect(
            lambda: self.start_game('Rock Paper Scissors'))

        # tic tac toe
        self.ttt_button.setText(_translate("PythonGames", "Tic Tac Toe"))
        # rules
        self.ttt_button.clicked.connect(lambda: self.show_rules('Tic Tac Toe'))
        # game
        self.ttt_button.clicked.connect(lambda: self.start_game('Tic Tac Toe'))

        # RULES TEXT
        self.rules_label.setText(_translate(
            "PythonGames", "Click on a game to see the rules"))

        # EXIT BUTTON TEXT
        self.exit_button.setText(_translate("PythonGames", "Exit"))
        # on click
        self.exit_button.clicked.connect(self.exit_application)

    def show_rules(self, game):
        """Rules."""

        self.rules_label.setText(game + '\n\n' + rulebook.rule_book(game))
        self.rules_label.setAlignment(QtCore.Qt.AlignJustify)

    def start_game(self, game):
        """Start game."""

        self.replace = QtWidgets.QWidget()
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.replace.sizePolicy().hasHeightForWidth())
        self.replace.setSizePolicy(sizePolicy)
        self.replace.setMinimumSize(QtCore.QSize(530, 530))
        # adding to games frame
        self.games_frame_layout.addWidget(self.replace, 0, 0, 1, 1)

        game = game.lower()
        the_game = False

        if game == 'blackjack':
            blackjack = QtWidgets.QWidget()
            ui = Ui_blackjack()
            ui.setupUi(blackjack)

            the_game = blackjack

        elif game == 'hangman':
            hangman = QtWidgets.QWidget()
            ui = Ui_hangman()
            ui.setupUi(hangman)

            the_game = hangman

        elif game == 'number guessing':
            num_guess = QtWidgets.QWidget()
            ui = Ui_num_guess()
            ui.setupUi(num_guess)

            the_game = num_guess

        elif game == 'rock paper scissors':
            rps = QtWidgets.QWidget()
            ui = Ui_rps()
            ui.setupUi(rps)

            the_game = rps

        elif game == 'tic tac toe':
            tic_tac_toe = QtWidgets.QWidget()
            ui = Ui_tic_tac_toe()
            ui.setupUi(tic_tac_toe)

            the_game = tic_tac_toe

        if the_game:
            self.games_frame_layout.replaceWidget(self.replace, the_game)

    def exit_application(self):
        """Exits."""

        sys.exit()


def main():
    app = QtWidgets.QApplication(sys.argv)

    PythonGames = QtWidgets.QMainWindow()

    ui = Ui_PythonGames()
    ui.setupUi(PythonGames)

    PythonGames.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
