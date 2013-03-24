#!/usr/bin/env python

############################################################################
##
## Copyright (C) 2005-2005 Trolltech AS. All rights reserved.
##
## This file is part of the example classes of the Qt Toolkit.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http://www.trolltech.com/products/qt/opensource.html
##
## If you are unsure which license is appropriate for your use, please
## review the following information:
## http://www.trolltech.com/products/qt/licensing.html or contact the
## sales department at sales@trolltech.com.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
############################################################################


from PySide import QtCore, QtGui
from PySide.QtGui import QHBoxLayout, QPushButton, QStandardItem


class TreeviewDelegate(QtGui.QItemDelegate):
    def createEditor(self, parent, option, index):
        return self._create_editor_composite_widget(parent)

    def _create_editor_composite_widget(self, parent):
        #editor = QtGui.QWidget(parent)  #currently parent is qstitem
        editor = QtGui.QWidget()

        hlayout = QHBoxLayout()
        button_1 = QPushButton('bt1')
        button_2 = QPushButton('bt2')
        hlayout.addWidget(button_1)
        hlayout.addWidget(button_2)
        editor.setLayout(hlayout)

        button_1.pressed.connect(self._button_slot)

        return editor

    def _button_slot(self):
        print ('button pressed')

    def _create_editor_spinbox(self, parent):
        editor = QtGui.QSpinBox(parent)
        editor.setMinimum(0)
        editor.setMaximum(100)

        return editor

    def setEditorData(self, spinBox, index):
        value = index.model().data(index, QtCore.Qt.EditRole)

        spinBox.setValue(value)

    def setModelData(self, spinBox, model, index):
        spinBox.interpretText()
        value = spinBox.value()

        model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    row_max = 5
    col_max = 1

    model = QtGui.QStandardItemModel(row_max, 2)
    rootitem = model.invisibleRootItem()

    _view = QtGui.QTreeView()
    _view.setModel(model)

    delegate = TreeviewDelegate()
    _view.setItemDelegate(delegate)

    for row in range(row_max):
        for column in range(col_max):
            index = model.index(row, column, QtCore.QModelIndex())
            #model.setData(index, (row_max + 1) * (column + 1))

            std_item = QStandardItem('r' + str(row))
            #model.setItem(row, column, std_item)

            if row % 2 == 0:
                #std_item_child = QStandardItem('child')
                #std_item.appendRow(std_item_child)
                widget = delegate._create_editor_composite_widget(std_item)
                _view.setIndexWidget(index, widget)

    _view.setWindowTitle("View Delegate")
    _view.show()
    sys.exit(app.exec_())
