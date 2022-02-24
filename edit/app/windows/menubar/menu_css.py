__all__ = [
    'MENUBAR_CSS',
    'MENU',

]

MENUBAR_CSS = """
QMenuBar {
    background-color: blue;
    height: 14px;
    width: 60px;
    font-size: 14px;
}
"""

MENU = """
QMenu {
    margin-top: 2px;
}
"""


def content_center_h(height: int, content_height: int) -> float:
    """
    在高度上居中
    :return:
    """
    return (height - content_height) / 2
