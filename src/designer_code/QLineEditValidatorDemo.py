# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QLineEditValidatorDemo.py
"""QLineEdit控件的输入（校验器）
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditValidatorDemo(QWidget):
    def __init__(self):
        super(QLineEditValidatorDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        regExpLineEdit = QLineEdit()

        intLineEdit.setPlaceholderText('整数')
        doubleLineEdit.setPlaceholderText('小数')
        regExpLineEdit.setPlaceholderText('字母和数字')

        # 创建校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 50)  # [1,50]取值范围
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-100, 100, 2)  # [-100,100]小数点后两位
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)  # 标准化将字符串转为double
        regExpValidator = QRegExpValidator(self)
        reg = QRegExp('[a-zA-Z0-9]+$')
        regExpValidator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        regExpLineEdit.setValidator(regExpValidator)

        formLayout = QFormLayout()
        formLayout.addRow('整型类型', intLineEdit)
        formLayout.addRow('浮点类型', doubleLineEdit)
        formLayout.addRow('数字和字母', regExpLineEdit)
        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lineEditValidatorDemo = QLineEditValidatorDemo()
    lineEditValidatorDemo.show()
    sys.exit(app.exec_())
