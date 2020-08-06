# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QFileDialogDemo.py


import sys
from PyQt5.QtWidgets import QTextEdit, QVBoxLayout, QWidget, QApplication, QFileDialog, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文件对话框')
        self.resize(300, 280)

        layout = QVBoxLayout()

        self.button = QPushButton('选择图片')
        self.button.clicked.connect(self.SelectPic)
        layout.addWidget(self.button)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.button2 = QPushButton('选择文件')
        self.button2.clicked.connect(self.SelectFile)
        layout.addWidget(self.button2)

        self.texts = QTextEdit()
        layout.addWidget(self.texts)

        self.setLayout(layout)

    def SelectPic(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.ico *.png)')
        self.label.setPixmap(QPixmap(fname))

    def SelectFile(self):
        filedialog = QFileDialog()
        filedialog.setFileMode(QFileDialog.AnyFile)
        filedialog.setFilter(QDir.Files)

        if filedialog.exec():
            filenames = filedialog.selectedFiles()
            print(filenames[0])
            with open(filenames[0], encoding='utf-8', mode='r') as file:
                print(file)
                data = file.read()
                print(data)
                self.texts.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
