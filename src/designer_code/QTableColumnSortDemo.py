# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTableColumnSortDemo.py
"""QTableWidget（对扩展二维表操作）

1. 点击button后按体重这一列排序，排序类型升序或降序
2. 单元格文本对齐方式
3. 合并行和列
4. 改变列或行的尺寸
5. 将图片和文本混合放入单元格中
6. 在单元格中设置图片的尺寸
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

        # 改变列或行的尺寸
        self.table.setRowHeight(0, 100)
        self.table.setColumnWidth(1, 80)

        nameitem1 = QTableWidgetItem('张三')
        ageitem1 = QTableWidgetItem('15')
        weightitem1 = QTableWidgetItem('150')
        # 设置单元格文本对齐方式
        nameitem1.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        ageitem1.setTextAlignment(Qt.AlignLeft)
        weightitem1.setTextAlignment(Qt.AlignCenter)
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
        nameitem3.setTextAlignment(Qt.AlignCenter)
        ageitem3 = QTableWidgetItem('21')
        weightitem3 = QTableWidgetItem('145')
        self.table.setItem(2, 0, nameitem3)
        self.table.setItem(2, 1, ageitem3)
        self.table.setItem(2, 2, weightitem3)

        # 将图片和文本混合放入单元格中
        # 在单元格中设置图片的尺寸
        self.table.setRowHeight(3, 80)
        self.table.setIconSize(QSize(80, 80))
        item = QTableWidgetItem(QIcon('./icon/adobereader.ico'), '占两列')
        item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(3, 1, item)

        # 单元格合并两行
        self.table.setSpan(2, 0, 2, 1)
        self.table.setSpan(3, 1, 1, 2)

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