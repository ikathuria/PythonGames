# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hangman.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hangman(object):
    def setupUi(self, hangman):
        hangman.setObjectName("hangman")
        hangman.resize(530, 530)
        hangman.setMinimumSize(QtCore.QSize(530, 530))
        hangman.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_layout = QtWidgets.QGridLayout(hangman)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setHorizontalSpacing(20)
        self.main_layout.setVerticalSpacing(5)
        self.main_layout.setObjectName("main_layout")
        self.welcome = QtWidgets.QLabel(hangman)
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
        self.game_box = QtWidgets.QWidget(hangman)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_box.sizePolicy().hasHeightForWidth())
        self.game_box.setSizePolicy(sizePolicy)
        self.game_box.setObjectName("game_box")
        self.game_box_layout = QtWidgets.QGridLayout(self.game_box)
        self.game_box_layout.setContentsMargins(10, 10, 10, 10)
        self.game_box_layout.setSpacing(5)
        self.game_box_layout.setObjectName("game_box_layout")
        self.image = QtWidgets.QLabel(self.game_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QtCore.QSize(200, 200))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.game_box_layout.addWidget(self.image, 0, 0, 1, 1)
        self.letters = QtWidgets.QScrollArea(self.game_box)
        self.letters.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255);\n"
"                     color: rgb(0, 0, 0);\n"
"                     border-radius: 5px;\n"
"                     font-size: 40px; }\n"
"                \n"
"QPushButton::pressed { background-color: rgb(0, 0, 0);\n"
"                                    color: rgb(255, 255, 255); }\n"
"                \n"
"QPushButton::disabled { background-color: rgb(0, 0, 0, 0.2);\n"
"                                    color: rgb(75, 75, 75); }")
        self.letters.setWidgetResizable(True)
        self.letters.setObjectName("letters")
        self.letter_buttons = QtWidgets.QWidget()
        self.letter_buttons.setGeometry(QtCore.QRect(0, 0, 263, 606))
        self.letter_buttons.setObjectName("letter_buttons")
        self.letters_layout = QtWidgets.QGridLayout(self.letter_buttons)
        self.letters_layout.setContentsMargins(10, 10, 10, 10)
        self.letters_layout.setSpacing(5)
        self.letters_layout.setObjectName("letters_layout")
        self.button_x = QtWidgets.QPushButton(self.letter_buttons)
        self.button_x.setMinimumSize(QtCore.QSize(60, 60))
        self.button_x.setObjectName("button_x")
        self.letters_layout.addWidget(self.button_x, 7, 2, 1, 1)
        self.button_c = QtWidgets.QPushButton(self.letter_buttons)
        self.button_c.setMinimumSize(QtCore.QSize(60, 60))
        self.button_c.setObjectName("button_c")
        self.letters_layout.addWidget(self.button_c, 0, 2, 1, 1)
        self.button_o = QtWidgets.QPushButton(self.letter_buttons)
        self.button_o.setMinimumSize(QtCore.QSize(60, 60))
        self.button_o.setObjectName("button_o")
        self.letters_layout.addWidget(self.button_o, 4, 2, 1, 1)
        self.button_t = QtWidgets.QPushButton(self.letter_buttons)
        self.button_t.setMinimumSize(QtCore.QSize(60, 60))
        self.button_t.setObjectName("button_t")
        self.letters_layout.addWidget(self.button_t, 6, 1, 1, 1)
        self.button_g = QtWidgets.QPushButton(self.letter_buttons)
        self.button_g.setMinimumSize(QtCore.QSize(60, 60))
        self.button_g.setObjectName("button_g")
        self.letters_layout.addWidget(self.button_g, 2, 0, 1, 1)
        self.button_i = QtWidgets.QPushButton(self.letter_buttons)
        self.button_i.setMinimumSize(QtCore.QSize(60, 60))
        self.button_i.setObjectName("button_i")
        self.letters_layout.addWidget(self.button_i, 2, 2, 1, 1)
        self.button_j = QtWidgets.QPushButton(self.letter_buttons)
        self.button_j.setMinimumSize(QtCore.QSize(60, 60))
        self.button_j.setObjectName("button_j")
        self.letters_layout.addWidget(self.button_j, 3, 0, 1, 1)
        self.button_l = QtWidgets.QPushButton(self.letter_buttons)
        self.button_l.setMinimumSize(QtCore.QSize(60, 60))
        self.button_l.setObjectName("button_l")
        self.letters_layout.addWidget(self.button_l, 3, 2, 1, 1)
        self.button_p = QtWidgets.QPushButton(self.letter_buttons)
        self.button_p.setMinimumSize(QtCore.QSize(60, 60))
        self.button_p.setObjectName("button_p")
        self.letters_layout.addWidget(self.button_p, 5, 0, 1, 1)
        self.button_m = QtWidgets.QPushButton(self.letter_buttons)
        self.button_m.setMinimumSize(QtCore.QSize(60, 60))
        self.button_m.setObjectName("button_m")
        self.letters_layout.addWidget(self.button_m, 4, 0, 1, 1)
        self.button_e = QtWidgets.QPushButton(self.letter_buttons)
        self.button_e.setMinimumSize(QtCore.QSize(60, 60))
        self.button_e.setObjectName("button_e")
        self.letters_layout.addWidget(self.button_e, 1, 1, 1, 1)
        self.button_w = QtWidgets.QPushButton(self.letter_buttons)
        self.button_w.setMinimumSize(QtCore.QSize(60, 60))
        self.button_w.setObjectName("button_w")
        self.letters_layout.addWidget(self.button_w, 7, 1, 1, 1)
        self.button_u = QtWidgets.QPushButton(self.letter_buttons)
        self.button_u.setMinimumSize(QtCore.QSize(60, 60))
        self.button_u.setObjectName("button_u")
        self.letters_layout.addWidget(self.button_u, 6, 2, 1, 1)
        self.button_s = QtWidgets.QPushButton(self.letter_buttons)
        self.button_s.setMinimumSize(QtCore.QSize(60, 60))
        self.button_s.setObjectName("button_s")
        self.letters_layout.addWidget(self.button_s, 6, 0, 1, 1)
        self.button_b = QtWidgets.QPushButton(self.letter_buttons)
        self.button_b.setMinimumSize(QtCore.QSize(60, 60))
        self.button_b.setObjectName("button_b")
        self.letters_layout.addWidget(self.button_b, 0, 1, 1, 1)
        self.button_h = QtWidgets.QPushButton(self.letter_buttons)
        self.button_h.setMinimumSize(QtCore.QSize(60, 60))
        self.button_h.setObjectName("button_h")
        self.letters_layout.addWidget(self.button_h, 2, 1, 1, 1)
        self.button_r = QtWidgets.QPushButton(self.letter_buttons)
        self.button_r.setMinimumSize(QtCore.QSize(60, 60))
        self.button_r.setObjectName("button_r")
        self.letters_layout.addWidget(self.button_r, 5, 2, 1, 1)
        self.button_a = QtWidgets.QPushButton(self.letter_buttons)
        self.button_a.setMinimumSize(QtCore.QSize(60, 60))
        self.button_a.setObjectName("button_a")
        self.letters_layout.addWidget(self.button_a, 0, 0, 1, 1)
        self.button_d = QtWidgets.QPushButton(self.letter_buttons)
        self.button_d.setMinimumSize(QtCore.QSize(60, 60))
        self.button_d.setObjectName("button_d")
        self.letters_layout.addWidget(self.button_d, 1, 0, 1, 1)
        self.button_f = QtWidgets.QPushButton(self.letter_buttons)
        self.button_f.setMinimumSize(QtCore.QSize(60, 60))
        self.button_f.setObjectName("button_f")
        self.letters_layout.addWidget(self.button_f, 1, 2, 1, 1)
        self.button_n = QtWidgets.QPushButton(self.letter_buttons)
        self.button_n.setMinimumSize(QtCore.QSize(60, 60))
        self.button_n.setObjectName("button_n")
        self.letters_layout.addWidget(self.button_n, 4, 1, 1, 1)
        self.button_k = QtWidgets.QPushButton(self.letter_buttons)
        self.button_k.setMinimumSize(QtCore.QSize(60, 60))
        self.button_k.setObjectName("button_k")
        self.letters_layout.addWidget(self.button_k, 3, 1, 1, 1)
        self.button_q = QtWidgets.QPushButton(self.letter_buttons)
        self.button_q.setMinimumSize(QtCore.QSize(60, 60))
        self.button_q.setObjectName("button_q")
        self.letters_layout.addWidget(self.button_q, 5, 1, 1, 1)
        self.button_v = QtWidgets.QPushButton(self.letter_buttons)
        self.button_v.setMinimumSize(QtCore.QSize(60, 60))
        self.button_v.setObjectName("button_v")
        self.letters_layout.addWidget(self.button_v, 7, 0, 1, 1)
        self.button_y = QtWidgets.QPushButton(self.letter_buttons)
        self.button_y.setMinimumSize(QtCore.QSize(60, 60))
        self.button_y.setObjectName("button_y")
        self.letters_layout.addWidget(self.button_y, 8, 0, 1, 1)
        self.button_z = QtWidgets.QPushButton(self.letter_buttons)
        self.button_z.setMinimumSize(QtCore.QSize(60, 60))
        self.button_z.setObjectName("button_z")
        self.letters_layout.addWidget(self.button_z, 8, 1, 1, 1)
        self.letters.setWidget(self.letter_buttons)
        self.game_box_layout.addWidget(self.letters, 0, 1, 1, 1)
        self.main_layout.addWidget(self.game_box, 1, 0, 1, 2)
        self.the_word = QtWidgets.QLabel(hangman)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.the_word.sizePolicy().hasHeightForWidth())
        self.the_word.setSizePolicy(sizePolicy)
        self.the_word.setMinimumSize(QtCore.QSize(300, 75))
        self.the_word.setMaximumSize(QtCore.QSize(16777215, 200))
        self.the_word.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
        self.the_word.setAlignment(QtCore.Qt.AlignCenter)
        self.the_word.setObjectName("the_word")
        self.main_layout.addWidget(self.the_word, 2, 0, 1, 1)
        self.new_game = QtWidgets.QPushButton(hangman)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_game.sizePolicy().hasHeightForWidth())
        self.new_game.setSizePolicy(sizePolicy)
        self.new_game.setMinimumSize(QtCore.QSize(0, 50))
        self.new_game.setMaximumSize(QtCore.QSize(16777215, 100))
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

        self.retranslateUi(hangman)
        QtCore.QMetaObject.connectSlotsByName(hangman)

    def retranslateUi(self, hangman):
        _translate = QtCore.QCoreApplication.translate
        hangman.setWindowTitle(_translate("hangman", "hangman"))
        self.welcome.setText(_translate("hangman", "WELCOME TO HANGMAN!"))
        self.image.setText(_translate("hangman", "TextLabel"))
        self.button_x.setText(_translate("hangman", "X"))
        self.button_c.setText(_translate("hangman", "C"))
        self.button_o.setText(_translate("hangman", "O"))
        self.button_t.setText(_translate("hangman", "T"))
        self.button_g.setText(_translate("hangman", "G"))
        self.button_i.setText(_translate("hangman", "I"))
        self.button_j.setText(_translate("hangman", "J"))
        self.button_l.setText(_translate("hangman", "L"))
        self.button_p.setText(_translate("hangman", "P"))
        self.button_m.setText(_translate("hangman", "M"))
        self.button_e.setText(_translate("hangman", "E"))
        self.button_w.setText(_translate("hangman", "W"))
        self.button_u.setText(_translate("hangman", "U"))
        self.button_s.setText(_translate("hangman", "S"))
        self.button_b.setText(_translate("hangman", "B"))
        self.button_h.setText(_translate("hangman", "H"))
        self.button_r.setText(_translate("hangman", "R"))
        self.button_a.setText(_translate("hangman", "A"))
        self.button_d.setText(_translate("hangman", "D"))
        self.button_f.setText(_translate("hangman", "F"))
        self.button_n.setText(_translate("hangman", "N"))
        self.button_k.setText(_translate("hangman", "K"))
        self.button_q.setText(_translate("hangman", "Q"))
        self.button_v.setText(_translate("hangman", "V"))
        self.button_y.setText(_translate("hangman", "Y"))
        self.button_z.setText(_translate("hangman", "Z"))
        self.the_word.setText(_translate("hangman", "The word"))
        self.new_game.setText(_translate("hangman", "New Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hangman = QtWidgets.QWidget()
    ui = Ui_hangman()
    ui.setupUi(hangman)
    hangman.show()
    sys.exit(app.exec_())