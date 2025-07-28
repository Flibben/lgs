import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.recipe import Recipe


async def get_recipe(db: AsyncSession, recipe_id: uuid.UUID) -> Optional[Recipe]:
    result = await db.execute(select(Recipe).where(Recipe.id == recipe_id))
    return result.scalar_one_or_none()  # type: ignore[no-any-return]


async def get_recipes(db: AsyncSession, owner_id: uuid.UUID) -> List[Recipe]:
    result = await db.execute(select(Recipe).where(Recipe.owner_id == owner_id))
    # Break the long line for flake8
    return result.scalars().all()  # type: ignore[no-any-return]


async def create_recipe(
    db: AsyncSession, recipe: Dict[str, Any], owner_id: uuid.UUID
) -> Recipe:
    if "updated_at" not in recipe or recipe["updated_at"] is None:
        recipe["updated_at"] = datetime.utcnow()
    db_recipe = Recipe(**recipe, owner_id=owner_id)
    db.add(db_recipe)
    await db.commit()
    await db.refresh(db_recipe)
    return db_recipe


async def update_recipe(
    db: AsyncSession, db_recipe: Recipe, updates: Dict[str, Any]
) -> Recipe:
    for key, value in updates.items():
        setattr(db_recipe, key, value)
    await db.commit()
    await db.refresh(db_recipe)
    return db_recipe


async def delete_recipe(db: AsyncSession, db_recipe: Recipe) -> None:
    await db.delete(db_recipe)
    await db.commit()
