"""
main window default config
"""
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QBoxLayout

from edit.app.app import MAIN_WINDOW

MAIN_WINDOW_TITLE = 'PythonEdit'


__all__ = [
    'MAIN_WINDOW',
    'MainLayout',

    'MAIN_WINDOW_TITLE',

    'get_main_window_height',
    'get_main_window_width',

    'DEFAULT_WINDOW_WIDTH',
    'DEFAULT_WINDOW_HEIGHT',
]


DEFAULT_WINDOW_WIDTH = 800
DEFAULT_WINDOW_HEIGHT = 400

MainLayout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
MainLayout.setContentsMargins(0, 0, 0, 0)

MAIN_WINDOW.setLayout(MainLayout)

MAIN_WINDOW.setWindowTitle(MAIN_WINDOW_TITLE)


qp = QPalette(QColor('red'))

MAIN_WINDOW.setPalette(qp)
MAIN_WINDOW.setBackgroundRole(qp.ColorRole.Window)


def get_main_window_height():
    return MAIN_WINDOW.height()


def get_main_window_width():
    return MAIN_WINDOW.width()
