from PySide6.QtWidgets import QPushButton

with open("src\\presentation\\styles\\widgets.qss") as f:
    style = f.read()


class Button(QPushButton):

    def __init__(self, texto):
        super().__init__()

        self.setText(texto)
        self.setStyleSheet(style)
