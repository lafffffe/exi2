import sys

import random
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellips(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_ellips(self, qp):
        qp.setBrush(QColor(255, 207, 64))
        r = random.randint(1, 400)
        qp.drawEllipse(r, r, r, r)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())