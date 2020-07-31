# encoding=utf-8
# 代码文件:HelloProj/src/designer_code/QLabelBuddyDemo.py
"""
QLabel与伙伴关系

"""


import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QWidget, QApplication, QGridLayout, QLabel, QLineEdit


class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴关系')

        nameLabel = QLabel('&Name', self)
        nameEdit = QLineEdit(self)
        nameLabel.setBuddy(nameEdit)  # 设置伙伴关系

        passwordLabel = QLabel('&Password', self)
        passwordEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordEdit)  # 设置伙伴关系

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    labelBuddy = QLabelBuddy()
    labelBuddy.show()
    sys.exit(app.exec_())
