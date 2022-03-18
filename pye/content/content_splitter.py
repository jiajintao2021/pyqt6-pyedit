from PyQt6.QtWidgets import QSplitter


__all__ = [
    'content_splitter',
]

content_splitter = QSplitter()
content_splitter.setContentsMargins(0, 0, 0, 0)
content_splitter.setMinimumWidth(100)
content_splitter.setHandleWidth(1)
content_splitter.setStyleSheet(
    """
    QSplitter::handle {
        background-color: #7B7B7B;
    }
    """
)

from pye.content.content_left import content_left
content_splitter.addWidget(content_left)

from pye.content.content_middle import middle_default
content_splitter.addWidget(middle_default)

from pye.content.content_right import content_right
content_splitter.addWidget(content_right)

content_splitter.setSizes([200, 400, 200])
