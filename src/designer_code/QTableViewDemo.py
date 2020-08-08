# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QSpinBoxDemo.py
"""QTableView（显示二维表数据）

需要创建QTableView实例和一个数据源（Model），将其关联
MVC：Model   Viewer  Controller
降低后端数据与前端页面的耦合度
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class TableViewDemo(QWidget):
    def __init__(self):
        super(TableViewDemo, self).__init__()
        self.setWindowTitle('表格视图控件演示')
        self.resize(500, 300)

        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])

        self.tableview = QTableView()
        # 关联QTableView控件和Model关联
        self.tableview.setModel(self.model)

        # 添加数据
        item1 = QStandardItem('31520')
        item2 = QStandardItem('雷神')
        item3 = QStandardItem('男')
        self.model.setItem(0, 0, item1)
        self.model.setItem(0, 1, item2)
        self.model.setItem(0, 2, item3)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableViewDemo()
    main.show()
    sys.exit(app.exec_())
