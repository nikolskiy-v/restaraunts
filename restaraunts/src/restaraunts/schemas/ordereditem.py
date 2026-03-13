from pydantic import BaseModel
from .base import Base
from .item import Item
import enum

class OrderedItem(Base):
    item: Item
    status: OrderedItemStatus
    price: int


class OrderedItemStatus(enum.StrEnum):
    NOT_READY = 'Не готов'
    READY_FOR_DELIVERY = 'Готов к выдаче'
    DELIVERED = 'Выдан'
    