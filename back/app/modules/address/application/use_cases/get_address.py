from app.core.errors.base import AppException
from app.modules.address.domain.repository import AddressRepository
from app.modules.address.infrastructure.mapper import AddressMapper


class GetAddressUseCase:

    def __init__(self, repo: AddressRepository):
        self.repo = repo

    def execute(self, address_id: int):
        address = self.repo.get_by_id(address_id)
        if not address:
            raise AppException("Address not found", 404)
        return AddressMapper.to_response(address)
