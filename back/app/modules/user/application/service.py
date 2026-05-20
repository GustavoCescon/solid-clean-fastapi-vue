from app.modules.user.domain.repository import UserRepository
from app.modules.user.domain.entities import User
from app.core.errors.base import AppException

class UserService:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create(self, name: str, lastName: str):

        if len(name) < 3:
            raise AppException("Name too short", 400)

        if len(lastName) < 3:
            raise AppException("Last name too short", 400)

        return self.repo.create(User(None, name, lastName))

    def list(self):
        user = self.repo.list()
        if not user:
            raise AppException("No users found", 404)
        return user
    
    def get(self, id: int):
        user = self.repo.get_by_id(id)

        if not user:
            raise AppException("User not found", 404)

        return user