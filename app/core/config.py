from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):  # type: ignore[misc]
    app_env: str = "development"
    database_url: str
    secret_key: str
    jwt_secret: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
