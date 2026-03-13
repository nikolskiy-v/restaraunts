from fastapi import APIRouter
from src.restaraunts.schemas.menu import Menu
from datetime import datetime

router = APIRouter(tags=['menu'])

@router.get('/restaurants/{restaurant_id}/menu')
async def get_menus():
    ...


@router.get('/restaurants/{restaurant_id}/menu/{menu_id}')
async def get_menu(
        menu_id: str
) -> Menu:
    return Menu(
        items= [],
        restaraunt_id= '1',
        version= 1,
        name= "test",
        id= menu_id,
        created_at= datetime.now(),
        updated_at= datetime.now()
    )


#async def create_menu():
#    ... 

