from PyQt6.QtGui import QAction, QIcon

from pye.cores.static import load_icon

_icon = QIcon(load_icon('file-earmark-minus.svg'))

file_remove_action = QAction('remove file')
file_remove_action.setIcon(_icon)
