#создай приложение для запоминания информац
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

app = QApplication([])

win = QWidget()
win.resize(400,200)
win.setWindowTitle('memory card')
text = QLabel('какой национальности не существует?')
ans = QPushButton('ответить')


text1 = QLabel('правильно/неправильно')
text2 = QLabel('правильный ответ')

class Question():
    def __init__(self,q,ans1,ans2,ans3,ans4):
        self.q = q
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        answers = [ans1,ans2,ans3,ans4]
        shuffle(answers)
        self.answers = answers

q1 = Question('день независимости кыргызыстана','31 августа','7 апреля','8 марта','31 декабря')

text.setText(q1.q)

groupbox = QGroupBox('варианты ответов')
a1 = QRadioButton(q1.answers[0])
a2 = QRadioButton(q1.answers[1])
a3 = QRadioButton(q1.answers[2])
a4 = QRadioButton(q1.answers[3])

button = QPushButton('ответить')

buttonbox = QButtonGroup()
buttonbox.addButton(a1)
buttonbox.addButton(a2)
buttonbox.addButton(a3)
buttonbox.addButton(a4)

def checkans():
    if a1.isChecked():
        text1.setText('правильно')
        return a1.text()
    else:
        text1.setText('неправильно')
        if a2.isChecked():
            return a2.text()
        if a3.isChecked():
            return a3.text()
        if a4.isChecked():
            return a4.text()


def cleanbut():
    buttonbox.setExclusive(False)
    a1.setChecked(False)
    a2.setChecked(False)
    a3.setChecked(False)
    a4.setChecked(False)
    buttonbox.setExclusive(True)


def ans():
    checkans()
    text.setText('самый сложный вопрос в мире')
    groupbox.hide()
    text2.setText(f'ваш ответ:\n  {checkans()}')
    layt2.addWidget(groupbox1)
    groupbox1.show()
    button.setText('следующий вопрос')

def question():
    cleanbut()
    text.setText('какой национальности не существует?')
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
