from PyQt6.QtWidgets import QFileDialog


file_dialog = QFileDialog()

# file_dialog.setSidebarUrls(
# )

file_dialog.setOptions(
    QFileDialog.Option.ShowDirsOnly | QFileDialog.Option.DontUseNativeDialog
)

file_dialog.setFileMode(
    QFileDialog.FileMode.Directory
)
