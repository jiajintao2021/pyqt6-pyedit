__all__ = [
    'open_project_event',
    'open_project_event_file',
]


def open_project_event():
    from pye.events.menus.open_project_e_0 import win2
    win2.show()
    return win2


def open_project_event_file():
    from pye.events.menus.open_project_e_1 import file_dialog
    file_dialog.exec()
    return file_dialog
