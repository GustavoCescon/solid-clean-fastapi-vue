from app.core.errors.base import AppException
from app.modules.user.domain.entities import User
from app.modules.user.domain.repository import UserRepository
from app.modules.user.domain.ports.email_service import EmailService
from app.modules.user.domain.services.user_validator import UserValidator

class CreateUserUseCase:

    def __init__(self, repo: UserRepository, email_service: EmailService = None):
        self.repo = repo
        self.email_service = email_service
        self.validator = UserValidator(repo)
        
    def execute(self, name: str, lastName: str):
        self.validator.validate_for_creation(name, lastName)
        user = User(None, name, lastName)
        created = self.repo.create(user)
        # self.email_service.send_welcome(user.email, user.name)
        return created