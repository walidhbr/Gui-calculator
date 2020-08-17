from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 450)
        self.setWindowTitle('Calculator')
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.setFont(font)
        self.string = str(0)
        self.val = float(0)
        self.op = ''
        self.ans = float(0)
        self.ini_window()

    def ini_window(self):
        grid = QGridLayout()
        self.setLayout(grid)
        name = ['CE', 'C', '%', '*', '7', '8', '9', '/', '4', '5',
                '6', '-', '1', '2', '3', '+', '00', '0', '.', '=', ]
        position = [(i + 1, j) for i in range(5) for j in range(4)]
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.setFixedHeight(100)

        grid.addWidget(self.lcd, 0, 0, 1, 4)
        for position, name in zip(position, name):
            self.button = QPushButton(name)
            self.button.setFixedSize(80, 60)
            grid.addWidget(self.button, *position)
            self.button.clicked.connect(self.click_btn)
        self.show()

    def click_btn(self):
        try:
            sender = self.button.sender().text()
            if sender in ['00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                self.string += sender
                self.lcd.display(float(self.string))

            elif sender in ['+', '-', '*', '/', '%']:
                self.op = sender
                if self.ans == float(0):
                    if self.val == float(0):
                        self.val = self.string
                        self.string = str(0)
                else:
                    self.val = self.ans
                    self.string = str(0)

            elif sender == '=':
                if self.op in ['+', '-', '/', '*', '%']:
                    self.ans = eval(str(float(self.val)) + self.op + str(float(self.string)))
                    self.lcd.display(self.ans)
                else:
                    self.ans = float(self.string)
                    self.lcd.display(self.ans)

            elif sender == 'C':
                self.string = str(0)
                self.ans = float(0)
                self.val = float(0)
                self.op = ''
                self.lcd.display(0)
            else:
                self.string = str(0)
                self.lcd.display(0)

        except ZeroDivisionError:
            self.lcd.display("Du Err")
        except ValueError:
            self.lcd.display("Sy Err ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    sys.exit(app.exec())
