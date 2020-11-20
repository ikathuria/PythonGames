from PyQt5 import QtCore, QtGui, QtWidgets

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

grid_style = """QPushButton { background-color: rgb(255, 255, 255); }"""

x_clicked_style = """QPushButton::disabled { background-image: url(ui/images/x.png);
                                             background-repeat: no-repeat;
                                             background-position: center;
                                             color: rgb(255, 255, 255); }"""

o_clicked_style = """QPushButton::disabled { background-image: url(ui/images/o.png);
                                             background-repeat: no-repeat;
                                             background-position: center;
                                             color: rgb(255, 255, 255); }"""


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
        TicTacToe.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        self.welcome.setStyleSheet("background-color: rgb(255, 255, 255);"
                                   "border: 1px solid rgb(0, 0, 0);")
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
        font.setPointSize(1)
        # stylesheet
        self.grid.setStyleSheet("background-color: rgb(0, 0, 0);")
        # object name
        self.grid.setObjectName("grid")
        # layout
        self.gridLayout = QtWidgets.QGridLayout(self.grid)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        # the buttons
        # 1
        self.pushButton_1 = QtWidgets.QPushButton(self.grid)
        # size
        self.pushButton_1.setMinimumSize(QtCore.QSize(160, 160))
        # font
        self.pushButton_1.setFont(font)
        # stylesheet
        self.pushButton_1.setStyleSheet(grid_style)
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
        self.pushButton_2.setStyleSheet(grid_style)
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
        self.pushButton_3.setStyleSheet(grid_style)
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
        self.pushButton_4.setStyleSheet(grid_style)
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
        self.pushButton_5.setStyleSheet(grid_style)
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
        self.pushButton_6.setStyleSheet(grid_style)
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
        self.pushButton_7.setStyleSheet(grid_style)
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
        self.pushButton_8.setStyleSheet(grid_style)
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
        self.pushButton_9.setStyleSheet(grid_style)
        # object name
        self.pushButton_9.setObjectName("pushButton_9")
        # adding to layout
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        # adding to main widget
        self.main_layout.addWidget(
            self.grid, 1, 0, 1, 1, alignment=QtCore.Qt.AlignCenter)

        # click click
        self.pushButton_1.clicked.connect(
            lambda: self.on_click(self.pushButton_1))
        self.pushButton_2.clicked.connect(
            lambda: self.on_click(self.pushButton_2))
        self.pushButton_3.clicked.connect(
            lambda: self.on_click(self.pushButton_3))
        self.pushButton_4.clicked.connect(
            lambda: self.on_click(self.pushButton_4))
        self.pushButton_5.clicked.connect(
            lambda: self.on_click(self.pushButton_5))
        self.pushButton_6.clicked.connect(
            lambda: self.on_click(self.pushButton_6))
        self.pushButton_7.clicked.connect(
            lambda: self.on_click(self.pushButton_7))
        self.pushButton_8.clicked.connect(
            lambda: self.on_click(self.pushButton_8))
        self.pushButton_9.clicked.connect(
            lambda: self.on_click(self.pushButton_9))

        # TEXT ####################################################
        self.text = QtWidgets.QLabel(TicTacToe)
        # size
        self.text.setMinimumSize(QtCore.QSize(500, 0))
        # font
        font.setPointSize(18)
        self.text.setFont(font)
        # stylesheet
        self.text.setStyleSheet("border-radius: 10px;"
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
        self.new_game.setFont(font)
        # stylesheet
        self.new_game.setStyleSheet(button_style)
        # object name
        self.new_game.setObjectName("new_game")
        # adding to main layout
        self.main_layout.addWidget(self.new_game, 3, 0, 1, 1)

        # restarting game
        self.new_game.clicked.connect(lambda: self.restart(TicTacToe))

        # OTHER VARIABLES #########################################
        self.turn = 'X'  # 'X' or 'O'
        self.count = 0  # if == 9 then draw

        self.buttons = [[self.pushButton_1, self.pushButton_2, self.pushButton_3],
                        [self.pushButton_4, self.pushButton_5, self.pushButton_6],
                        [self.pushButton_7, self.pushButton_8, self.pushButton_9]]

        ###################################################################
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
        self.pushButton_1.setText(_translate("TicTacToe", ""))
        self.pushButton_2.setText(_translate("TicTacToe", ""))
        self.pushButton_3.setText(_translate("TicTacToe", ""))
        self.pushButton_4.setText(_translate("TicTacToe", ""))
        self.pushButton_5.setText(_translate("TicTacToe", ""))
        self.pushButton_6.setText(_translate("TicTacToe", ""))
        self.pushButton_7.setText(_translate("TicTacToe", ""))
        self.pushButton_8.setText(_translate("TicTacToe", ""))
        self.pushButton_9.setText(_translate("TicTacToe", ""))

        # enable push button
        for i in self.buttons:
            for j in i:
                j.setEnabled(True)

        # label set text
        self.text.setText(_translate("TicTacToe", "Let's Start"))

        # new game button set text
        self.new_game.setText(_translate("TicTacToe", "New Game"))

    def restart(self, TicTacToe):
        self.turn == 'X'
        self.count = 0

        for row in self.buttons:
            for button in row:
                button.setStyleSheet(grid_style)

        self.retranslateUi(TicTacToe)
        QtCore.QMetaObject.connectSlotsByName(TicTacToe)

    def win_check(self):

        # all the rows
        for row in range(3):
            if self.buttons[row][0].text() == self.buttons[row][1].text() == self.buttons[row][2].text() != '':
                return True

        # all the columns
        for col in range(3):
            if self.buttons[0][col].text() == self.buttons[1][col].text() == self.buttons[2][col].text() != '':
                return True

        # diagonals
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != '':
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != '':
            return True

        return False

    def on_click(self, button):
        self.count += 1

        button.setEnabled(False)
        opacity = QtWidgets.QGraphicsOpacityEffect()
        opacity.setOpacity(1)
        button.setGraphicsEffect(opacity)

        if self.turn == 'X':
            button.setText('X')
            button.setStyleSheet(x_clicked_style)

        else:
            button.setText('O')
            button.setStyleSheet(o_clicked_style)

        if self.win_check():
            self.text.setText(
                f'{self.turn} WINS!\nClick the button below to play again')

            for i in self.buttons:
                for j in i:
                    j.setEnabled(False)

        else:
            if self.count == 9:
                self.text.setText(
                    'DRAW!\nClick the button below to play again')

            else:
                if self.turn == 'X':
                    self.turn = 'O'
                else:
                    self.turn = 'X'
                self.text.setText(f"{self.turn}'s TURN")
