from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_num_guess(object):
    def setupUi(self, num_guess):
        num_guess.setObjectName("num_guess")
        num_guess.resize(530, 530)
        num_guess.setMinimumSize(QtCore.QSize(530, 530))
        num_guess.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_layout = QtWidgets.QGridLayout(num_guess)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(5)
        self.main_layout.setObjectName("main_layout")
        self.welcome = QtWidgets.QLabel(num_guess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome.sizePolicy().hasHeightForWidth())
        self.welcome.setSizePolicy(sizePolicy)
        self.welcome.setMinimumSize(QtCore.QSize(510, 0))
        self.welcome.setMaximumSize(QtCore.QSize(16777215, 100))
        self.welcome.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.main_layout.addWidget(self.welcome, 0, 0, 1, 2)
        self.new_game = QtWidgets.QPushButton(num_guess)
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
        self.main_layout.addWidget(self.new_game, 2, 1, 1, 1)
        self.game_box = QtWidgets.QWidget(num_guess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_box.sizePolicy().hasHeightForWidth())
        self.game_box.setSizePolicy(sizePolicy)
        self.game_box.setMinimumSize(QtCore.QSize(510, 300))
        self.game_box.setStyleSheet("")
        self.game_box.setObjectName("game_box")
        self.game_box_layout = QtWidgets.QGridLayout(self.game_box)
        self.game_box_layout.setContentsMargins(10, 10, 10, 10)
        self.game_box_layout.setHorizontalSpacing(10)
        self.game_box_layout.setVerticalSpacing(5)
        self.game_box_layout.setObjectName("game_box_layout")
        self.text = QtWidgets.QLabel(self.game_box)
        self.text.setMinimumSize(QtCore.QSize(275, 0))
        self.text.setMaximumSize(QtCore.QSize(16777215, 600))
        self.text.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        self.game_box_layout.addWidget(self.text, 0, 0, 3, 1)
        self.level_1 = QtWidgets.QCommandLinkButton(self.game_box)
        self.level_1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.level_1.setStyleSheet("background-color: rgb(232, 226, 255);")
        self.level_1.setObjectName("level_1")
        self.game_box_layout.addWidget(self.level_1, 0, 1, 1, 2)
        self.level_2 = QtWidgets.QCommandLinkButton(self.game_box)
        self.level_2.setEnabled(True)
        self.level_2.setMinimumSize(QtCore.QSize(0, 0))
        self.level_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.level_2.setStyleSheet("background-color: rgb(232, 226, 255);")
        self.level_2.setObjectName("level_2")
        self.game_box_layout.addWidget(self.level_2, 1, 1, 1, 2)
        self.level_3 = QtWidgets.QCommandLinkButton(self.game_box)
        self.level_3.setMinimumSize(QtCore.QSize(0, 0))
        self.level_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.level_3.setStyleSheet("background-color: rgb(232, 226, 255);")
        self.level_3.setObjectName("level_3")
        self.game_box_layout.addWidget(self.level_3, 2, 1, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.game_box)
        self.spinBox.setMinimumSize(QtCore.QSize(300, 100))
        self.spinBox.setObjectName("spinBox")
        self.game_box_layout.addWidget(self.spinBox, 3, 0, 1, 2)
        self.submit = QtWidgets.QPushButton(self.game_box)
        self.submit.setMinimumSize(QtCore.QSize(100, 100))
        self.submit.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0);\n"
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
        self.submit.setObjectName("submit")
        self.game_box_layout.addWidget(self.submit, 3, 2, 1, 1)
        self.main_layout.addWidget(self.game_box, 1, 0, 1, 2)

        self.retranslateUi(num_guess)
        QtCore.QMetaObject.connectSlotsByName(num_guess)

    def retranslateUi(self, num_guess):
        _translate = QtCore.QCoreApplication.translate
        num_guess.setWindowTitle(_translate("num_guess", "num_guess"))
        self.welcome.setText(_translate("num_guess", "WELCOME TO NUMBER GUESSING"))
        self.new_game.setText(_translate("num_guess", "New Game"))
        self.text.setText(_translate("num_guess", "Choose your level"))
        self.level_1.setText(_translate("num_guess", "1. Piece of Cake"))
        self.level_2.setText(_translate("num_guess", "2. Let\'s Rock!"))
        self.level_3.setText(_translate("num_guess", "3. Damn I\'m Good"))
        self.submit.setText(_translate("num_guess", "Submit"))

