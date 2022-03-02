import typing

from PyQt6.QtWidgets import QSizePolicy, QWidget


class NewWidget:
    widget: QWidget
    size_policy: QSizePolicy

    def __init__(
            self,
            parent=None,
            policy_h: typing.Union[QSizePolicy.Policy] = None, policy_v: typing.Union[QSizePolicy.Policy] = None,
            h: int = None, v: int = None,
            # w_margin: typing.Tuple[int, int, int, int] = None,
            # w_top_margin: int = None, w_bottom_margin: int = None,
            # w_left_margin: int = None, w_right_margin: int = None,
    ):
        # self.w_right_margin = w_right_margin
        # self.w_left_margin = w_left_margin
        # self.w_bottom_margin = w_bottom_margin
        # self.w_top_margin = w_top_margin
        # if w_margin:
        #     self.w_margin = w_margin
        # else:
        #     self.w_margin = (
        #         self.w_left_margin or 0, self.w_top_margin or 0, self.w_right_margin or 0, self.w_bottom_margin or 0
        #     )

        self.h = h
        self.v = v
        self.policy_v = policy_v
        self.policy_h = policy_h
        self.parent = parent
        self.widget = QWidget(self.parent)
        self.size_policy = QSizePolicy(self.policy_h, self.policy_v)
        self.size_policy.setHorizontalStretch(self.h)
        self.size_policy.setVerticalStretch(self.v)
        self.widget.setSizePolicy(self.size_policy)
