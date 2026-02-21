from pydantic import BaseModel
from .base import Base

class Item(Base):
    price: int