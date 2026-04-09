from fastapi import APIRouter, status
from src.restaraunts.repo import item
from src.restaraunts.schemas.item import Item, ItemCreate, ItemResponse
from src.restaraunts.schemas.ordereditem import OrderedItem, OrderedItemStatus

router = APIRouter(tags=['item'])


@router.get('/restaraunts/items', summary="Получить список всех товаров")
async def get_all() -> list[Item]:
    items = await item.get_all()
    return items


@router.get(
        '/restaraunts/{restaraunt_id}/menu/{menu_id}/items',
        summary="Получить список всех товаров (для меню)"
)
async def get_all_for_m(menu_id: int) -> list[Item]:
    items= await item.get_all_for_menu(menu_id)
    return items


@router.get(
        '/restaraunts/{restaraunt_id}/menu/{menu_id}/items/{item_id}',
        summary="Получить детальную информацию о товаре (для меню)"
)
async def get_item(menu_id: int, item_id: int) -> Item:
    i = await item.get_item_for_menu(menu_id, item_id)
    return i
   

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
