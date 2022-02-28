from PyQt6.QtWidgets import QMenu, QMenuBar

from pye.window.app import PyE_App, PyE_Master, Master_Layout

__all__ = [
    'PyE_App',
    'PyE_Master',
    'Master_Layout',
]

import pye.window.menus

PyE_Master.show()
