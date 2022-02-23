from PyQt6.QtWidgets import QMenuBar

from edit.app.app import MAIN_WINDOW

__all__ = [
    'MasterMenuBar',
]

MASTER_MENUBAR_H = 1

# master menubar
MasterMenuBar = QMenuBar(MAIN_WINDOW)

# MasterMenuBar.setStyleSheet(
#     """
#     QMenuBar {
#         width: 60px;
#     }
# """
# )
