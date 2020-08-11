# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTreeWidgetOperateNodeDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QTreeWidgetOperateNodeDemo(QWidget):
    def __init__(self):
        super(QTreeWidgetOperateNodeDemo, self).__init__()
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

        h_layout = QHBoxLayout()

        btn_add = QPushButton('添加节点')
        btn_add.clicked.connect(self.AddNode)
        h_layout.addWidget(btn_add)

        btn_modify = QPushButton('修改节点')
        btn_modify.clicked.connect(self.ModifyNode)
        h_layout.addWidget(btn_modify)

        btn_delete = QPushButton('删除结点')
        btn_delete.clicked.connect(self.DeleteNode)
        h_layout.addWidget(btn_delete)

        layout.addLayout(h_layout)

        layout.addWidget(self.tree)
        self.setLayout(layout)

    def DeleteNode(self):
        item = self.tree.currentItem()
        for i in self.tree.selectedItems():
            i.parent().removeChild(item)
        pass

    def ModifyNode(self):
        item = self.tree.currentItem()
        item.setText(0, '修改节点')
        item.setIcon(0, QIcon('./icon/file1.png'))

    def AddNode(self):
        item = self.tree.currentItem()
        new_node = QTreeWidgetItem(item)
        new_node.setText(0, '新节点')
        new_node.setIcon(0, QIcon('./icon/file1.png'))

    def ClickNode(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print("Key=%s,Value=%s" % (item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTreeWidgetOperateNodeDemo()
    main.show()
    sys.exit(app.exec_())
