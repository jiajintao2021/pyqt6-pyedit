import os
import typing

from settings import BASE_DIR, ICONS_STATIC


def get_dirtree(path, ignore_str: typing.List[str] = None) -> dict:
    if path is None:
        return {}

    _, _name = os.path.split(path)
    tree_info = {}

    ignore_str = ignore_str or []

    for _ in os.listdir(path):
        if _ in ignore_str:
            continue

        _path = os.path.join(path, _)
        tree_info[_] = {}

        if os.path.isdir(_path):
            tree_info[_].update(get_dirtree(_path, ignore_str))

        elif os.path.isfile(_path):
            tree_info[_] = _

    return tree_info


def get_static_file(basedir=None):
    basedir = basedir or BASE_DIR
    return os.path.join(basedir, ICONS_STATIC)


def get_icon(icon_name, basedir=None):
    return os.path.join(get_static_file(basedir=basedir), icon_name)
