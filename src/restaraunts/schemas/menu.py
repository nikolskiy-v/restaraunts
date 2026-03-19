from pydantic import BaseModel
from src.restaraunts.schemas.base import Base

class MenuCreate(BaseModel):
    version: int
    name: str

class Menu(Base, MenuCreate):
    pass

