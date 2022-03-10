from PyQt6.QtCore import QMargins
from PyQt6.QtWidgets import QBoxLayout

__all__ = [
    'content',
]

margins = QMargins(0, 0, 0, 0)

content_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
content_layout.setContentsMargins(margins)
content_layout.setSpacing(0)

from pye.content.content import content
content.setLayout(content_layout)

from pye.content.left_menu import left_menubar
content_layout.addWidget(left_menubar)

from pye.content.content_left import content_left
content_layout.addWidget(content_left)

from pye.content.content_middle import middle
content_layout.addWidget(middle)

from pye.content.content_right import content_right
content_layout.addWidget(content_right)

from pye.content.right_menu import right_tool_bar
content_layout.addWidget(right_tool_bar)
