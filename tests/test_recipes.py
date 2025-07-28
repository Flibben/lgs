import pytest

@pytest.mark.asyncio
async def test_list_recipes(async_client):
    response = await async_client.get("/api/v1/recipes")
    assert response.status_code in (200, 401)  # 401 if not authenticated 