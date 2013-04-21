#!/usr/bin/env python
import os

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.uic import loadUi


class PrvQslider(QMainWindow):

    def __init__(self):
        super(PrvQslider, self).__init__()
        self.uiw = loadUi("resource/prv_qslider.ui")

        self.uiw.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # window = TreeviewWidgetSelectProve()
    window = PrvQslider()
    # window = TreeviewWidgetSelectProve()
    window.resize(320, 240)
    # window.show();
    window.setWindowTitle(
         QApplication.translate("toplevel", "Top-level widget"))

    sys.exit(app.exec_())
