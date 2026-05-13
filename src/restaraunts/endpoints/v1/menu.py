from fastapi import APIRouter, status, HTTPException, Response
from src.restaraunts.schemas.menu import Menu, MenuCreate, MenuResponse
from src.restaraunts.schemas.menuitem import LinkItemResponse
from src.restaraunts.repo import menu, item
from typing import List

router = APIRouter()

@router.get('/restaraunts/menus', summary="Получить список всех меню")
async def get_all() -> List[Menu]:
    return await menu.get_all()


@router.get('/restaraunts/{restaraunt_id}/menu', summary="Получить список всех меню (для ресторана)")
async def get_all_for_r(restaraunt_id: int) -> List[Menu]:
    return await menu.get_all_for_restaraunt(restaraunt_id)


@router.get('/restaraunts/{restaraunt_id}/menu/{menu_id}', summary="Получить детальную информацию о меню (для ресторана)")
async def get_menu(restaraunt_id: int, menu_id: int) -> Menu:
    return await menu.get_menu_for_restaraunt(restaraunt_id, menu_id)


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

@router.post(
    "/restaraunts/{restaraunt_id}/menu/{menu_id}/items/{item_id}",
    status_code=status.HTTP_201_CREATED,
    summary="Привязать товар к меню",
    responses={204: {"model": None}}
)
async def add_item_to_menu(menu_id: int, item_id: int) -> LinkItemResponse:
    result = await menu.link_menu_and_item(menu_id, item_id)
    if result == "not_found":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu or Item not found"
        )
    if result == "already_exists":
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    all_items = await item.get_all_for_menu(menu_id)
    return LinkItemResponse(
        status="created",
        menu_id=menu_id,
        items=all_items
    )
