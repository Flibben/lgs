from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.recipe import RecipeRead, RecipeCreate, RecipeUpdate
from app.services.recipe_service import get_recipe, get_recipes, create_recipe, update_recipe, delete_recipe
from app.db.session import get_db
from app.dependencies.auth import fastapi_users
from app.models.user import User
import uuid
from typing import List

router = APIRouter()

current_active_user = fastapi_users.current_user(active=True)

@router.get("/recipes", response_model=List[RecipeRead])
async def list_recipes(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await get_recipes(db, user.id)

@router.post("/recipes", response_model=RecipeRead, status_code=status.HTTP_201_CREATED)
async def create_new_recipe(
    recipe: RecipeCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    return await create_recipe(db, recipe.dict(), user.id)

@router.get("/recipes/{recipe_id}", response_model=RecipeRead)
async def get_single_recipe(
    recipe_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    db_recipe = await get_recipe(db, recipe_id)
    if not db_recipe or db_recipe.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@router.put("/recipes/{recipe_id}", response_model=RecipeRead)
async def update_existing_recipe(
    recipe_id: uuid.UUID,
    updates: RecipeUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    db_recipe = await get_recipe(db, recipe_id)
    if not db_recipe or db_recipe.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return await update_recipe(db, db_recipe, updates.dict(exclude_unset=True))

@router.delete("/recipes/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_recipe(
    recipe_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    db_recipe = await get_recipe(db, recipe_id)
    if not db_recipe or db_recipe.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Recipe not found")
    await delete_recipe(db, db_recipe) 