from pydantic import BaseModel
from .base import Base

class MenuCreate(BaseModel):
    items: [] 

class Menu(Base, MenuCreate):
    pass
