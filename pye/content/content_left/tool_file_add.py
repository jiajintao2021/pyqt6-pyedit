from PyQt6.QtGui import QAction, QIcon

from pye.cores.static import load_icon

_icon = QIcon(load_icon('file-earmark-plus.svg'))

file_add_action = QAction('add file')
file_add_action.setIcon(_icon)
