# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTabWidgetDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QTabWidgetDemo(QTabWidget):
    def __init__(self):
        super(QTabWidgetDemo, self).__init__()
        self.resize(300, 280)
        # 创建显示控件的窗口
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, '选项卡1')
        self.addTab(self.tab2, '选项卡1')
        self.addTab(self.tab3, '选项卡1')

        self.initUI1()
        self.initUI2()
        self.initUI3()

    def initUI1(self):
        layout = QFormLayout()
        layout.addRow('姓名：', QLineEdit())
        layout.addRow('地址：', QLineEdit())
        self.setTabText(0, '联系方式')
        self.tab1.setLayout(layout)

    def initUI2(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'), sex)
        layout.addRow(QLabel('生日'), QLineEdit())
        self.setTabText(1, '详细信息')
        self.tab2.setLayout(layout)

    def initUI3(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目：'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('数学'))
        self.setTabText(2, '教育程度')
        self.tab3.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTabWidgetDemo()
    main.show()
    sys.exit(app.exec_())
