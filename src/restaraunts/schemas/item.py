from pydantic import BaseModel
from src.restaraunts.schemas.base import Base

class Item(Base):
    price: int
    name: str
    