from pydantic import BaseModel
from .item import Item
from .base import Base

class MenuCreate(BaseModel):
    items: list[Item]
    resraraunt_id: str
    version: int
    name: str

class Menu(Base, MenuCreate):
    pass

