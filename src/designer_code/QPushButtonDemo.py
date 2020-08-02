# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QPushButtonDemo.py


import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')
        self.resize(300, 280)

        self.btn1 = QPushButton('第一个按钮')
        self.btn1.setText('First Button')
        self.btn1.setCheckable(True)  # 可复选
        self.btn1.toggle()  # 初始按钮弹起

        # 在文本前显示图像
        self.btn2 = QPushButton('图像按钮')
        self.btn2.setIcon(QIcon(QPixmap('./icon/adobereader.ico')))

        # 不可用按钮
        self.btn3 = QPushButton('不可用按钮')
        self.btn3.setEnabled(False)

        # 不可用按钮
        self.btn4 = QPushButton('&MyButton')
        self.btn4.setDefault(True)

        # 将信号与槽绑定
        self.btn1.clicked.connect(lambda: self.whichButton(self.btn1))
        self.btn1.clicked.connect(self.buttonState)
        self.btn2.clicked.connect(lambda: self.whichButton(self.btn2))
        self.btn4.clicked.connect(lambda: self.whichButton(self.btn4))

        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        self.setLayout(layout)

    def whichButton(self, btn):
        print('按下按钮：<' + btn.text() + '>')

    def buttonState(self, btn):
        if self.btn1.isChecked():
            print('按钮1被按下')
        else:
            print('按钮1未被按下')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pushButton = QPushButtonDemo()
    pushButton.show()
    sys.exit(app.exec_())
