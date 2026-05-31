from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal


class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.clicked.emit()
        super().mousePressEvent(ev)
