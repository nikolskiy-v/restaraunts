from fastapi import APIRouter
from .v1 import menu, restaraunt, order, item

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(menu.router)
v1_router.include_router(restaraunt.router)
v1_router.include_router(order.router)
v1_router.include_router(item.router)
