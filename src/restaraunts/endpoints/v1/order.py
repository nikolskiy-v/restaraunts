from fastapi import APIRouter
from src.restaraunts.schemas.order import Order, OrderStatus
from datetime import datetime

router = APIRouter(tags=['order'])

@router.get('/restaraunts/{restaraunt_id}/orders')
async def get_orders():
    ...


@router.get('/restaraunts/{restaraunt_id}/orders/{order_id}')
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


@router.post('/restaraunts/{restaraunt_id}/orders')
async def add_order(
    order: Order
):
    #логика добавления заказа в БД
    pass


@router.post('/restaraunts/{restaraunt_id}/orders/{order_id}/items/{item_id}')
async def add_item_to_order(
    order_id: str,
    item_id: str
):
    pass


@router.patch("/restaraunts/{restaraunt_id}/orders/{order_id}", response_model=dict)
def update_order_status(
    order_id: int, 
    order_update: OrderStatus
):
    pass

