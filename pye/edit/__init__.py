from PyQt6.QtWidgets import QBoxLayout

edit_content_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
edit_content_layout.setSpacing(0)

from pye.edit.edit_content import edit_content
from pye.edit.edit_content_left import edit_content_left
from pye.edit.edit_content_right import edit_content_right

# edit_content_layout.addLayout(edit_dirtree_layout)

edit_content_layout.addWidget(edit_content_left)
edit_content_layout.addWidget(edit_content)
edit_content_layout.addWidget(edit_content_right)
