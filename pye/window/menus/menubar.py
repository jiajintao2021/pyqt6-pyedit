from PyQt6.QtWidgets import QBoxLayout, QMenuBar, QSizePolicy

from pye.window import PyE_Master, Master_Layout

MenuBar_Policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
MenuBar_Policy.setHorizontalStretch(1)
MenuBar_Policy.setVerticalStretch(1)

MenuBar_Layout = QBoxLayout(QBoxLayout.Direction.LeftToRight, PyE_Master)
Master_Layout.addChildLayout(MenuBar_Layout)

PE_MenuBar = QMenuBar(PyE_Master)
PE_MenuBar.setLayout(MenuBar_Layout)

from pye.window.menus.menu_file import PE_Menu_File
PE_MenuBar.addMenu(PE_Menu_File)

print(MenuBar_Layout.isEnabled())
# PE_MenuBar.setSizePolicy(MenuBar_Policy)
# MenuBar_Layout.setMenuBar(PE_MenuBar)
# PE_MenuBar.setLayout(MenuBar_Layout)
# Master_Layout.setLayout()
