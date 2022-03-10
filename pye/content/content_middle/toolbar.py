from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QToolBar

from cores.static import load_qss
from statics import MIDDLE_MIN_TOOL_HEIGHT

middle_toolbar = QToolBar()
middle_toolbar.setMinimumHeight(MIDDLE_MIN_TOOL_HEIGHT)
middle_toolbar.setOrientation(Qt.Orientation.Horizontal)

middle_toolbar.setStyleSheet(
    load_qss('content_middle_toolbar.qss')
)
