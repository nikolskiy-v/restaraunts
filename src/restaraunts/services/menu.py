from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.restaraunts.entities.menu import Menu
from src.restaraunts.schemas.menu import Menu as MenuSchema, MenuCreate, MenuResponse

async def get_all(session: AsyncSession) -> list[MenuSchema]:
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
