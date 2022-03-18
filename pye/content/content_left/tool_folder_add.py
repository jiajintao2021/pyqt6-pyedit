from PyQt6.QtGui import QAction, QIcon

from pye.cores.static import load_icon

_icon = QIcon(load_icon('folder-plus.svg'))

folder_add_action = QAction('add folder')
folder_add_action.setIcon(_icon)
