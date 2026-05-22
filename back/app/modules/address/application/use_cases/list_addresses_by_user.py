from app.modules.address.domain.repository import AddressRepository
from app.modules.address.infrastructure.mapper import AddressMapper


class ListAddressesByUserUseCase:

    def __init__(self, repo: AddressRepository):
        self.repo = repo

    def execute(self, user_id: int):
        addresses = self.repo.list_by_user(user_id)
        return [AddressMapper.to_response(a) for a in addresses]
