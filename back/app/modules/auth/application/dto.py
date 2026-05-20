from pydantic import BaseModel

class LoginRequest(BaseModel):
    login: str | None = None
    email: str
    password: str