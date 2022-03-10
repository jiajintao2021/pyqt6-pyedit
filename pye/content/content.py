from PyQt6.QtWidgets import QWidget

from cores.static import load_qss

content = QWidget()

content.setStyleSheet(
    load_qss('content_global.qss')
)
