#!/usr/bin/env python
import os

from PySide.QtCore import QFile
from PySide.QtGui import (QApplication, QMainWindow, QStandardItem,
                          QStandardItemModel,
                          QTreeView)
from PySide.QtUiTools import QUiLoader


class TreeviewWidgetSelectProve(QMainWindow):

    def __init__(self):
        super(TreeviewWidgetSelectProve, self).__init__()
        ui_file_path = os.path.join(
            '/home/n130s/link/ROS/groovy_quantal/catkin_ws/src/rqt_prove',
            'resource', 'treeview_2.ui')

        loader = QUiLoader(self)
        ui_file = QFile(ui_file_path)
        self._widget_top = loader.load(ui_file, self)

        self._std_model = QStandardItemModel()
        self._rootitem = self._std_model.invisibleRootItem()

        item_r_1 = QStandardItem("r1")

        self._rootitem.appendRow(item_r_1)
        # self._rootitem.appendRow(item_r_2)
        print('_rootitem index={}'.format(self._rootitem.index()))

        self._treeview = self._widget_top.findChild(QTreeView, '_treeview')
        self._treeview.setModel(self._std_model)
        self.selectionModel = self._widget_top._treeview.selectionModel()

        print('del/sel?\tde/sel index\tde/sel.row\tde/sel.dat\tparent\tinternal id')
        self._widget_top.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = TreeviewWidgetSelectProve()
    window.resize(320, 240)
    window.setWindowTitle(
         QApplication.translate("toplevel", "Top-level widget"))
    sys.exit(app.exec_())
