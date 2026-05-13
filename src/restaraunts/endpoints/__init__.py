from fastapi import APIRouter
from .v1 import menu, restaraunt, order, item
from .v2 import menu as menu_v2, restaraunt as restaraunt_v2, order as order_v2, item as item_v2


v1_router = APIRouter(prefix="/v1")
v1_router.include_router(menu.router, tags=["v1 | menu"])
v1_router.include_router(item.router, tags=["v1 | item"])
v1_router.include_router(restaraunt.router, tags=["v1 | restaraunt"])
v1_router.include_router(order.router, tags=["v1 | order"])

v2_router = APIRouter(prefix="/v2")
v2_router.include_router(menu_v2.router, tags=["v2 (ORM) | menu"])
v2_router.include_router(item_v2.router, tags=["v2 (ORM) | item"])
v2_router.include_router(restaraunt_v2.router, tags=["v2 (ORM) | restaraunt"])
v2_router.include_router(order_v2.router, tags=["v2 (ORM) | order"])