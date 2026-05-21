from app.modules.user.infrastructure.mapper import UserMapper


class ListUsersUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, skip: int = 0, limit: int = 10):
        items = [UserMapper.to_response(u) for u in self.repo.list(skip=skip, limit=limit)]
        total = self.repo.count()
        return {"items": items, "total": total}