from PyQt6.QtWidgets import QWidget

from pye.cores.static import load_qss

content = QWidget()

sheet_style = load_qss('content_global.qss')
content.setStyleSheet(
    sheet_style
)
