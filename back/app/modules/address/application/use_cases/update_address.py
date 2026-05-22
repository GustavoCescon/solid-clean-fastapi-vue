from app.core.errors.base import AppException
from app.modules.address.domain.entities import Address
from app.modules.address.domain.repository import AddressRepository
from app.modules.address.domain.services.address_validator import AddressValidator
from app.modules.address.infrastructure.mapper import AddressMapper


class UpdateAddressUseCase:

    def __init__(self, repo: AddressRepository):
        self.repo = repo
        self.validator = AddressValidator()

    def execute(self, address_id: int, user_id: int, street: str, number: str,
                neighborhood: str, city: str, state: str, zip_code: str,
                complement: str | None = None):
        existing = self.repo.get_by_id(address_id)
        if not existing:
            raise AppException("Address not found", 404)
        self.validator.validate(street, number, neighborhood, city, state, zip_code)
        updated = Address(
            id=address_id,
            user_id=user_id,
            street=street,
            number=number,
            neighborhood=neighborhood,
            city=city,
            state=state.upper(),
            zip_code="".join(filter(str.isdigit, zip_code)),
            complement=complement,
        )
        result = self.repo.update(updated)
        return AddressMapper.to_response(result)
