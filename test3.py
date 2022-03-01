import sys

from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget
from pydantic.color import Color


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

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

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    PyEApp = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(PyEApp.exec())