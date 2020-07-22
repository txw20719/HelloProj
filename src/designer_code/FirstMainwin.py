# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/FirstMainwin.py


import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QWidget, QHBoxLayout


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()
        # 设置窗口标题
        self.setWindowTitle('第一个主窗口')

        # 设置窗口尺寸
        self.resize(400, 300)

        # 设置状态条
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒', 5000)

        self.center()

        # 创建button
        self.button1 = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        app.quit()

    def center(self):
        # 获取银幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('icon/adobereader.ico'))

    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
