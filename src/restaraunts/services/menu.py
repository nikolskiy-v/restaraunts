from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.restaraunts.entities.menu import Menu

async def get_all(session: AsyncSession):
    query = select(Menu) 
    result = await session.execute(query)
    
    return result.scalars().all()