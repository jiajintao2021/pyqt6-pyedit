from pye.content.left_menu.menubar import left_menubar

__all__ = [
    'left_menubar',
]

from pye.content.left_menu.menu_project import project_action
left_menubar.addAction(project_action)

# from pye.content.left_menu.menu_file import file_action
# left_menubar.addAction(file_action)
