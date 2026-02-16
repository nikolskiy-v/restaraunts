from pydantic import BaseModel
from .base import Base

class MenuCreate(BaseModel):
    items: list 

class Menu(Base, MenuCreate):
    pass