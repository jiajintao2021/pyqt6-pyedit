import sys

from PyQt6.QtWidgets import QApplication, QWidget


__all__ = [
    'APP',
    'MAIN_WINDOW',
]

APP = QApplication(sys.argv)

MAIN_WINDOW = QWidget()

import edit.app.windows
MAIN_WINDOW.show()
