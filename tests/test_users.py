import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(async_client: AsyncClient) -> None:
    response = await async_client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code in (200, 201, 400)  # 400 if already exists


@pytest.mark.asyncio
async def test_login_user(async_client: AsyncClient) -> None:
    # Register user first (idempotent)
    await async_client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    # Attempt login
    response = await async_client.post(
        "/api/v1/auth/jwt/login",
        data={"username": "test@example.com", "password": "testpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
