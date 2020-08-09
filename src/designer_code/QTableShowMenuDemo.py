# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTableShowManuDemo.py
"""QTableWidget（在表格中显示上下文菜单）

1. 如何弹出菜单
2. 如何满足条件的情况下弹出菜单
<<<<<<< HEAD
QMenu.exc_()
=======
QMenu实例中的exec(pos)
>>>>>>> 5e4dde4... tableShowManu
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QTableShowManuDemo(QWidget):
    def __init__(self):
        super(QTableShowManuDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在表格中显示上下文菜单')
        self.resize(500, 300)
        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['姓名', '年龄', '体重'])

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

        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.GenerateMenu)

        layout.addWidget(self.table)
        self.setLayout(layout)

    def GenerateMenu(self, pos):
        print(pos)

        for i in self.table.selectionModel().selection().indexes():
            rowNum = i.row()
            column = i.column()
            # print(rowNum)
            if rowNum < 2:
                menu = QMenu()
                item1 = menu.addAction('菜单项1')
                item2 = menu.addAction('菜单项2')
                item3 = menu.addAction('菜单项3')
                screenpos = self.table.mapToGlobal(pos)
                # 被阻塞
                action = menu.exec(screenpos)
                if action == item1:
                    print('菜单项1', self.table.item(rowNum, column).text())
                elif action == item2:
                    print('菜单项2', self.table.item(rowNum, column).text())
                elif action == item3:
                    print('菜单项3', self.table.item(rowNum, column).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTableShowManuDemo()
    main.show()
    sys.exit(app.exec_())