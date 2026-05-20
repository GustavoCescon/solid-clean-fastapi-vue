from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int | None
    name: str
    lastName: str
    createdAt: datetime | None = None
    
    def __post_init__(self):
        if not self.name:
            raise ValueError("name is required")
        if not self.lastName:
            raise ValueError("lastName is required")
