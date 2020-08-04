# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QSpinBoxDemo.py
"""计数器控件（QSpinBox）
"""

import sys
from PyQt5.QtWidgets import QLabel, QSlider, QApplication, QSpinBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计数器控件')
        self.resize(300, 280)
        layout = QVBoxLayout()

        self.label = QLabel('数值：')
        self.label.setAlignment(Qt.AlignCenter)

        self.spinBox = QSpinBox()
        self.spinBox.valueChanged.connect(self.ValueChanged)
        self.spinBox.setRange(1, 99999)
        self.spinBox.setSingleStep(20)
        self.spinBox.setValue(20)

        layout.addWidget(self.label)
        layout.addWidget(self.spinBox)
        self.setLayout(layout)

    def ValueChanged(self):
        self.label.setText('数值：' + str(self.spinBox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    spinBoxDemo = QSpinBoxDemo()
    spinBoxDemo.show()
    sys.exit(app.exec_())