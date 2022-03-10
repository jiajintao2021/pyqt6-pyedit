from PyQt6.QtWidgets import QWidgetAction
from PyQt6.QtGui import QAction, QIcon

from cores.static import load_icon

_icon = QIcon(load_icon('folder2.svg'))


project_action = QAction('project')
project_action.setIcon(_icon)
