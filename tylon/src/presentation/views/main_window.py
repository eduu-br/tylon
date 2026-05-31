from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from tylon.src.presentation.widgets.buttons import Button

with open(".\\src\\presentation\\styles\\main_window.qss") as f:
    style = f.read()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(style)

        cw = QWidget()
        self.setCentralWidget(cw)
        main_layout = QVBoxLayout()
        cw.setLayout(main_layout)

        main_layout.addWidget(Button("texto"))
