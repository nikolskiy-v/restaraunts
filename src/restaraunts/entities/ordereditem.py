from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
if TYPE_CHECKING:
    from .item import Item
    from .order import Order
from .base import TimeStampedWithId
import enum


class OrderedItemStatus(str, enum.Enum):
    NOT_READY = 'Не готов'
    READY_FOR_DELIVERY = 'Готов к выдаче'
    DELIVERED = 'Выдан'


class OrderedItem(TimeStampedWithId):
    __tablename__ = 'OrderedItems'

    item_id: Mapped[int] = mapped_column(ForeignKey("Items.id"))
    status: Mapped[OrderedItemStatus] = mapped_column(
        Enum(OrderedItemStatus),
        default=OrderedItemStatus.NOT_READY,
        nullable=False
    )
    price: Mapped[float]
    order_id: Mapped[int] = mapped_column(ForeignKey("Orders.id"))

    item: Mapped["Item"] = relationship(back_populates="ordereditems")
    order: Mapped["Order"] = relationship(back_populates="ordereditems")
