from fastapi import FastAPI
import uvicorn
from users.schemas import CreateUser

from items_views import router as items_router
from users.views import router as users_router

from core.models import Base, db_helper
from core.config import settings
from contextlib import asynccontextmanager

from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def hello_ind():
    return {"message": "hello"}


@app.get("/hello")
def hel(name: str = "World"):
    name = name.title()
    return {"message": f"Hello {name}"}


@app.post("/users")
def cr_us(user: CreateUser):
    return {"message": "success", "email": user.email}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
