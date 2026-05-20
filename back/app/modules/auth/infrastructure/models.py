from app.core.database import Base
from sqlalchemy import Column, Integer, String

class AuthModel(Base):
    __tablename__ = "auth_users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)