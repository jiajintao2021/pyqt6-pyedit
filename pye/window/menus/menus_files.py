from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction


class FileMenu(QMenu):
    open_action: QAction

    def __init__(self, parent):
        super().__init__('File', parent)

        self.open_action = OpenAction()
        self.addAction(self.open_action)


class OpenAction(QAction):

    def __init__(self):
        super().__init__('Open')
