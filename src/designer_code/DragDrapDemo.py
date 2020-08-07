# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/DragDrapDemo.py


import sys
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QFormLayout, QWidget, QApplication, QLabel, QComboBox
from PyQt5.QtCore import Qt


class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        print(e.mimeData().text())
        self.addItem(e.mimeData().text())


class MyTextEdit(QTextEdit):
    def __init__(self):
        super(MyTextEdit, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class DragDrapDemo(QWidget):
    def __init__(self):
        super(DragDrapDemo, self).__init__()
        self.setWindowTitle('拖拽案例')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        layout = QFormLayout()
        layout.addRow(QLabel('请将左边的文本拖进右边下拉列表框中...'))

        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)
        comboBox = MyComboBox()
        layout.addRow(lineEdit, comboBox)
        layout.addRow(MyTextEdit())

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DragDrapDemo()
    main.show()
    sys.exit(app.exec_())
