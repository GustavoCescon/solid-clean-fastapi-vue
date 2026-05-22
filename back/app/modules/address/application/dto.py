from pydantic import BaseModel


class CreateAddressDTO(BaseModel):
    street: str
    number: str
    neighborhood: str
    city: str
    state: str
    zip_code: str
    complement: str | None = None
