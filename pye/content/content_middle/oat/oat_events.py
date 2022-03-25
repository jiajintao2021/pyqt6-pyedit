from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QLabel


def add_middle_toolbar():
    tool_name = 'oat'
    # oat = QAction(tool_name)
    oat = QLabel(tool_name)
    # oat.setStyleSheet(
    #     """
    #     QLabel {
    #         background-color: white;
    #         height: 20px;
    #     }
    #     """
    # )

    from pye.content.content_middle.content_toolbar import middle_toolbar, middle_toolbar_layout
    middle_toolbar_layout.addWidget(oat)
    from pye.content.content_middle.content_toolbar import toolbars
    toolbars.append(oat)
    return oat
