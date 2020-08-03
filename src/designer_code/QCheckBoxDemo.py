# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QCheckBoxDemo.py
"""复选框组件（QCheckBox）

3种状态
0：未选中
1：半选中
2：选中
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import Qt


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QCheckBoxDemo')
        layout = QHBoxLayout()

        self.checkBox1 = QCheckBox('复选框1')
        self.checkBox2 = QCheckBox('复选框2')
        self.checkBox3 = QCheckBox('半选框')

        # 设置状态
        self.checkBox1.setChecked(True)
        self.checkBox2.setChecked(False)
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)

        # 为信号绑定槽
        self.checkBox1.stateChanged.connect(lambda: self.CheckBoxState(self.checkBox1))
        self.checkBox2.stateChanged.connect(lambda: self.CheckBoxState(self.checkBox2))
        self.checkBox3.stateChanged.connect(lambda: self.CheckBoxState(self.checkBox3))

        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.checkBox3)
        self.setLayout(layout)

    def CheckBoxState(self, cb):
        checkState1 = self.checkBox1.text() + ',isChecked=' + str(self.checkBox1.isChecked()) + ',isState=' + str(
            self.checkBox1.checkState()) + '\n'
        checkState2 = self.checkBox2.text() + ',isChecked=' + str(self.checkBox2.isChecked()) + ',isState=' + str(
            self.checkBox2.checkState()) + '\n'
        checkState3 = self.checkBox3.text() + ',isChecked=' + str(self.checkBox3.isChecked()) + ',isState=' + str(
            self.checkBox3.checkState()) + '\n'
        print(checkState1 + checkState2 + checkState3 + '\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkBoxDemo = QCheckBoxDemo()
    checkBoxDemo.show()
    sys.exit(app.exec_())
