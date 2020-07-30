# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/ScreenGeometry.py


import sys

from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QPushButton, QMainWindow


def onClick_Button():
    print('窗口外围坐标系')
    print('widget.x():%d' % widget.x())
    print('widget.y():%d' % widget.y())
    print('widget.width():%d' % widget.width())  # 工作区宽度
    print('widget.height():%d' % widget.height())

    print('窗口坐标系')
    print('widget.geometry().x():%d' % widget.geometry().x())
    print('widget.geometry().y():%d' % widget.geometry().y())
    print('widget.geometry().width():%d' % widget.geometry().width())  # 工作区宽度
    print('widget.geometry().height():%d' % widget.geometry().height())

    print('widget.frameGeometry().x():%d' % widget.frameGeometry().x())
    print('widget.frameGeometry().x():%d' % widget.frameGeometry().y())
    print('widget.frameGeometry().width():%d' % widget.frameGeometry().width())  # 窗口宽度
    print('widget.frameGeometry().height():%d' % widget.frameGeometry().height())


app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_Button)
btn.move(20, 20)

widget.resize(400, 300)  # 设置工作区的尺寸
widget.move(100, 200)
widget.setWindowTitle('屏幕坐标系测试')
widget.show()
sys.exit(app.exec_())
