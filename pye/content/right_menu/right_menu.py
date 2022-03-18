from PyQt6.QtWidgets import QToolBar, QBoxLayout
from PyQt6.QtCore import Qt

from pye.cores.static import load_qss

right_tool_bar_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

right_tool_bar = QToolBar()

right_tool_bar.setStyleSheet(
    load_qss('menubar_right.qss')
)
right_tool_bar.setLayout(right_tool_bar_layout)

right_tool_bar.setOrientation(Qt.Orientation.Vertical)
