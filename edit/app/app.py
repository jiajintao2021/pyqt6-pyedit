import sys

from PyQt6.QtWidgets import QApplication, QSizePolicy, QWidget


__all__ = [
    'APP',
    'MAIN_WINDOW',
    'MAIN_WINDOW_SIZE_POLICY',
]

APP = QApplication(sys.argv)
MAIN_WINDOW = QWidget()

MAIN_WINDOW_SIZE_POLICY = MAIN_WINDOW.sizePolicy()

import edit.app.windows
MAIN_WINDOW.show()
