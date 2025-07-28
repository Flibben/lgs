import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = os.getenv("APP_ENV", "development")
    database_url: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./app.db")
    secret_key: str = os.getenv("SECRET_KEY", "test-secret")
    jwt_secret: str = os.getenv("JWT_SECRET", "test-jwt-secret")


def get_settings() -> Settings:
    return Settings()
