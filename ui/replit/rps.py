from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rps(object):
    def setupUi(self, rps):
        rps.setObjectName("rps")
        rps.resize(530, 530)
        rps.setMinimumSize(QtCore.QSize(530, 530))
        rps.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_layout = QtWidgets.QGridLayout(rps)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setHorizontalSpacing(20)
        self.main_layout.setVerticalSpacing(5)
        self.main_layout.setObjectName("main_layout")
        self.welcome = QtWidgets.QLabel(rps)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome.sizePolicy().hasHeightForWidth())
        self.welcome.setSizePolicy(sizePolicy)
        self.welcome.setMinimumSize(QtCore.QSize(510, 50))
        self.welcome.setMaximumSize(QtCore.QSize(16777215, 100))
        self.welcome.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.main_layout.addWidget(self.welcome, 0, 0, 1, 2)
        self.choice_widget = QtWidgets.QWidget(rps)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_widget.sizePolicy().hasHeightForWidth())
        self.choice_widget.setSizePolicy(sizePolicy)
        self.choice_widget.setObjectName("choice_widget")
        self.choices_layout = QtWidgets.QGridLayout(self.choice_widget)
        self.choices_layout.setContentsMargins(10, 10, 10, 10)
        self.choices_layout.setSpacing(5)
        self.choices_layout.setObjectName("choices_layout")
        self.player_choice = QtWidgets.QLabel(self.choice_widget)
        self.player_choice.setMinimumSize(QtCore.QSize(210, 210))
        self.player_choice.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.player_choice.setAlignment(QtCore.Qt.AlignCenter)
        self.player_choice.setObjectName("player_choice")
        self.choices_layout.addWidget(self.player_choice, 0, 0, 1, 1)
        self.vs_label = QtWidgets.QLabel(self.choice_widget)
        self.vs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vs_label.setObjectName("vs_label")
        self.choices_layout.addWidget(self.vs_label, 0, 1, 1, 1)
        self.computer_choice = QtWidgets.QLabel(self.choice_widget)
        self.computer_choice.setMinimumSize(QtCore.QSize(210, 210))
        self.computer_choice.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.computer_choice.setAlignment(QtCore.Qt.AlignCenter)
        self.computer_choice.setObjectName("computer_choice")
        self.choices_layout.addWidget(self.computer_choice, 0, 2, 1, 1)
        self.main_layout.addWidget(self.choice_widget, 1, 0, 1, 2)
        self.buttons = QtWidgets.QWidget(rps)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setMinimumSize(QtCore.QSize(510, 0))
        self.buttons.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0);\n"
"                      color: rgb(255, 255, 255);\n"
"                      border-radius: 10px; }\n"
"\n"
"QPushButton::pressed { background-color: rgb(255, 255, 255);\n"
"                                    color: rgb(0, 0, 0);\n"
"                                    border: 1px solid rgb(0, 0, 0);\n"
"                                    border-radius: 10px; }\n"
"\n"
"QPushButton::disabled { background-color: rgb(0, 0, 0, 0.2);\n"
"                                    color: rgb(75, 75, 75); }")
        self.buttons.setObjectName("buttons")
        self.buttons_layout = QtWidgets.QGridLayout(self.buttons)
        self.buttons_layout.setContentsMargins(10, 10, 10, 10)
        self.buttons_layout.setSpacing(5)
        self.buttons_layout.setObjectName("buttons_layout")
        self.pushButton = QtWidgets.QPushButton(self.buttons)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton.setObjectName("pushButton")
        self.buttons_layout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.buttons)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttons_layout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.buttons)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.buttons_layout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.main_layout.addWidget(self.buttons, 2, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.turn_winner = QtWidgets.QLabel(rps)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turn_winner.sizePolicy().hasHeightForWidth())
        self.turn_winner.setSizePolicy(sizePolicy)
        self.turn_winner.setMinimumSize(QtCore.QSize(300, 75))
        self.turn_winner.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.turn_winner.setAlignment(QtCore.Qt.AlignCenter)
        self.turn_winner.setObjectName("turn_winner")
        self.main_layout.addWidget(self.turn_winner, 3, 0, 1, 1)
        self.new_game = QtWidgets.QPushButton(rps)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_game.sizePolicy().hasHeightForWidth())
        self.new_game.setSizePolicy(sizePolicy)
        self.new_game.setMinimumSize(QtCore.QSize(0, 50))
        self.new_game.setMaximumSize(QtCore.QSize(16777215, 50))
        self.new_game.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0);\n"
"                      color: rgb(255, 255, 255);\n"
"                      border-radius: 10px; }\n"
"\n"
"QPushButton::pressed { background-color: rgb(255, 255, 255);\n"
"                                    color: rgb(0, 0, 0);\n"
"                                    border: 1px solid rgb(0, 0, 0);\n"
"                                    border-radius: 10px; }\n"
"\n"
"QPushButton::disabled { background-color: rgb(0, 0, 0, 0.2);\n"
"                                    color: rgb(75, 75, 75); }")
        self.new_game.setObjectName("new_game")
        self.main_layout.addWidget(self.new_game, 3, 1, 1, 1)

        self.retranslateUi(rps)
        QtCore.QMetaObject.connectSlotsByName(rps)

    def retranslateUi(self, rps):
        _translate = QtCore.QCoreApplication.translate
        rps.setWindowTitle(_translate("rps", "rps"))
        self.welcome.setText(_translate("rps", "WELCOME TO ROCK-PAPER-SCISSORS!"))
        self.player_choice.setText(_translate("rps", "Player"))
        self.vs_label.setText(_translate("rps", "Vs."))
        self.computer_choice.setText(_translate("rps", "Computer"))
        self.pushButton.setText(_translate("rps", "Rock"))
        self.pushButton_2.setText(_translate("rps", "Paper"))
        self.pushButton_3.setText(_translate("rps", "Scissors"))
        self.turn_winner.setText(_translate("rps", "Make your choice"))
        self.new_game.setText(_translate("rps", "New Game"))

