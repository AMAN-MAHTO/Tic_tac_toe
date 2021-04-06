from PyQt5.uic import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
import sys
import time

turn = '0'
game_over = 0
app = QApplication(sys.argv)

ui = loadUi('game_tik_tac_toe.ui')
ui.Button_11.clicked.connect(lambda:change(11,ui.Button_11.text()))
ui.Button_12.clicked.connect(lambda:change(12,ui.Button_12.text()))
ui.Button_13.clicked.connect(lambda:change(13,ui.Button_13.text()))
ui.Button_22.clicked.connect(lambda:change(22,ui.Button_22.text()))
ui.Button_21.clicked.connect(lambda:change(21,ui.Button_21.text()))
ui.Button_23.clicked.connect(lambda:change(23,ui.Button_23.text()))
ui.Button_33.clicked.connect(lambda:change(33,ui.Button_33.text()))
ui.Button_32.clicked.connect(lambda:change(32,ui.Button_32.text()))
ui.Button_31.clicked.connect(lambda:change(31,ui.Button_31.text()))
ui.reset_button.clicked.connect(lambda:reset())

def change_value(current_value):
        global turn
        if current_value == "X":
            turn = '0'
        elif current_value == '0':
            turn ='X'

def reset():
    global game_over
    ui.Button_11.setText('')
    ui.Button_12.setText('')
    ui.Button_13.setText('')
    ui.Button_21.setText('')
    ui.Button_22.setText('')
    ui.Button_23.setText('')
    ui.Button_31.setText('')
    ui.Button_32.setText('')
    ui.Button_33.setText('')
    ui.turn.setText('0')
    ui.winner.setText('')
    ui.Turn_lable.setText('Turn')
    game_over = 0

def if_someone_win(winner):
    global game_over
    ui.winner.setText(winner)
    ui.Turn_lable.setText('')
    ui.turn.setText('Game\nOver!!')
    game_over = 1

def who_win():
        b_11 = ui.Button_11.text()
        b_12 = ui.Button_12.text()
        b_13 = ui.Button_13.text()
        b_21 = ui.Button_21.text()
        b_22 = ui.Button_22.text()
        b_23 = ui.Button_23.text()
        b_31 = ui.Button_31.text()
        b_32 = ui.Button_32.text()
        b_33 = ui.Button_33.text()

        if b_11 == b_12 == b_13 != '':
            if_someone_win(b_11)
        elif b_11 == b_21 == b_31 != '':
            if_someone_win(b_11)
        elif b_11 == b_22 == b_33 != '':
            if_someone_win(b_11)
        elif b_12 == b_22 == b_32 != '':
            if_someone_win(b_12)
        elif b_13 == b_23 == b_33 != '':
            if_someone_win(b_13)
        elif b_13 == b_22 == b_31 != '':
            if_someone_win(b_13)
        elif b_21 == b_22 == b_23 != '':
            if_someone_win(b_21)
        elif b_31 == b_32 == b_33 != '':
            if_someone_win(b_31)
        
def change(_button_number,button_text):
        global turn
        if button_text == "" and game_over == 0:
            if _button_number == 11:
                ui.Button_11.setText(turn)
            elif _button_number == 12:
                ui.Button_12.setText(turn)
            elif _button_number == 13:
                ui.Button_13.setText(turn)
            elif _button_number == 21:
                ui.Button_21.setText(turn)
            elif _button_number == 22:
                ui.Button_22.setText(turn)
            elif _button_number == 23:
                ui.Button_23.setText(turn)
            elif _button_number == 33:
                ui.Button_33.setText(turn)
            elif _button_number == 31:
                ui.Button_31.setText(turn)
            elif _button_number == 32:
                ui.Button_32.setText(turn)
            change_value(turn)
            ui.turn.setText(turn)
            who_win()
            
            

ui.show()


sys.exit(app.exec_())
