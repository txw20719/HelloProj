# encoding=utf-8
# 代码文件：C:/Users/Administrator/PycharmProjects/HelloProj/src/basic/First.py


import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置一个窗口
    w.resize(300, 150)  # 大小
    w.move(300, 300)  # 坐标
    w.setWindowTitle('第一个窗口')  # 标题
    w.show()  # 显示
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
