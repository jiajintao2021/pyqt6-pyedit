from PyQt6.QtWidgets import QMenuBar, QSizePolicy

from edit.app.app import MAIN_WINDOW, MAIN_WINDOW_SIZE_POLICY
from edit.app.utils import to_css
from edit.app.windows.main_window.master_window import get_main_window_width, DEFAULT_WINDOW_WIDTH
from edit.app.windows.menubar.menu_css import MENUBAR_CSS


__all__ = [
    'MasterMenuBar',
]


width = get_main_window_width()

# master menubar
MasterMenuBar = QMenuBar(MAIN_WINDOW)

MASTER_MENUBAR_H = MasterMenuBar.height()  # 初始高度
MASTER_MENUBAR_W = DEFAULT_WINDOW_WIDTH  # 菜单栏的宽度和window窗口的宽度相同

# MasterMenuBar.setMinimumWidth(MASTER_MENUBAR_W)

MasterMenuBar.setStyleSheet(
    (''
     '    QMenuBar {'
     '        background-color: blue;'
     '        width: 60px;'
     '    }'
     '    ')
)

# MasterMenuBar.resize(MASTER_MENUBAR_W, MASTER_MENUBAR_H)

# MMB_QSIZE_POLICY = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
MMB_QSIZE_POLICY = QSizePolicy(MAIN_WINDOW_SIZE_POLICY)
MMB_QSIZE_POLICY.setHorizontalStretch(2)
MMB_QSIZE_POLICY.setVerticalStretch(2)

MasterMenuBar.setSizePolicy(MMB_QSIZE_POLICY)


# MasterMenuBar.setMaximumWidth(width)  # 最大宽度
# MasterMenuBar.setMinimumWidth(DEFAULT_WINDOW_WIDTH)  # 最小宽度

