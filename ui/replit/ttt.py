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

x_clicked_style = """QPushButton::disabled { border-image: url(ui/images/x.png);
                                             color: #ff615f; }"""

o_clicked_style = """QPushButton::disabled { border-image: url(ui/images/o.png);
                                             color: rgb(255, 255, 255); }"""


class Ui_tic_tac_toe(object):
    """Ui Class."""

    def setupUi(self, tic_tac_toe):
        """setup ui."""

        tic_tac_toe.setObjectName("tic_tac_toe")

        # size
        tic_tac_toe.resize(530, 530)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            tic_tac_toe.sizePolicy().hasHeightForWidth())
        tic_tac_toe.setSizePolicy(sizePolicy)
        tic_tac_toe.setMinimumSize(QtCore.QSize(530, 530))

        # stylesheet
        tic_tac_toe.setStyleSheet("background-color: rgb(255, 255, 255);")

        # the main grid layout
        self.main_layout = QtWidgets.QGridLayout(tic_tac_toe)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setHorizontalSpacing(20)
        self.main_layout.setVerticalSpacing(5)
        self.main_layout.setObjectName("main_layout")

        # WELCOME #############################################################
        self.welcome = QtWidgets.QLabel(tic_tac_toe)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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

        # THE GRID ##############################################################
        self.grid = QtWidgets.QWidget(tic_tac_toe)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(True)
        self.grid.setSizePolicy(sizePolicy)
        self.grid.setMinimumSize(QtCore.QSize(350, 350))
        # stylesheet
        self.grid.setStyleSheet("background-color: rgb(0, 0, 0);")
        # object name
        self.grid.setObjectName("grid")

        # layout
        self.grid_layout = QtWidgets.QGridLayout(self.grid)
        self.grid_layout.setContentsMargins(70, 10, 70, 10)
        self.grid_layout.setSpacing(10)
        self.grid_layout.setObjectName("grid_layout")

        # the buttons
        # 1
        self.button_1 = QtWidgets.QPushButton(self.grid)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setMinimumSize(QtCore.QSize(110, 110))
        # object name
        self.button_1.setObjectName("button_1")
        # add to grid layout
        self.grid_layout.addWidget(self.button_1, 0, 0, 1, 1)

        # 2
        self.button_2 = QtWidgets.QPushButton(self.grid)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setMinimumSize(QtCore.QSize(110, 110))
        # object name
        self.button_2.setObjectName("button_2")
        # add to grid layout
        self.grid_layout.addWidget(self.button_2, 0, 1, 1, 1)

        # 3
        self.button_3 = QtWidgets.QPushButton(self.grid)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setMinimumSize(QtCore.QSize(110, 110))
        # object name
        self.button_3.setObjectName("button_3")
        # add to grid layout
        self.grid_layout.addWidget(self.button_3, 0, 2, 1, 1)

        # 4
        self.button_4 = QtWidgets.QPushButton(self.grid)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setMinimumSize(QtCore.QSize(110, 110))
        # object name
        self.button_4.setObjectName("button_4")
        # add to grid layout
        self.grid_layout.addWidget(self.button_4, 1, 0, 1, 1)

        # 5
        self.button_5 = QtWidgets.QPushButton(self.grid)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setMinimumSize(QtCore.QSize(110, 110))
        # object name
        self.button_5.setObjectName("button_5")
        # add to grid layout
        self.grid_layout.addWidget(self.button_5, 1, 1, 1, 1)

        # 6
        self.button_6 = QtWidgets.QPushButton(self.grid)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setMinimumSize(QtCore.QSize(110, 110))
        # object name
        self.button_6.setObjectName("button_6")
        # add to grid layout
        self.grid_layout.addWidget(self.button_6, 1, 2, 1, 1)

        # 7
        self.button_7 = QtWidgets.QPushButton(self.grid)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setMinimumSize(QtCore.QSize(110, 110))
        # object name
        self.button_7.setObjectName("button_7")
        # add to grid layout
        self.grid_layout.addWidget(self.button_7, 2, 0, 1, 1)

        # 8
        self.button_8 = QtWidgets.QPushButton(self.grid)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setMinimumSize(QtCore.QSize(110, 110))
        # object name
        self.button_8.setObjectName("button_8")
        # add to grid layout
        self.grid_layout.addWidget(self.button_8, 2, 1, 1, 1)

        # 9
        self.button_9 = QtWidgets.QPushButton(self.grid)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(True)
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setMinimumSize(QtCore.QSize(110, 110))
        # object name
        self.button_9.setObjectName("button_9")
        # add to grid layout
        self.grid_layout.addWidget(self.button_9, 2, 2, 1, 1)

        # adding to main layout
        self.main_layout.addWidget(self.grid, 1, 0, 1, 2)

        # button click click
        self.button_1.clicked.connect(
            lambda: self.on_click(self.button_1))
        self.button_2.clicked.connect(
            lambda: self.on_click(self.button_2))
        self.button_3.clicked.connect(
            lambda: self.on_click(self.button_3))
        self.button_4.clicked.connect(
            lambda: self.on_click(self.button_4))
        self.button_5.clicked.connect(
            lambda: self.on_click(self.button_5))
        self.button_6.clicked.connect(
            lambda: self.on_click(self.button_6))
        self.button_7.clicked.connect(
            lambda: self.on_click(self.button_7))
        self.button_8.clicked.connect(
            lambda: self.on_click(self.button_8))
        self.button_9.clicked.connect(
            lambda: self.on_click(self.button_9))

        # TURN/WINNER ############################################################
        self.turn_winner = QtWidgets.QLabel(tic_tac_toe)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.turn_winner.sizePolicy().hasHeightForWidth())
        self.turn_winner.setSizePolicy(sizePolicy)
        self.turn_winner.setMinimumSize(QtCore.QSize(300, 75))
        self.turn_winner.setMaximumSize(QtCore.QSize(16777215, 200))
        # stylesheet
        self.turn_winner.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # allignment
        self.turn_winner.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.turn_winner.setObjectName("turn_winner")

        # adding to main layout
        self.main_layout.addWidget(self.turn_winner, 2, 0, 1, 1)

        # NEW GAME BUTTON ######################################################
        self.new_game = QtWidgets.QPushButton(tic_tac_toe)
        # size
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        self.main_layout.addWidget(self.new_game, 2, 1, 1, 1)

        # restarting game
        self.new_game.clicked.connect(lambda: self.restart(tic_tac_toe))

        # OTHER VARIABLES ##########################################################
        self.turn = 'X'
        self.count = 0

        self.buttons = [[self.button_1, self.button_2, self.button_3],
                        [self.button_4, self.button_5, self.button_6],
                        [self.button_7, self.button_8, self.button_9]]

        ###########################################################################
        self.retranslateUi(tic_tac_toe)
        QtCore.QMetaObject.connectSlotsByName(tic_tac_toe)

    def retranslateUi(self, tic_tac_toe):
        _translate = QtCore.QCoreApplication.translate

        # WINDOW TITLE
        tic_tac_toe.setWindowTitle(_translate("tic_tac_toe", "ttt"))

        # WELCOME TEXT
        self.welcome.setText(_translate(
            "tic_tac_toe", "WELCOME TO TIC-TAC-TOE!"))

        # BUTTONS
        # enable push button and set text
        for row in self.buttons:
            for button in row:
                button.setStyleSheet(grid_style)
                button.setEnabled(True)
                button.setText("")

        # TURN/WINNER TEXT
        self.turn_winner.setText(_translate("tic_tac_toe", "Let's Go!"))

        # NEW GAME BUTTON
        self.new_game.setText(_translate("tic_tac_toe", "New Game"))

    def restart(self, tic_tac_toe):
        self.turn == 'X'
        self.count = 0

        self.retranslateUi(tic_tac_toe)
        QtCore.QMetaObject.connectSlotsByName(tic_tac_toe)

    def win_check(self):
        win = False

        # all the rows
        for row in range(3):
            if self.buttons[row][0].text() == self.buttons[row][1].text() == self.buttons[row][2].text() != "":
                win = True

        # all the columns
        for col in range(3):
            if self.buttons[0][col].text() == self.buttons[1][col].text() == self.buttons[2][col].text() != "":
                win = True

        # diagonals
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != "":
            win = True

        elif self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != "":
            win = True

        return win

    def on_click(self, button):
        self.count += 1

        button.setEnabled(False)

        opacity = QtWidgets.QGraphicsOpacityEffect()
        opacity.setOpacity(1)
        button.setGraphicsEffect(opacity)

        if self.turn == 'X':
            button.setText('X')
            button.setStyleSheet(x_clicked_style)

        elif self.turn == 'O':
            button.setText('O')
            button.setStyleSheet(o_clicked_style)

        if self.win_check():
            self.turn_winner.setText(
                f"{self.turn} WINS!\nClick the button below to play again")

            for i in self.buttons:
                for j in i:
                    j.setEnabled(False)

        else:
            if self.count == 9:
                self.turn_winner.setText(
                    "DRAW!\nClick the button below to play again")

            else:
                if self.turn == 'X':
                    self.turn = 'O'

                elif self.turn == 'O':
                    self.turn = 'X'

                self.turn_winner.setText(f"{self.turn}'s TURN")
