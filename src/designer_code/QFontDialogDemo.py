# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QFontDialog.py

import sys
from PyQt5.QtWidgets import QFontDialog, QLabel, QWidget, QApplication, QVBoxLayout, QPushButton


class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('字体对话框')
        self.resize(300, 280)

        layout = QVBoxLayout()

        self.button = QPushButton('选择字体')
        self.button.clicked.connect(self.SelectFont)
        layout.addWidget(self.button)

        self.label = QLabel()
        self.label.setText('Hello World!')
        layout.addWidget(self.label)

        self.setLayout(layout)

    def SelectFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())