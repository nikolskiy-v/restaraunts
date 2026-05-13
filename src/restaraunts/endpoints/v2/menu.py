from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from src.restaraunts.database import get_db
from src.restaraunts.schemas.menu import Menu, MenuCreate, MenuResponse
from src.restaraunts.schemas.menuitem import LinkItemResponse
from src.restaraunts.services import menu
from src.restaraunts.services import item
from src.restaraunts.auth.deps import AuthTokenDep

router = APIRouter()

@router.get('/restaraunts/menus', summary="Получить список всех меню")
async def get_all(token:AuthTokenDep, db: AsyncSession = Depends(get_db)) -> list[Menu]:
    print(f'{token=}', flush=True)
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


@router.post(
    "/restaraunts/{restaraunt_id}/menu/{menu_id}/items/{item_id}",
    status_code=status.HTTP_201_CREATED,
    summary="Привязать товар к меню",
    responses={204: {"model": None}}
)
async def add_item_to_menu(menu_id: int, item_id: int, db: AsyncSession = Depends(get_db)) -> LinkItemResponse:
    result = await menu.link_menu_and_item(menu_id, item_id, db)
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
