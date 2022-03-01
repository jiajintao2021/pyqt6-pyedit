import sys

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication, QWidget

from pye.base import PyEMain

PyEApp = QApplication(sys.argv)


class MasterWindow(PyEMain):
    pass


master_window = MasterWindow()
master_window.show()
