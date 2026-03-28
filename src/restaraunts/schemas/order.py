from .base import Base
import enum

class Order(Base):
    status: OrderStatus
    price: float
    restaraunt_id: int


class OrderStatus(enum.StrEnum):
    NEW = 'Новый'
    COMPLETED = 'Сформирован'
    READY = 'Готов'
    PAID = 'Оплачен'
