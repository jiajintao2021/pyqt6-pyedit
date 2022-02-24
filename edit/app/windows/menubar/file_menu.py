from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu

from edit.app.windows.menubar.menu_css import MENU

__all__ = [
    'FileMenu',

    'NewSubmenuFile',
    'OpenSubmenuFile',
]

NewSubmenuFile = QAction(
    'New File | Ctrl + N'
)

OpenSubmenuFile = QAction(
    'Open File | Ctrl + O'
)

FileMenu = QMenu('文件(&F)')
FileMenu.setStyleSheet(MENU)


FileMenu.addAction(NewSubmenuFile)
FileMenu.addAction(OpenSubmenuFile)
