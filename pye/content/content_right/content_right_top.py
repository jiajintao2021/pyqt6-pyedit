from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSizePolicy, QToolBar

from pye.cores.static import load_qss
from statics import CONTENT_RIGHT_TOOL_POLICY, RIGHT_MAX_TOOL_HEIGHT, RIGHT_MIN_TOOL_HEIGHT

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

h, v = CONTENT_RIGHT_TOOL_POLICY
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

content_right_tool = QToolBar()
content_right_tool.setOrientation(Qt.Orientation.Horizontal)
content_right_tool.setSizePolicy(_size_policy)
content_right_tool.setMinimumHeight(RIGHT_MIN_TOOL_HEIGHT)
content_right_tool.setMaximumHeight(RIGHT_MAX_TOOL_HEIGHT)

content_right_tool.setStyleSheet(load_qss('content_right_toolbar.qss'))
