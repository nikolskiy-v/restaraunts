from .base import Base
from .ordereditem import OrderedItem
import enum

class Order(Base):
    ordereditems: list[OrderedItem]
    status: OrderStatus
    price: int


class OrderStatus(enum.StrEnum):
    NEW = 'Новый'
    COMPLETED = 'Сформирован'
    READY = 'Готов'
    PAID = 'Оплачен'
