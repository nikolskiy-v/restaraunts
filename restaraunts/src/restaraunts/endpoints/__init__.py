from fastapi import APIRouter
from .v1 import menu, restaraunt

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(menu.router)
v1_router.include_router(restaraunt.router)