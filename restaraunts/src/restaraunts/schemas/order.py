from .base import Base
from .ordereditem import OrderedItem
import enum

class Order(Base):
    ordereditems: list[OrderedItem]
    status: str
    price: int


class OrderStatus(enum.StrEnum):
    NEW = 'Новый'
    COMPLETED = 'Сформирован'
    READY = 'Готов'
    PAID = 'Оплачен'
