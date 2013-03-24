#!/usr/bin/env python
import os

from PyQt4.QtCore import QModelIndex, QPersistentModelIndex, Qt
from PyQt4.QtGui import QApplication, QItemSelectionModel, \
                        QMainWindow, QPushButton, QStandardItem, \
                        QStandardItemModel, QTreeView
from PyQt4.uic import loadUi

# from python_qt_binding import loadUi
# from python_qt_binding.QtCore import QModelIndex, Qt
# from python_qt_binding import QtGui
# from python_qt_binding.QtGui import (QItemSelectionModel, QMainWindow,
#                                     QStandardItem, QStandardItemModel,
#                                     QTreeView, QWidget)
import rospkg
# import rospy

# from rqt_reconfigure.filter_children_model import FilterChildrenModel
# from rqt_reconfigure.treenode_qstditem import TreenodeQstdItem


class TreeviewWidgetSelectProve(QMainWindow):

    def __init__(self):
        super(TreeviewWidgetSelectProve, self).__init__()
        # self.uiw = loadUi("~/link/ROS/groovy_quantal/catkin_ws/src/rqt_prove/resource/treeview.ui")
        # self.uiw = loadUi("/resource/treeview.ui")
        self.uiw = loadUi("/home/n130s/link/ROS/groovy_quantal/catkin_ws/src/rqt_prove/resource/treeview.ui")

#        self._treeview = QTreeView(self)
#        self._treeview.SelectionMode = QAbstractItemView.ContiguousSelection

#        rp = rospkg.RosPack()
#        ui_file = os.path.join(rp.get_path('rqt_prove'),
#                               'resource', 'treeview.ui')
#        loadUi(ui_file, self)

        self._std_model = QStandardItemModel()
        self._rootitem = self._std_model.invisibleRootItem()

        item_r_1 = QStandardItem("r1")
        # item_r_2 = QStandardItem("r2")
        # item_r_3 = QStandardItem("r3")
        # self.item_r_3_1 = QStandardItem("r3-1")
        # self.item_r_3_1_1 = QStandardItem("child_c")
        # item_r_3.appendRow(self.item_r_3_1)
        # self.item_r_3_1.appendRow(self.item_r_3_1_1)
        # item_r_4 = QStandardItem("r4")
        # item_r_5 = QStandardItem("r5")
#        item_r_1 = TreenodeQstdItem("/a/rowrowrowrow1")
#        item_r_2 = TreenodeQstdItem("/b/rowrowrowrow2")
#        item_r_3 = TreenodeQstdItem("/c/rowrow3")
#        self.item_r_3_1 = TreenodeQstdItem("/c/rowrow3/child")
#        item_r_3.appendRow(self.item_r_3_1)
#        item_r_4 = TreenodeQstdItem("/d/row4")

        self._rootitem.appendRow(item_r_1)
        # self._rootitem.appendRow(item_r_2)
#        self._rootitem.appendRow(item_r_3)
#        self._rootitem.appendRow(item_r_4)
#        self._rootitem.appendRow(item_r_5)
        print('_rootitem index={}'.format(self._rootitem.index()))

        self.uiw._treeview.setModel(self._std_model)
        self.selectionModel = self.uiw._treeview.selectionModel()
        self.selectionModel.selectionChanged.connect(
                                                 self._selection_changed_slot)

        # print('del/sel?\tde/sel index\tde/sel.row\tde/sel.dat\tsel.item\tsel.item.name\tparent.de/sel\tparent.sel.dat\tinternal id')
        print('del/sel?\tde/sel index\tde/sel.row\tde/sel.dat\tparent\tinternal id')

        self.uiw.show()

    def _selection_changed_slot(self, selected, deselected):
        """
        Receives args from signal QItemSelectionModel.selectionChanged.

        :type selected: QItemSelection
        :type deselected: QItemSelection
        """
        self._test_sel_index(selected, deselected)

    def _test_sel_index(self, selected, deselected):
        src_model = self._std_model
        index_current = None
        index_deselected = None
        index_parent_sel = None
        index_parent_desel = None
        curr_qstd_item = None
        indexes = selected.indexes()
        del_or_sel = 'Sel'
        index_internalid = -1

        if len(indexes) > 0:
            index_internalid = selected.indexes()[0].internalId()

            # # Trying many approaches to get the right qindex
            # # Approach-1
            index_current = selected.indexes()[0]

            # # Approach-2

            # index_current_from_indexes = selected.indexes()[0]
            # index_current = src_model.index(index_current_from_indexes.row(),
                                            # 0, QModelIndex())
                                            # 0, index_current_from_indexes)
            # index_current = self.selectionModel.currentIndex()

            index_parent_sel = index_current.parent()
            curr_qstd_item = src_model.itemFromIndex(# index_parent)
                                                 index_current)
        elif len(deselected.indexes()) > 0:
            index_internalid = deselected.indexes()[0].internalId()

            del_or_sel = 'Desel'
            index_deselected = self.selectionModel.currentIndex()
            index_parent_desel = index_deselected.parent()
            curr_qstd_item = src_model.itemFromIndex(index_deselected)

        tabular_format = '{}\t{}\t{}\t{}\t{}\t{}'
        if len(indexes) > 0:
            print(tabular_format.format(
                              del_or_sel,
                              index_current,
                              index_current.row(),
                              index_current.data(Qt.DisplayRole).toString(),
                                  # curr_qstd_item,
                                  # curr_qstd_item.data(Qt.DisplayRole),
                              index_parent_sel,
                                  # index_parent_sel.data(Qt.DisplayRole),
                              index_internalid))
        elif len(deselected.indexes()) > 0:
            print(tabular_format.format(
                              del_or_sel,
                              index_deselected,
                              index_deselected.row(),
                              index_deselected.data(Qt.DisplayRole).toString(),
                              # curr_qstd_item,
                              #    curr_qstd_item.data(),
                                  index_parent_desel,
                              #  index_parent_desel.data(Qt.DisplayRole),
                                  index_internalid))
            self.selectionModel.select(index_deselected,
                                       QItemSelectionModel.Deselect)


class PersistendIndexProve(QMainWindow):

    def __init__(self):
        super(PersistendIndexProve, self).__init__()
        self.uiw = loadUi("/u/isaito/data/Dropbox/ROS/groovy_quantal/catkin_ws/src/rqt_prove/resource/treeview.ui")

        self._std_model = QStandardItemModel()
        self._rootitem = self._std_model.invisibleRootItem()

        item_r_1 = QStandardItem("r1")
        item_r_2 = QStandardItem("r2")
        print 'index before {}'.format(item_r_1.index())

        qindex_persistent = QPersistentModelIndex(item_r_1.index())

        self._std_model.beginInsertRows(self._rootitem.index(), 0, 0)
        self._rootitem.appendRow(item_r_1)
        self._rootitem.appendRow(item_r_2)
        self._std_model.endInsertRows()
        print 'index after {}'.format(item_r_1.index())
        print 'index after 2 {}'.format(self._std_model.index(0, 0,
                                                              QModelIndex()))

        print '_rootitem index={} persistent list={}'.format(
                                         self._rootitem.index(),
                                         self._std_model.persistentIndexList())

        self.uiw._treeview.setModel(self._std_model)
        self.selectionModel = self.uiw._treeview.selectionModel()
        self.selectionModel.selectionChanged.connect(
                                                 self._selection_changed_slot)
        self.selectionModel.currentChanged.connect(
                                                 self._current_changed_slot)

        print('del/sel?\tde/sel index\tde/sel.row\tde/sel.dat\tparent\tinternal id')

        self.uiw.show()

    def _current_changed_slot(self, current, previous):
        print 'changed slot current={} prev={}'.format(
                                      current.data(Qt.DisplayRole).toString(),
                                      previous.data(Qt.DisplayRole).toString())

    def _selection_changed_slot(self, selected, deselected):
        """
        Receives args from signal QItemSelectionModel.selectionChanged.

        :type selected: QItemSelection
        :type deselected: QItemSelection
        """
        # self._test_sel_index(selected, deselected)
        self._sel_index_2(selected, deselected)

    def _sel_index_2(self, selected, deselected):
        # index_list = self.selectionModel.selectedIndexes()
        for index in self.selectionModel.selectedIndexes():
            print 'indices selected={} len selected={} deseled={}'.format(
                                               str(index.data(Qt.DisplayRole)),
                                               len(selected), len(deselected))

    def _test_sel_index(self, selected, deselected):
        src_model = self._std_model
        index_current = None
        index_deselected = None
        index_parent_sel = None
        index_parent_desel = None
        curr_qstd_item = None
        indexes = selected.indexes()
        del_or_sel = 'Sel'
        index_internalid = -1

        if len(indexes) > 0:
            index_internalid = selected.indexes()[0].internalId()

            # # Trying many approaches to get the right qindex
            # # Approach-1
            index_current = selected.indexes()[0]

            # # Approach-2

            # index_current_from_indexes = selected.indexes()[0]
            # index_current = src_model.index(index_current_from_indexes.row(),
                                            # 0, QModelIndex())
                                            # 0, index_current_from_indexes)
            # index_current = self.selectionModel.currentIndex()

            index_parent_sel = index_current.parent()
            curr_qstd_item = src_model.itemFromIndex(# index_parent)
                                                 index_current)
        elif len(deselected.indexes()) > 0:
            index_internalid = deselected.indexes()[0].internalId()

            del_or_sel = 'Desel'
            index_deselected = self.selectionModel.currentIndex()
            index_parent_desel = index_deselected.parent()
            curr_qstd_item = src_model.itemFromIndex(index_deselected)

        tabular_format = '{}\t{}\t{}\t{}\t{}\t{}'
        if len(indexes) > 0:
            print(tabular_format.format(
                              del_or_sel,
                              index_current,
                              index_current.row(),
                              index_current.data(Qt.DisplayRole).toString(),
                                  # curr_qstd_item,
                                  # curr_qstd_item.data(Qt.DisplayRole),
                              index_parent_sel,
                                  # index_parent_sel.data(Qt.DisplayRole),
                              index_internalid))
        elif len(deselected.indexes()) > 0:
            print(tabular_format.format(
                              del_or_sel,
                              index_deselected,
                              index_deselected.row(),
                              index_deselected.data(Qt.DisplayRole).toString(),
                              # curr_qstd_item,
                              #    curr_qstd_item.data(),
                                  index_parent_desel,
                              #  index_parent_desel.data(Qt.DisplayRole),
                                  index_internalid))
            self.selectionModel.select(index_deselected,
                                       QItemSelectionModel.Deselect)


class StditemWidget(QTreeView):
    def __init__(self):
        super(PrvTreeviewNest, self).__init__()


class PrvTreeviewNest(QTreeView):
    def __init__(self):
        super(PrvTreeviewNest, self).__init__()

        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('rqt_prove'),
                              'resource', 'treeview_nest.ui')
        loadUi(ui_file, self)
        #loadUi('/home/n130s/data/Dropbox/ROS/groovy_quantal/catkin_ws/src/' + \
            #'rqt_prove/resource/treeview_nest.ui')

        # row can be 0 even when it's more than 0.
        self._datamodel = QStandardItemModel(0, 2)

        self.setModel(self._datamodel)

        for i in range(4):
            self._add_widget(i + 1)

        self.show()

    def _add_widget(self, n):
        item_toplevel = QStandardItem('{}th item'.format(n))
        self._datamodel.setItem(n, 0, item_toplevel)

        widget_toplevel = QPushButton('{}th button'.format(n))
        qindex_toplevel = self._datamodel.index(n, 1, QModelIndex())
        self.setIndexWidget(qindex_toplevel, widget_toplevel)

        if n == 2:
            item_child_col0 = QStandardItem('child col0')
            item_child_col1 = QStandardItem('child col1')
            #item_toplevel.appendRow(item_child_col0)

            item_child_col2 = QStandardItem('child col2')
            item_toplevel.insertRow(0, [item_child_col0, item_child_col1])
            #item_child_col0.insertColumn(0, [item_child_col1, item_child_col2])
            #item_child_col0.appendColumn([item_child_col1])  # appends another child

            widget_child = QPushButton('child widget')
            #qindex_child = self._datamodel.index(n, 1, QModelIndex())
            qindex_child = item_child_col1.index()
            #qindex_child = item_toplevel.index(0, 1, QModelIndex())
            self.setIndexWidget(qindex_child, widget_child)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # window = TreeviewWidgetSelectProve()
    window = PrvTreeviewNest()
    # window = TreeviewWidgetSelectProve()
    window.resize(320, 240)
    # window.show();
    window.setWindowTitle(
         QApplication.translate("toplevel", "Top-level widget"))

    sys.exit(app.exec_())
