from PyQt6.QtWidgets import QLabel


__all__ = [
    'add_middle_toolbar_monkey',
]


def add_middle_toolbar_monkey():
    tool_name = 'Monkey'
    # oat = QAction(tool_name)
    monkey = QLabel(tool_name)
    # monkey.setStyleSheet(
    #     """
    #     QLabel {
    #         background-color: white;
    #         height: 30px;
    #     }
    #     """
    # )
    from pye.content.content_middle.content_toolbar import middle_toolbar_layout
    middle_toolbar_layout.addWidget(monkey)
    # middle_toolbar.addAction(oat)
    from pye.content.content_middle.content_toolbar import toolbars
    toolbars.append(monkey)
    return monkey
