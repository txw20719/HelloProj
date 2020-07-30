# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QLabelDemo.py


import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QLabel, QPushButton, QWidget
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color='yellow'>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)
        # 设置调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)  # 设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)  # 设置文字对齐方式

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('icon/adobereader.ico'))

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='http://www.baidu.com'>百度一下</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print('鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('鼠标点击label4标签时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    labelDemo = QLabelDemo()
    labelDemo.show()
    sys.exit(app.exec_())
