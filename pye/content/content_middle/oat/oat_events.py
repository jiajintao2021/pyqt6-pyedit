from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QAction


def add_middle_toolbar():
    label = QAction('test oat')

    from pye.content.content_middle.default.toolbar_default import middle_toolbar_layout
    middle_toolbar_layout.addWidget(label)
