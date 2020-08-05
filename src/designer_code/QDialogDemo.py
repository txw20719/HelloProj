# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QDialogDemo.py
"""QDialog（对话框）

1. QMessageBox
2. QColorDialog
3. QFileDialog
4. QInputDialog
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QPushButton, QApplication
from PyQt5.QtCore import Qt


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('主窗口')

        self.pushButton = QPushButton(self)
        self.pushButton.setText('弹出对话框')
        self.pushButton.move(50, 50)
        self.pushButton.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)

        button = QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)

        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogDemo = QDialogDemo()
    dialogDemo.show()
    sys.exit(app.exec_())
