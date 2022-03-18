from PyQt6.QtWidgets import QMenu

menu_file = QMenu('文件(&F)')

from pye.menus.file_action import open_action, new_action, recent_menu
menu_file.addAction(open_action)
menu_file.addAction(new_action)
menu_file.addMenu(recent_menu)
