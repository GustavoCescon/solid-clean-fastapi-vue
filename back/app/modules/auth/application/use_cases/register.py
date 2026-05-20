from app.core.errors.base import AppException

class RegisterUseCase:

    def __init__(self, auth_repo):
        self.auth_repo = auth_repo

    def execute(self, login: str | None, email: str, password: str):

        if self.auth_repo.find_by_email(email):
            raise AppException("Email already exists", 409)

        return self.auth_repo.create_auth(login, email, password)