from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QTreeWidget, QTreeView, QLabel
from PyQt6.QtCore import Qt

from cores.static import load_qss

top_dir = None

if not top_dir:
    dirtree = QLabel('Is None!')
    dirtree.setAlignment(Qt.AlignmentFlag.AlignCenter)
else:
    dirtree = QTreeView()
    dirtree.addAction(QAction('test'))


dirtree.setStyleSheet(
    load_qss('content_left_dirtree.qss')
)
