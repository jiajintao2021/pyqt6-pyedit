from PyQt6.QtWidgets import QMenu, QMenuBar, QBoxLayout

from pye.window.menus.menus_files import FileMenu
from style_sheets.default import DEFAULT_MENUBAR


class PyEMenuBarLayout(QBoxLayout):

    def __init__(self, parent):
        direction = QBoxLayout.Direction.LeftToRight
        super().__init__(direction, parent)

        self.py_menubar = PyEMenuBar(parent)

        self.setMenuBar(self.py_menubar)


class PyEMenuBar(QMenuBar):
    menu_file: QMenu

    def __init__(self, parent):
        super().__init__(parent)

        self.add_menus()

        # self.setFont(MenuFont_File)
        self.add_style_sheet()

    def add_menus(self):
        self.menu_file = FileMenu(self)
        self.addMenu(self.menu_file)

    def add_style_sheet(self):
        self.setStyleSheet(DEFAULT_MENUBAR)
