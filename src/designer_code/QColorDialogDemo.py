# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QColorDialogDemo.py

import sys
from PyQt5.QtWidgets import QColorDialog, QLabel, QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPalette


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('字体对话框')
        self.resize(300, 280)

        layout = QVBoxLayout()

        self.button = QPushButton('选择字体颜色')
        self.button.clicked.connect(self.SelectFontColor)
        layout.addWidget(self.button)

        self.button2 = QPushButton('选择字体背景颜色')
        self.button2.clicked.connect(self.SelectFontBGColor)
        layout.addWidget(self.button2)

        self.label = QLabel()
        self.label.setText('Hello World!')
        layout.addWidget(self.label)

        self.setLayout(layout)

    def SelectFontColor(self):
        fontcolor = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, fontcolor)
        self.label.setPalette(p)

    def SelectFontBGColor(self):
        fontbgcolor = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, fontbgcolor)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())