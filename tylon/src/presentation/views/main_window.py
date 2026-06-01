from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton

from tylon.src.presentation.widgets.toolbar import TopToolbar
from tylon.src.presentation.widgets.vault_widget import VaultWidget
from PySide6.QtCore import Qt

with open(".\\tylon\\src\\presentation\\styles\\window.qss") as f:
    style = f.read()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(style)
        self.resize(800, 600)
        self.setWindowTitle("Tylon")

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        central_widget = QWidget()
        central_widget.setObjectName("window")
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        toolbar = TopToolbar()
        toolbar.close_button.pressed.connect(self.close)
        toolbar.minimize_button.pressed.connect(self.showMinimized)
        main_layout.addWidget(toolbar)

        main_layout.addStretch()

        vw = VaultWidget()

        main_layout.addWidget(vw)

        main_layout.addStretch()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self._drag_pos:
            delta = event.globalPosition().toPoint() - self._drag_pos
            self.move(self.pos() + delta)
            self._drag_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None

    def center(self):
        screen = self.screen().availableGeometry()
        frame = self.frameGeometry()
        frame.moveCenter(screen.center())
        self.move(frame.topLeft())
