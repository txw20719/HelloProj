# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QListViewDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class QListWidgetDemo(QMainWindow):
    def __init__(self):
        super(QListWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('扩展列表')
        self.resize(300, 700)

        self.listWidget = QListWidget()
        self.listWidget.addItem('列表1')
        self.listWidget.addItem('列表2')
        self.listWidget.addItem('列表3')

        self.listWidget.itemClicked.connect(self.ClickList)

        self.setCentralWidget(self.listWidget)

    def ClickList(self, index):
        QMessageBox.information(self, 'QListWidget', '您选择了：' + self.listWidget.item(self.listWidget.row(index)).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QListWidgetDemo()
    main.show()
    sys.exit(app.exec_())
