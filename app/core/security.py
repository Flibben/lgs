from fastapi_users.authentication import JWTStrategy
from fastapi_users.password import PasswordHelper

from app.core.config import get_settings


def get_jwt_strategy() -> JWTStrategy:
    settings = get_settings()
    return JWTStrategy(secret=settings.SECRET_KEY, lifetime_seconds=3600)


password_helper = PasswordHelper()
