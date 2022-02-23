import sys

from PyQt6.QtWidgets import QApplication, QWidget

APP = QApplication(sys.argv)

MAIN_WINDOW = QWidget()

MAIN_WINDOW.setMinimumWidth(800)
MAIN_WINDOW.setMinimumHeight(400)
import edit.app.windows
MAIN_WINDOW.show()
