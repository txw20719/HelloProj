# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTreeWidgetClickDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QTreeWidgetClickDemo(QWidget):
    def __init__(self):
        super(QTreeWidgetClickDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('树控件')
        self.resize(300, 280)
        layout = QVBoxLayout()

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])
        self.tree.setColumnWidth(0, 180)


        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        root.setText(1, '根节点的数据')
        root.setIcon(0, QIcon('./icon/file2.png'))

        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0, QIcon('./icon/file1.png'))

        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setIcon(0, QIcon('./icon/file1.png'))
        child2.setCheckState(0, Qt.Checked)

        child2_child = QTreeWidgetItem(child2)
        child2_child.setText(0, '子节点2的子节点')
        child2_child.setIcon(0, QIcon('./icon/file1.png'))

        # 所有结点展开
        self.tree.expandAll()
        # 为节点添加点击事件
        self.tree.clicked.connect(self.ClickNode)

        layout.addWidget(self.tree)
        self.setLayout(layout)

    def ClickNode(self, index):
        item = self.tree.currentItem()
        rowNum = index.row()
        print("Key=%s,Value=%s" % (item.text(0),item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTreeWidgetClickDemo()
    main.show()
    sys.exit(app.exec_())
