"""
读取个性化配置
"""
from PyQt6.QtWidgets import QBoxLayout


def middle_oat():
    from pye.content.content_middle.oat.oat_settings import oat_setting_default, oat_setting_model_default

    middle_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
    middle_layout.setContentsMargins(0, 0, 0, 0)
    middle_layout.setSpacing(0)
