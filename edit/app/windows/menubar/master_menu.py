from PyQt6.QtWidgets import QBoxLayout, QLayout, QMenuBar, QSizePolicy, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from edit.app.app import MAIN_WINDOW
from edit.app.utils import to_css

__all__ = [
    'MasterMenuBar',
]

MasterMenuBar = QMenuBar(MAIN_WINDOW)

# MenuBarPolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
# MenuBarPolicy.setHorizontalStretch(1)

# MenuBarLayout = QBoxLayout(QBoxLayout.Direction.LeftToRight, MainWindow)

# MasterMenuBar.setSizePolicy(MenuBarPolicy)

# MMB_LAYOUT.setMenuBar(MasterMenuBar)


# MainLayout.addWidget(MasterMenuBar)

# QBL = QBoxLayout(QBoxLayout.Direction.LeftToRight, MAIN_WINDOW)


# MasterMenuBar.setLayout(QBL)
# MasterMenuBar.setSizePolicy(MM_SP)

# qb.addWidget(MasterMenuBar)
# qb.addStretch(1)
# MasterMenuBar.setLayout(qb)
