from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QApplication
from PyQt5.QtCore import Qt

window = QWidget()
btn_menu = QPushButton('Meny')
btn_rest = QPushButton('Відпочинок')
btn_next = QPushButton('відповісти')

rb_ans1 = QRadioButton('1')
rb_ans2 = QRadioButton('2')
rb_ans3 = QRadioButton('3')
rb_ans4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)

lb_question = QLabel('Запитання')
lb_question.setStyleSheet('color:#0A09D6; font-size:20px')
window.setStyleSheet('background:red')
lb_rest = QLabel('хвилин')
lb_result = QLabel('Правильно')
lb_right_answer = QLabel('відповідь')

sp_rest = QSpinBox()
gb_guestion = QGroupBox('Варіанти відповідей')

rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h1 = QHBoxLayout()

rb_v1. addWidget(rb_ans1)
rb_v1. addWidget(rb_ans2)
rb_v2. addWidget(rb_ans3)
rb_v2. addWidget(rb_ans4)

rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)
gb_guestion.seLayour(rb_h1)

gb_answer = QGroupBox()
v1 = QVBoxLayout()
v1.addWidget(lb_right_answer)
gb_answer.setLayout(v1)

h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QVBoxLayout()

h1_main.addWidget(btn_menu)
h1_main.addStretch(1)
h1_main.addWidget(btn_rest)
h1_main.addWidget(sp_rest)
h1_main.addWidget(lb_rest)

h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QVBoxLayout()

h1_main.addWidget(btn_menu)
h1_main.addStretch(1)
h1_main.addWidget(btn_rest)
h1_main.addWidget(sp_rest)
h1_main.addWidget(lb_rest)

h2_main.addWidget(lb_question, alignment=(Qt.AlignHCeter | Qt.AlignVCenter))
h3_main.addWidget(gb_answer)
h3_main.addWidget(gb_guestion)
gb_answer.hide()

h4_main.addStretch(1)
h4_main.addWidget(btn_next, stretch=2)
h4_main.addStretch(1)

v1_main.addChildLayout(h1_main, stretch=1)
v1_main.addChildLayout(h2_main, stretch=2)
v1_main.addChildLayout(h3_main, stretch=8)
v1_main.addChildLayout(h4_main)
v1_main.setSpacing(5)
window.setLayout(v1_main)
window.resize(550, 450)
