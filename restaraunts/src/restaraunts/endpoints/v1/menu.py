from fastapi import APIRouter
from ...schemas.menu import Menu
from datetime import datetime

router = APIRouter(tags=['menu'])

@router.get('/menu')
async def get_menus():
    ...


@router.get('/menu/{menu_id}')
async def get_menu(
        menu_id: str
):
    return Menu(
        items= [],
        id= menu_id,
        created_at= datetime.now(),
        updated_at= datetime.now()
    )


#async def create_menu():
#    ... 
