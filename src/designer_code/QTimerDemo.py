# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTimerDemo.py
"""QTimer（时间控件）

1. 动态显示当前时间
2. 五秒后程序自动关闭
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QTimerDemo(QWidget):
    def __init__(self):
        super(QTimerDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('时间案例')
        self.resize(300, 280)

        layout = QGridLayout()
        self.label = QLabel('显示当前时间')
        self.btn_start = QPushButton('开始')
        self.btn_stop = QPushButton('结束')
        self.timer = QTimer()

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.btn_start, 1, 0)
        layout.addWidget(self.btn_stop, 1, 1)

        self.timer.timeout.connect(self.ShowTime)
        self.btn_start.clicked.connect(self.StartTimer)
        self.btn_stop.clicked.connect(self.StopTimer)

        self.setLayout(layout)

    def ShowTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(timeDisplay)

    def StartTimer(self):
        # 间隔调用
        self.timer.start(1000)
        self.btn_start.setEnabled(False)
        self.btn_stop.setEnabled(True)

    def StopTimer(self):
        self.timer.stop()
        self.btn_start.setEnabled(True)
        self.btn_stop.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTimerDemo()
    main.show()
    # 五秒后程序自动关闭
    QTimer.singleShot(5000, app.quit)
    sys.exit(app.exec_())
