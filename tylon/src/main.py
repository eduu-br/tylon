from tylon.src.bootstrap.init_app import init
from tylon.src.infrastructure.database.connection import (
    get_connection,
    close_connection,
)
from tylon.src.infrastructure.database.repositories.user_repository import (
    SQLiteUserRepository,
)
from PySide6.QtWidgets import QApplication
from tylon.src.presentation.views.main_window import MainWindow
from tylon.src.presentation.views.auth_window import AuthWindow
from tylon.src.presentation.viewmodels.auth_viewmodel import AuthViewmodel
from tylon.src.infrastructure.crypto.hashing import Hasher
from tylon.src.application.session.session_manager import SessionManager

init()

app = QApplication()
connection = get_connection()

hasher = Hasher()
session_manager = SessionManager()

user_repo = SQLiteUserRepository(connection)

auth_vm = AuthViewmodel(user_repo, hasher, session_manager)
auth_window = AuthWindow(auth_vm)
main_window = MainWindow()

auth_window.login_successful.connect(main_window.show)
auth_window.login_successful.connect(main_window.center)

auth_window.show()
auth_window.center()


app.exec()


close_connection()
