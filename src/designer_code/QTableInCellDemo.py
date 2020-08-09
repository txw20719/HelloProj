# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTableInCellDemo.py
"""QTableWidget（向扩展二维表中的Cell添加控件）

1. 在单元格中放置控件
2. 设置单元格字体颜色和背景颜色
3. 查找内容匹配对应单元格并行定位
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class TableViewDemo(QWidget):
    def __init__(self):
        super(TableViewDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('表格中Cell的操作')
        self.resize(500, 300)
        layout = QVBoxLayout()

        table = QTableWidget()
        table.setRowCount(20)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(['姓名', '年龄', '地址'])

        item1 = QTableWidgetItem('小明')
        # 设置字体、字体颜色和背景色
        item1.setFont(QFont('Arial', 24, QFont.Black))
        item1.setBackground(QBrush(QColor(0, 255, 0)))
        item1.setForeground(QBrush(QColor(255, 0, 0)))

        comboBox = QComboBox()
        comboBox.addItems(['男', '女'])
        # QSS
        comboBox.setStyleSheet('QComboBox{margin:3px}')
        button = QPushButton('修改')
        button.setStyleSheet('QPushButton{margin:3px}')

        table.setItem(0, 0, item1)
        table.setCellWidget(0, 1, comboBox)
        table.setCellWidget(0, 2, button)

        for i in range(1, 20):
            for j in range(3):
                content = '(%d, %d)' % (i, j)
                item = QTableWidgetItem(content)
                table.setItem(i, j, item)

        # 搜索满足条件的Cell
        matchtext = '(15, 2)'
        items = table.findItems(matchtext, Qt.MatchExactly)
        # 定位到指定的行
        row = items[0].row()
        table.verticalScrollBar().setSliderPosition(row)

        layout.addWidget(table)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableViewDemo()
    main.show()
    sys.exit(app.exec_())