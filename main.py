from PyQt5.QtWidgets import QApplication

from random import choice, shuffle
from time import sleep

app = QApplication([])

from qwq import *
from ууу import *

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_afk = 0
        self.count_right = 0
    def got_right(self):
        self.count_afk += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_afk += 1
q1 = Question('У виразі (50-1)+(21-20) відповідь буде', '50', '1', '49', '20')
q2 = Question('У виразі 56-(90-80)+2 відповідь буде', '48', '10', '44', '84')
q3 = Question('У виразі 65+(34-30)-60 відповідь буде', '9', '30', '17', '3')
q4 = Question('У виразі 12-(15-7) відповідь буде', '4', '7', '13', '9')
q5 = Question('У виразі 6+(13-5) відповідь буде', '14', '67', '41', '0')
q6 = Question('У виразі 28-(35-24) відповідь буде', '17', '20', '13', '10')
q7 = Question('У виразі 16-8 відповідь буде', '8', '6', '9', '2')
q8 = Question('У виразі 13-9 відповідь буде', '4', '2', '6', '3')
q9 = Question('У виразі 13-7 відповідь буде', '6', '2', '0', '7')
q10 = Question('У виразі 34-6 відповідь буде', '28', '21', '31', '24')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Правильно!')
                answer.setChecked(False)
                break
    else:
        lb_result.setText('Неправильно!')
    RadioGroup.setExclusive(True)

def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_guestion.hide()
        gb_answer.show()
        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_guestion.show()
        btn_next.setText('Відповісти')
btn_next.clicked.connect(click_ok)
def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)
def add_question():
    new_q = Question(le_question.text(), lb_right_answer.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(new_q)
    clear()
btn_add_qustion.clicked.connect(add_question)

def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)

window.show()
app.exec_()

