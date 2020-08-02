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

        # 给button的信号绑定槽
        self.buttonText.clicked.connect(self.onClick_buttonText)
        self.buttonHTML.clicked.connect(self.onClick_buttonHTML)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)

        self.setLayout(layout)

    def onClick_buttonText(self):
        self.textEdit.setText('Hello World!!')

    def onClick_buttonHTML(self):
        self.textEdit.setHtml("<font color='green' size='10'>Hello World!!</font>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    textEdit = QTextEditDemo()
    textEdit.show()
    sys.exit(app.exec_())
