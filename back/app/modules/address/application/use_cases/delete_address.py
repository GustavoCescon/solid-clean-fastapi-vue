from app.core.errors.base import AppException
from app.modules.address.domain.repository import AddressRepository


class DeleteAddressUseCase:

    def __init__(self, repo: AddressRepository):
        self.repo = repo

    def execute(self, address_id: int):
        address = self.repo.get_by_id(address_id)
        if not address:
            raise AppException("Address not found", 404)
        self.repo.delete(address_id)
        return {"message": "Address deleted successfully"}
