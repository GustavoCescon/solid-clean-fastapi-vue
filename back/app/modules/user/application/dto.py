import re
from pydantic import BaseModel, field_validator


class CreateUserDTO(BaseModel):
    name: str
    lastName: str
    cpf: str

    @field_validator("cpf")
    @classmethod
    def cpf_format(cls, v: str) -> str:
        digits = re.sub(r"\D", "", v)
        if len(digits) != 11:
            raise ValueError("CPF must have 11 digits")
        return v