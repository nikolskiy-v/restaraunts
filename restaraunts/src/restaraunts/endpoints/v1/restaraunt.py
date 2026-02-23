from fastapi import APIRouter
from src.restaraunts.schemas.restaraunt import Restaraunt
from datetime import datetime

router = APIRouter(tags=['restaraunt'])

@router.get('/restaraunt')
async def get_restaraunts():
    ...


@router.get('/restaraunt/{restaraunt_id}')
async def get_restaraunt(
        restaraunt_id: str
)-> Restaraunt :
    return Restaraunt(
        id= restaraunt_id,
        created_at= datetime.now(),
        updated_at= datetime.now(),
        name= 'test',
        menus= [],
        orders= [])
