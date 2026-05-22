from app.modules.address.domain.repository import AddressRepository
from app.modules.address.domain.entities import Address
from app.modules.address.infrastructure.models import AddressModel
from app.modules.address.infrastructure.mapper import AddressMapper


class AddressRepositorySQL(AddressRepository):

    def __init__(self, db):
        self.db = db

    def create(self, address: Address) -> Address:
        model = AddressMapper.to_model(address)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return AddressMapper.to_entity(model)

    def update(self, address: Address) -> Address | None:
        model = self.db.query(AddressModel).filter(AddressModel.id == address.id).first()
        if model:
            model.street = address.street
            model.number = address.number
            model.neighborhood = address.neighborhood
            model.city = address.city
            model.state = address.state
            model.zip_code = address.zip_code
            model.complement = address.complement
            self.db.commit()
            self.db.refresh(model)
        return AddressMapper.to_entity(model) if model else None

    def get_by_id(self, address_id: int) -> Address | None:
        model = self.db.query(AddressModel).filter(AddressModel.id == address_id).first()
        return AddressMapper.to_entity(model) if model else None

    def list_by_user(self, user_id: int) -> list[Address]:
        models = (
            self.db.query(AddressModel)
            .filter(AddressModel.user_id == user_id)
            .order_by(AddressModel.created_at.desc())
            .all()
        )
        return [AddressMapper.to_entity(m) for m in models]

    def delete(self, address_id: int) -> Address | None:
        model = self.db.query(AddressModel).filter(AddressModel.id == address_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()
        return AddressMapper.to_entity(model) if model else None
