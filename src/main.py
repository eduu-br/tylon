from src.bootstrap.init_app import init
from src.infrastructure.database.connection import get_connection, close_connection
from src.domain.entities.credential import Credential
from datetime import datetime
from src.infrastructure.database.repositories.credential_repository import (
    SQLiteCredentialRepository,
)
from PySide6.QtWidgets import QApplication
from src.presentation.views.main_window import MainWindow
from src.presentation.views.login_window import LoginWindow
from src.presentation.viewmodels.login_viewmodel import LoginViewmodel

init()

app = QApplication()
connection = get_connection()

login_vm = LoginViewmodel()
main_window = LoginWindow(login_vm)

main_window.show()
app.exec()


close_connection()
