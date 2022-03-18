from PyQt6.QtWidgets import QToolBar
from PyQt6.QtCore import Qt

from pye.cores.static import load_qss

left_menubar = QToolBar()
left_menubar.setOrientation(Qt.Orientation.Vertical)

left_menubar.setStyleSheet(
    load_qss('menubar_left.qss')
)
