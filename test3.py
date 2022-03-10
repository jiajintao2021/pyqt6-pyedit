import sys

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication, QBoxLayout, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget
from pydantic.color import Color


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout(self)
        layout2 = QVBoxLayout(self)
        layout3 = QVBoxLayout(self)

        qw1 = QWidget()
        qw1.setStyleSheet(
            """QWidget {background-color: red;}"""
        )
        qw2 = QWidget()
        qw2.setStyleSheet(
            """QWidget {background-color: yellow;}"""
        )
        qw3 = QWidget()
        qw3.setStyleSheet(
            """QWidget {background-color: purple;}"""
        )
        # layout2.addWidget(Color('red'))
        layout2.addWidget(qw1)
        # layout2.addWidget(Color('yellow'))
        layout2.addWidget(qw2)
        # layout2.addWidget(Color('purple'))
        layout2.addWidget(qw3)

        layout1.addLayout(layout2)

        qw4 = QWidget()
        qw4.setStyleSheet(
            """QWidget {background-color: green;}"""
        )
        # layout1.addWidget(Color('green'))
        layout1.addWidget(qw4)

        qw5 = QWidget()
        qw5.setStyleSheet(
            """QWidget {background-color: red;}"""
        )
        layout3.addWidget(qw5)
        qw6 = QWidget()
        qw6.setStyleSheet(
            """QWidget {background-color: purple;}"""
        )
        # layout3.addWidget(Color('purple'))
        layout3.addWidget(qw6)

        layout1.addLayout(layout3)

        # widget = QWidget()
        # widget.setLayout(layout1)
        # self.setCentralWidget(widget)
        self.setLayout(layout1)


class Base(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet(
            """
                Base {background-color: red;}
            """
        )


class PyEContentLayout(QBoxLayout):

    def __init__(self):
        direction = QBoxLayout.Direction.TopToBottom
        super().__init__(direction)

        # qw = Base()
        qw = QWidget()
        qw.setStyleSheet(
            """
                QWidget {background-color: red;}
            """
        )
        self.addWidget(qw)


class MasterWindowBase(QWidget):
    master_window_color: QColor
    master_window_palette: QPalette

    def __init__(self):
        super().__init__()

        self.setMinimumWidth(600)
        self.setMinimumHeight(300)

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom, self)

        # menubar = PyEMenuBarLayout(self)
        content = PyEContentLayout()

        # layout.addChildLayout(menubar)
        layout.addLayout(content)
        # layout.addChildLayout(content_middle)

        self.setLayout(layout)
        # self.add_menubar()
        # self.add_content()


if __name__ == '__main__':
    PyEApp = QApplication(sys.argv)
    mainwindow = MasterWindowBase()
    # mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(PyEApp.exec())
