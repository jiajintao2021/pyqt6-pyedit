import sys

from PyQt6.QtGui import QAction, QColor, QPalette
from PyQt6.QtWidgets import QApplication, QBoxLayout, QMenu, QMenuBar, QWidget

PyEApp = QApplication(sys.argv)

pye_window = QWidget()
pye_window_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
pye_window_layout.setContentsMargins(0, 0, 0, 0)

pye_window.setMinimumWidth(800)
pye_window.setMinimumHeight(300)

from pye.menu.menubar import pye_menubar
pye_window_layout.setMenuBar(pye_menubar)

from pye.edit import edit_content_layout
pye_window_layout.addLayout(edit_content_layout)

pye_window.setLayout(pye_window_layout)
pye_window.show()
