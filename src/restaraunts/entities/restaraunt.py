from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship
from .base import TimeStampedWithId
from .associations import restaraunt_menu_association
if TYPE_CHECKING:
    from .order import Order
    from .menu import Menu


class Restaraunt(TimeStampedWithId):
    __tablename__ = 'Restaraunts'

    name: Mapped[str]

    orders: Mapped[List["Order"]] = relationship(back_populates="restaraunt")
    menus: Mapped[list["Menu"]] = relationship(secondary=restaraunt_menu_association, back_populates="restaraunts")
