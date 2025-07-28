import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):  # type: ignore[misc]
    pass


class UserCreate(schemas.BaseUserCreate):  # type: ignore[misc]
    pass


class UserUpdate(schemas.BaseUserUpdate):  # type: ignore[misc]
    pass
