from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction

from pye.events import open_project_event, open_project_event_file

file_menu = QMenu('File(&F)')

open_action = QAction('Open(&O)')
open_action.triggered.connect(open_project_event_file)

file_menu.addAction(open_action)
