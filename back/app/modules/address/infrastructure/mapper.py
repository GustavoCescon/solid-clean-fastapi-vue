from app.modules.address.domain.entities import Address
from app.modules.address.infrastructure.models import AddressModel


class AddressMapper:

    @staticmethod
    def to_entity(model: AddressModel) -> Address:
        return Address(
            id=model.id,
            user_id=model.user_id,
            street=model.street,
            number=model.number,
            neighborhood=model.neighborhood,
            city=model.city,
            state=model.state,
            zip_code=model.zip_code,
            complement=model.complement,
            created_at=model.created_at,
        )

    @staticmethod
    def to_model(entity: Address) -> AddressModel:
        return AddressModel(
            user_id=entity.user_id,
            street=entity.street,
            number=entity.number,
            neighborhood=entity.neighborhood,
            city=entity.city,
            state=entity.state,
            zip_code=entity.zip_code,
            complement=entity.complement,
        )

    @staticmethod
    def to_response(entity: Address) -> dict:
        zc = entity.zip_code
        masked_zip = f"{zc[:5]}-{zc[5:]}" if zc and len(zc) == 8 else zc
        return {
            "id": entity.id,
            "user_id": entity.user_id,
            "street": entity.street,
            "number": entity.number,
            "neighborhood": entity.neighborhood,
            "city": entity.city,
            "state": entity.state,
            "zip_code": masked_zip,
            "complement": entity.complement,
        }
