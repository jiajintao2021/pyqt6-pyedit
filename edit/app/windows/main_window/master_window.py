"""
main window default config
"""
from PyQt6.QtGui import QColor, QPalette

from edit.app.app import MAIN_WINDOW, MAIN_WINDOW_SIZE_POLICY
from edit.app.windows.layouts import MainLayout

MAIN_WINDOW_TITLE = 'PythonEdit'


__all__ = [
    'MAIN_WINDOW',

    'MAIN_WINDOW_TITLE',
    'MAIN_WINDOW_SIZE_POLICY',

    'get_main_window_height',
    'get_main_window_width',

    'DEFAULT_WINDOW_WIDTH',
    'DEFAULT_WINDOW_HEIGHT',
]

# MainLayout.addWidget(MAIN_WINDOW)

DEFAULT_WINDOW_WIDTH = 800
DEFAULT_WINDOW_HEIGHT = 400

# MAIN_WINDOW.setMinimumWidth(DEFAULT_WINDOW_WIDTH)
# MAIN_WINDOW.setMinimumHeight(DEFAULT_WINDOW_HEIGHT)

MAIN_WINDOW.setWindowTitle(MAIN_WINDOW_TITLE)

qp = QPalette(QColor('red'))

MAIN_WINDOW.setPalette(qp)
MAIN_WINDOW.setBackgroundRole(qp.ColorRole.Window)


def get_main_window_height():
    return MAIN_WINDOW.height()


def get_main_window_width():
    return MAIN_WINDOW.width()
