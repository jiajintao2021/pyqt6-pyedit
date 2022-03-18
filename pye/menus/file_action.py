from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu, QFileDialog

from pye.cores import Settings


def open_project():
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.FileMode.Directory)
    file_dialog.setOptions(
        QFileDialog.Option.ShowDirsOnly | QFileDialog.Option.DontUseNativeDialog | QFileDialog.Option.ReadOnly)
    file_dialog.exec()

    project_dirpath = file_dialog.selectedFiles()[0]

    if project_dirpath not in Settings.settings.project:
        Settings.update(project=project_dirpath)
        Settings.save()

        recent_project_add()


def recent_project_add():
    for project_name in Settings.settings.project:
        if project_name not in _project_info:
            _action = QAction(project_name)
            recent_menu.addAction(_action)
            _project_info[project_name] = _action


open_action = QAction('打开项目 (&O)')
open_action.triggered.connect(open_project)

new_action = QAction('新建项目 (&N)')

recent_manager_action = QAction('管理项目')

recent_menu = QMenu('打开最近 (&R)')
_project_info = {}
recent_menu.aboutToShow.connect(recent_project_add)
recent_menu.addAction(recent_manager_action)
recent_menu.addSeparator()
