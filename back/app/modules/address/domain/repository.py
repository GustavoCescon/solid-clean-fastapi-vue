from abc import ABC, abstractmethod
from app.modules.address.domain.entities import Address


class AddressRepository(ABC):

    @abstractmethod
    def create(self, address: Address) -> Address: ...

    @abstractmethod
    def update(self, address: Address) -> Address | None: ...

    @abstractmethod
    def get_by_id(self, address_id: int) -> Address | None: ...

    @abstractmethod
    def list_by_user(self, user_id: int) -> list[Address]: ...

    @abstractmethod
    def delete(self, address_id: int) -> Address | None: ...
