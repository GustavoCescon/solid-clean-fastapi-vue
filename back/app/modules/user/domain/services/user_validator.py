# domain/services/user_validator.py
from app.modules.user.domain.repository import UserRepository

class UserValidator:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def validate_for_creation(self, name: str, lastName: str):
        if not name or not lastName:
            raise ValueError("Name and last name are required")
        if len(name) < 3:
            raise ValueError("Name must be than 3 characters")
        if len(lastName) < 3:
            raise ValueError("Last name must be than 3 characters")
        
    def validate_for_update(self, user_id: int, name: str, lastName: str):
        if not name or not lastName:
            raise ValueError("Name and last name are required")
        if len(name) < 3:
            raise ValueError("Name must be than 3 characters")
        if len(lastName) < 3:
            raise ValueError("Last name must be than 3 characters")