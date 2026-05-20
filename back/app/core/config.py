import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "dev"

    DATABASE_URL: str = "sqlite:///./dev.db"

    class Config:
        env_file = f".env.{os.getenv('ENV', 'dev')}"


settings = Settings()