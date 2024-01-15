import sys
from random import choice
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Template:
    def __init__(self, screen):
        uic.loadUi('UI.ui', screen)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        Template(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            for i in range(10):
                self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setPen(QColor(choice(range(256)), choice(range(256)), choice(range(256))))
        diametr = choice(range(200))
        qp.drawEllipse(choice(range(self.width())), choice(range(self.height())), diametr, diametr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
