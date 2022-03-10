from PyQt6.QtWidgets import QBoxLayout

__all__ = [
    'middle',
]


middle_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
middle_layout.setContentsMargins(0, 0, 0, 0)
middle_layout.setSpacing(0)

from pye.content.content_middle.content_middle import middle
middle.setLayout(middle_layout)

from pye.content.content_middle.toolbar import middle_toolbar
middle_layout.addWidget(middle_toolbar)

from pye.content.content_middle.content import content_middle
middle_layout.addWidget(content_middle)
