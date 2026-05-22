from fastapi import FastAPI

from app.modules.user.presentation.routes import router as user_router
from app.modules.auth.presentation.routes import router as auth_router
from app.modules.address.presentation.routes import router as address_router


def register_routers(app: FastAPI) -> None:
    app.include_router(auth_router)
    app.include_router(user_router)
    app.include_router(address_router)
