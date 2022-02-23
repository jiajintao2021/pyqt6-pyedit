from PyQt6.QtWidgets import QMenu

from . import menu_css

ViewMenu = QMenu(
    '视图(&V)'
)
ViewMenu.setStyleSheet(menu_css.MENU)
