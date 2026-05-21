from app.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastName = Column(String)
    cpf = Column(String, unique=True, nullable=True)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )