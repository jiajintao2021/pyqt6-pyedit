from PyQt6.QtWidgets import QBoxLayout, QWidget

main_window = QWidget()
from pye.configs import main_window_config

content_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
content_layout.setContentsMargins(0, 0, 0, 0)

main_window.setLayout(content_layout)

from pye.menus import menubar
content_layout.setMenuBar(menubar)

from pye.content import content
content_layout.addWidget(content)

main_window.show()
