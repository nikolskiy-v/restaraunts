from .base import Base
from .menu import Menu
from .order import Order

class Restaraunt(Base):
    name: str
    menus: list[Menu]
    orders: list[Order]
