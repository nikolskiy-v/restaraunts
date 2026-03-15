from src.restaraunts.schemas.base import Base
from src.restaraunts.schemas.menu import Menu
from src.restaraunts.schemas.order import Order
from typing import List, Optional

class Restaraunt(Base):
    name: str
    menus: List[Optional[Menu]] = [] 
    orders: List[Optional[Order]] = []
