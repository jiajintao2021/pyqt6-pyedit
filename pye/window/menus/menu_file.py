from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction

PE_Menu_File = QMenu('File')

PE_Menu_File_New = QAction('New File')
PE_Menu_File_Open = QAction('Open File')

PE_Menu_File.addAction(PE_Menu_File_New)
PE_Menu_File.addAction(PE_Menu_File_Open)
