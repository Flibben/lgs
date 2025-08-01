import uuid

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport

from app.core.security import get_jwt_strategy
from app.models.user import User
from app.services.user_service import get_user_manager

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(  # type: ignore[type-var]
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](  # type: ignore[type-var]
    get_user_manager,
    [auth_backend],
)
