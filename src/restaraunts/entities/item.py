from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import TimeStampedWithId
from .associations import menu_item_association
if TYPE_CHECKING:
    from .ordereditem import OrderedItem
    from .menu import Menu


class Item(TimeStampedWithId):
    __tablename__ = 'Items'

    price: Mapped[float]
    name: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=1)

    ordereditems: Mapped[List["OrderedItem"]] = relationship(back_populates="item")
    menus: Mapped[list["Menu"]] = relationship(secondary=menu_item_association, back_populates="items")
