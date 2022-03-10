from PyQt6.QtWidgets import QBoxLayout

from pye.content.content_right.content_right import content_right

__all__ = [
    'content_right',
]


content_right_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
content_right_layout.setContentsMargins(0, 0, 0, 0)

content_right.setLayout(content_right_layout)

from pye.content.content_right.content_right_top import content_right_tool
content_right_layout.addWidget(content_right_tool)

from pye.content.content_right.content_right_middle import content_right_middle
content_right_layout.addWidget(content_right_middle)
