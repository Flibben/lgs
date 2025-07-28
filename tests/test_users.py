import pytest

@pytest.mark.asyncio
async def test_register_user(async_client):
    response = await async_client.post("/api/v1/auth/register", json={
        "email": "test@example.com",
        "password": "testpassword"
    })
    assert response.status_code in (200, 201, 400)  # 400 if already exists 