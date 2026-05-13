from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.restaraunts.entities.base import Base
from src.restaraunts.entities import *
from src.restaraunts.database import test_conn, engine
from src.restaraunts.endpoints import v1_router, v2_router

@asynccontextmanager
async def on_start(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Restaurant API",
    description="V1 - SQL, V2 - SQLAlchemy ORM",
    version="2.0.0",
    lifespan=on_start
)
app.include_router(v1_router, prefix="/api")
app.include_router(v2_router, prefix="/api")


@app.get('/test')
async def get_test():
    await test_conn()
    return {"status": "OK"}
