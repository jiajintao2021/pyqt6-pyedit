from pye.content.right_menu.right_menu import right_tool_bar

__all__ = [
    'right_tool_bar',
]

from pye.content.right_menu.tool_1 import tool_1_action
right_tool_bar.addAction(tool_1_action)
