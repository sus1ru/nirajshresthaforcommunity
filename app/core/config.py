# app/core/config.py

from pydantic_settings import BaseSettings
from pydantic import Field, computed_field
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str = "Portfolio API"
    API_V1_PREFIX: str = "/api"

    ADMIN_TOKEN: str

    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int = 5432

    DATABASE_URL: str | None = None

    SECRET_KEY: str = "change-this-super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    MEDIA_DIR: str = "app/static/uploads"

    class Config:
        env_file = ".env"
        extra = "ignore"

    @computed_field
    @property
    def database_url(self) -> str:
        """
        Builds async database URL if DATABASE_URL not provided.
        """
        if self.DATABASE_URL:
            return self.DATABASE_URL

        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()