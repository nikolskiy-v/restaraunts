from src.restaraunts.schemas.base import Base
from pydantic import BaseModel
import enum

    
class OrderedItemResponse(BaseModel):
    item_id: int
    status: OrderedItemStatus
    price: float
    order_id: int

class OrderedItem(Base, OrderedItemResponse):
    ...

class OrderedItemStatus(str, enum.Enum):
    NOT_READY = 'Не готов'
    READY_FOR_DELIVERY = 'Готов к выдаче'
    DELIVERED = 'Выдан'

class OrderedItemStatusUpdate(BaseModel):
    new_status: OrderedItemStatus 
