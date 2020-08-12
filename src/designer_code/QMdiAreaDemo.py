# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QMdiAreaDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QMdiAreaDemo(QMainWindow):
    count = 0

    def __init__(self):
        super(QMdiAreaDemo, self).__init__()
        self.setWindowTitle('容纳多文档窗口')
        self.resize(300, 280)

        self.mdi = QMdiArea()
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('Cascade')
        file.addAction('Tiled')

        file.triggered.connect(self.WindowAction)
        self.setCentralWidget(self.mdi)

    def WindowAction(self, q):
        print(q.text())
        if q.text() == 'New':
            QMdiAreaDemo.count += 1
            sub = QMdiSubWindow()
            sub.setWidget(QLineEdit())
            sub.setWindowTitle('新窗口' + str(QMdiAreaDemo.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == 'Cascade':
            self.mdi.cascadeSubWindows()
        elif q.text() == 'Tiled':
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMdiAreaDemo()
    main.show()
    sys.exit(app.exec_())