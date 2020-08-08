# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTableWidgetDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QTableWidgetDemo(QWidget):
    def __init__(self):
        super(QTableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('表格视图控件演示')
        self.resize(500, 300)
        layout = QVBoxLayout()

        tableWidget = QTableWidget()
        # 设置tableWidget
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        tableWidget.setHorizontalHeaderLabels(['姓名', '年龄', '地址'])

        # 禁止编辑
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选择
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 调整行和列
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()
        # 隐藏水平头
        tableWidget.horizontalHeader().setVisible(False)
        # 设置垂直头
        tableWidget.setVerticalHeaderLabels(['a', 'b'])
        # 隐藏表格线
        tableWidget.setShowGrid(False)
        # 添加数据
        item1 = QTableWidgetItem('张三')
        tableWidget.setItem(0, 0, item1)

        item2 = QTableWidgetItem('15')
        tableWidget.setItem(0, 1, item2)

        item3 = QTableWidgetItem('安徽')
        tableWidget.setItem(0, 2, item3)

        layout.addWidget(tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTableWidgetDemo()
    main.show()
    sys.exit(app.exec_())


