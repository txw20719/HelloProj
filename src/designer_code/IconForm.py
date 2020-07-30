# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/IconForm.py


import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QWidget, QHBoxLayout
'''
QMainWindow中的setWindowIcon方法同于设置窗口的图标，只在windows中可用

QApplication中的setWindowIcon方法用于设置主窗口的图标和应用程序图标
但调用QMainWindow中的setWindowIcon方法只能设置应用程序图标
'''


class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置位置和尺寸
        self.setGeometry(300, 300, 250, 250)
        # 设置窗口标题
        self.setWindowTitle('设置窗口图标')
        # 设置图标
        self.setWindowIcon(QIcon('./icon/adobereader.ico'))  # 在windows下起效果


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./icon/adobereader.ico'))

    main = IconForm()
    main.show()
    sys.exit(app.exec_())
