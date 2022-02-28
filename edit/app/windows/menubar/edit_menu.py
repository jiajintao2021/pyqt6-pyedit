from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu

__all__ = [
    'EditMenu',

    'BackSpace',
    'WorkModel',
]


BackSpace = QAction(
    '撤销'
)
WorkModel = QAction(
    '工作模式'
)


EditMenu = QMenu('编辑(&E)')
# EditMenu.setStyleSheet(menu_css.MENU)

EditMenu.addAction(BackSpace)
EditMenu.addAction(WorkModel)
