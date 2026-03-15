from pydantic import BaseModel
from src.restaraunts.schemas.item import Item
from src.restaraunts.schemas.base import Base

class MenuCreate(BaseModel):
    items: list[Item]
    restaraunt_id: str
    version: int
    name: str

class Menu(Base, MenuCreate):
    pass

