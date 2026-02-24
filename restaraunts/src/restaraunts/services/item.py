from datetime import datetime
from src.restaraunts.schemas.item import Item

fake_db = {
    'test_item_id' : {
        'id' : 'test_item_id',
        'created_at' : datetime.now(),
        'updated_at' : datetime.now(),
        'price' : 999,
        'name' : 'item_name'
    }
}

test_item = Item(**fake_db['test_item_id'])