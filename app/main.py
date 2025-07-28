from fastapi import FastAPI
from app.api.v1 import users, recipes

app = FastAPI()

app.include_router(users.router, prefix="/api/v1")
app.include_router(recipes.router, prefix="/api/v1")

# Other routers will be included here in the future