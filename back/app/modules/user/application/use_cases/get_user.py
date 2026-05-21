from app.core.errors.base import AppException
from app.modules.user.infrastructure.mapper import UserMapper


class GetUserUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, user_id: int):
        user = self.repo.get_by_id(user_id)

        if not user:
            raise AppException("User not found", 404)

        return UserMapper.to_response(user)