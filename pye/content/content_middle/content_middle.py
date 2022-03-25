from PyQt6.QtWidgets import QSizePolicy, QWidget

from pye.cores.static import load_qss
from statics import CONTENT_MIDDLE_POLICY

h, v = CONTENT_MIDDLE_POLICY

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

middle_default = QWidget()
middle_default.setSizePolicy(_size_policy)

middle_default.setStyleSheet(
    load_qss('content_middle_middle.qss')
)
