from abc import ABC, abstractmethod

class AuthRepository(ABC):

    @abstractmethod
    def find_by_email(self, email: str): ...

    @abstractmethod
    def create_auth(self, login: str, email: str, password: str): ...