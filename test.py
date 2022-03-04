import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QWidget, QBoxLayout, QToolBar

PyEApp = QApplication(sys.argv)

window = QWidget()
window.resize(600, 300)
window_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)


# layout1 = QBoxLayout(QBoxLayout.Direction.TopToBottom)
# print(list(QBoxLayout.Direction))
qw1 = QToolBar(window)
# qw1.setLayout(layout1)

# qw1.setLayoutDirection(QBoxLayout.Direction.TopToBottom)
qw1.setOrientation(QToolBar.Orientation)
qw1.addAction(QAction('Test1', window))
qw1.addAction(QAction('Test2', window))

# qw2 = QToolBar()
# qw2.addAction(QAction('Test3'))
# qw2.addAction(QAction('Test4'))
# layout2 = QBoxLayout(QBoxLayout.Direction.LeftToRight)
# qw2.setLayout(layout2)
#
# # window_layout.addWidget(qw1)
# # window_layout.addWidget(qw2)
# window_layout.addLayout(layout1)
# window_layout.addLayout(layout2)
# window.setLayout(window_layout)
window.show()


if __name__ == '__main__':
    sys.exit(PyEApp.exec())
