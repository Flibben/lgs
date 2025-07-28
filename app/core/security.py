from fastapi_users.authentication import JWTStrategy
from fastapi_users.password import PasswordHelper
from app.core.config import get_settings

settings = get_settings()

SECRET = settings.jwt_secret

password_helper = PasswordHelper()

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600) 