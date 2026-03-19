from fastapi import APIRouter, HTTPException, status
from src.restaraunts.schemas.restaraunt import Restaraunt
from src.restaraunts.repo.restaraunt import get_all_restaraunts_from_db, get_restaraunt_from_db
import asyncio

router = APIRouter(tags=['restaraunts'])

@router.get('/restaraunts')
async def get_restaraunts() -> list[Restaraunt]:
    restaraunts = await get_all_restaraunts_from_db()
    return restaraunts


@router.get('/restaraunts/{restaraunt_id}')
async def get_restaraunt(restaraunt_id: int) -> Restaraunt:
    restaraunt = await get_restaraunt_from_db(restaraunt_id)
    if restaraunt is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Restaurant with id {restaraunt_id} not found"
        )
    return restaraunt
