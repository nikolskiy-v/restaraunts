from fastapi import APIRouter
from src.restaraunts.schemas.item import Item
from src.restaraunts.schemas.ordereditem import OrderedItem, OrderedItemStatus
from datetime import datetime

router = APIRouter(tags=['item'])

@router.get('/restaraunts/{restaraunt_id}/menu/{menu_id}/items')
async def get_items():
    ...


@router.get('/restaraunts/{restaraunt_id}/menu/{menu_id}/items/{item_id}')
async def get_item(
        item_id: str
) -> Item:
    ...
    # return Item(
    #     id= item_id,
    #     created_at= datetime.now(),
    #     updated_at= datetime.now(),
    #     price= 999,
    #     name= 'test_item_name'
    # )


@router.get('/restaraunts/{restaraunt_id}/orders/{order_id}/items')
async def get_ordereditems():
    ...


@router.get('/restaraunts/{restaraunt_id}/orders/{order_id}/items/{item_id}')
async def get_ordereditem(
        item_id: str
) -> OrderedItem:
    ...
    # return OrderedItem(
    #     id= item_id,
    #     created_at= datetime.now(),
    #     updated_at= datetime.now(),
    #     item= test_item,
    #     status= 'Не готов',
    #     price= 999
    # )



@router.post('/restaraunts/{restaraunt_id}/orders/{order_id}/items/{item_id}')
async def add_item_to_order(
    order_id: str,
    item_id: str
):
    pass



@router.patch("/restaraunts/{restaraunt_id}/orders/{order_id}/items/{item_id}", response_model=dict)
def update_ordereditem_status(
    item_id: int, 
    ordereditem_update: OrderedItemStatus
):
    pass


@router.delete('/restaraunts/{restaraunt_id}/orders/{order_id}/items/{item_id}')
async def delete_ordereditem_from_order(
    item_id: str,
    order_id: str
):
    pass
