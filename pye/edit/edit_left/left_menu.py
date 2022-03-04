# from PyQt6.QtCore import QUrl
# from PyQt6.QtWidgets import QMenuBar, QBoxLayout, QWidget
# from PyQt6.QtGui import QAction, QIcon
#
# from pye.core.dir import get_icon
#
# layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
# # get_icon('folder2.svg')
# menu_icon = QIcon()
#
# icons_menu = QWidget()
# layout.addWidget(icons_menu)
# _project = QAction()
# menu_icon.addFile(get_icon('folder2.svg'))
# _project.setIcon(menu_icon)
#
# icons_menu.addAction(_project)
#
# _edit_file = QAction('Edit Files')
#
# # funcs_menu.setLayout(layout)


from PyQt6.QtWidgets import QBoxLayout, QWidget
from PyQt6.QtGui import QAction, QIcon

from pye.core.dir import get_icon

menus_icons_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

menus_icons = QWidget()
menus_icons.setStyleSheet(
    """
    QWidget {background-color: black;}
    """
)

# icon_p = QAction()
# icon_p.setIcon(QIcon(get_icon('folder2.svg')))

menus_icons_layout.addWidget(menus_icons)

# menus_icons = QWidget()
