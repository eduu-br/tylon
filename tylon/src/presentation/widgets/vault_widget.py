from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

with open(".\\tylon\\src\\presentation\\styles\\widgets.qss") as f:
    style = f.read()


class VaultWidget(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet(style)
        self.setObjectName("vault_widget")

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        title = QLabel("insert text")
        main_layout.addWidget(title)

        aa = QPushButton("aaa")
        main_layout.addWidget(aa)
