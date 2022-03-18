from PyQt6.QtWidgets import QSizePolicy, QToolBar
from PyQt6.QtCore import QSize, Qt

from pye.cores.static import load_qss
from statics import CONTENT_LEFT_TOOL_POLICY, LEFT_MAX_TOOL_HEIGHT, LEFT_MIN_TOOL_HEIGHT

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

h, v = CONTENT_LEFT_TOOL_POLICY
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

content_left_tool = QToolBar()
content_left_tool.setOrientation(Qt.Orientation.Horizontal)
content_left_tool.setSizePolicy(_size_policy)
content_left_tool.setIconSize(QSize(15, 15))
content_left_tool.setMinimumHeight(LEFT_MIN_TOOL_HEIGHT)
content_left_tool.setMaximumHeight(LEFT_MAX_TOOL_HEIGHT)


content_left_tool.setStyleSheet(load_qss('content_left_toolbar.qss'))

from pye.content.content_left.tool_folder_add import folder_add_action
content_left_tool.addAction(folder_add_action)

from pye.content.content_left.tool_file_add import file_add_action
content_left_tool.addAction(file_add_action)

from pye.content.content_left.tool_file_remove import file_remove_action
content_left_tool.addAction(file_remove_action)
