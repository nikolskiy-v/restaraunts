from fastapi import APIRouter, HTTPException, status
from src.restaraunts.schemas.restaraunt import Restaraunt
from src.restaraunts.repo import restaraunt

router = APIRouter(tags=['restaraunts'])

@router.get('/restaraunts')
async def get_restaraunts() -> list[Restaraunt]:
    restaraunts = await restaraunt.get_all()
    return restaraunts


@router.get('/restaraunts/{restaraunt_id}')
async def get_restaraunt(restaraunt_id: int) -> Restaraunt:
    r = await restaraunt.get_restaraunt(restaraunt_id)
    if r is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Restaurant with id {restaraunt_id} not found"
        )
    return r
