"""Rock Paper Scissors."""

# imports
from PyQt5 import QtCore, QtGui, QtWidgets


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
            "background-color: rgb(255, 217, 218);")
        # layout
        self.main_layout = QtWidgets.QGridLayout(RockPaperScissors)
        self.main_layout.setObjectName("main_layout")

        # WELCOME ##############################################
        self.welcome = QtWidgets.QLabel(RockPaperScissors)
        # size
        self.welcome.setMinimumSize(QtCore.QSize(700, 0))
        # font
        font.setPointSize(23)
        self.welcome.setFont(font)
        # stylesheet
        self.welcome.setStyleSheet("background-color: rgb(255, 255, 255);")
        # allignment
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.welcome.setObjectName("welcome")
        # adding to main widget
        self.main_layout.addWidget(self.welcome, 0, 0, 1, 1)

        # players outer widget ##################################################
        self.players_widget = QtWidgets.QWidget(RockPaperScissors)
        # font
        font.setPointSize(20)
        self.players_widget.setFont(font)
        # object name
        self.players_widget.setObjectName("players_widget")
        # layout
        self.players_layout = QtWidgets.QGridLayout(self.players_widget)
        self.players_layout.setObjectName("players_layout")

        # VS. LABEL inside players_widget ##########################
        self.vs_label = QtWidgets.QLabel(self.players_widget)
        # font
        font.setPointSize(28)
        self.vs_label.setFont(font)
        # allignment
        self.vs_label.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.vs_label.setObjectName("vs_label")
        # layout
        self.players_layout.addWidget(self.vs_label, 0, 1, 1, 1)

        # PLAYER 2 ################################################
        self.widget_2 = QtWidgets.QWidget(self.players_widget)
        # size
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        # object name
        self.widget_2.setObjectName("widget_2")
        # layout
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # CHOICE IMAGE #####
        self.choice_2 = QtWidgets.QLabel(self.widget_2)
        # size
        self.choice_2.setMinimumSize(QtCore.QSize(220, 220))
        self.choice_2.setMaximumSize(QtCore.QSize(220, 220))
        # image
        self.choice_2.setPixmap(QtGui.QPixmap("ui/images/rock.png"))
        self.choice_2.setScaledContents(True)
        # allignment
        self.choice_2.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.choice_2.setObjectName("choice_2")
        # adding to widget 2
        self.gridLayout_2.addWidget(self.choice_2, 0, 0, 1, 1)

        # ROCK #####
        self.rock_2 = QtWidgets.QPushButton(self.widget_2)
        # size
        self.rock_2.setMinimumSize(QtCore.QSize(150, 100))
        self.rock_2.setMaximumSize(QtCore.QSize(220, 100))
        # font
        font.setPointSize(20)
        self.rock_2.setFont(font)
        # stylesheet
        self.rock_2.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(167, 167, 167);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::pressed {\n"
                                  "background-color : white;\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "}")
        # object name
        self.rock_2.setObjectName("rock_2")
        # adding to widget 2
        self.gridLayout_2.addWidget(self.rock_2, 1, 0, 1, 1)

        # PAPER #####
        self.paper_2 = QtWidgets.QPushButton(self.widget_2)
        # size
        self.paper_2.setMinimumSize(QtCore.QSize(150, 100))
        self.paper_2.setMaximumSize(QtCore.QSize(220, 100))
        # font
        font.setPointSize(20)
        self.paper_2.setFont(font)
        # stylesheet
        self.paper_2.setStyleSheet("QPushButton {\n"
                                   "background-color: rgb(216, 255, 253);\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::pressed {\n"
                                   "background-color : rgb(0, 0, 0);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "}")
        # object name
        self.paper_2.setObjectName("paper_2")
        # adding to widget 2
        self.gridLayout_2.addWidget(self.paper_2, 2, 0, 1, 1)

        # SCISSORS #####
        self.scissors_2 = QtWidgets.QPushButton(self.widget_2)
        # size
        self.scissors_2.setMinimumSize(QtCore.QSize(150, 100))
        self.scissors_2.setMaximumSize(QtCore.QSize(220, 100))
        # font
        font.setPointSize(20)
        self.scissors_2.setFont(font)
        # stylesheet
        self.scissors_2.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(255, 75, 75);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed {\n"
                                      "background-color : white;\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "}")
        # object name
        self.scissors_2.setObjectName("scissors_2")
        # adding to widget 2
        self.gridLayout_2.addWidget(self.scissors_2, 3, 0, 1, 1)

        # adding widget 2 to outer widget
        self.players_layout.addWidget(self.widget_2, 0, 2, 1, 1)

        # PLAYER 1 ##########################################################
        self.widget_1 = QtWidgets.QWidget(self.players_widget)
        # size
        self.widget_1.setMinimumSize(QtCore.QSize(300, 0))
        # object name
        self.widget_1.setObjectName("widget_1")
        # layout
        self.gridLayout = QtWidgets.QGridLayout(self.widget_1)
        self.gridLayout.setObjectName("gridLayout")

        # CHOICE IMAGE #####
        self.choice_1 = QtWidgets.QLabel(self.widget_1)
        # size
        self.choice_1.setMinimumSize(QtCore.QSize(220, 220))
        self.choice_1.setMaximumSize(QtCore.QSize(220, 220))
        # image
        self.choice_1.setPixmap(QtGui.QPixmap("ui/images/rock.png"))
        self.choice_1.setScaledContents(True)
        # allignment
        self.choice_1.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.choice_1.setObjectName("choice_1")
        # layout
        self.gridLayout.addWidget(self.choice_1, 0, 0, 1, 1)

        # ROCK #####
        self.rock_1 = QtWidgets.QPushButton(self.widget_1)
        # size
        self.rock_1.setMinimumSize(QtCore.QSize(100, 100))
        self.rock_1.setMaximumSize(QtCore.QSize(220, 100))
        # font
        font.setPointSize(20)
        self.rock_1.setFont(font)
        # stylesheet
        self.rock_1.setStyleSheet("QPushButton {\n"
                                  "background-color: rgb(167, 167, 167);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::pressed {\n"
                                  "background-color : white;\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "}")
        # object name
        self.rock_1.setObjectName("rock_1")
        # layout
        self.gridLayout.addWidget(self.rock_1, 1, 0, 1, 1)

        # PAPER #####
        self.paper_1 = QtWidgets.QPushButton(self.widget_1)
        # size
        self.paper_1.setMinimumSize(QtCore.QSize(150, 100))
        self.paper_1.setMaximumSize(QtCore.QSize(220, 100))
        # font
        font.setPointSize(20)
        self.paper_1.setFont(font)
        # stylesheet
        self.paper_1.setStyleSheet("QPushButton {\n"
                                   "background-color: rgb(216, 255, 253);\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::pressed {\n"
                                   "background-color : rgb(0, 0, 0);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "}")
        # object name
        self.paper_1.setObjectName("paper_1")
        # layout
        self.gridLayout.addWidget(self.paper_1, 2, 0, 1, 1)

        # SCISSORS #####
        self.scissors_1 = QtWidgets.QPushButton(self.widget_1)
        # size
        self.scissors_1.setMinimumSize(QtCore.QSize(150, 100))
        self.scissors_1.setMaximumSize(QtCore.QSize(220, 100))
        # font
        font.setPointSize(20)
        self.scissors_1.setFont(font)
        # stylesheet
        self.scissors_1.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(255, 75, 75);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed {\n"
                                      "background-color : white;\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "}")
        # object name
        self.scissors_1.setObjectName("scissors_1")
        # layout
        self.gridLayout.addWidget(self.scissors_1, 3, 0, 1, 1)

        # adding widget 1 to outer widget
        self.players_layout.addWidget(self.widget_1, 0, 0, 1, 1)

        # adding players_widget to main widget
        self.main_layout.addWidget(self.players_widget, 1, 0, 1, 1)

        # TEXT #########################################################
        self.text = QtWidgets.QLabel(RockPaperScissors)
        # size
        self.text.setMinimumSize(QtCore.QSize(500, 0))
        # font
        font.setPointSize(18)
        self.text.setFont(font)
        # stylesheet
        self.text.setStyleSheet("background-color: #759FBC;\n"
                                "border-radius: 10px;\n"
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
        font.setBold(True)
        font.setWeight(75)
        self.new_game.setFont(font)
        # stylesheet
        self.new_game.setStyleSheet("QPushButton {\n"
                                    "background-color: #49516F;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 20px;\n"
                                    "border: 1px inset white;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::pressed {\n"
                                    "background-color : white;\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "border-radius: 20px;\n"
                                    "border: 1px inset black;\n"
                                    "}")
        # object name
        self.new_game.setObjectName("new_game")
        # layout
        self.main_layout.addWidget(self.new_game, 3, 0, 1, 1)

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

        # player 2 text
        # rock
        self.rock_2.setText(_translate("RockPaperScissors", "ROCK"))
        # paper
        self.paper_2.setText(_translate("RockPaperScissors", "PAPER"))
        # scissors
        self.scissors_2.setText(_translate("RockPaperScissors", "SCISSORS"))

        # player 1 text
        # rock
        self.rock_1.setText(_translate("RockPaperScissors", "ROCK"))
        # paper
        self.paper_1.setText(_translate("RockPaperScissors", "PAPER"))
        # scissors
        self.scissors_1.setText(_translate("RockPaperScissors", "SCISSORS"))

        # text text
        self.text.setText(_translate("RockPaperScissors", "LET\'S START!"))

        # new game text
        self.new_game.setText(_translate("RockPaperScissors", "New Game"))
