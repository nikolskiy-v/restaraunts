from fastapi import APIRouter, status
from src.restaraunts.schemas.order import Order, OrderCreate, OrderResponse, OrderStatus
from src.restaraunts.repo import order

router = APIRouter(tags=['order'])

@router.get('/restaraunts/{restaraunt_id}/orders', summary="Получить список всех заказов (для ресторана)")
async def get_all_for_r(restaraunt_id: int) -> list[Order]:
    orders = await order.get_all_for_restaraunt(restaraunt_id)
    return orders


@router.get('/restaraunts/{restaraunt_id}/orders/{order_id}', summary="Получить детальную информацию о заказе (для ресторана)")
async def get_order(restaraunt_id: int, order_id: int) -> Order:
    o = await order.get_order_for_restaraunt(restaraunt_id, order_id)
    return o


@router.post(
        '/restaraunts/{restaraunt_id}/orders',
        status_code=status.HTTP_201_CREATED,
        summary="Создать новый заказ для ресторана",
)
async def create_order(restaraunt_id: int, order_data: OrderCreate) -> OrderResponse:
    new_id = await order.add_order(order_data.price, restaraunt_id)
    return OrderResponse(
        id=new_id, 
        price=order_data.price,
        restaraunt_id=restaraunt_id,
        status="Новый"
    )


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
