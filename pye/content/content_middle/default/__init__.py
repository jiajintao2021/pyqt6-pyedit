from PyQt6.QtWidgets import QBoxLayout

__all__ = [
    'middle_default',
]


def middle_default():

    middle_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    middle_layout.setContentsMargins(0, 0, 0, 0)
    middle_layout.setSpacing(0)

    from pye.content.content_middle.default.content_middle_default import _middle_default
    _middle_default.setLayout(middle_layout)

    from pye.content.content_middle.default.toolbar_default import middle_toolbar
    middle_layout.addWidget(middle_toolbar)

    from pye.content.content_middle.default.content_default import content_middle
    middle_layout.addWidget(content_middle)

    return _middle_default
