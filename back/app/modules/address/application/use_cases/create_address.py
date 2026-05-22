from app.modules.address.domain.entities import Address
from app.modules.address.domain.repository import AddressRepository
from app.modules.address.domain.services.address_validator import AddressValidator
from app.modules.address.infrastructure.mapper import AddressMapper


class CreateAddressUseCase:

    def __init__(self, repo: AddressRepository):
        self.repo = repo
        self.validator = AddressValidator()

    def execute(self, user_id: int, street: str, number: str, neighborhood: str,
                city: str, state: str, zip_code: str, complement: str | None = None):
        self.validator.validate(street, number, neighborhood, city, state, zip_code)
        address = Address(
            id=None,
            user_id=user_id,
            street=street,
            number=number,
            neighborhood=neighborhood,
            city=city,
            state=state.upper(),
            zip_code="".join(filter(str.isdigit, zip_code)),
            complement=complement,
        )
        created = self.repo.create(address)
        return AddressMapper.to_response(created)
