from fastapi import FastAPI
from app.core.database import Base, engine
from app.core.cors import add_cors
from app.modules.user.presentation.routes import router as user_router
from app.modules.auth.presentation.routes import router as auth_router

from app.core.errors.handlers import app_exception_handler, value_error_handler
from app.core.errors.base import AppException

Base.metadata.create_all(bind=engine)

app = FastAPI()

add_cors(app)

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(ValueError, value_error_handler)

app.include_router(auth_router)
app.include_router(user_router)