from settings import BASE_DIR, HISTORY_DIRPATH


def open_project_history_dir():
    return HISTORY_DIRPATH


def open_project_default_dirpath():
    return BASE_DIR


def init_history():
    default = open_project_default_dirpath()
