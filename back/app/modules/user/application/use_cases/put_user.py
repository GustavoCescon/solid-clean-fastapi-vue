from app.core.errors.base import AppException
from app.modules.user.domain.entities import User
from app.modules.user.domain.repository import UserRepository
from app.modules.user.domain.services.user_validator import UserValidator

class PutUserUseCase:

    def __init__(self, repo: UserRepository):
        self.repo = repo
        self.validator = UserValidator(repo)

    def execute(self, id: int, name: str, lastName: str):
        user = self.repo.get_by_id(id)
        if not user:
            raise AppException("User not found")
        self.validator.validate_for_update(id, name, lastName)
        user.name = name
        user.lastName = lastName
        return self.repo.update(user)