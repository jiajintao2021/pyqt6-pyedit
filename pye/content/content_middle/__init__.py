__all__ = [
    'middle_default',
]

from PyQt6.QtWidgets import QBoxLayout

load_middle_history = None

middle_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
middle_layout.setContentsMargins(0, 0, 0, 0)
middle_layout.setSpacing(0)

from pye.content.content_middle.content_middle import middle_default
middle_default.setLayout(middle_layout)

from pye.content.content_middle.content_toolbar import middle_toolbar
middle_layout.addWidget(middle_toolbar)

from pye.content.content_middle.default.content_default import content_middle
middle_layout.addWidget(content_middle)
