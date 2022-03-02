from PyQt6.QtWidgets import QBoxLayout, QSizePolicy, QWidget

from config import EDIT_CONTENT_LEFT_POLICY

h, v = EDIT_CONTENT_LEFT_POLICY

_size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding, )
_size_policy.setHorizontalStretch(h)
_size_policy.setVerticalStretch(v)

edit_dirtree_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
edit_dirtree_layout.setContentsMargins(0, 0, 0, 0)
edit_dirtree_layout.setSpacing(0)

edit_content_left = QWidget()
edit_content_left.setSizePolicy(_size_policy)

from pye.edit.edit_left.left_menu import funcs_menu
edit_dirtree_layout.setMenuBar(funcs_menu)

from pye.edit.edit_left.dirtree_win import dirtree
edit_dirtree_layout.addWidget(dirtree)

edit_content_left.setLayout(edit_dirtree_layout)