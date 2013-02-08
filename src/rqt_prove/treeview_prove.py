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

from rqt_reconfigure.filter_children_model import FilterChildrenModel
from rqt_reconfigure.treenode_qstditem import TreenodeQstdItem

class TreeviewWidgetProve(QWidget):
    
    def __init__(self):
        super(TreeviewWidgetProve, self).__init__()
                
        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('rqt_prove'), 
                               'resource', 'treeview.ui')
        loadUi(ui_file, self)
        
        self._std_model = QStandardItemModel()
        self._rootitem = self._std_model.invisibleRootItem()
        

        self.item_r_3_1 = QStandardItem("child")
        item_r_3.appendRow(self.item_r_3_1)

        item_r_1 = QStandardItem("row1")
        item_r_2 = QStandardItem("row2")
        item_r_3 = QStandardItem("row3")
        self._rootitem.appendRow(item_r_1)
        self._rootitem.appendRow(item_r_2)
        self._rootitem.appendRow(item_r_3)
        
        self._treeview.setModel(self._std_model)

        self.show()
        
    def add_cols(self):
        time.sleep(1)
        
        item_c_1 = QStandardItem("col1")
        item_c_2 = QStandardItem("col2")
        item_c_3 = QStandardItem("col3")
        item_c_4 = QStandardItem("col4")
        items_col = [item_c_1, item_c_2, item_c_3, item_c_4]
        #self._rootitem.appendColumn(items_col)
        self.item_r_3_1.appendColumn(items_col)
                
        self._treeview.update()
        
class TreeviewWidgetSelectProve(QWidget):
    
    def __init__(self):
        super(TreeviewWidgetSelectProve, self).__init__()
                
#        loader = QUiLoader()
#        file = QFile("treeview.ui")
#        file.open(QFile.ReadOnly)
#        treeview_widget = loader.load(file, self)        
        
        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('rqt_prove'), 
                               'resource', 'treeview.ui')
        loadUi(ui_file, self)
        
        self._std_model = QStandardItemModel()
        self._rootitem = self._std_model.invisibleRootItem()

        #self._proxy_model = FilterChildrenModel(self)
        #self._proxy_model.setDynamicSortFilter(True)
        #self._proxy_model.setSourceModel(self._std_model)
        #self._treeview.setModel(self._proxy_model)
        
        item_r_1 = QStandardItem("r1")
        item_r_2 = QStandardItem("r2")
        item_r_3 = QStandardItem("r3")
        self.item_r_3_1 = QStandardItem("r3-1")
        item_r_3.appendRow(self.item_r_3_1)
        item_r_4 = QStandardItem("r4")
#        item_r_1 = TreenodeQstdItem("/a/rowrowrowrow1")
#        item_r_2 = TreenodeQstdItem("/b/rowrowrowrow2")
#        item_r_3 = TreenodeQstdItem("/c/rowrow3")
#        self.item_r_3_1 = TreenodeQstdItem("/c/rowrow3/child")
#        item_r_3.appendRow(self.item_r_3_1)
#        item_r_4 = TreenodeQstdItem("/d/row4")

        self._rootitem.appendRow(item_r_1)
        self._rootitem.appendRow(item_r_2)
        self._rootitem.appendRow(item_r_3)
        self._rootitem.appendRow(item_r_4)
        print('_rootitem index={}'.format(self._rootitem.index()))
        
        self._treeview.setModel(self._std_model)
        
        self.selectionModel = self._treeview.selectionModel()
        self.selectionModel.selectionChanged.connect(self._selection_changed_slot)

        print('LEN(sel) sel sel.row parent.sel  desel  desel.row sel.dat  parent.sel.dat  desel.dat  sel.item')

        self.show()

    def _selection_changed_slot(self, selected, deselected):
        """
        Receives args from signal QItemSelectionModel.selectionChanged.
        
        :type selected: QItemSelection
        :type deselected: QItemSelection
        """
#        selmodel = self._treeview.selectionModel()
#        index_current = selmodel.currentIndex()
#        curr_qstd_item_2 = self._std_model.itemFromIndex(index_current)
#        print 'src 2 -- row={} count={} data={}'.format(index_current.row(), 
#                                          index_current.column(),
#                                          curr_qstd_item_2.data(Qt.DisplayRole))
#        curr_qstd_item_2_child = curr_qstd_item_2.child(0, 0)
#        print 'child={} valid?={}'.format(curr_qstd_item_2_child, 
#                                curr_qstd_item_2_child.isValid())
        self._test_sel_index(selected, deselected)
#        indexes = selected.indexes()
#        print 'len indexes={}'.format(len(indexes))
#        qmi = indexes[0]
#        if qmi == None:
#            #rospy.logwarn('none')
#            print 'none'
#            return
#        curr_qstd_item = self._std_model.itemFromIndex(qmi)
#        #rospy.logwarn('item {}'.format(curr_qstd_item.data(Qt.DisplayRole)))
#        print 'item {}'.format(curr_qstd_item.data(Qt.DisplayRole))
#        print 'Item type={}'.format(curr_qstd_item)
#        
#        print 'src 1 -- row={} count={} data={}'.format(qmi.row(), qmi.column(),
#                                                qmi.data(Qt.DisplayRole))
                
        #child = qmi.child(0, 0)
        #if not child.isValid():
        #    self.add_cols(qmi)
    def _test_sel_index(self, selected, deselected):
      #---------------- From here debug
        #index_current = self.selectionModel.currentIndex()
        src_model = self._std_model
        index_current = None
        index_deselected = None
        index_parent_sel = None
        index_parent_desel = None
        curr_qstd_item = None
        if len(selected.indexes()) > 0:
            index_current = selected.indexes()[0]
            index_parent_sel = index_current.parent()
            curr_qstd_item = src_model.itemFromIndex(#index_parent)
                                                 index_current)                        
        elif len(deselected.indexes()) > 0:
            index_deselected = deselected.indexes()[0]
            index_parent_desel = index_deselected.parent()        
            curr_qstd_item = src_model.itemFromIndex(index_deselected)                        
        #index_current = selected.indexes()[0]     
        #index_deselected = deselected.indexes()[0]     

        if len(selected.indexes()) > 0:
            print('{}  {}  {}  {}  {}  {}  {}  {}  {}  {}'.format(
                                  len(selected.indexes()), 
                                  index_current,                                  
                                  index_current.row(), 
                                  index_parent_sel, 
                                  index_deselected,
                                  '-',
                                  index_current.data(Qt.DisplayRole),
                                  index_parent_sel.data(Qt.DisplayRole),
                                  None,#index_deselected.data(Qt.DisplayRole),
                                  curr_qstd_item))
        elif len(deselected.indexes()) > 0:
            #print('LEN(dsel)={} sel={}           par.d={} desel={} desel.row={} sel.d={} par.d.d={} desel.d={} cur.item={}'.format(                                                                                                            
            print('{}  {}  {}  {}  {}  {}  {}  {}  {}  {}'.format(
                                  len(deselected.indexes()), index_current,
                                  '-',
                                  index_parent_desel, index_deselected,
                                  index_deselected.row(), None,
                                  index_parent_desel.data(Qt.DisplayRole),
                                  index_deselected.data(Qt.DisplayRole),
                                  curr_qstd_item))
            self.selectionModel.select(index_deselected, QItemSelectionModel.Deselect)
                                                            
        # Tried so hard to obtain Item instance by either of following but never succeeds.
        #item = self._std_model.itemFromIndex(index_current)
        #item = self._std_model.itemFromIndex(curr_qstd_item)
        #self._proxy_model.sourceModel().itemFromIndex(index_current)

        # If rosnode_name_selected is in the nodename_list, this index is node.
        # Otherwise, this index is a parameter.
        #---------------- Til here debug         
                
    def add_cols(self, qmi):
        time.sleep(1)
        
        item_c_1 = QStandardItem("col1")
        item_c_2 = QStandardItem("col2")
        item_c_3 = QStandardItem("col3")
        item_c_4 = QStandardItem("col4")
        items_col = [item_c_1, item_c_2, item_c_3, item_c_4]
        #self._rootitem.appendColumn(items_col)
        self.item_r_3_1.appendColumn(items_col)
                
        self._treeview.update()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window =TreeviewWidgetSelectProve() 
    window.resize(320, 240);
    #window.show();
    window.setWindowTitle(
         QtGui.QApplication.translate("toplevel", "Top-level widget"))
    #window.add_cols()

    sys.exit(app.exec_())
            