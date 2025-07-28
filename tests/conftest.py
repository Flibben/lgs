from typing import AsyncGenerator

import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.main import app


@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with LifespanManager(app):
        async with AsyncClient(base_url="http://test", app=app) as ac:
            yield ac
