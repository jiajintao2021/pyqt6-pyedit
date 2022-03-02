from PyQt6.QtWidgets import QSizePolicy, QWidget

from config import EDIT_CONTENT_RIGHT_POLICY

h, v = EDIT_CONTENT_RIGHT_POLICY


_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding, )
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

edit_content_right = QWidget()
edit_content_right.setSizePolicy(_size_policy)

edit_content_right.setStyleSheet(
    """
        QWidget {background-color: yellow;}
    """
)
