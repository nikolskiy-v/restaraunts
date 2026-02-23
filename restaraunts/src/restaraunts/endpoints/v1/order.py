from fastapi import APIRouter
from src.restaraunts.schemas.order import Order
from datetime import datetime

router = APIRouter(tags=['order'])

@router.get('/{restaraunt}/order')
async def get_orders():
    ...


@router.get('/{restaraunt}/order/{order_id}')
async def get_order(
        order_id: str
) -> Order:
    return Order(
        id= order_id,
        created_at= datetime.now(),
        updated_at= datetime.now(),
        ordereditems= [],
        status= 'Новый',
        price= 9999
    )

