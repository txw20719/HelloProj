# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QCalendarDemo.py

import sys
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QCalendarWidget
from PyQt5.QtCore import QDate


class QCalendarWidgetDemo(QWidget):
    def __init__(self):
        super(QCalendarWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('日历控件测试')
        self.resize(300, 600)
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1997, 6, 20))
        self.cal.setMaximumDate(QDate(2020, 6, 20))
        self.cal.setGridVisible(True)  # 设置网格
        self.cal.move(20, 20)

        self.cal.clicked.connect(self.SelectDate)

        self.label = QLabel(self)
        self.label.setText(self.cal.selectedDate().toString('yyyy/MM/dd dddd'))
        self.label.move(20, 300)

    def SelectDate(self):
        self.label.setText(self.cal.selectedDate().toString('yyyy/MM/dd dddd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCalendarWidgetDemo()
    main.show()
    sys.exit(app.exec_())