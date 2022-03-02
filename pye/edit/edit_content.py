from PyQt6.QtWidgets import QWidget, QSizePolicy

from config import EDIT_CONTENT_POLICY

h, v = EDIT_CONTENT_POLICY

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding, )
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

edit_content = QWidget()

edit_content.setSizePolicy(_size_policy)

edit_content.setStyleSheet(
    """
        QWidget {background-color: blue;}
    """
)
