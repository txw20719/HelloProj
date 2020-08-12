# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QDockWidgetDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDockWidgetDemo(QMainWindow):
    def __init__(self):
        super(QDockWidgetDemo, self).__init__()
        self.setWindowTitle('停靠控件')
        self.resize(300, 280)

        self.dock = QDockWidget('Dockable', self)
        # 设置初始悬浮
        self.dock.setFloating(True)

        self.list = QListWidget()
        self.list.addItem('列表项1')
        self.list.addItem('列表项2')
        self.list.addItem('列表项3')

        self.dock.setWidget(self.list)

        self.setCentralWidget(QLineEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDockWidgetDemo()
    main.show()
    sys.exit(app.exec_())
