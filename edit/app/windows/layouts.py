from PyQt6.QtWidgets import QBoxLayout

__all__ = [
    'MainLayout',
    'MenuBarLayout',
]

MainLayout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
# MainLayout.setContentsMargins(0, 0, 0, 0)

MenuBarLayout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
MainLayout.addLayout(MenuBarLayout)
