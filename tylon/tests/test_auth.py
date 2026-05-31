from tylon.src.application.use_cases.authenticate_user import AuthenticateUserUseCase

auth = AuthenticateUserUseCase()

# auth.register_user("eduardo123", "102030")

print(auth.login_user("eduardo123", "102030"))
