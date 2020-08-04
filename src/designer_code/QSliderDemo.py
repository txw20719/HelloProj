# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QSliderDemo.py
"""滑块控件（QSlider）
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件测试')
        self.resize(300, 280)
        layout = QGridLayout()
        self.label = QLabel('Hello Word！')
        self.label.setAlignment(Qt.AlignCenter)
        self.vertical_Slider = QSlider(Qt.Vertical)
        # 设置最大值、最小值、当前值、步长
        self.vertical_Slider.setMinimum(10)
        self.vertical_Slider.setMaximum(30)
        self.vertical_Slider.setValue(20)
        self.vertical_Slider.setSingleStep(5)
        # 设置刻度位置、间隔
        self.vertical_Slider.setTickPosition(QSlider.TicksLeft)
        self.vertical_Slider.setTickInterval(10)

        self.Horizontal_Slider = QSlider(Qt.Horizontal)
        # 设置最大值、最小值、当前值、步长
        self.Horizontal_Slider.setMinimum(10)
        self.Horizontal_Slider.setMaximum(30)
        self.Horizontal_Slider.setValue(14)
        self.Horizontal_Slider.setSingleStep(4)
        # 设置刻度位置、间隔
        self.Horizontal_Slider.setTickPosition(QSlider.TicksBelow)
        self.Horizontal_Slider.setTickInterval(4)

        # 为信号绑定槽
        self.vertical_Slider.valueChanged.connect(self.ValueChange)
        self.Horizontal_Slider.valueChanged.connect(self.ValueChange)

        layout.addWidget(self.vertical_Slider, 0, 0, 6, 1)
        layout.addWidget(self.label, 0, 1, 2, 4)
        layout.addWidget(self.Horizontal_Slider, 1, 1, 4, 4)
        self.setLayout(layout)

    def ValueChange(self):
        print('当前值：%s' % self.sender().value())
        font_Size = self.sender().value()
        self.label.setFont(QFont('Arial', font_Size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sliderDemo = QSliderDemo()
    sliderDemo.show()
    sys.exit(app.exec_())
