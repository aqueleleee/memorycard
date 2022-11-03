#создай приложение для запоминания информац
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

app = QApplication([])

win = QWidget()
win.resize(400,200)
win.setWindowTitle('memory card')
text = QLabel()
ans = QPushButton('ответить')


text1 = QLabel('правильно/неправильно')
text2 = QLabel('правильный ответ')


class Question():
    def __init__(self, q, ans1, wr2, wr3, wr4):
        self.q = q
        self.ans1 = ans1
        self.wr2 = wr2
        self.wr3 = wr3
        self.wr4 = wr4



quest1 = Question('день независимости кыргызыстана', '31 августа', '7 апреля', '8 марта', '31 декабря')
quest2 = Question('Сколько синих полос на флаге США?',0,7,8,4)
quest3 = Question('Сколько костей в теле человека?',206,280,170,649)
quest4 = Question('Как назывался корабль капитана Джека Воробья в "Пиратах Карибского моря"?',
                  'Черная жемчужина','Мародер','Слизерин','Черный питон')

qlist = [quest1,quest2,quest3,quest4]

groupbox = QGroupBox('варианты ответов')
a1 = QRadioButton()
a2 = QRadioButton()
a3 = QRadioButton()
a4 = QRadioButton()

answers = [a1,a2,a3,a4]


button = QPushButton('ответить')

buttonbox = QButtonGroup()
buttonbox.addButton(a1)
buttonbox.addButton(a2)
buttonbox.addButton(a3)
buttonbox.addButton(a4)

def checkans():
    if answers[0].isChecked():
        text1.setText('правильно')
        return answers[0].text()
    else:
        text1.setText('неправильно')
        if answers[1].isChecked():
            return answers[1].text()
        if answers[2].isChecked():
            return answers[2].text()
        if answers[3].isChecked():
            return answers[3].text()


def cleanbut():
    buttonbox.setExclusive(False)
    a1.setChecked(False)
    a2.setChecked(False)
    a3.setChecked(False)
    a4.setChecked(False)
    buttonbox.setExclusive(True)

def question():
    cleanbut()
    nextq()
    groupbox1.hide()
    groupbox.show()
    button.setText('ответить')

def ans():
    checkans()
    text.setText('самый сложный вопрос в мире')
    groupbox.hide()
    text2.setText(f'ваш ответ:\n  {checkans()}')
    layt2.addWidget(groupbox1)
    groupbox1.show()
    button.setText('следующий вопрос')




def checkbutton():
    if button.text() == 'ответить':
        ans()
    elif button.text() == 'следующий вопрос':
        question()


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



def nextq():
    time += 1
    if time >= len(qlist):
        time = 0
    addq(qlist[time])

time = -1

def addq(cls):
    shuffle(answers)
    text.setText(cls.q)
    answers[0].setText(cls.ans1)
    answers[1].setText(cls.wr2)
    answers[2].setText(cls.wr3)
    answers[3].setText(cls.wr4)


win.setLayout(thelayt)
win.show()
app.exec()
