from PyQt5.QtCore import Qt,QTime,QTimer, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout , QVBoxLayout, QGridLayout, QGroupBox,QRadioButton,QPushButton,QLabel,QListWidget,QLineEdit)

from all_text import *
from second import *

class MainWin(QWidget):#экран и что есть в нем
    def __init__(self):#описаниеэкаран
        super().__init__()
        self.set_appear()#размер экрана
        self.initUI()#виджеты которык будут на экране
        self.connects()#за возможности кнопок
        self.show()#Показывать экран

    def set_appear(self):#Делаем экран название, размер и координат где будет находится
        self.setWindowTitle('Проверка сердце')
        self.resize(800, 500)
        self.move(400,200)

    def initUI(self):#виджеты
        self.hello_text = QLabel('Добро пожаловать в программу по определению состоянию здоровья!')
        self.instruction = QLabel(txt_instruk )
        self.btn_next = QPushButton('Начать')
        self.layout = QVBoxLayout()#Линии
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)#для запуска

    def next_click(self):
        self.tw = TestWin()
        self.hide()#закрывает 1 страницу и открывет 2 экарн

    def connects(self):#подключаем кнопки
        self.btn_next.clicked.connect(self.next_click)


def main():#запуск
    app = QApplication([])
    mw = MainWin()
    app.exec_()

main()

