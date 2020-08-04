# encoding=utf-8
# 代码文件：HelloProj/src/QComboBoxDemo.py
"""列表控件（QComboBox）

1.将列表项添加到QComboBox
2.获取选中的列表项
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QFont


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QComboBoxDemo')
        self.resize(300, 280)
        layout = QVBoxLayout()

        self.label = QLabel('请选择语言...')

        self.cb = QComboBox()
        self.cb.addItem('C')
        self.cb.addItem('C++')
        self.cb.addItems(['Java', 'Python'])

        self.cb.currentIndexChanged.connect(self.SelectionChanged)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def SelectionChanged(self, i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()
        self.label.setFont(QFont('Arial', 20))

        for item in range(self.cb.count()):
            print('Item:' + str(item) + ',' + self.cb.itemText(item))

        print('CurrentIndex:' + str(i) + ',SelecctionChanged：' + self.cb.itemText(i))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboBoxDemo = QComboBoxDemo()
    comboBoxDemo.show()
    sys.exit(app.exec_())
