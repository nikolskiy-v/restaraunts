from pydantic import BaseModel, Field
from .base import Base
import enum

class OrderCreate(BaseModel):
    price: float = Field(gt=0)


class OrderResponse(BaseModel):
    id: int
    price: float
    restaraunt_id: int
    status: str = "Новый"


class Order(Base, OrderCreate):
    status: OrderStatus
    restaraunt_id: int


class OrderStatus(str, enum.Enum):
    NEW = 'Новый'
    COMPLETED = 'Сформирован'
    READY = 'Готов'
    PAID = 'Оплачен'


class OrderStatusUpdate(BaseModel):
    new_status: OrderStatus 
