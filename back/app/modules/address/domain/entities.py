from dataclasses import dataclass
from datetime import datetime


@dataclass
class Address:
    id: int | None
    user_id: int
    street: str
    number: str
    neighborhood: str
    city: str
    state: str
    zip_code: str
    complement: str | None = None
    created_at: datetime | None = None

    def __post_init__(self):
        if not self.street:
            raise ValueError("street is required")
        if not self.number:
            raise ValueError("number is required")
        if not self.neighborhood:
            raise ValueError("neighborhood is required")
        if not self.city:
            raise ValueError("city is required")
        if not self.state:
            raise ValueError("state is required")
        if not self.zip_code:
            raise ValueError("zip_code is required")
