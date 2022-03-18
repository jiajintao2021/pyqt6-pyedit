from PyQt6.QtWidgets import QWidget, QSizePolicy

from statics import CONTENT_LEFT_POLICY

h, v = CONTENT_LEFT_POLICY

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

content_left = QWidget()
content_left.setSizePolicy(_size_policy)
content_left.setStyleSheet(
    """

    """
)
