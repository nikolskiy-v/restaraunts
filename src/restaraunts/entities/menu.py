from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import TimeStampedWithId
from .associations import restaraunt_menu_association
from .associations import menu_item_association
if TYPE_CHECKING:
    from .restaraunt import Restaraunt
    from .item import Item

class Menu(TimeStampedWithId):
    __tablename__ = 'Menus'

    name: Mapped[str]
    version: Mapped[int] = mapped_column(default=1)

    restaraunts: Mapped[list["Restaraunt"]] = relationship(secondary=restaraunt_menu_association, back_populates="menus")
    items: Mapped[list["Item"]] = relationship(secondary=menu_item_association, back_populates="menus")
