"""
main window default config
"""
from edit.app.app import MAIN_WINDOW, MAIN_WINDOW_SIZE_POLICY

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

DEFAULT_WINDOW_WIDTH = 800
DEFAULT_WINDOW_HEIGHT = 400

MAIN_WINDOW.setMinimumWidth(DEFAULT_WINDOW_WIDTH)
MAIN_WINDOW.setMinimumHeight(DEFAULT_WINDOW_HEIGHT)

MAIN_WINDOW.setWindowTitle(MAIN_WINDOW_TITLE)


def get_main_window_height():
    return MAIN_WINDOW.height()


def get_main_window_width():
    return MAIN_WINDOW.width()
