# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QRadioButtonDemo.py


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButtonDemo')
        layout = QHBoxLayout()

        self.radioButton1 = QRadioButton('单选按钮1')
        self.radioButton2 = QRadioButton('单选按钮2')

        self.radioButton1.setChecked(True)

        # 为信号设置槽
        self.radioButton1.toggled.connect(self.buttonState)
        self.radioButton2.toggled.connect(self.buttonState)

        layout.addWidget(self.radioButton1)
        layout.addWidget(self.radioButton2)
        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print('<'+radioButton.text()+'>被选中')
        else:
            print('<' + radioButton.text() + '>被取消选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    radioButtonDemo = QRadioButtonDemo()
    radioButtonDemo.show()
    sys.exit(app.exec_())
