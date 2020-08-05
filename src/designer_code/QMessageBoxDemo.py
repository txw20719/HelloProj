# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QMessageBoxDemo.py
"""QMessageBox(消息对话框)

1. 关于对话框
2. 消息对话框
3. 错误对话框
4. 警告对话框
5. 提问对话框

1. 图标不一样
2. 按钮可能不一样
"""

import sys
from PyQt5.QtWidgets import QMessageBox, QWidget, QVBoxLayout, QApplication, QPushButton


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('主窗口')
        self.resize(300, 500)

        layout = QVBoxLayout()

        self.button1 = QPushButton('显示关于对话框')
        self.button2 = QPushButton('显示消息对话框')
        self.button3 = QPushButton('显示错误对话框')
        self.button4 = QPushButton('显示警告对话框')
        self.button5 = QPushButton('显示提问对话框')

        # 为信号绑定槽
        self.button1.clicked.connect(self.ShowDialog)
        self.button2.clicked.connect(self.ShowDialog)
        self.button3.clicked.connect(self.ShowDialog)
        self.button4.clicked.connect(self.ShowDialog)
        self.button5.clicked.connect(self.ShowDialog)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)

        self.setLayout(layout)

    def ShowDialog(self):
        clicked_text = self.sender().text()
        if clicked_text == '显示关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        elif clicked_text == '显示消息对话框':
            reply = QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply == QMessageBox.Yes)
        elif clicked_text == '显示错误对话框':
            reply = QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply == QMessageBox.Yes)
        elif clicked_text == '显示警告对话框':
            QMessageBox.warning(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif clicked_text == '显示提问对话框':
            QMessageBox.question(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    messageBoxDemo = QMessageBoxDemo()
    messageBoxDemo.show()
    sys.exit(app.exec_())
