from sqlalchemy import select, insert
import sqlite3
from sqlalchemy.ext.asyncio import AsyncSession
from src.restaraunts.entities.menu import Menu
from src.restaraunts.entities.associations import menu_item_association
from src.restaraunts.schemas.menu import Menu as MenuSchema, MenuCreate, MenuResponse
from typing import List

async def get_all(session: AsyncSession) -> List[MenuSchema]:
    stmt = select(Menu) 
    result = await session.execute(stmt)
    return [
        MenuSchema.model_validate(data, from_attributes=True)
        for data in list(result.scalars().all())
    ]
    

async def get_one(id: int, session: AsyncSession) -> MenuSchema:
    stmt = select(Menu).where(Menu.id == id)
    result = await session.execute(stmt)
    return MenuSchema.model_validate(result.scalar(), from_attributes=True)


async def add_menu(menu_create: MenuCreate, session:AsyncSession) -> MenuResponse:
    menu = Menu(**menu_create.model_dump())
    session.add(menu)
    await session.flush()
    return MenuResponse.model_validate(menu, from_attributes=True)


async def link_menu_and_item(menu_id: int, item_id: int, session:AsyncSession) -> str:
    data = {"menu_id": menu_id, "item_id": item_id}
    stmt = insert(menu_item_association).values(**data)
    try:
        await session.execute(stmt)
    except sqlite3.IntegrityError as e:
            if "FOREIGN KEY constraint failed" in str(e):
                return "not_found"
            if "UNIQUE constraint failed" in str(e):
                return "already_exists"
            raise e
    return "success"
