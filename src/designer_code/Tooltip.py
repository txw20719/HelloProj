# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/Tooltip.py

import sys
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon


class TooltipFrom(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Sanserif', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('设置控件提示信息')

        self.button1 = QPushButton('按钮')
        self.button1.setToolTip('这是一个按钮Are you ok？')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('icon/adobereader.ico'))
    tooltipFrom = TooltipFrom()
    tooltipFrom.show()
    sys.exit(app.exec_())
