from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
)
from tylon.src.presentation.viewmodels.auth_viewmodel import AuthViewmodel
from tylon.src.presentation.widgets.clickable_label import ClickableLabel
from tylon.src.application.enums.auth_return_code import AuthReturnCode
from tylon.src.presentation.widgets.text_input_field import InputText
from tylon.src.presentation.viewmodels.auth_mode import AuthMode
from PySide6.QtCore import Qt, Signal

with open(".\\tylon\\src\\presentation\\styles\\window.qss") as f:
    style = f.read()


class AuthWindow(QWidget):
    login_sucessful = Signal()

    def __init__(self, vm: AuthViewmodel):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Tylon")
        self.auth_mode = AuthMode.LOGIN
        self.vm = vm

        self.setStyleSheet(style)

        central_widget = QWidget(self)
        central_widget.setFixedSize(320, 350)
        central_widget.setObjectName("window")

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        toolbar_layout = QHBoxLayout()
        self.toolbar_container = QWidget()
        self.toolbar_container.setObjectName("toolbar")
        self.toolbar_container.setLayout(toolbar_layout)

        toolbar_layout.addStretch()

        minimize_button = QPushButton("-")
        minimize_button.setFixedSize(25, 25)
        minimize_button.setObjectName("minimize_button")
        minimize_button.pressed.connect(self.showMinimized)
        toolbar_layout.addWidget(minimize_button, alignment=Qt.AlignmentFlag.AlignRight)

        close_button = QPushButton("X")
        close_button.setFixedSize(25, 25)
        close_button.setObjectName("close_button")
        close_button.pressed.connect(self.close)
        toolbar_layout.addWidget(close_button, alignment=Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(self.toolbar_container)

        self.title = QLabel("login for Tylon")
        self.title.setObjectName("title")
        main_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)

        self.input_username = InputText("username")
        self.input_username.lineedit.returnPressed.connect(self.on_return1)
        self.input_username.info.setObjectName("info")
        self.input_username.lineedit.setProperty("state", "ok")
        self.input_username.setMinimumWidth(250)

        main_layout.addWidget(
            self.input_username,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        self.input_password = InputText("password")
        self.input_password.info.setObjectName("info")
        self.input_password.setMinimumWidth(250)
        self.input_password.lineedit.setProperty("state", "ok")
        self.input_password.lineedit.returnPressed.connect(self.on_auth_pressed)
        self.input_password.lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        main_layout.addWidget(
            self.input_password,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        self.input_username.info.hide()
        self.input_password.info.hide()

        self.auth_button = QPushButton("login")
        self.auth_button.setMinimumWidth(235)
        self.auth_button.setFixedHeight(30)
        main_layout.addWidget(self.auth_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.cancel_button = QPushButton("cancel")
        self.cancel_button.setMinimumWidth(235)
        self.cancel_button.setMinimumHeight(30)
        self.cancel_button.setObjectName("cancel")
        main_layout.addWidget(
            self.cancel_button, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.cancel_button.pressed.connect(self.show_login)
        self.cancel_button.hide()

        self.create_acc_container = QWidget()
        create_acc_container_layout = QHBoxLayout()
        self.create_acc_container.setLayout(create_acc_container_layout)

        no_account_label = QLabel("don't have an account?")
        create_acc_container_layout.addWidget(no_account_label)

        create_account_link = ClickableLabel("Register")
        create_account_link.setObjectName("register")
        create_account_link.clicked.connect(self.show_register)
        create_acc_container_layout.addWidget(create_account_link)

        main_layout.addWidget(
            self.create_acc_container, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.auth_button.pressed.connect(self.on_auth_pressed)

        main_layout.addStretch()

    def show_login(self):
        self.cancel_button.hide()
        self.title.setText("login for Tylon")
        self.auth_button.setText("login")
        self.create_acc_container.show()
        self.auth_mode = AuthMode.LOGIN

    def on_return1(self):
        self.input_password.lineedit.setCursorPosition(
            len(self.input_password.lineedit.text())
        )
        self.input_password.lineedit.setFocus()

    def set_error_input(self, input: InputText, err_msg: str):
        input.lineedit.setProperty("state", "error")
        input.lineedit.style().unpolish(input.lineedit)
        input.lineedit.style().polish(input.lineedit)
        input.lineedit.update()

        input.set_info_text(err_msg)
        input.info.show()

    def set_ok_input(self, input: InputText):
        input.lineedit.setProperty("state", "ok")
        input.lineedit.style().unpolish(input.lineedit)
        input.lineedit.style().polish(input.lineedit)
        input.lineedit.update()

        input.info.hide()

    def show_register(self):
        self.input_username.lineedit.clear()
        self.input_password.lineedit.clear()

        self.set_ok_input(self.input_username)
        self.set_ok_input(self.input_password)

        self.auth_mode = AuthMode.REGISTER
        self.title.setText("register for Tylon")
        self.auth_button.setText("register")
        self.cancel_button.show()
        self.create_acc_container.hide()

    # todo: arrumar isso aqui
    def on_auth_pressed(self):
        username = self.input_username.text()
        password = self.input_password.text()

        code = self.vm.auth(self.auth_mode, username, password)

        if AuthReturnCode.SUCCESS in code:

            if self.auth_mode == AuthMode.REGISTER:
                self.show_login()
                self.input_username.lineedit.clear()
                self.input_password.lineedit.clear()

            self.set_ok_input(self.input_username)
            self.set_ok_input(self.input_password)

            self.login_sucessful.emit()
            self.close()
            # todo: implementar a mudança para mainwindow

            return

        if (
            AuthReturnCode.REGISTER_USERNAME_EXISTS in code
            or AuthReturnCode.INVALID_USERNAME in code
        ):
            if AuthReturnCode.REGISTER_USERNAME_EXISTS in code:
                self.set_error_input(self.input_username, "username already exists")
            else:
                self.set_error_input(self.input_username, "invalid username")
        else:
            self.set_ok_input(self.input_username)

        if AuthReturnCode.INVALID_PASSWORD in code:
            self.set_error_input(self.input_password, "invalid password")
        else:
            self.set_ok_input(self.input_password)

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
