from pydantic import BaseModel
from typing import Optional
import uuid

class RecipeBase(BaseModel):
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
    class Config:
        orm_mode = True 