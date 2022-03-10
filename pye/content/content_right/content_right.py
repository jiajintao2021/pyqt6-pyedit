from PyQt6.QtWidgets import QWidget, QBoxLayout, QSizePolicy

from cores.static import load_qss
from statics import CONTENT_RIGHT_POLICY

h, v = CONTENT_RIGHT_POLICY

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

content_right = QWidget()
content_right.setSizePolicy(_size_policy)

content_right.setStyleSheet(
    load_qss('menubar_right.qss')
)
