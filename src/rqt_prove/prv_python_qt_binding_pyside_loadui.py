#!/usr/bin/env python
import os
import sys

from PySide.QtGui import (QApplication,
                          QStandardItemModel, QWidget)
setattr(sys, 'SELECT_QT_BINDING',
        #'pyside')
        'pyqt')
from python_qt_binding import loadUi
from python_qt_binding.binding_helper import QT_BINDING

from rqt_prove.qview_custom import CustomQTableview, CustomQTreeview


class LoaduiProve(QWidget):

    def __init__(self):
        super(LoaduiProve, self).__init__()
        print ('QT_BINDING=' + QT_BINDING)
        ui_file_path = os.path.join(
            '/home/n130s/link/ROS/groovy_quantal/catkin_ws/src/rqt_prove',
            'resource', 'treeview_3.ui')

        #uiw = loadUi(ui_file_path)
        uiw = loadUi(ui_file_path,
               #{'LoaduiProve': LoaduiProve,
               {'CustomQTableview': CustomQTableview,
               'CustomQTreeview': CustomQTreeview})

        self._std_model = QStandardItemModel()
        self._rootitem = self._std_model.invisibleRootItem()

        uiw._treeview.setModel(self._std_model)
        self.selectionModel = self._treeview.selectionModel()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoaduiProve()
    window.resize(320, 240)
    window.setWindowTitle(
         QApplication.translate("toplevel", "Top-level widget"))
    sys.exit(app.exec_())
