from PyQt6.QtWidgets import QBoxLayout, QLayout, QMenuBar, QSizePolicy, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from edit.app.app import MAIN_WINDOW
from edit.app.utils import to_css
from edit.app.windows.layouts import MainLayout

__all__ = [
    'MasterMenuBar',
]

qb = QSizePolicy()

MasterMenuBar = QMenuBar()

# qb.addWidget(MasterMenuBar)
# qb.addStretch(1)
# MasterMenuBar.setLayout(qb)
