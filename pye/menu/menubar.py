from PyQt6.QtWidgets import QBoxLayout, QMenuBar, QSizePolicy

from pye.main import pye_window

pye_menubar_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
pye_menubar_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
pye_menubar_policy.setHorizontalStretch(1)

pye_menubar = QMenuBar(pye_window)
pye_menubar.setSizePolicy(pye_menubar_policy)
pye_menubar.setLayout(pye_menubar_layout)
from pye.menu.file_menu import file_menu
pye_menubar.addMenu(file_menu)
