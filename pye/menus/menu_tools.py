from PyQt6.QtWidgets import QMenu


menu_tool = QMenu('工具 (&T)')

from pye.menus.tool_action import oat_action, tool_action
menu_tool.addAction(oat_action)
menu_tool.addAction(tool_action)
