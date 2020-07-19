# encoding=utf-8
# 代码文件：HelloProj/src/basic/RunMainWinHorizontalLayout.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


from src.designer.MainWinHorizontalLayout import Ui_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())
