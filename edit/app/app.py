import sys

from PyQt6.QtWidgets import QApplication, QSizePolicy, QWidget


__all__ = [
    'APP',
    'MAIN_WINDOW',
    'MAIN_WINDOW_SIZE_POLICY',
]

APP = QApplication(sys.argv)
# APP.setStyle('Fusion')
MAIN_WINDOW = QWidget()

MAIN_WINDOW.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

MAIN_WINDOW_SIZE_POLICY = MAIN_WINDOW.sizePolicy()
# MAIN_WINDOW_SIZE_POLICY = None

import edit.app.windows
MAIN_WINDOW.show()
