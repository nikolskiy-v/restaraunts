from .base import Base
from .menu import Menu
from .order import Order
from typing import List, Optional

class Restaraunt(Base):
    name: str
    menus: List[Optional[Menu]] = [] 
    orders: List[Optional[Order]] = []
