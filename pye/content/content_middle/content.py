from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QSizePolicy, QWidget

from cores.static import load_qss
from statics import CONTENT_MIDDLE_POLICY

h, v = CONTENT_MIDDLE_POLICY

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

content_middle = QWidget()
content_middle.setSizePolicy(_size_policy)

content_middle.setStyleSheet(
    load_qss('content_middle_middle.qss')
)
