from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.restaraunts.entities.item import Item
from src.restaraunts.entities.menu import Menu
from src.restaraunts.schemas.item import Item as ItemSchema


async def get_all_for_menu(menu_id: int, session: AsyncSession) -> list[ItemSchema]:
    stmt = (
        select(Item)
        .where(Item.menus.any(Menu.id == menu_id)) 
    )
    result = await session.execute(stmt)
    return [
        ItemSchema.model_validate(data, from_attributes=True)
        for data in list(result.scalars().all())
    ]
    

async def get_item_for_menu(menu_id: int, item_id: int, session: AsyncSession) -> ItemSchema | None:
    stmt = (
        select(Item)
        .where(Item.id == item_id)
        .where(Item.menus.any(Menu.id == menu_id))
    )
    result = await session.execute(stmt)
    item_model = result.scalar_one_or_none()
    if item_model is None:
        return None
    return ItemSchema.model_validate(item_model, from_attributes=True)
    