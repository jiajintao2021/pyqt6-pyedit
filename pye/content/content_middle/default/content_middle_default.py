from PyQt6.QtWidgets import QWidget, QSizePolicy

from statics import CONTENT_MIDDLE_POLICY

h, v = CONTENT_MIDDLE_POLICY

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

_middle_default = QWidget()
_middle_default.setSizePolicy(_size_policy)
