from abc import ABC, abstractmethod
from app.modules.user.domain.entities import User
from app.modules.user.domain.specifications.user_spec import UserSpecification


class UserRepository(ABC):

    @abstractmethod
    def create(self, user: User): ...

    @abstractmethod
    def update(self, user: User): ...

    @abstractmethod
    def list(self, skip: int = 0, limit: int = 10): ...

    @abstractmethod
    def count(self) -> int: ...

    @abstractmethod
    def get_by_id(self, user_id: int): ...

    @abstractmethod
    def delete(self, user_id: int): ...

    @abstractmethod
    def exists(self, spec: UserSpecification) -> bool: ...