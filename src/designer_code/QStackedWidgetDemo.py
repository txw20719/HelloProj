# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QStackedWidgetDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QStackedWidgetDemo(QTabWidget):
    def __init__(self):
        super(QStackedWidgetDemo, self).__init__()
        self.setWindowTitle('堆栈窗口控件')
        self.resize(300, 280)

        self.list = QListWidget()
        self.list.insertItem(0, '联系方式')
        self.list.insertItem(1, '个人信息')
        self.list.insertItem(2, '教育程度')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.initUI1()
        self.initUI2()
        self.initUI3()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        # 为信号添加槽
        self.list.currentRowChanged.connect(self.ChangeStack)

        layout = QHBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.stack)
        self.setLayout(layout)

    def ChangeStack(self, index):
        self.stack.setCurrentIndex(index)

    def initUI1(self):
        layout = QFormLayout()
        layout.addRow('姓名：', QLineEdit())
        layout.addRow('地址：', QLineEdit())
        self.stack1.setLayout(layout)

    def initUI2(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'), sex)
        layout.addRow(QLabel('生日'), QLineEdit())
        self.stack2.setLayout(layout)

    def initUI3(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目：'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('数学'))
        self.stack3.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QStackedWidgetDemo()
    main.show()
    sys.exit(app.exec_())
