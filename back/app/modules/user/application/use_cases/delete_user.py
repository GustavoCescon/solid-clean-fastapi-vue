from app.core.errors.base import AppException

class DeleteUserUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, user_id: int):
        user = self.repo.get_by_id(user_id)

        if not user:
            raise AppException("User not found", 404)

        self.repo.delete(user_id)
        return {"message": "User deleted successfully"}