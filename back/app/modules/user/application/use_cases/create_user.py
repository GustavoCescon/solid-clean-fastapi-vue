from app.core.errors.base import AppException
from app.modules.user.domain.entities import User
from app.modules.user.domain.repository import UserRepository
from app.modules.user.domain.ports.email_service import EmailService
from app.modules.user.domain.services.user_validator import UserValidator
from app.modules.user.infrastructure.mapper import UserMapper


class CreateUserUseCase:

    def __init__(self, repo: UserRepository, email_service: EmailService = None):
        self.repo = repo
        self.email_service = email_service
        self.validator = UserValidator(repo)

    def execute(self, name: str, lastName: str, cpf: str):
        self.validator.validate_for_creation(name, lastName, cpf)
        user = User(None, name, lastName, cpf)
        created = self.repo.create(user)
        return UserMapper.to_response(created)