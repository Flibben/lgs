import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.main import app


@pytest_asyncio.fixture  # type: ignore[misc]
async def async_client() -> AsyncClient:
    async with LifespanManager(app):
        async with AsyncClient(base_url="http://test", app=app) as ac:
            yield ac
