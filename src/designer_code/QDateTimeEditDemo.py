# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QDateTimeEditDemo.py

import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QDateTimeEdit, QVBoxLayout
from PyQt5.QtCore import QDateTime, QDate, QTime


class QDateTimeEditDemo(QWidget):
    def __init__(self):
        super(QDateTimeEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('不同风格的日期格式')
        layout = QVBoxLayout()
        datetime1 = QDateTimeEdit(QDateTime.currentDateTime())
        datetime2 = QDateTimeEdit(QDateTime.currentDateTime())
        date = QDateTimeEdit(QDate.currentDate())
        time = QDateTimeEdit(QTime.currentTime())
        # 设置最大最小日期时间、下拉日期
        datetime1.setMaximumDate(QDate.currentDate().addDays(365))
        datetime1.setMinimumDate(QDate.currentDate().addDays(-365))
        datetime1.setCalendarPopup(True)

        datetime1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        datetime2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')
        date.setDisplayFormat('yyyy-MM-dd')
        time.setDisplayFormat('HH:mm:ss')

        # 为信号设置槽
        self.datetime1 = datetime1
        datetime1.dateTimeChanged.connect(self.ChangeDateTime)
        datetime2.dateChanged.connect(self.ChangeDate)

        self.btn = QPushButton('点击获取时间')
        self.btn.clicked.connect(self.Onclick_Button)
        layout.addWidget(datetime1)
        layout.addWidget(datetime2)
        layout.addWidget(date)
        layout.addWidget(time)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def ChangeDate(self, date):
        print(date)

    def ChangeDateTime(self, datetime):
        print(datetime)

    def Onclick_Button(self):
        print(self.datetime1.dateTime())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDateTimeEditDemo()
    main.show()
    sys.exit(app.exec_())
