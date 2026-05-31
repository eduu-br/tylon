from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout
from PySide6.QtCore import Qt, Signal
from src.presentation.widgets.buttons import Button
from src.presentation.widgets.text_input_field import InputText
from src.presentation.widgets.clickable_label import ClickableLabel
from src.presentation.viewmodels.login_viewmodel import LoginViewmodel
from src.domain.value_objects.login_return_code import AuthReturnCode
from src.domain.value_objects.auth_type import Auth

with open("src\\presentation\\styles\\login_window.qss") as f:
    style = f.read()


class LoginWindow(QWidget):

    def __init__(self, vm: LoginViewmodel):
        super().__init__()
        self.auth_type = Auth.LOGIN
        self.vm = vm

        self.setStyleSheet(style)
        self.resize(600, 400)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.title = QLabel("login for tylon")
        self.title.setObjectName("title")
        main_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.input_username = InputText("username")
        self.input_username.lineedit.returnPressed.connect(self.on_return1)

        self.input_username.lineedit.setProperty("state", "ok")
        self.input_username.setMinimumWidth(250)
        main_layout.addWidget(
            self.input_username,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter,
        )

        self.input_password = InputText("password")
        self.input_password.setMinimumWidth(250)
        self.input_password.lineedit.setProperty("state", "ok")
        self.input_password.lineedit.returnPressed.connect(self.on_auth_pressed)
        self.input_password.lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        main_layout.addWidget(
            self.input_password,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter,
        )

        self.auth_button = Button("login")
        self.auth_button.setMinimumWidth(235)
        self.auth_button.setFixedHeight(30)
        main_layout.addWidget(self.auth_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.cancel_button = Button("cancel")
        self.cancel_button.setMinimumWidth(235)
        self.cancel_button.setMinimumHeight(30)
        self.cancel_button.setObjectName("cancel")
        main_layout.addWidget(
            self.cancel_button, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.cancel_button.pressed.connect(self.on_cancel)
        self.cancel_button.hide()

        self.create_acc_container = QWidget()
        create_acc_container_layout = QHBoxLayout()
        self.create_acc_container.setLayout(create_acc_container_layout)

        no_account_label = QLabel("don't have an account?")
        create_acc_container_layout.addWidget(no_account_label)

        create_account_link = ClickableLabel("Register")
        create_account_link.setObjectName("register")
        create_account_link.clicked.connect(self.on_register)
        create_acc_container_layout.addWidget(create_account_link)

        main_layout.addWidget(
            self.create_acc_container, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.auth_button.pressed.connect(self.on_auth_pressed)

        main_layout.addStretch()

    def on_cancel(self):
        self.cancel_button.hide()
        self.title.setText("login for tylon")
        self.auth_button.setText("login")
        self.create_acc_container.show()
        self.auth_type = Auth.LOGIN

    def on_return1(self):
        self.input_password.lineedit.setCursorPosition(
            len(self.input_password.lineedit.text())
        )
        self.input_password.lineedit.setFocus()

    def on_register(self):
        self.auth_type = Auth.REGISTER
        self.title.setText("register for tylon")
        self.auth_button.setText("register")
        self.cancel_button.show()
        self.create_acc_container.hide()

    def on_auth_pressed(self):
        username = self.input_username.text()
        password = self.input_password.text()

        code = self.vm.auth(self.auth_type, username, password)

        match code:
            case AuthReturnCode.SUCCESSFUL:
                self.input_username.lineedit.setProperty("state", "ok")
                self.input_username.lineedit.style().unpolish(
                    self.input_username.lineedit
                )
                self.input_username.lineedit.style().polish(
                    self.input_username.lineedit
                )
                self.input_username.lineedit.update()

                self.input_password.lineedit.setProperty("state", "ok")
                self.input_password.lineedit.style().unpolish(
                    self.input_password.lineedit
                )
                self.input_password.lineedit.style().polish(
                    self.input_password.lineedit
                )
                self.input_password.lineedit.update()
            case AuthReturnCode.INVALID_USERNAME:
                self.input_username.lineedit.setProperty("state", "error")
                self.input_username.lineedit.style().unpolish(
                    self.input_username.lineedit
                )
                self.input_username.lineedit.style().polish(
                    self.input_username.lineedit
                )
                self.input_username.lineedit.update()
            case AuthReturnCode.INVALID_PASSWORD:
                self.input_password.lineedit.setProperty("state", "error")
                self.input_password.lineedit.style().unpolish(
                    self.input_password.lineedit
                )
                self.input_password.lineedit.style().polish(
                    self.input_password.lineedit
                )
                self.input_password.lineedit.update()
        print("aaaaa")
