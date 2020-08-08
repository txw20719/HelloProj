# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QListViewDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class QListViewDemo(QWidget):
    def __init__(self):
        super(QListViewDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('显示列表数据')
        self.resize(300, 280)

        listView = QListView()
        model = QStringListModel()
        self.list = ['列表项1', '列表项2', '列表项3']
        model.setStringList(self.list)

        # 向View中添加Model
        listView.setModel(model)
        # 为信号绑定槽
        listView.clicked.connect(self.ClickList)

        layout = QVBoxLayout()
        layout.addWidget(listView)
        self.setLayout(layout)

    def ClickList(self, item):
        QMessageBox.information(self, 'QListView', '您选择了：' + self.list[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QListViewDemo()
    main.show()
    sys.exit(app.exec_())
