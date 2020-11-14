from PyQt5 import QtCore, QtGui, QtWidgets
import rps


class Ui_players(object):

    def setupUi(self, players):
        # PLAYER WIDGET
        players.setObjectName("players")
        # size
        players.resize(730, 775)
        players.setMaximumSize(QtCore.QSize(730, 775))
        # stylesheet
        players.setStyleSheet("background-color: #C3E9F2;")
        # layout
        self.verticalLayout = QtWidgets.QVBoxLayout(players)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # LABEL
        self.label = QtWidgets.QLabel(players)
        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(45)
        self.label.setFont(font)
        # allignment
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.label.setObjectName("label")
        # layout
        self.verticalLayout.addWidget(self.label)

        # BUTTONS WIDGET
        self.widget = QtWidgets.QWidget(players)
        # objects name
        self.widget.setObjectName("widget")
        # layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 1 player
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        # size
        self.pushButton_1.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_1.setMaximumSize(QtCore.QSize(300, 300))
        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(36)
        self.pushButton_1.setFont(font)
        # stylesheet
        self.pushButton_1.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border: 1px inset rgb(0, 0, 0);\n"
                                      "border-radius: 150px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed {\n"
                                      "background-color : rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 1px inset rgb(0, 0, 0);\n"
                                      "border-radius: 150px;\n"
                                      "}")
        # object name
        self.pushButton_1.setObjectName("pushButton_1")        
        self.horizontalLayout.addWidget(self.pushButton_1)

        # 2 players
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        # size
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton_2.setMaximumSize(QtCore.QSize(300, 300))
        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        # stylesheet
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border: 1px inset rgb(0, 0, 0);\n"
                                        "border-radius: 150px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed {\n"
                                        "background-color : rgb(0, 0, 0);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 1px inset rgb(0, 0, 0);\n"
                                        "border-radius: 150px;\n"
                                        "}")
        # object name
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.addWidget(self.widget)

        # push push button
        self.pushButton_1.clicked.connect(lambda: self.how_many_players(players, 1))
        self.pushButton_2.clicked.connect(lambda: self.how_many_players(players, 2))

        self.retranslateUi(players)
        QtCore.QMetaObject.connectSlotsByName(players)

    def retranslateUi(self, players):
        _translate = QtCore.QCoreApplication.translate
        # window title
        players.setWindowTitle(_translate("players", "players"))
        
        # label text
        self.label.setText(_translate("players", "How many players?"))
        
        # button 1 text
        self.pushButton_1.setText(_translate("players", "1 Player"))
        # button 2 text
        self.pushButton_2.setText(_translate("players", "2 Players"))
    
    def how_many_players(self, players, button):
        if button == 1:
            self.num_of_players = 1
            RockPaperScissors = QtWidgets.QWidget()
            ui = rps.Ui_RockPaperScissors()
            ui.setupUi(RockPaperScissors)

            RockPaperScissors.setParent(players)
            RockPaperScissors.show()

        elif button == 2:
            self.num_of_players = 2
            RockPaperScissors = QtWidgets.QWidget()
            ui = rps.Ui_RockPaperScissors()
            ui.setupUi(RockPaperScissors)

            RockPaperScissors.setParent(players)
            RockPaperScissors.show()

