import os
import typing
import re

from settings import ICONS_DIRPATH, QSS_DIRPATH


def get_qss_base_path():
    return QSS_DIRPATH


def get_icons_base_path():
    return ICONS_DIRPATH


def load_qss(name):
    path = os.path.join(get_qss_base_path(), name)
    with open(path, mode='r', encoding='utf8') as f:
        return f.read()


def load_icon(name):
    path = os.path.join(get_icons_base_path(), name)
    return path
