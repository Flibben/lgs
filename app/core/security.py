import uuid

from fastapi_users.authentication import JWTStrategy
from fastapi_users.password import PasswordHelper

from app.core.config import get_settings
from app.models.user import User


def get_jwt_strategy() -> JWTStrategy[User, uuid.UUID]:  # type: ignore[type-var]
    settings = get_settings()
    return JWTStrategy(secret=settings.secret_key, lifetime_seconds=3600)


password_helper = PasswordHelper()
