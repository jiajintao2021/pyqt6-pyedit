import sys

from PyQt6.QtGui import QAction, QColor, QPalette
from PyQt6.QtWidgets import QApplication, QBoxLayout, QMenu, QMenuBar, QSizePolicy, QWidget

APP = QApplication(sys.argv)

# main_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

main_color = QColor('red')
main_palette = QPalette(main_color)

MainWindow = QWidget()
# MainWindow.setLayout(main_layout)
MainWindow.setPalette(main_palette)

# menu_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
# menu_policy.setHorizontalStretch(1)
# menu_policy.setVerticalStretch(1)

menu_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight, MainWindow)

PE_MenuBar = QMenuBar(MainWindow)
# PE_MenuBar.setSizePolicy(menu_policy)
# PE_MenuBar.setLayout(menu_layout)
# menu_layout.addWidget(PE_MenuBar, 1, alignment=)
menu_layout.setMenuBar(PE_MenuBar)

PE_Menu_File = QMenu('File')

# PE_Menu_File_New = QAction('New File')
# PE_Menu_File_Open = QAction('Open File')

# PE_Menu_File.addAction(PE_Menu_File_New)
# PE_Menu_File.addAction(PE_Menu_File_Open)

PE_MenuBar.addMenu(PE_Menu_File)

MainWindow.show()

if __name__ == '__main__':
    sys.exit(APP.exec())

