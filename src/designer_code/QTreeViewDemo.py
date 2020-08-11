# encoding=utf-8
# 代码文件：HelloProj/src/designer_code/QTreeWidgetOperateNodeDemo.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)
    tree.setWindowTitle('QTreeViewDemo')
    tree.show()

    sys.exit(app.exec_())
