from fastapi import FastAPI
import uvicorn

from app.core.config import settings
from app.core.database import Base, engine
from app.core.cors import add_cors
from app.core.routes import register_routers

from app.core.errors.handlers import (
    app_exception_handler,
    value_error_handler,
)

from app.core.errors.base import AppException


Base.metadata.create_all(bind=engine)

app = FastAPI()

add_cors(app)

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(ValueError, value_error_handler)

register_routers(app)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=True,
    )
