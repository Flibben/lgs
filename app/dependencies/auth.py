from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, CookieTransport
from app.models.user import User
from app.core.security import get_jwt_strategy
from app.db.session import AsyncSessionLocal
from fastapi_users.db import SQLAlchemyUserDatabase

cookie_transport = CookieTransport(cookie_name="auth", cookie_max_age=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

async def get_user_db():
    async with AsyncSessionLocal() as session:
        yield SQLAlchemyUserDatabase(session, User)

fastapi_users = FastAPIUsers[User, str](
    get_user_db,
    [auth_backend],
) 