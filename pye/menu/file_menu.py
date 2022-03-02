from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction


file_menu = QMenu('File(&F)')

open_action = QAction('Open(&O)')

file_menu.addAction(open_action)
