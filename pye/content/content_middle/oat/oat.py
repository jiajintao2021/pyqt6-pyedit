from PyQt6.QtWidgets import QSizePolicy, QWidget

from statics import OAT_MIDDLE_POLICY

h, v = OAT_MIDDLE_POLICY

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

middle_oat = QWidget()
middle_oat.setStyleSheet(
    """
    QWidget {
        background-color: red;
    }
    """
)
