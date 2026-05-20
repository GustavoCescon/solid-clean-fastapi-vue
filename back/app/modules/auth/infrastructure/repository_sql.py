from app.modules.auth.domain.repository import AuthRepository
from app.modules.auth.infrastructure.models import AuthModel

class AuthRepositorySQL(AuthRepository):

    def __init__(self, db):
        self.db = db

    def find_by_email(self, email: str):
        return self.db.query(AuthModel).filter(AuthModel.email == email).first()

    def create_auth(self, login: str | None, email: str, password: str):
        user = AuthModel(
            login=login,
            email=email,
            password=password
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user