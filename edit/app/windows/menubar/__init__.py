from .master_menu import MasterMenuBar
from .file_menu import FileMenu, OpenSubmenuFile, NewSubmenuFile
from .edit_menu import EditMenu, BackSpace, WorkModel
from .view_menu import ViewMenu

__all__ = [
    'MasterMenuBar',

    'FileMenu',  # file menu
    'NewSubmenuFile',
    'OpenSubmenuFile',

    'EditMenu',  # Edit menu
    'BackSpace',
    'WorkModel',

    'ViewMenu',  # view menu
]

# MasterMenuBar.setStyleSheet(
#     """
#     QMenuBar {
#         width: 70px;
#         height: 30px;
#     }
# """
# )

MasterMenuBar.addMenu(FileMenu)
MasterMenuBar.addMenu(EditMenu)
MasterMenuBar.addMenu(ViewMenu)

MasterMenuBar.show()

# MasterMenuBar.setStyleSheet(
#     """
#     QMenuBar {
#         width: 70px;
#         height: 30px;
#     }
# """
# )
