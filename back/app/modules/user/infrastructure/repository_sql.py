from app.modules.user.domain.repository import UserRepository
from app.modules.user.domain.specifications.user_spec import UserSpecification
from app.modules.user.infrastructure.models import UserModel
from app.modules.user.infrastructure.mapper import UserMapper

from app.modules.user.domain.entities import User


class UserRepositorySQL(UserRepository):

    def __init__(self, db):
        self.db = db

    def create(self, user):
        model = UserMapper.to_model(user)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return UserMapper.to_entity(model)

    def list(self, skip: int = 0, limit: int = 10):
        return [
            UserMapper.to_entity(u)
            for u in self.db.query(UserModel).order_by(UserModel.created_at.desc()).offset(skip).limit(limit).all()
        ]

    def count(self) -> int:
        return self.db.query(UserModel).count()

    def get_by_id(self, user_id: int):
        model = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        return UserMapper.to_entity(model) if model else None

    def update(self, user: User):
        model = self.db.query(UserModel).filter(UserModel.id == user.id).first()
        if model:
            model.name = user.name
            model.lastName = user.lastName
            model.cpf = user.cpf
            self.db.commit()
            self.db.refresh(model)
        return UserMapper.to_entity(model) if model else None

    def delete(self, user_id: int):
        model = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()
        return UserMapper.to_entity(model) if model else None

    def exists(self, spec: UserSpecification) -> bool:
        params = spec.to_query()
        query = self.db.query(UserModel)
        if "cpf" in params:
            query = query.filter(UserModel.cpf == params["cpf"])
        if params.get("exclude_id") is not None:
            query = query.filter(UserModel.id != params["exclude_id"])
        return query.first() is not None