import pytest
from httpx import AsyncClient

RECIPE_DATA = {
    "title": "Test Recipe",
    "description": "A test recipe description.",
    "ingredients": "Eggs, Flour, Milk",
    "instructions": "Mix and cook.",
}


@pytest.mark.asyncio  # type: ignore[misc]
async def test_list_recipes(async_client: AsyncClient) -> None:
    response = await async_client.get("/api/v1/recipes")
    assert response.status_code in (200, 401)  # 401 if not authenticated


@pytest.mark.asyncio  # type: ignore[misc]
async def test_recipe_crud_flow(async_client: AsyncClient) -> None:
    # Register and login user
    email = "recipeuser@example.com"
    password = "testpassword"
    await async_client.post(
        "/api/v1/auth/register", json={"email": email, "password": password}
    )
    login_resp = await async_client.post(
        "/api/v1/auth/jwt/login",
        data={"username": email, "password": password},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert login_resp.status_code == 200
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create recipe
    create_resp = await async_client.post(
        "/api/v1/recipes", json=RECIPE_DATA, headers=headers
    )
    assert create_resp.status_code == 201
    recipe = create_resp.json()
    recipe_id = recipe["id"]

    # Get single recipe
    get_resp = await async_client.get(f"/api/v1/recipes/{recipe_id}", headers=headers)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == RECIPE_DATA["title"]

    # Update recipe
    update_data = {**RECIPE_DATA, "title": "Updated Title"}
    update_resp = await async_client.put(
        f"/api/v1/recipes/{recipe_id}", json=update_data, headers=headers
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["title"] == "Updated Title"

    # Delete recipe
    delete_resp = await async_client.delete(
        f"/api/v1/recipes/{recipe_id}", headers=headers
    )
    assert delete_resp.status_code == 204

    # Ensure recipe is gone
    get_resp = await async_client.get(f"/api/v1/recipes/{recipe_id}", headers=headers)
    assert get_resp.status_code == 404


@pytest.mark.asyncio  # type: ignore[misc]
async def test_recipe_unauthorized_access(async_client: AsyncClient) -> None:
    # Try to create recipe without auth
    resp = await async_client.post("/api/v1/recipes", json=RECIPE_DATA)
    assert resp.status_code == 401
    # Try to get recipes without auth
    resp = await async_client.get("/api/v1/recipes")
    assert resp.status_code == 401
