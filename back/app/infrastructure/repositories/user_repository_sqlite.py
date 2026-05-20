from sqlalchemy.orm import Session
from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User
from app.infrastructure.db.models import UserModel

class UserRepositorySQLite(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User):
        db_user = UserModel(name=user.name, email=user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User(db_user.id, db_user.name, db_user.email)

    def get_all(self):
        return [
            User(u.id, u.name, u.email)
            for u in self.db.query(UserModel).all()
        ]

    def get_by_id(self, user_id: int):
        u = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        return User(u.id, u.name, u.email) if u else None

    def update(self, user: User):
        db_user = self.db.query(UserModel).filter(UserModel.id == user.id).first()
        db_user.name = user.name
        db_user.email = user.email
        self.db.commit()
        return user

    def delete(self, user_id: int):
        self.db.query(UserModel).filter(UserModel.id == user_id).delete()
        self.db.commit()