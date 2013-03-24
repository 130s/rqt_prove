#!/usr/bin/env python

import os
import sys

setattr(sys, 'SELECT_QT_BINDING',
        'pyside')
        #'pyqt')
from python_qt_binding.QtCore import Qt
from python_qt_binding.QtGui import (QApplication, QItemSelectionModel,
                          QStandardItem, QStandardItemModel, QWidget)
from python_qt_binding import loadUi

from rqt_prove.qview_custom import CustomQTreeview

import rospkg


class TreeviewWidgetSelectProve(QWidget):

    def __init__(self):
        super(TreeviewWidgetSelectProve, self).__init__()

        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('rqt_prove'), 'resource',
                               #'treeview_non_custom.ui')  # Works with pyqt.
                               'treeview_with_custom.ui')  # No good.
        #loadUi(ui_file, self)
        loadUi(ui_file, self, {'CustomQTreeview': CustomQTreeview})

        self._std_model = QStandardItemModel()
        self._rootitem = self._std_model.invisibleRootItem()

        item_r_1 = QStandardItem("r1")

        self._rootitem.appendRow(item_r_1)

        print('_rootitem index={}'.format(self._rootitem.index()))

        self.treeview.setModel(self._std_model)
        self.selectionModel = self.treeview.selectionModel()
        self.selectionModel.selectionChanged.connect(
                                                 self._selection_changed_slot)

        print('del/sel?\tde/sel index\tde/sel.row\tde/sel.dat\tparent\tinternal id')

        self.show()

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
            curr_qstd_item = src_model.itemFromIndex(  # index_parent)
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
                                  #curr_qstd_item,
                                  #curr_qstd_item.data(Qt.DisplayRole),
                              index_parent_sel,
                                  #index_parent_sel.data(Qt.DisplayRole),
                              index_internalid))
        elif len(deselected.indexes()) > 0:
            print(tabular_format.format(
                              del_or_sel,
                              index_deselected,
                              index_deselected.row(),
                              index_deselected.data(Qt.DisplayRole).toString(),
                              #curr_qstd_item,
                              #    curr_qstd_item.data(),
                                  index_parent_desel,
                              #  index_parent_desel.data(Qt.DisplayRole),
                                  index_internalid))
            self.selectionModel.select(index_deselected,
                                       QItemSelectionModel.Deselect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #window = TreeviewWidgetSelectProve()
    #window = PrvTreeviewNest()
    window = TreeviewWidgetSelectProve()
    window.resize(320, 240)
    # window.show();
    window.setWindowTitle(
         QApplication.translate("toplevel", "Top-level widget"))
    # window.add_cols()

    sys.exit(app.exec_())
