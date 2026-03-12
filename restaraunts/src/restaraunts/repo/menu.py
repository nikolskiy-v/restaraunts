from src.restaraunts.schemas.menu import Menu
from datetime import datetime

fake_db = {
    'test_menu_id' : {
        'id' : 'test_menu_id',
        'created_at' : datetime.now(),
        'updated_at' : datetime.now(),
        'items' : [],
        'resraraunt_id' : 'test_restaraunt_id',
        'version' : 1,
        'name' : 'test_menu_name'
    }
}
