from typing import Any
from fastapi import APIRouter, HTTPException, status, Response
from src.restaraunts.schemas.restaraunt import Restaraunt
from src.restaraunts.schemas.restarauntmenu import LinkMenuResponse
from src.restaraunts.repo import restaraunt
from src.restaraunts.repo import menu

router = APIRouter(tags=['restaraunts'])

@router.get('/restaraunts', summary="Получить список всех ресторанов")
async def get_restaraunts() -> list[Restaraunt]:
    restaraunts = await restaraunt.get_all()
    return restaraunts


@router.get('/restaraunts/{restaraunt_id}', summary="Получить детальную информацию о ресторане")
async def get_restaraunt(restaraunt_id: int) -> Restaraunt:
    r = await restaraunt.get_restaraunt(restaraunt_id)
    if r is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Restaurant with id {restaraunt_id} not found"
        )
    return r


@router.post(
    "/restaraunts/{restaraunt_id}/menu/{menu_id}",
    response_model=LinkMenuResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Привязать меню к ресторану",
    responses={204: {"model": None}}
)
async def add_menu_to_rest(restaraunt_id: int, menu_id: int) -> Any:
    result = await restaraunt.link_restaraunt_and_menu(restaraunt_id, menu_id)
    if result == "not_found":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaraunt or Menu not found"
        )
    if result == "already_exists":
        #связь уже есть(идемпотентно)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    all_menus = await menu.get_all_for_restaraunt(restaraunt_id)
    return LinkMenuResponse(
        status="created",
        restaraunt_id=restaraunt_id,
        menus=all_menus
    )
