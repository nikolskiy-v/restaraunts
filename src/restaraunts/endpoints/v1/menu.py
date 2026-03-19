from fastapi import APIRouter
from src.restaraunts.schemas.menu import Menu
from src.restaraunts.repo.menu import get_menus_for_restaraunt

router = APIRouter(tags=['menu'])

@router.get('/restaraunt/{restaraunt_id}/menu')
async def get_menus(restaraunt_id: int) -> list[Menu]:
    menus = await get_menus_for_restaraunt(restaraunt_id)
    return menus


@router.get('/restaraunt/{restaraunt_id}/menu/{menu_id}')
async def get_menu(
        menu_id: str
) -> Menu:
        ...

#async def create_menu():
#    ... 

