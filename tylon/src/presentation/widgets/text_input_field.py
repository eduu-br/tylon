from PySide6.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout


class InputText(QWidget):
    def __init__(self, text: str) -> None:
        super().__init__()
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.addStretch()
        self.lineedit = QLineEdit()
        self.label = QLabel(text)

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.lineedit)

    def text(self):
        return self.lineedit.text()
