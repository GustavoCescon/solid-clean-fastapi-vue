from app.modules.user.domain.entities import User
from app.modules.user.infrastructure.models import UserModel


class UserMapper:

    @staticmethod
    def to_entity(model: UserModel) -> User:
        return User(
            id=model.id,
            name=model.name,
            lastName=model.lastName,
            cpf=model.cpf,
        )

    @staticmethod
    def to_model(entity: User) -> UserModel:
        return UserModel(
            name=entity.name,
            lastName=entity.lastName,
            cpf=entity.cpf,
        )

    @staticmethod
    def to_response(entity: User) -> dict:
        cpf = entity.cpf
        masked = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if cpf and len(cpf) == 11 else cpf
        return {
            "id": entity.id,
            "name": entity.name,
            "lastName": entity.lastName,
            "cpf": masked,
        }