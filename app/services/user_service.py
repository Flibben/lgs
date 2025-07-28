import uuid
from typing import Any, AsyncGenerator

from fastapi_users.manager import BaseUserManager
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from app.core.config import get_settings
from app.db.session import AsyncSessionLocal
from app.models.user import User

settings = get_settings()


class UserManager(BaseUserManager[User, uuid.UUID]):  # type: ignore[misc]
    reset_password_token_secret = settings.secret_key
    verification_token_secret = settings.secret_key

    async def on_after_register(self, user: User, request: Any = None) -> None:
        pass  # You can add custom logic here

    def parse_id(self, value: Any) -> uuid.UUID:
        if isinstance(value, uuid.UUID):
            return value
        return uuid.UUID(str(value))


async def get_user_manager() -> AsyncGenerator[UserManager, None]:
    async with AsyncSessionLocal() as session:
        yield UserManager(SQLAlchemyUserDatabase(session, User))
