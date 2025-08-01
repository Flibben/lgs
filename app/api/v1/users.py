from fastapi import APIRouter
from fastapi.routing import APIRouter as FastAPIRouter

from app.dependencies.auth import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

router: FastAPIRouter = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
