from app.modules.user.domain.entities import User
from app.modules.user.infrastructure.models import UserModel

class UserMapper:

    @staticmethod
    def to_entity(model: UserModel):
        return User(
            id=model.id,
            name=model.name,
            lastName=model.lastName
        )

    @staticmethod
    def to_model(entity: User):
        return UserModel(
            name=entity.name,
            lastName=entity.lastName
        )