from PyQt6.QtWidgets import QWidget, QBoxLayout, QMenuBar
from PyQt6.QtGui import QActionGroup, QAction

from pye.edit.edit_content_left import edit_content_left

funcs_menu_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)

funcs_menu = QMenuBar(edit_content_left)

_project = QAction('Project')
_edit_file = QAction('Edit Files')

funcs_menu.addActions([_project, _edit_file])

funcs_menu.setLayout(funcs_menu_layout)
