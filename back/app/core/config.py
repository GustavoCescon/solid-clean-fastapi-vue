import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: str = "dev"

    DATABASE_URL: str = "sqlite:///./dev.db"

    PORT: int = 8001

    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv('ENV', 'dev')}",
        extra="forbid",
    )


settings = Settings()