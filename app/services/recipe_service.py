import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.recipe import Recipe
from app.schemas.recipe import RecipeRead


async def get_recipe(db: AsyncSession, recipe_id: uuid.UUID) -> Optional[RecipeRead]:
    result = await db.execute(select(Recipe).where(Recipe.id == recipe_id))
    db_recipe = result.scalar_one_or_none()
    if db_recipe is None:
        return None
    return RecipeRead.model_validate(db_recipe)


async def get_recipes(db: AsyncSession, owner_id: uuid.UUID) -> List[RecipeRead]:
    result = await db.execute(select(Recipe).where(Recipe.owner_id == owner_id))
    db_recipes = result.scalars().all()
    return [RecipeRead.model_validate(r) for r in db_recipes]


async def create_recipe(
    db: AsyncSession, recipe: Dict[str, Any], owner_id: uuid.UUID
) -> RecipeRead:
    if "updated_at" not in recipe or recipe["updated_at"] is None:
        recipe["updated_at"] = datetime.utcnow()
    db_recipe = Recipe(**recipe, owner_id=owner_id)
    db.add(db_recipe)
    await db.commit()
    await db.refresh(db_recipe)
    return RecipeRead.model_validate(db_recipe)


async def update_recipe(
    db: AsyncSession, db_recipe: Recipe, updates: Dict[str, Any]
) -> RecipeRead:
    for key, value in updates.items():
        setattr(db_recipe, key, value)
    await db.commit()
    await db.refresh(db_recipe)
    return RecipeRead.model_validate(db_recipe)


async def delete_recipe(db: AsyncSession, db_recipe: Recipe) -> None:
    await db.delete(db_recipe)
    await db.commit()
