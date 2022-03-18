from PyQt6.QtWidgets import QSizePolicy, QWidget

from pye.cores.static import load_qss
from statics import CONTENT_RIGHT_MIDDLE_POLICY

h, v = CONTENT_RIGHT_MIDDLE_POLICY

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

content_right_middle = QWidget()
content_right_middle.setSizePolicy(_size_policy)

content_right_middle.setStyleSheet(
    load_qss('menubar_right.qss')
)
