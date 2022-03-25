from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QToolBar, QLabel, QWidget, QBoxLayout

from pye.cores.static import load_qss
from statics import MIDDLE_MAX_TOOL_HEIGHT, MIDDLE_MIN_TOOL_HEIGHT


__all__ = [
    'toolbars',

    'middle_toolbar_layout',
    'middle_toolbar',
]


toolbars = []


middle_toolbar_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)


middle_toolbar = QWidget()
middle_toolbar.setMinimumHeight(MIDDLE_MIN_TOOL_HEIGHT)
middle_toolbar.setMaximumHeight(MIDDLE_MAX_TOOL_HEIGHT)
# middle_toolbar.setOrientation(Qt.Orientation.Horizontal)

middle_toolbar.setStyleSheet(
    load_qss('content_middle_toolbar.qss')
)

middle_toolbar.setLayout(middle_toolbar_layout)
