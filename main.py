#создай приложение для запоминания информац
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

win = QWidget()
win.resize(400,200)
win.setWindowTitle('memory card')
text = QLabel('какой национальности не существует?')
ans = QPushButton('ответить')


groupbox = QGroupBox('варианты ответов')
a1 = QRadioButton('энцы')
a2 = QRadioButton('чулымцы')
a3 = QRadioButton('смурфы')
a4 = QRadioButton('алеуты')
button = QPushButton('ответить')






def ans():
    checkans()
    text.setText('самый сложный вопрос в мире')
    groupbox.hide()

    text2.setText(a1.text())

    layt2.addWidget(groupbox1)
    groupbox1.show()
    button.setText('следующий вопрос')

def question():
    text.setText('question')
    groupbox1.hide()
    groupbox.show()
    button.setText('ответить')


def checkbutton():
    if button.text() == 'ответить':
        ans()
    elif button.text() == 'следующий вопрос':
        question()

def ask(q,*args):
    text.setText(q)
    a1.setText(args[1])
    a3.setText(args[2])
    a3.setText(args[3])
    a4.setText(args[4])



button.clicked.connect(checkbutton)


thelayt = QVBoxLayout()
layt1 = QHBoxLayout()
layt2 = QHBoxLayout()
laytbut = QVBoxLayout()

laytans1 = QHBoxLayout()
laytans2 = QVBoxLayout()
laytans3 = QVBoxLayout()


laytans2.addWidget(a1)
laytans2.addWidget(a2)
laytans3.addWidget(a3)
laytans3.addWidget(a4)
laytans1.addLayout(laytans2)
laytans1.addLayout(laytans3)
laytbut.addWidget(button)


groupbox.setLayout(laytans1)
groupbox1 = QGroupBox('результаты теста')

text1 = QLabel('правильно/неправильно')
text2 = QLabel('правильный ответ')

boxlayt = QVBoxLayout()

boxlayt.addWidget(text1)
boxlayt.addWidget(text2,alignment=Qt.AlignHCenter)
groupbox1.setLayout(boxlayt)

layt1.addWidget(text,alignment=Qt.AlignHCenter)
layt2.addWidget(groupbox)
thelayt.addLayout(layt1)
thelayt.addLayout(layt2)
thelayt.addLayout(laytbut)






win.setLayout(thelayt)
win.show()
app.exec()

