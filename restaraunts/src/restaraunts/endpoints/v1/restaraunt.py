from fastapi import APIRouter
from ...schemas.restaraunt import Restaraunt
from datetime import datetime
from ...schemas.menu import Menu

router = APIRouter(tags=['restaraunt'])

@router.get('/restaraunt')
async def get_restaraunts():
    ...
@router.get('/restaraunt/{restaraunt_id}')
async def get_restaraunt(
        restaraunt_id: str
):
    return Restaraunt(
        id= restaraunt_id,
        created_at= datetime.now(),
        updated_at= datetime.now(),
        name= 'test',
        menu= Menu,
        orders= [])
