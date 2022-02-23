"""
main window default config
"""
from edit.app.app import MAIN_WINDOW

MAIN_WINDOW_TITLE = 'PythonEdit'


__all__ = [
    'MAIN_WINDOW',

    'MAIN_WINDOW_TITLE',

    'get_main_window_height',
    'get_main_window_width',
]

MAIN_WINDOW.setWindowTitle(MAIN_WINDOW_TITLE)


def get_main_window_height():
    return MAIN_WINDOW.height()


def get_main_window_width():
    return MAIN_WINDOW.width()
