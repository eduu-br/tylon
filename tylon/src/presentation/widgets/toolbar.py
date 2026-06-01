from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication
from PySide6.QtCore import Qt


class TopToolbar(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
QPushButton {
    background-color: #2C2B3C;
    font-family: sans-serif;
    font-weight: bold;
    color: #fff;
    padding: 2px;
    margin: 0;
}
QPushButton::hover {
    background-color: #21202d;        
}
#close::hover {
    background-color: red;
}                           
""")

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.main_layout.addStretch()

        self.minimize_button = QPushButton("—")
        self.minimize_button.setFixedSize(25, 25)
        self.main_layout.addWidget(
            self.minimize_button,
        )

        self.close_button = QPushButton("⨉")
        self.close_button.setFixedSize(25, 25)
        self.close_button.setObjectName("close")
        self.main_layout.addWidget(
            self.close_button,
        )
