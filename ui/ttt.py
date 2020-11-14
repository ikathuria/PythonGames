from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TicTacToe(object):

    def setupUi(self, TicTacToe):
        # object name
        TicTacToe.setObjectName("TicTacToe")
        # size
        TicTacToe.resize(730, 775)
        TicTacToe.setMaximumSize(QtCore.QSize(730, 775))
        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        TicTacToe.setFont(font)
        # stylesheet
        TicTacToe.setStyleSheet("background-color: #B9B8D3;")
        # grid layout
        self.main_layout = QtWidgets.QGridLayout(TicTacToe)
        self.main_layout.setObjectName("main_layout")

        # WELCOME ##############################################
        self.welcome = QtWidgets.QLabel(TicTacToe)
        # size
        self.welcome.setMinimumSize(QtCore.QSize(700, 0))
        # font
        font.setPointSize(30)
        self.welcome.setFont(font)
        # stylesheet
        self.welcome.setStyleSheet("background-color: rgb(255, 255, 255);")
        # allignment
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.welcome.setObjectName("welcome")
        # adding to main widget
        self.main_layout.addWidget(self.welcome, 0, 0, 1, 1)

        # THE GRID ######################################################
        self.grid = QtWidgets.QFrame(TicTacToe)
        # size
        self.grid.setMinimumSize(QtCore.QSize(500, 500))
        self.grid.setMaximumSize(QtCore.QSize(500, 500))
        # font size
        font.setPointSize(20)
        # stylesheet
        self.grid.setStyleSheet("background-color: rgb(0, 0, 0);")
        # object name
        self.grid.setObjectName("grid")
        # layout
        self.gridLayout = QtWidgets.QGridLayout(self.grid)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

        # the buttons
        # 1
        self.pushButton_1 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_1.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_1.setFont(font)
        # stylesheet
        self.pushButton_1.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # objext name
        self.pushButton_1.setObjectName("pushButton_1")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        # 2
        self.pushButton_2 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_2.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_2.setFont(font)
        # stylsheet
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # object name
        self.pushButton_2.setObjectName("pushButton_2")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        # 3
        self.pushButton_3 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_3.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_3.setFont(font)
        # stylsheet
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # object name
        self.pushButton_3.setObjectName("pushButton_3")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        # 4
        self.pushButton_4 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_4.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_4.setFont(font)
        # stylsheet
        self.pushButton_4.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # object name
        self.pushButton_4.setObjectName("pushButton_4")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        # 5
        self.pushButton_5 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_5.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_5.setFont(font)
        # stylsheet
        self.pushButton_5.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # object name
        self.pushButton_5.setObjectName("pushButton_5")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        # 6
        self.pushButton_6 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_6.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_6.setFont(font)
        # stylsheet
        self.pushButton_6.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # object name
        self.pushButton_6.setObjectName("pushButton_6")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        # 7
        self.pushButton_7 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_7.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_7.setFont(font)
        # stylsheet
        self.pushButton_7.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # object name
        self.pushButton_7.setObjectName("pushButton_7")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        # 8
        self.pushButton_8 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_8.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_8.setFont(font)
        # stylsheet
        self.pushButton_8.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # object name
        self.pushButton_8.setObjectName("pushButton_8")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        # 9
        self.pushButton_9 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_9.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_9.setFont(font)
        # stylsheet
        self.pushButton_9.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        # object name
        self.pushButton_9.setObjectName("pushButton_9")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        # adding to main widget
        self.main_layout.addWidget(
            self.grid, 1, 0, 1, 1, alignment=QtCore.Qt.AlignCenter)

        # TEXT ####################################################
        self.text = QtWidgets.QLabel(TicTacToe)
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
        # adding to main widget
        self.main_layout.addWidget(self.text, 2, 0, 1, 1)

        # NEW GAME BUTTON #####################################
        self.new_game = QtWidgets.QPushButton(TicTacToe)
        # size
        self.new_game.setMinimumSize(QtCore.QSize(500, 50))
        # font
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.new_game.setFont(font)
        # stylesheet
        self.new_game.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: #49516F;"
                                    "color: rgb(255, 255, 255);"
                                    "border-radius: 20px;"
                                    "border: 1px inset white;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color : white;"
                                    "color: rgb(0, 0, 0);"
                                    "border-radius: 20px;"
                                    "border: 1px inset black;"
                                    "}")
        # object name
        self.new_game.setObjectName("new_game")
        self.main_layout.addWidget(self.new_game, 3, 0, 1, 1)

        self.retranslateUi(TicTacToe)
        QtCore.QMetaObject.connectSlotsByName(TicTacToe)

    def retranslateUi(self, TicTacToe):
        """restranslateUi."""

        _translate = QtCore.QCoreApplication.translate
        # set window title
        TicTacToe.setWindowTitle(_translate("TicTacToe", "TicTacToe"))

        # welcome label
        self.welcome.setText(_translate(
            "TicTacToe", "WELCOME TO TIC TAC TOE!"))

        # grid buttons set text
        self.pushButton_1.setText(_translate("TicTacToe", "1"))
        self.pushButton_2.setText(_translate("TicTacToe", "2"))
        self.pushButton_3.setText(_translate("TicTacToe", "3"))
        self.pushButton_4.setText(_translate("TicTacToe", "4"))
        self.pushButton_5.setText(_translate("TicTacToe", "5"))
        self.pushButton_6.setText(_translate("TicTacToe", "6"))
        self.pushButton_7.setText(_translate("TicTacToe", "7"))
        self.pushButton_8.setText(_translate("TicTacToe", "8"))
        self.pushButton_9.setText(_translate("TicTacToe", "9"))

        # label set text
        self.text.setText(_translate("TicTacToe", "LET\'S START!"))

        # new game button set text
        self.new_game.setText(_translate("TicTacToe", "New Game"))
