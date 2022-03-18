import os

from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QTreeView, QLabel
from PyQt6.QtCore import Qt, QDir


__all__ = [
    'top_dir',
    'dirtree',
    'file_model',

    'loaded',
    'root_index_model'
]

from pye.cores.static import load_qss

top_dir = QDir.currentPath()


def loaded(path):
    col = 0
    for row in range(file_model.rowCount(root_index_model)):
        _model_index = file_model.index(row, col, root_index_model)
        if _model_index.data() != root_dirname:
            dirtree.setRowHidden(row, root_index_model, True)


if not top_dir:
    dirtree = QLabel('select project')
    dirtree.setAlignment(Qt.AlignmentFlag.AlignCenter)
else:
    root_path, root_dirname = os.path.split(top_dir)
    file_model = QFileSystemModel()

    file_model.directoryLoaded.connect(loaded)

    root_index_model = file_model.setRootPath(root_path)

    dirtree = QTreeView()

    dirtree.setUniformRowHeights(True)
    dirtree.setHeaderHidden(True)
    dirtree.setModel(file_model)

    dirtree.hideColumn(1)
    dirtree.hideColumn(2)
    dirtree.hideColumn(3)

    dirtree.setRootIndex(root_index_model)

    vertical_scrollbar = dirtree.verticalScrollBar()

    vertical_scrollbar.setStyleSheet(
        load_qss('dirtree_scrollbar.qss')
    )


dirtree.setStyleSheet(
    load_qss('content_left_dirtree.qss')
)
