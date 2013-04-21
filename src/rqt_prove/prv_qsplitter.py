#!/usr/bin/env python
import os

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QWidget
from PyQt4.uic import loadUi


class SampleWidget(QWidget):
    def __init__(self, parent=None):
        super(SampleWidget, self).__init__()
        self._parent = parent
        print 'SampleWidget parent={}'.format(parent)


class PrvQSplitter(QWidget):
    def __init__(self):
        super(PrvQSplitter, self).__init__()
        self.uiw = loadUi("resource/prv_qsplitter.ui")

        self.uiw._splitter.addWidget(self.uiw._widget_custom)

        self.uiw.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = PrvQSplitter()
    window.resize(320, 240)
    window.setWindowTitle(
         QApplication.translate("toplevel", "Top-level widget"))

    sys.exit(app.exec_())
