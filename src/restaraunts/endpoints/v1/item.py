from fastapi import APIRouter, status, HTTPException, Response
from src.restaraunts.repo import item, ordereditem
from src.restaraunts.schemas.item import Item, ItemCreate, ItemResponse
from src.restaraunts.schemas.ordereditem import OrderedItem, OrderedItemStatus, OrderedItemResponse, OrderedItemStatusUpdate
from typing import List

router = APIRouter()


@router.get('/restaraunts/items', summary="Получить список всех товаров")
async def get_all() -> List[Item]:
    return await item.get_all()


@router.get(
    '/restaraunts/{restaraunt_id}/menu/{menu_id}/items',
    summary="Получить список всех товаров (для меню)"
)
async def get_all_for_m(menu_id: int) -> List[Item]:
    return await item.get_all_for_menu(menu_id)


@router.get(
    '/restaraunts/{restaraunt_id}/menu/{menu_id}/items/{item_id}',
    summary="Получить детальную информацию о товаре (для меню)"
)
async def get_item(menu_id: int, item_id: int) -> Item:
    return await item.get_item_for_menu(menu_id, item_id)
   

@router.post(
    "/restaraunts/items", 
    status_code=status.HTTP_201_CREATED,
    summary="Создать новый товар"
)
async def create_item(item_data: ItemCreate) -> ItemResponse:
    new_id = await item.add_item(item_data.name, item_data.price)
    return ItemResponse(
        id=new_id, 
        name=item_data.name,
        price=item_data.price,
        status="created"
    )


@router.delete(
    '/restaraunts/items/{item_id}',
    summary="Деактивировать товар"
)
async def delete_item(item_id:int) -> Item:
    return await item.delete(item_id)


@router.patch(
    '/restaraunts/items/{item_id}/restore',
    summary="Восстановить ранее деактивированый товар"
)
async def restore_item(item_id:int) -> Item:
    return await item.restore(item_id)


@router.post(
    '/restaraunts/{restaraunt_id}/orders/{order_id}/items/{item_id}',
    summary="Добавить товар в заказ"  
)
async def add_item_to_order(order_id: int, item_id: int) -> OrderedItemResponse:
    item = await ordereditem.add_ordered_item(item_id, order_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Order or Item not found"
        )
    return OrderedItemResponse(
        item_id=item.id,
        status=OrderedItemStatus.NOT_READY,
        price=item.price,
        order_id=item.order_id
    )


@router.patch(
    "/restaraunts/{restaraunt_id}/orders/{order_id}/items/{item_id}",
    summary="Изменить статус заказанного товара"
)
async def update_ordereditem_status(item_id: int, status_data: OrderedItemStatusUpdate) -> OrderedItem:
    updated_item = await ordereditem.update_status(item_id, status_data.new_status)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")    
    return updated_item


@router.delete(
    '/restaraunts/{restaraunt_id}/orders/{order_id}/items/{item_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить товар из заказа"
)
async def delete_item(order_id: int, item_id: int):
    ordered_item = await ordereditem.get_ordereditem(order_id, item_id)
    if not ordered_item:
        raise HTTPException(status_code=404, detail="Товар в заказе не найден")
    if ordered_item.status != "Не готов":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Нельзя удалить товар, который уже готов"
        )
    success = await ordereditem.remove_from_order(order_id, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Товар не найден или уже готов")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
