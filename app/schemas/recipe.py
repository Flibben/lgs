import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RecipeBase(BaseModel):  # type: ignore[misc]
    title: str
    description: Optional[str] = None
    ingredients: str
    instructions: str


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(RecipeBase):
    pass


class RecipeRead(RecipeBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)
