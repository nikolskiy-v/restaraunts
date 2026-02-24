from fastapi import APIRouter
from src.restaraunts.schemas.ordereditem import OrderedItem, OrderedItemStatus
from src.restaraunts.services.item import test_item
from datetime import datetime

router = APIRouter(tags=['ordereditem'])

@router.get('/{restaraunt}/orders/{order_id}/ordereditem')
async def get_ordereditems():
    ...


@router.get('/{restaraunt}/orders/{order_id}/ordereditem/{ordereditem_id}')
async def get_ordereditem(
        ordereditem_id: str
) -> OrderedItem:
    return OrderedItem(
        id= ordereditem_id,
        created_at= datetime.now(),
        updated_at= datetime.now(),
        item= test_item,
        status= 'Не готов',
        price= 999
    )


@router.patch("/{restaraunt}/orders/{order_id}/ordereditem/{ordereditem_id}", response_model=dict)
def update_ordereditem_status(
    ordereditem_id: int, 
    ordereditem_update: OrderedItemStatus
):
    pass


@router.delete('/{restaraunt}/orders/{order_id}/ordereditem/{ordereditem_id}')
async def delete_ordereditem_from_order(
    ordereditem_id: str,
    item_id: str
):
    pass

