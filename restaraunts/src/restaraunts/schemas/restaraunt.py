from .base import Base
from .menu import Menu

class Restaraunt(Base):
    name: str
    menu: list[Menu]
    orders: list[Order]
