# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTextEditDemo.py

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QVBoxLayout, QPushButton


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('多行文本控件')
        self.resize(300, 280)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')
        self.buttonToText = QPushButton('获取文本')
        self.buttonToHTML = QPushButton('获取HTML')

        # 给button的信号绑定槽
        self.buttonText.clicked.connect(self.onClick_buttonText)
        self.buttonHTML.clicked.connect(self.onClick_buttonHTML)
        self.buttonToText.clicked.connect(self.onClick_buttonToText)
        self.buttonToHTML.clicked.connect(self.onClick_buttonToHTML)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHTML)

        self.setLayout(layout)

    def onClick_buttonText(self):
        self.textEdit.setPlainText('Hello World!!')

    def onClick_buttonHTML(self):
        self.textEdit.setHtml("<font color='green' size='10'>Hello World!!</font>")

    def onClick_buttonToText(self):
        print(self.textEdit.toPlainText())

    def onClick_buttonToHTML(self):
        print(self.textEdit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    textEdit = QTextEditDemo()
    textEdit.show()
    sys.exit(app.exec_())
