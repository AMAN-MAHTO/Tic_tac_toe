from PyQt5.uic import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QThreadPool
import sys
import time
import random


turn = '0'
game_over = 0


app = QApplication(sys.argv)
ui = loadUi('game_tik_tac_toe.ui')
QtWidgets.QPushButton.setStyleSheet(ui,open('style.css').read())

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

def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

def ai():
    oponnent_move = '0'
    ai_move = 'X'
    global turn
    # text = text()
    b_11=ui.Button_11.text()
    b_12=ui.Button_12.text()
    b_13=ui.Button_13.text()
    b_21=ui.Button_21.text()
    b_22=ui.Button_22.text()
    b_23=ui.Button_23.text()
    b_31=ui.Button_31.text()
    b_32=ui.Button_32.text()
    b_33=ui.Button_33.text()

    screen = [b_11,b_12,b_13,b_21,b_22,b_23,b_31,b_32,b_33]

    row1 = [b_11,b_21,b_31]
    row2 = [b_12,b_22,b_32]
    row3 = [b_13,b_23,b_33]

    col1 = [b_11,b_12,b_13]
    col2 = [b_21,b_22,b_23]
    col3 = [b_31,b_32,b_33]

    dig1 = [b_11,b_22,b_33]
    dig2 = [b_13,b_22,b_31]

    # winning moves
    # row moves
    if row1.count(ai_move) == 2 and '' in row1:
        print('w_row1')
        index=row1.index('')
        if index == 0:
            ui.Button_11.setText(ai_move)
        elif index == 1:
            ui.Button_21.setText(ai_move)
        else:
            ui.Button_31.setText(ai_move)

    elif row2.count(ai_move) == 2 and '' in row2:
        print('w_row2')
        index=row2.index('')
        if index == 0:
            ui.Button_12.setText(ai_move)
        elif index == 1:
            ui.Button_22.setText(ai_move)
        else:
            ui.Button_32.setText(ai_move)
            
    elif row3.count(ai_move) == 2 and '' in row3:
        print('w_row3')
        index=row3.index('')
        if index == 0:
            ui.Button_13.setText(ai_move)
        elif index == 1:
            ui.Button_23.setText(ai_move)
        else:
            ui.Button_33.setText(ai_move)
    #colume moves
    elif col1.count(ai_move) == 2 and '' in col1:
        print('w_col1')
        index=col1.index('')
        if index == 0:
            ui.Button_11.setText(ai_move)
        elif index == 1:
            ui.Button_12.setText(ai_move)
        else:
            ui.Button_13.setText(ai_move)

    elif col2.count(ai_move) == 2 and '' in col2:
        print('w_col2')
        index=col2.index('')
        if index == 0:
            ui.Button_21.setText(ai_move)
        elif index == 1:
            ui.Button_22.setText(ai_move)
        else:
            ui.Button_23.setText(ai_move)

    elif col3.count(ai_move) == 2 and '' in col3:
        print('w_col3')
        index=col3.index('')
        if index == 0:
            ui.Button_31.setText(ai_move)
        elif index == 1:
            ui.Button_32.setText(ai_move)
        else:
            ui.Button_33.setText(ai_move)
    
    # digonal moves
    elif dig1.count(ai_move) == 2 and '' in dig1:
        print('w_digonal1')
        index=dig1.index('')
        if index == 0:
            ui.Button_11.setText(ai_move)
        elif index == 1:
            ui.Button_22.setText(ai_move)
        else:
            ui.Button_33.setText(ai_move)

    elif dig2.count(ai_move) == 2 and '' in dig2:
        print('w_digonal2')
        index=dig2.index('')
        if index == 0:
            ui.Button_13.setText(ai_move)
        elif index == 1:
            ui.Button_22.setText(ai_move)
        else:
            ui.Button_31.setText(ai_move)
    

    # saving moves

    # row moves
    elif row1.count(oponnent_move) == 2 and '' in row1:
        print('row1')
        index=row1.index('')
        if index == 0:
            ui.Button_11.setText(ai_move)
        elif index == 1:
            ui.Button_21.setText(ai_move)
        else:
            ui.Button_31.setText(ai_move)

    elif row2.count(oponnent_move) == 2 and '' in row2:
        print('row2')
        index=row2.index('')
        if index == 0:
            ui.Button_12.setText(ai_move)
        elif index == 1:
            ui.Button_22.setText(ai_move)
        else:
            ui.Button_32.setText(ai_move)
            
    elif row3.count(oponnent_move) == 2 and '' in row3:
        print('row3')
        index=row3.index('')
        if index == 0:
            ui.Button_13.setText(ai_move)
        elif index == 1:
            ui.Button_23.setText(ai_move)
        else:
            ui.Button_33.setText(ai_move)
    #colume moves
    elif col1.count(oponnent_move) == 2 and '' in col1:
        print('col1')
        index=col1.index('')
        if index == 0:
            ui.Button_11.setText(ai_move)
        elif index == 1:
            ui.Button_12.setText(ai_move)
        else:
            ui.Button_13.setText(ai_move)

    elif col2.count(oponnent_move) == 2 and '' in col2:
        print('col2')
        index=col2.index('')
        if index == 0:
            ui.Button_21.setText(ai_move)
        elif index == 1:
            ui.Button_22.setText(ai_move)
        else:
            ui.Button_23.setText(ai_move)

    elif col3.count(oponnent_move) == 2 and '' in col3:
        print('col3')
        index=col3.index('')
        if index == 0:
            ui.Button_31.setText(ai_move)
        elif index == 1:
            ui.Button_32.setText(ai_move)
        else:
            ui.Button_33.setText(ai_move)
    
    # digonal moves
    elif dig1.count(oponnent_move) == 2 and '' in dig1:
        print('digonal1')
        index=dig1.index('')
        if index == 0:
            ui.Button_11.setText(ai_move)
        elif index == 1:
            ui.Button_22.setText(ai_move)
        else:
            ui.Button_33.setText(ai_move)

    elif dig2.count(oponnent_move) == 2 and '' in dig2:
        print('digonal2')
        index=dig2.index('')
        if index == 0:
            ui.Button_13.setText(ai_move)
        elif index == 1:
            ui.Button_22.setText(ai_move)
        else:
            ui.Button_31.setText(ai_move)
    

    # random moves
    elif '' in screen:
        print('random')
        lsit_empty_place=indices(screen,'')
        rand = random.choice(lsit_empty_place)
        if rand == 0:
            ui.Button_11.setText(ai_move)
        elif rand == 1:
            ui.Button_12.setText(ai_move)
        elif rand == 2:
            ui.Button_13.setText(ai_move)
        elif rand == 3:
            ui.Button_21.setText(ai_move)
        elif rand == 4:
            ui.Button_22.setText(ai_move)
        elif rand == 5:
            ui.Button_23.setText(ai_move)
        elif rand == 6:
            ui.Button_31.setText(ai_move)
        elif rand == 7:
            ui.Button_32.setText(ai_move)
        elif rand == 8:
            ui.Button_33.setText(ai_move)
        
    change_value(turn)
    ui.turn.setText(turn)
    who_win()
    
def change_value(current_value):
        global turn
        if current_value == "X":
            turn = '0'
        elif current_value == '0':
            turn ='X'


def reset():
    global game_over,turn
    ui.reset_button.setText('Reset')
    ui.Button_11.setText('')
    ui.Button_12.setText('')
    ui.Button_13.setText('')
    ui.Button_21.setText('')
    ui.Button_22.setText('')
    ui.Button_23.setText('')
    ui.Button_31.setText('')
    ui.Button_32.setText('')
    ui.Button_33.setText('')
    turn = '0'
    ui.turn.setText(turn)
    ui.winner.setText('')
    ui.Turn_lable.setText('Turn')
    ui.winner_lable.setText('Winner is:')
    game_over = 0

def if_someone_win(winner):
    global game_over
    threadpool = QThreadPool()
    if winner == "D R A W":
            ui.winner_lable.setText('')
    elif winner == 'X':
        ui.winner.setText('Comp.')
    else:
        ui.winner.setText('You')
    ui.Turn_lable.setText('')
    ui.reset_button.setText('Play')
    ui.turn.setText('Game\nOver!!')
    game_over = 1

def who_win():
        b_11=ui.Button_11.text()
        b_12=ui.Button_12.text()
        b_13=ui.Button_13.text()
        b_21=ui.Button_21.text()
        b_22=ui.Button_22.text()
        b_23=ui.Button_23.text()
        b_31=ui.Button_31.text()
        b_32=ui.Button_32.text()
        b_33=ui.Button_33.text()
        
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

        elif b_12 != '' and b_11 != '' and b_13 != '' and b_21 != '' and b_22 != '' and b_23 != '' and b_31 != '' and b_32 != '' and b_33 != '':
                if_someone_win('D R A W')
        return game_over
        
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
            if game_over == 0:
                ai()
            
            

ui.show()


sys.exit(app.exec_())
