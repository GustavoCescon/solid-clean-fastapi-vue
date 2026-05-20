from app.core.errors.base import AppException
from app.core.security.security import create_access_token

class LoginUseCase:

    def __init__(self, auth_repo):
        self.auth_repo = auth_repo

    def execute(self, email: str, password: str):

        user = self.auth_repo.find_by_email(email)

        if not user:
            raise AppException("Invalid credentials", 401)

        # depois entra hash aqui
        if user.password != password:
            raise AppException("Invalid credentials", 401)

        token = create_access_token({"sub": str(user.id)})

        return {"access_token": token}