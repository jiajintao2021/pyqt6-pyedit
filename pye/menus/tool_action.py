from PyQt6.QtGui import QAction

from pye.content.content_middle.monkey.monkey_event import add_middle_toolbar_monkey
from pye.content.content_middle.oat.oat_events import add_middle_toolbar

oat_action = QAction('OAT')
oat_action.triggered.connect(add_middle_toolbar)

tool_action = QAction('Monkey')
tool_action.triggered.connect(add_middle_toolbar_monkey)
