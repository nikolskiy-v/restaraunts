from fastapi import APIRouter
from src.restaraunts.schemas.item import Item
from datetime import datetime

router = APIRouter(tags=['item'])

@router.get('/{restaraunt}/{menu}/item')
async def get_items():
    ...


@router.get('/{restaraunt}/{menu}/{item_id}')
async def get_item(
        item_id: str
) -> Item:
    return Item(
        id= item_id,
        created_at= datetime.now(),
        updated_at= datetime.now(),
        price= 99,
        name= 'item_name'
    )
