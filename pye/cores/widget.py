from PyQt6 import QtGui
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import pyqtSignal, Qt


class NewLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        print(True)
