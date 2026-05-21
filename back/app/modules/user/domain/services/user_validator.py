from app.modules.user.domain.repository import UserRepository
from app.modules.user.domain.specifications.user_spec import UniqueCPFSpecification


class UserValidator:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def validate_for_creation(self, name: str, lastName: str, cpf: str):
        if not name or not lastName:
            raise ValueError("Name and last name are required")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        if len(lastName) < 3:
            raise ValueError("Last name must be at least 3 characters")
        if self.repo.exists(UniqueCPFSpecification(cpf)):
            raise ValueError("CPF already registered")

    def validate_for_update(self, user_id: int, name: str, lastName: str, cpf: str):
        if not name or not lastName:
            raise ValueError("Name and last name are required")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        if len(lastName) < 3:
            raise ValueError("Last name must be at least 3 characters")
        if self.repo.exists(UniqueCPFSpecification(cpf, exclude_id=user_id)):
            raise ValueError("CPF already registered")