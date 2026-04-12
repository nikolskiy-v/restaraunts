from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.restaraunts.database import get_db
from src.restaraunts.schemas.menu import Menu
from src.restaraunts.services import menu

router = APIRouter(tags=['menu'])

@router.get('/restaraunts/menus', summary="Получить список всех меню")
async def get_all(db: AsyncSession = Depends(get_db)) -> list[Menu]:
    menus = await menu.get_all(db)
    return menus
