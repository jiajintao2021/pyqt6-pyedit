from pye.menus.menubar import menubar
from pye.menus.menu_edit import menu_edit
from pye.menus.menu_file import menu_file

__all__ = [
    'menubar',
]

menubar.addMenu(menu_file)
menubar.addMenu(menu_edit)
