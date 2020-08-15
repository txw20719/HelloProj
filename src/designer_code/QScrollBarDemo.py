# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QScrollBarDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QScrollBarDemo(QWidget):
    def __init__(self):
        super(QScrollBarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滚动条案例')
        self.resize(300, 280)

        layout = QHBoxLayout()
        self.label = QLabel('拖动滚动条改变颜色和位置')
        layout.addWidget(self.label)

        self.scrollbar1 = QScrollBar()
        self.scrollbar2 = QScrollBar()
        self.scrollbar3 = QScrollBar()
        self.scrollbar4 = QScrollBar()

        self.scrollbar1.setMaximum(255)
        self.scrollbar2.setMaximum(255)
        self.scrollbar3.setMaximum(255)
        self.scrollbar4.setMaximum(255)

        self.scrollbar1.sliderMoved.connect(self.Slidder1)
        self.scrollbar2.sliderMoved.connect(self.Slidder1)
        self.scrollbar3.sliderMoved.connect(self.Slidder1)
        self.scrollbar4.sliderMoved.connect(self.Move)

        layout.addWidget(self.scrollbar1)
        layout.addWidget(self.scrollbar2)
        layout.addWidget(self.scrollbar3)
        layout.addWidget(self.scrollbar4)

        self.setGeometry(300, 300, 300, 200)

        self.y = self.label.pos().y()
        self.setLayout(layout)

    def Move(self):
        self.label.move(self.label.x(), self.y + self.scrollbar4.value())

    def Slidder1(self):
        print(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value())
        palette = QPalette()
        c = QColor(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QScrollBarDemo()
    main.show()
    sys.exit(app.exec_())
