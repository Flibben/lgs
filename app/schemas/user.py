import uuid

from fastapi_users import schemas
from pydantic import ConfigDict


class UserRead(schemas.BaseUser[uuid.UUID]):  # type: ignore[misc]
    model_config = ConfigDict(from_attributes=True)


class UserCreate(schemas.BaseUserCreate):  # type: ignore[misc]
    pass


class UserUpdate(schemas.BaseUserUpdate):  # type: ignore[misc]
    pass
