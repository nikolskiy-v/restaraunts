from pydantic import BaseModel, Field
from src.restaraunts.schemas.base import Base

class MenuCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, example="Летнее меню")

class Menu(Base, MenuCreate):
    version: int

class MenuResponse(BaseModel):
    id: int
    name: str
    status: str = "created"
