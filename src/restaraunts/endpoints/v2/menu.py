from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.restaraunts.database import get_db
from src.restaraunts.schemas.menu import Menu, MenuCreate, MenuResponse
from src.restaraunts.services import menu

router = APIRouter()

@router.get('/restaraunts/menus', summary="Получить список всех меню")
async def get_all(db: AsyncSession = Depends(get_db)) -> list[Menu]:
    return await menu.get_all(db)


@router.get('/restaraunts/menus/{menu_id}', summary="Получить детальную информацию о меню")
async def get_menu(menu_id: int, db: AsyncSession = Depends(get_db)) -> Menu:
    return await menu.get_one(menu_id, db)


@router.post(
    "/restaraunts/menus", 
    status_code=status.HTTP_201_CREATED,
    summary="Создать новое меню"
)
async def create_menu(menu_data: MenuCreate, db: AsyncSession = Depends(get_db)) -> MenuResponse:
    return await menu.add_menu(menu_data, db)
   