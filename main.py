import sys

from PyQt5 import uic
from random import randrange
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        self.pnt(painter)
        painter.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def pnt(self, painter):
        painter.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
        n = randrange(321)
        painter.drawEllipse(270, 210, n, n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
