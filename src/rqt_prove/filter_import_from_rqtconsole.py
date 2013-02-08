#!/usr/bin/env python
import os
import time

from PySide.QtCore import QFile, Qt
from PySide.QtGui import QApplication, QItemSelectionModel, QMainWindow, QStandardItem, QStandardItemModel, QWidget
from PySide.QtUiTools import QUiLoader

from python_qt_binding import loadUi
from python_qt_binding.QtCore import Qt
from python_qt_binding import QtGui
from python_qt_binding.QtGui import QItemSelectionModel, QMainWindow, QStandardItem, QStandardItemModel, QWidget
import rospkg
import rospy

from rqt_console.filters.filter_wrapper_widget import FilterWrapperWidget
from rqt_console.filters.text_filter_widget import TextFilterWidget
from rqt_console.filters.message_filter import MessageFilter
        
class FilterImportProve(QWidget):
    
    def __init__(self):
        super(FilterImportProve, self).__init__()
        
#        rp = rospkg.RosPack()
#        ui_file = os.path.join(rp.get_path('rqt_prove'), 
#                               'resource', 'treeview.ui')
#        loadUi(ui_file, self)

        nf = NodeFilter()
        self.addWidget(FilterWrapperWidget(nf, 'NFilter'))

        self.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    #window = FilterImportProve()
    
    nf = MessageFilter()
    window = TextFilterWidget(nf, (1, 5))
    #window = FilterWrapperWidget(tfw, 'NFilter')
    window.resize(320, 240);
    window.show();
    window.setWindowTitle(
         QtGui.QApplication.translate("toplevel", "Top-level widget"))

    sys.exit(app.exec_())
            