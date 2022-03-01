from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget, QBoxLayout

from pye.window.content.content import PyEContentLayout
from pye.window.menus.menubar import PyEMenuBarLayout


class MasterWindowBase(QWidget):
    master_window_color: QColor
    master_window_palette: QPalette

    def __init__(self):
        super().__init__()

        self.setMinimumWidth(600)
        self.setMinimumHeight(300)

        # self.set_color()

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom, self)

        # menubar = PyEMenuBarLayout(self)
        content = PyEContentLayout(self)

        # layout.addChildLayout(menubar)
        layout.addLayout(content)
        # layout.addChildLayout(content)

        # self.add_menubar()
        # self.add_content()

    def set_color(self):
        self.master_window_color = QColor('#d0d0d0')
        self.master_window_palette = QPalette(self.master_window_color)
        self.setPalette(
            self.master_window_palette
        )

    def add_menubar(self):
        PyEMenuBarLayout(self)

    def add_content(self):
        PyEContentLayout(self)


class PyEMain(MasterWindowBase):
    pass
