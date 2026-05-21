from fastapi import APIRouter, Depends
from app.core.database import get_db
from app.modules.user.infrastructure.repository_sql import UserRepositorySQL
from app.modules.user.application.use_cases.create_user import CreateUserUseCase
from app.modules.user.application.use_cases.list_users import ListUsersUseCase
from app.modules.user.application.use_cases.get_user import GetUserUseCase
from app.modules.user.application.use_cases.put_user import PutUserUseCase

from app.modules.user.application.dto import CreateUserDTO

from app.core.dependencies.auth import get_current_user

router = APIRouter(prefix="/users")
      
def get_repo(db=Depends(get_db)):
    return UserRepositorySQL(db)

@router.post("")
def create(user: CreateUserDTO, repo=Depends(get_repo)):
    use_case = CreateUserUseCase(repo)
    return use_case.execute(user.name, user.lastName, user.cpf)

@router.get("")
def list_users(page: int = 1, size: int = 10, current_user=Depends(get_current_user), repo=Depends(get_repo)):
    use_case = ListUsersUseCase(repo)
    skip = (page - 1) * size
    return use_case.execute(skip=skip, limit=size)

@router.get("/{id}")
def get_user_by_id(id: int, current_user=Depends(get_current_user), repo=Depends(get_repo)):
    use_case = GetUserUseCase(repo)
    return use_case.execute(id)

@router.put("/{id}")
def update_user(id: int, user: CreateUserDTO, current_user=Depends(get_current_user), repo=Depends(get_repo)):
    use_case = PutUserUseCase(repo)
    return use_case.execute(id, user.name, user.lastName, user.cpf)

@router.delete("/{id}")
def delete_user(id: int, current_user=Depends(get_current_user), repo=Depends(get_repo)):
    repo.delete(id)
    return {"message": "User deleted successfully"}