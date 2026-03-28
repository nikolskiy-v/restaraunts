from fastapi import APIRouter, status
from src.restaraunts.schemas.menu import Menu, MenuCreate, MenuResponse
from src.restaraunts.repo import menu

router = APIRouter(tags=['menu'])

@router.get('/restaraunts/menus', summary="Получить список всех меню")
async def get_all() -> list[Menu]:
    menus = await menu.get_all()
    return menus


@router.get('/restaraunts/{restaraunt_id}/menu', summary="Получить список всех меню (для ресторана)")
async def get_all_for_r(restaraunt_id: int) -> list[Menu]:
    menus = await menu.get_all_for_restaraunt(restaraunt_id)
    return menus


@router.get('/restaraunts/{restaraunt_id}/menu/{menu_id}', summary="Получить детальную информацию о меню (для ресторана)")
async def get_menu(restaraunt_id: int, menu_id: int) -> Menu:
    m = await menu.get_menu_for_restaraunt(restaraunt_id, menu_id)
    return m


@router.post(
    "/restaraunts/menus", 
    status_code=status.HTTP_201_CREATED,
    summary="Создать новое меню"
)
async def create_menu(menu_data: MenuCreate) -> MenuResponse:
    new_id = await menu.add_menu(menu_data.name)
    return MenuResponse(
        id=new_id, 
        name=menu_data.name,
        status="created"
    )
