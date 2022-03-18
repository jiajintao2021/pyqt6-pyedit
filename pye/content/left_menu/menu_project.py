from PyQt6.QtGui import QAction, QIcon

from pye.cores.static import load_icon

_icon = QIcon(load_icon('folder2.svg'))


project_action = QAction('project')
project_action.setIcon(_icon)
