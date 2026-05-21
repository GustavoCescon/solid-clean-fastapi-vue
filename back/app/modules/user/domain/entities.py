import re
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int | None
    name: str
    lastName: str
    cpf: str | None = None
    createdAt: datetime | None = None

    def __post_init__(self):
        if not self.name:
            raise ValueError("name is required")
        if not self.lastName:
            raise ValueError("lastName is required")
        if self.cpf is not None:
            self.cpf = self._strip_cpf(self.cpf)
            if not self._is_valid_cpf(self.cpf):
                raise ValueError("Invalid CPF")

    @staticmethod
    def _strip_cpf(cpf: str) -> str:
        return re.sub(r"\D", "", cpf)

    @staticmethod
    def _is_valid_cpf(cpf: str) -> bool:
        if len(cpf) != 11 or len(set(cpf)) == 1:
            return False
        for i in range(9, 11):
            total = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digit = (total * 10 % 11) % 10
            if digit != int(cpf[i]):
                return False
        return True
