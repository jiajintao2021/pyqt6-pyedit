import os

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QDialog

from pye.core.dir import get_icon, get_static_file

win2 = QDialog()

win2.setWindowIcon(
    QIcon(
        get_icon('folder2.svg')
    )
)

win2.setWindowTitle('选择项目')

win2.resize(300, 400)
win2.setMinimumWidth(200)
win2.setMinimumHeight(400)

win2.setStyleSheet(
    """
    QWidget {background-color: black;}
    """
)
