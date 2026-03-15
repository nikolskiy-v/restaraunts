from pydantic import BaseModel
from src.restaraunts.schemas.item import Item
from src.restaraunts.schemas.base import Base
import enum

class OrderedItem(Base):
    item: Item
    status: OrderedItemStatus
    price: int


class OrderedItemStatus(enum.StrEnum):
    NOT_READY = 'Не готов'
    READY_FOR_DELIVERY = 'Готов к выдаче'
    DELIVERED = 'Выдан'
    