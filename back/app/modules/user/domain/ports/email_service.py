# domain/ports/email_service.py
from abc import ABC, abstractmethod

class EmailService(ABC):

    @abstractmethod
    def send_welcome(self, email: str, name: str): ...