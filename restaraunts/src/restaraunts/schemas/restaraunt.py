from .base import Base
from .menu import Menu

class Restaraunt(Base):
    name: str
    menu: Menu
    orders: list