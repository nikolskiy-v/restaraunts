from sqlalchemy import Table, Column, ForeignKey
from .base import Base

restaraunt_menu_association = Table(
    "Restarauntmenus",
    Base.metadata,
    Column("restaraunt_id", ForeignKey("Restaraunts.id"), primary_key=True),
    Column("menu_id", ForeignKey("Menus.id"), primary_key=True),
)


menu_item_association = Table(
    "Menuitems",
    Base.metadata,
    Column("menu_id", ForeignKey("Menus.id"), primary_key=True),
    Column("item_id", ForeignKey("Items.id"), primary_key=True),
)
