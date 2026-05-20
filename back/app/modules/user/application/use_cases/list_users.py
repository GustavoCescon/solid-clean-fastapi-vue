class ListUsersUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, skip: int = 0, limit: int = 10):
        items = self.repo.list(skip=skip, limit=limit)
        total = self.repo.count()
        return {"items": items, "total": total}