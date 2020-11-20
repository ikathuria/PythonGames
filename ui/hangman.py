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

letter_style = """QPushButton { background-color: rgb(255, 255, 255);
                                 color: rgb(0, 0, 0);
                                 border-radius: 5px;
                                 font-size: 40px; }
                
                QPushButton::pressed { background-color: rgb(0, 0, 0);
                                    color: rgb(255, 255, 255); }
                
                QPushButton::disabled { background-color: rgb(0, 0, 0, 0.2);
                                        color: rgb(75, 75, 75); }"""


class Ui_Hangman(object):

    def setupUi(self, Hangman):
        # object name
        Hangman.setObjectName("Hangman")
        # size
        Hangman.resize(730, 775)
        Hangman.setMinimumSize(QtCore.QSize(730, 775))
        Hangman.setMaximumSize(QtCore.QSize(730, 775))
        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        Hangman.setFont(font)
        # stylesheet
        Hangman.setStyleSheet("background-color: rgb(255, 255, 255);")
        # layout
        self.main_layout = QtWidgets.QGridLayout(Hangman)
        self.main_layout.setObjectName("main_layout")

        # WIDGET ##################################################
        self.widget = QtWidgets.QWidget(Hangman)
        # size
        self.widget.setMinimumSize(QtCore.QSize(710, 550))
        # stylesheet
        self.widget.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # object name
        self.widget.setObjectName("widget")

        # WELCOME ####################################################
        self.welcome = QtWidgets.QLabel(self.widget)
        self.welcome.setGeometry(QtCore.QRect(20, 20, 331, 111))
        # font
        font.setPointSize(26)
        self.welcome.setFont(font)
        # allignment
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.welcome.setObjectName("welcome")

        # IMAGE ######################################################
        self.image = QtWidgets.QLabel(self.widget)
        # size
        self.image.setGeometry(QtCore.QRect(20, 160, 340, 380))
        self.image.setMinimumSize(QtCore.QSize(340, 380))
        self.image.setMaximumSize(QtCore.QSize(340, 380))
        # stylesheet
        self.image.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        # adding image
        self.image.setPixmap(QtGui.QPixmap("images/hang1.png"))
        self.image.setScaledContents(True)
        # object name
        self.image.setObjectName("image")

        # LETTERS #######################################################
        self.letters = QtWidgets.QWidget(self.widget)
        # size
        self.letters.setGeometry(QtCore.QRect(380, 10, 320, 530))
        self.letters.setMinimumSize(QtCore.QSize(320, 530))
        self.letters.setMaximumSize(QtCore.QSize(320, 530))
        # stylesheet
        self.letters.setStyleSheet(letter_style)
        # object name
        self.letters.setObjectName("letters")
        # layout
        self.gridLayout = QtWidgets.QGridLayout(self.letters)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # LETTER BUTTONS
        self.button_a = QtWidgets.QPushButton(self.letters)
        self.button_a.setMinimumSize(QtCore.QSize(60, 60))
        self.button_a.setMaximumSize(QtCore.QSize(60, 60))
        self.button_a.setObjectName("button_a")
        self.gridLayout.addWidget(self.button_a, 0, 0, 1, 1)

        self.button_b = QtWidgets.QPushButton(self.letters)
        self.button_b.setMinimumSize(QtCore.QSize(60, 60))
        self.button_b.setMaximumSize(QtCore.QSize(60, 60))
        self.button_b.setObjectName("button_b")
        self.gridLayout.addWidget(self.button_b, 0, 1, 1, 1)

        self.button_c = QtWidgets.QPushButton(self.letters)
        self.button_c.setMinimumSize(QtCore.QSize(60, 60))
        self.button_c.setMaximumSize(QtCore.QSize(60, 60))
        self.button_c.setObjectName("button_c")
        self.gridLayout.addWidget(self.button_c, 0, 2, 1, 1)

        self.button_d = QtWidgets.QPushButton(self.letters)
        self.button_d.setMinimumSize(QtCore.QSize(60, 60))
        self.button_d.setMaximumSize(QtCore.QSize(60, 60))
        self.button_d.setObjectName("button_d")
        self.gridLayout.addWidget(self.button_d, 0, 3, 1, 1)

        self.button_e = QtWidgets.QPushButton(self.letters)
        self.button_e.setMinimumSize(QtCore.QSize(60, 60))
        self.button_e.setMaximumSize(QtCore.QSize(60, 60))
        self.button_e.setObjectName("button_e")
        self.gridLayout.addWidget(self.button_e, 1, 0, 1, 1)

        self.button_f = QtWidgets.QPushButton(self.letters)
        self.button_f.setMinimumSize(QtCore.QSize(60, 60))
        self.button_f.setMaximumSize(QtCore.QSize(60, 60))
        self.button_f.setObjectName("button_f")
        self.gridLayout.addWidget(self.button_f, 1, 1, 1, 1)

        self.button_g = QtWidgets.QPushButton(self.letters)
        self.button_g.setMinimumSize(QtCore.QSize(60, 60))
        self.button_g.setMaximumSize(QtCore.QSize(60, 60))
        self.button_g.setObjectName("button_g")
        self.gridLayout.addWidget(self.button_g, 1, 2, 1, 1)

        self.button_h = QtWidgets.QPushButton(self.letters)
        self.button_h.setMinimumSize(QtCore.QSize(60, 60))
        self.button_h.setMaximumSize(QtCore.QSize(60, 60))
        self.button_h.setObjectName("button_h")
        self.gridLayout.addWidget(self.button_h, 1, 3, 1, 1)

        self.button_i = QtWidgets.QPushButton(self.letters)
        self.button_i.setMinimumSize(QtCore.QSize(60, 60))
        self.button_i.setMaximumSize(QtCore.QSize(60, 60))
        self.button_i.setObjectName("button_i")
        self.gridLayout.addWidget(self.button_i, 2, 0, 1, 1)

        self.button_j = QtWidgets.QPushButton(self.letters)
        self.button_j.setMinimumSize(QtCore.QSize(60, 60))
        self.button_j.setMaximumSize(QtCore.QSize(60, 60))
        self.button_j.setObjectName("button_j")
        self.gridLayout.addWidget(self.button_j, 2, 1, 1, 1)

        self.button_k = QtWidgets.QPushButton(self.letters)
        self.button_k.setMinimumSize(QtCore.QSize(60, 60))
        self.button_k.setMaximumSize(QtCore.QSize(60, 60))
        self.button_k.setObjectName("button_k")
        self.gridLayout.addWidget(self.button_k, 2, 2, 1, 1)

        self.button_l = QtWidgets.QPushButton(self.letters)
        self.button_l.setMinimumSize(QtCore.QSize(60, 60))
        self.button_l.setMaximumSize(QtCore.QSize(60, 60))
        self.button_l.setObjectName("button_l")
        self.gridLayout.addWidget(self.button_l, 2, 3, 1, 1)

        self.button_m = QtWidgets.QPushButton(self.letters)
        self.button_m.setMinimumSize(QtCore.QSize(60, 60))
        self.button_m.setMaximumSize(QtCore.QSize(60, 60))
        self.button_m.setObjectName("button_m")
        self.gridLayout.addWidget(self.button_m, 3, 0, 1, 1)

        self.button_n = QtWidgets.QPushButton(self.letters)
        self.button_n.setMinimumSize(QtCore.QSize(60, 60))
        self.button_n.setMaximumSize(QtCore.QSize(60, 60))
        self.button_n.setObjectName("button_n")
        self.gridLayout.addWidget(self.button_n, 3, 1, 1, 1)

        self.button_o = QtWidgets.QPushButton(self.letters)
        self.button_o.setMinimumSize(QtCore.QSize(60, 60))
        self.button_o.setMaximumSize(QtCore.QSize(60, 60))
        self.button_o.setObjectName("button_o")
        self.gridLayout.addWidget(self.button_o, 3, 2, 1, 1)

        self.button_p = QtWidgets.QPushButton(self.letters)
        self.button_p.setMinimumSize(QtCore.QSize(60, 60))
        self.button_p.setMaximumSize(QtCore.QSize(60, 60))
        self.button_p.setObjectName("button_p")
        self.gridLayout.addWidget(self.button_p, 3, 3, 1, 1)

        self.button_q = QtWidgets.QPushButton(self.letters)
        self.button_q.setMinimumSize(QtCore.QSize(60, 60))
        self.button_q.setMaximumSize(QtCore.QSize(60, 60))
        self.button_q.setObjectName("button_q")
        self.gridLayout.addWidget(self.button_q, 4, 0, 1, 1)

        self.button_r = QtWidgets.QPushButton(self.letters)
        self.button_r.setMinimumSize(QtCore.QSize(60, 60))
        self.button_r.setMaximumSize(QtCore.QSize(60, 60))
        self.button_r.setObjectName("button_r")
        self.gridLayout.addWidget(self.button_r, 4, 1, 1, 1)

        self.button_s = QtWidgets.QPushButton(self.letters)
        self.button_s.setMinimumSize(QtCore.QSize(60, 60))
        self.button_s.setMaximumSize(QtCore.QSize(60, 60))
        self.button_s.setObjectName("button_s")
        self.gridLayout.addWidget(self.button_s, 4, 2, 1, 1)

        self.button_t = QtWidgets.QPushButton(self.letters)
        self.button_t.setMinimumSize(QtCore.QSize(60, 60))
        self.button_t.setMaximumSize(QtCore.QSize(60, 60))
        self.button_t.setObjectName("button_t")
        self.gridLayout.addWidget(self.button_t, 4, 3, 1, 1)

        self.button_u = QtWidgets.QPushButton(self.letters)
        self.button_u.setMinimumSize(QtCore.QSize(60, 60))
        self.button_u.setMaximumSize(QtCore.QSize(60, 60))
        self.button_u.setObjectName("button_u")
        self.gridLayout.addWidget(self.button_u, 5, 0, 1, 1)

        self.button_v = QtWidgets.QPushButton(self.letters)
        self.button_v.setMinimumSize(QtCore.QSize(60, 60))
        self.button_v.setMaximumSize(QtCore.QSize(60, 60))
        self.button_v.setObjectName("button_v")
        self.gridLayout.addWidget(self.button_v, 5, 1, 1, 1)

        self.button_w = QtWidgets.QPushButton(self.letters)
        self.button_w.setMinimumSize(QtCore.QSize(60, 60))
        self.button_w.setMaximumSize(QtCore.QSize(60, 60))
        self.button_w.setObjectName("button_w")
        self.gridLayout.addWidget(self.button_w, 5, 2, 1, 1)

        self.button_x = QtWidgets.QPushButton(self.letters)
        self.button_x.setMinimumSize(QtCore.QSize(60, 60))
        self.button_x.setMaximumSize(QtCore.QSize(60, 60))
        self.button_x.setObjectName("button_x")
        self.gridLayout.addWidget(self.button_x, 5, 3, 1, 1)

        self.button_y = QtWidgets.QPushButton(self.letters)
        self.button_y.setMinimumSize(QtCore.QSize(60, 60))
        self.button_y.setMaximumSize(QtCore.QSize(60, 60))
        self.button_y.setObjectName("button_y")
        self.gridLayout.addWidget(self.button_y, 6, 1, 1, 1)

        self.button_z = QtWidgets.QPushButton(self.letters)
        self.button_z.setMinimumSize(QtCore.QSize(60, 60))
        self.button_z.setMaximumSize(QtCore.QSize(60, 60))
        self.button_z.setObjectName("button_z")
        self.gridLayout.addWidget(self.button_z, 6, 2, 1, 1)

        # adding to main layout
        self.main_layout.addWidget(self.widget, 0, 0, 1, 1)

        # THE WORD ##########################################
        self.the_word = QtWidgets.QLabel(Hangman)
        # font
        font.setPointSize(40)
        self.the_word.setFont(font)
        # allignment
        self.the_word.setAlignment(QtCore.Qt.AlignCenter)
        # object name
        self.the_word.setObjectName("the_word")
        # adding to main layout
        self.main_layout.addWidget(self.the_word, 1, 0, 1, 1)

        # NEW GAME BUTTON #####################################
        self.new_game = QtWidgets.QPushButton(Hangman)
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
        self.main_layout.addWidget(self.new_game, 2, 0, 1, 1)

        #########################################################
        self.retranslateUi(Hangman)
        QtCore.QMetaObject.connectSlotsByName(Hangman)

    def retranslateUi(self, Hangman):
        _translate = QtCore.QCoreApplication.translate

        # window title
        Hangman.setWindowTitle(_translate("Hangman", "Hangman"))

        # welcome text
        self.welcome.setText(_translate("Hangman", "WELCOME TO\nHANGMAN!"))

        # lettes text
        self.button_a.setText(_translate("Hangman", "A"))
        self.button_b.setText(_translate("Hangman", "B"))
        self.button_c.setText(_translate("Hangman", "C"))
        self.button_d.setText(_translate("Hangman", "D"))
        self.button_e.setText(_translate("Hangman", "E"))
        self.button_f.setText(_translate("Hangman", "F"))
        self.button_g.setText(_translate("Hangman", "G"))
        self.button_h.setText(_translate("Hangman", "H"))
        self.button_i.setText(_translate("Hangman", "I"))
        self.button_j.setText(_translate("Hangman", "J"))
        self.button_k.setText(_translate("Hangman", "K"))
        self.button_l.setText(_translate("Hangman", "L"))
        self.button_m.setText(_translate("Hangman", "M"))
        self.button_n.setText(_translate("Hangman", "N"))
        self.button_o.setText(_translate("Hangman", "O"))
        self.button_p.setText(_translate("Hangman", "P"))
        self.button_q.setText(_translate("Hangman", "Q"))
        self.button_r.setText(_translate("Hangman", "R"))
        self.button_s.setText(_translate("Hangman", "S"))
        self.button_t.setText(_translate("Hangman", "T"))
        self.button_u.setText(_translate("Hangman", "U"))
        self.button_v.setText(_translate("Hangman", "V"))
        self.button_w.setText(_translate("Hangman", "W"))
        self.button_x.setText(_translate("Hangman", "X"))
        self.button_y.setText(_translate("Hangman", "Y"))
        self.button_z.setText(_translate("Hangman", "Z"))

        # word text
        self.the_word.setText(_translate("Hangman", "The word"))

        # new game text
        self.new_game.setText(_translate("Hangman", "New Game"))
