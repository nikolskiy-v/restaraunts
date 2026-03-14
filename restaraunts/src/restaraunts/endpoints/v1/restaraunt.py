from fastapi import APIRouter
from src.restaraunts.schemas.restaraunt import Restaraunt
from src.restaraunts.repo.restaraunt import get_all_restaraunts_from_db
from datetime import datetime
from typing import List

router = APIRouter(tags=['restaraunts'])

@router.get('/restaraunts', response_model=List[Restaraunt])
async def get_restaraunts():
    restaraunts = get_all_restaraunts_from_db()
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
