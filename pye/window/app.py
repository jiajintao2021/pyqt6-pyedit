import sys

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication, QBoxLayout, QLayout, QSizePolicy, QWidget

__all__ = [
    'PyE_App',
    'PyE_Master',

    'Master_Layout',
    'Master_SizePolicy',
]


PyE_App = QApplication(sys.argv)
PyE_Master = QWidget()

# Master_SizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
# Master_SizePolicy.setHorizontalStretch(1)
# Master_SizePolicy.setVerticalStretch(1)

Master_Layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
Master_Color = QColor('#d0d0d0')
Master_Palette = QPalette(Master_Color)

PyE_Master.setPalette(Master_Palette)
# PyE_Master.setBackgroundRole(Master_Palette.ColorRole.Base)

PyE_Master.setLayout(Master_Layout)
# PyE_Master.setSizePolicy(Master_SizePolicy)
