from fastapi import APIRouter, status, HTTPException
from src.restaraunts.schemas.order import Order, OrderCreate, OrderResponse, OrderStatusUpdate
from src.restaraunts.schemas.ordereditem import OrderedItem
from src.restaraunts.repo import order, ordereditem
from typing import List

router = APIRouter()

@router.get(
        '/restaraunts/{restaraunt_id}/orders',
        summary="Получить список всех заказов (для ресторана)"
)
async def get_all_for_r(restaraunt_id: int) -> List[Order]:
    return await order.get_all_for_restaraunt(restaraunt_id)


@router.get(
        '/restaraunts/{restaraunt_id}/orders/{order_id}',
        summary="Получить детальную информацию о заказе (для ресторана)"
)
async def get_order(restaraunt_id: int, order_id: int) -> Order:
    return await order.get_order_for_restaraunt(restaraunt_id, order_id)


@router.post(
        '/restaraunts/{restaraunt_id}/orders',
        status_code=status.HTTP_201_CREATED,
        summary="Создать новый заказ для ресторана"
)
async def create_order(restaraunt_id: int, order_data: OrderCreate) -> OrderResponse:
    new_id = await order.add_order(order_data.price, restaraunt_id)
    return OrderResponse(
        id=new_id, 
        price=order_data.price,
        restaraunt_id=restaraunt_id,
        status="Новый"
    )


@router.patch(
        '/restaraunts/{restaraunt_id}/orders/{order_id}',
        summary="Изменить статус заказа"
)
async def update_order_status(order_id: int, status_data: OrderStatusUpdate) -> Order:
    updated_order = await order.update_status(order_id, status_data.new_status)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")    
    return updated_order


@router.get('/restaraunts/{restaraunt_id}/orders/{order_id}/items', summary="Получить список всех товаров в заказе")
async def get_all_ordered(order_id: int) -> List[OrderedItem]:
    return await ordereditem.get_all_ordered(order_id)


@router.get(
    '/restaraunts/{restaraunt_id}/orders/{order_id}/items/{item_id}',
    summary="Получить детальную информацию о товаре в заказе"
)
async def get_ordered_item(order_id: int, item_id: int) -> OrderedItem:
    return await ordereditem.get_ordereditem(order_id, item_id)

