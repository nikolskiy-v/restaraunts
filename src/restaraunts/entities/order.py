from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
if TYPE_CHECKING:
    from .restaraunt import Restaraunt
    from .ordereditem import OrderedItem
from .base import TimeStampedWithId
import enum


class OrderStatus(str, enum.Enum):
    NEW = 'Новый'
    COMPLETED = 'Сформирован'
    READY = 'Готов'
    PAID = 'Оплачен'


class Order(TimeStampedWithId):
    __tablename__ = 'Orders'

    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus),
        default=OrderStatus.NEW,
        nullable=False
    )
    price: Mapped[float]
    restaraunt_id: Mapped[int] = mapped_column(ForeignKey("Restaraunts.id"))

    restaraunt: Mapped["Restaraunt"] = relationship(back_populates="orders")
    ordereditems: Mapped[List["OrderedItem"]] = relationship(back_populates="order")
