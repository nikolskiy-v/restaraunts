from pydantic import BaseModel, Field
from src.restaraunts.schemas.base import Base

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, example="Пиво")
    price: float = Field(gt=0)

class Item(Base, ItemCreate):
    is_active: bool
    
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    status: str = "created"
