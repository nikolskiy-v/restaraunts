from fastapi import APIRouter
from src.restaraunts.schemas.restaraunt import Restaraunt
from src.restaraunts.repo.restaraunt import get_all_restaraunts_from_db
from datetime import datetime
import asyncio

router = APIRouter(tags=['restaraunts'])

@router.get('/restaraunts')
async def get_restaraunts() -> list[Restaraunt]:
    restaraunts = asyncio.run(get_all_restaraunts_from_db())
    return restaraunts


@router.get('/restaurants/{restaurant_id}')
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
