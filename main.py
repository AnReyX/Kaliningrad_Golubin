import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.qp = QPainter()
        self.flag = False
        self.button = QPushButton('Сделать круги', self)
        self.button.clicked.connect(self.drawf)
        self.button.resize(100, 100)
        self.button.move(250, 250)

    def initUI(self):
        self.setGeometry(400, 100, 500, 500)
        self.setWindowTitle('Кружочки owo')

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def drawf(self):
        self.flag = True
        self.update()

    def draw(self):
        R = randint(20, 100)
        coords = [randint(100, 400) for _ in range(2)]
        self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
        self.qp.drawEllipse(int(coords[0] - R / 2), int(coords[1] - R / 2), R, R)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
