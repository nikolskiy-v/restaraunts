from fastapi import APIRouter
from src.restaraunts.schemas.menu import Menu
from src.restaraunts.repo import menu

router = APIRouter(tags=['menu'])

@router.get('/restaraunt/{restaraunt_id}/menu')
async def get_menus(restaraunt_id: int) -> list[Menu]:
    menus = await menu.get_all_for_restaraunt(restaraunt_id)
    return menus


@router.get('/restaraunt/{restaraunt_id}/menu/{menu_id}')
async def get_menu(restaraunt_id: int, menu_id: int) -> Menu:
    m = await menu.get_menu_for_restaraunt(restaraunt_id, menu_id)
    return m


#async def create_menu():
#    ... 
