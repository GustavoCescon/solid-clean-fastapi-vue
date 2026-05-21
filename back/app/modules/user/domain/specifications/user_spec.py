from abc import ABC, abstractmethod


class UserSpecification(ABC):

    @abstractmethod
    def to_query(self) -> dict: ...


class UniqueCPFSpecification(UserSpecification):

    def __init__(self, cpf: str, exclude_id: int | None = None):
        self.cpf = cpf
        self.exclude_id = exclude_id

    def to_query(self) -> dict:
        return {"cpf": self.cpf, "exclude_id": self.exclude_id}
