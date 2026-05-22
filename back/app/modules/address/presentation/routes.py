from fastapi import APIRouter, Depends
from app.core.database import get_db
from app.core.dependencies.auth import get_current_user
from app.modules.address.infrastructure.repository_sql import AddressRepositorySQL
from app.modules.address.application.use_cases.create_address import CreateAddressUseCase
from app.modules.address.application.use_cases.list_addresses_by_user import ListAddressesByUserUseCase
from app.modules.address.application.use_cases.get_address import GetAddressUseCase
from app.modules.address.application.use_cases.update_address import UpdateAddressUseCase
from app.modules.address.application.use_cases.delete_address import DeleteAddressUseCase
from app.modules.address.application.dto import CreateAddressDTO

router = APIRouter(prefix="/users/{user_id}/addresses", tags=["addresses"])


def get_repo(db=Depends(get_db)):
    return AddressRepositorySQL(db)


@router.post("", status_code=201)
def create_address(
    user_id: int,
    body: CreateAddressDTO,
    current_user=Depends(get_current_user),
    repo=Depends(get_repo),
):
    use_case = CreateAddressUseCase(repo)
    return use_case.execute(
        user_id=user_id,
        street=body.street,
        number=body.number,
        neighborhood=body.neighborhood,
        city=body.city,
        state=body.state,
        zip_code=body.zip_code,
        complement=body.complement,
    )


@router.get("")
def list_addresses(
    user_id: int,
    current_user=Depends(get_current_user),
    repo=Depends(get_repo),
):
    use_case = ListAddressesByUserUseCase(repo)
    return use_case.execute(user_id)


@router.get("/{address_id}")
def get_address(
    user_id: int,
    address_id: int,
    current_user=Depends(get_current_user),
    repo=Depends(get_repo),
):
    use_case = GetAddressUseCase(repo)
    return use_case.execute(address_id)


@router.put("/{address_id}")
def update_address(
    user_id: int,
    address_id: int,
    body: CreateAddressDTO,
    current_user=Depends(get_current_user),
    repo=Depends(get_repo),
):
    use_case = UpdateAddressUseCase(repo)
    return use_case.execute(
        address_id=address_id,
        user_id=user_id,
        street=body.street,
        number=body.number,
        neighborhood=body.neighborhood,
        city=body.city,
        state=body.state,
        zip_code=body.zip_code,
        complement=body.complement,
    )


@router.delete("/{address_id}")
def delete_address(
    user_id: int,
    address_id: int,
    current_user=Depends(get_current_user),
    repo=Depends(get_repo),
):
    use_case = DeleteAddressUseCase(repo)
    return use_case.execute(address_id)
