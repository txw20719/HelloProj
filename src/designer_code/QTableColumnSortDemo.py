# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTableInCellDemo.py
"""QTableWidget（对扩展二维表按列排序）

1. 点击button后按体重这一列排序
2. 排序类型升序或降序
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QTableColumnSortDemo(QWidget):
    def __init__(self):
        super(QTableColumnSortDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('表格中Cell的操作')
        self.resize(500, 300)
        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['姓名', '年龄', '体重'])
        self.table.horizontalHeader().sectionClicked.connect(self.ClickSortByHeader)

        nameitem1 = QTableWidgetItem('张三')
        ageitem1 = QTableWidgetItem('15')
        weightitem1 = QTableWidgetItem('150')
        self.table.setItem(0, 0, nameitem1)
        self.table.setItem(0, 1, ageitem1)
        self.table.setItem(0, 2, weightitem1)

        nameitem2 = QTableWidgetItem('李四')
        ageitem2 = QTableWidgetItem('20')
        weightitem2 = QTableWidgetItem('120')
        self.table.setItem(1, 0, nameitem2)
        self.table.setItem(1, 1, ageitem2)
        self.table.setItem(1, 2, weightitem2)

        nameitem3 = QTableWidgetItem('王五')
        ageitem3 = QTableWidgetItem('21')
        weightitem3 = QTableWidgetItem('145')
        self.table.setItem(2, 0, nameitem3)
        self.table.setItem(2, 1, ageitem3)
        self.table.setItem(2, 2, weightitem3)

        button = QPushButton('排序')
        button.clicked.connect(self.ClickSort)
        self.typesort = Qt.AscendingOrder

        layout.addWidget(self.table)
        layout.addWidget(button)
        self.setLayout(layout)

    def ClickSortByHeader(self, index):
        self.typesort = Qt.DescendingOrder if self.typesort == Qt.AscendingOrder else Qt.AscendingOrder
        self.table.sortItems(index, self.typesort)

    def ClickSort(self):
        self.typesort = Qt.DescendingOrder if self.typesort == Qt.AscendingOrder else Qt.AscendingOrder
        self.table.sortItems(2, self.typesort)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTableColumnSortDemo()
    main.show()
    sys.exit(app.exec_())