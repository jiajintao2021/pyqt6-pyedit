from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget, QBoxLayout


class PyEContentLayout(QBoxLayout):
    content_left: QWidget
    content_right: QWidget
    content: QWidget

    def __init__(self, parent):
        direction = QBoxLayout.Direction.LeftToRight
        super().__init__(direction, parent)

        # self.content_left = PyEContentLeft(parent)
        # self.content_right = PyEContentRight(parent)

        self.content = PyEContent(parent)

        # self.addWidget(self.content_left, 1)
        self.addWidget(self.content, 2)
        # self.addWidget(self.content_right, 1)


class ContentBase(QWidget):
    content_left_color: QColor
    content_left_palette: QPalette
    color_str = ''

    def __init__(self, parent):
        super().__init__(parent)

        # self.set_color()
        self.setStyleSheet(
            """
                QWidget {
                    background-color: red;
                }
            """
        )

    def set_color(self):
        self.content_left_color = QColor(self.color_str)
        self.content_left_palette = QPalette(self.content_left_color)
        self.setPalette(self.content_left_palette)


class PyEContentRight(ContentBase):
    color_str = 'blue'


class PyEContentLeft(ContentBase):
    color_str = 'red'


class PyEContent(ContentBase):
    color_str = 'white'
