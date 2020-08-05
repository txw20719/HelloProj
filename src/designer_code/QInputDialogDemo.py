# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QInputDialogDemo.py

import sys
from PyQt5.QtWidgets import QLineEdit, QFormLayout, QWidget, QApplication, QInputDialog, QPushButton


class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('主窗口')
        self.resize(300, 280)

        layout = QFormLayout()

        self.button1 = QPushButton('获取列表中的选项')
        self.button1.clicked.connect(self.GetItem)
        self.label1 = QLineEdit()
        layout.addRow(self.button1, self.label1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.GetStr)
        self.label2 = QLineEdit()
        layout.addRow(self.button2, self.label2)

        self.button3 = QPushButton('获取字符串')
        self.button3.clicked.connect(self.GetInt)
        self.label3 = QLineEdit()
        layout.addRow(self.button3, self.label3)

        self.setLayout(layout)

    def GetItem(self):
        items = ('java', 'c', 'c++', 'python')
        item, ok = QInputDialog.getItem(self, '请选择编程语言', '语言列表', items)
        if item and ok:
            self.label1.setText(item)

    def GetStr(self):
        name, ok = QInputDialog.getText(self, '文本输入框', '请输入姓名')
        if name and ok:
            self.label2.setText(str(name))

    def GetInt(self):
        num, ok = QInputDialog.getInt(self, '整数输入框', '请输入数字')
        if num and ok:
            self.label3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())