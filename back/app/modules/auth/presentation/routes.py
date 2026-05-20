from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.database import get_db
from app.modules.auth.infrastructure.repository_sql import AuthRepositorySQL
from app.modules.auth.application.use_cases.login import LoginUseCase
from app.modules.auth.application.use_cases.register import RegisterUseCase

from app.modules.auth.application.dto import LoginRequest

router = APIRouter(prefix="/auth", tags=["auth"])

def get_repo(db=Depends(get_db)):
    return AuthRepositorySQL(db)

@router.post("/login")
def login(payload: LoginRequest, repo=Depends(get_repo)):
    use_case = LoginUseCase(repo)
    return use_case.execute(payload.email, payload.password)

@router.post("/register")
def register(payload: LoginRequest, repo=Depends(get_repo)):
    use_case = RegisterUseCase(repo)
    return use_case.execute(payload.login, payload.email, payload.password)
    