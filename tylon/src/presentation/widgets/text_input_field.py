from PySide6.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout


class InputText(QWidget):
    def __init__(self, title: str, info_text: str = "") -> None:
        super().__init__()
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.addStretch()
        self.lineedit = QLineEdit()
        self.title = QLabel(title)
        self.info = QLabel(info_text)

        main_layout.addWidget(self.title)
        main_layout.addWidget(self.lineedit)
        main_layout.addWidget(self.info)

    def set_info_text(self, text: str):
        self.info.setText(text)

    def text(self):
        return self.lineedit.text()
