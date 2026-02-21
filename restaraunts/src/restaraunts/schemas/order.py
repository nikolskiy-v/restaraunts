from pydantic import BaseModel
from .base import Base

class Order(Base):
    items: list[Item]
    status: str            #str.enum
    price: int
