from PyQt6.QtWidgets import QBoxLayout, QWidget

__all__ = [
    'content_left_layout',
    'content_left',
]

content_left_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

content_left_layout.setContentsMargins(0, 0, 0, 0)
content_left_layout.setSpacing(0)

from pye.content.content_left.content_left import content_left
content_left.setLayout(content_left_layout)

from pye.content.content_left.content_left_tool import content_left_tool
content_left_layout.addWidget(content_left_tool)

from pye.content.content_left.dirtree import dirtree
content_left_layout.addWidget(dirtree)
