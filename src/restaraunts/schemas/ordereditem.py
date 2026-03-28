from src.restaraunts.schemas.base import Base
import enum

class OrderedItem(Base):
    item_id: str
    status: OrderedItemStatus
    price: float
    order_id: str


class OrderedItemStatus(enum.StrEnum):
    NOT_READY = 'Не готов'
    READY_FOR_DELIVERY = 'Готов к выдаче'
    DELIVERED = 'Выдан'
    