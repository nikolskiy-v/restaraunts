from datetime import datetime
import sqlite3
from restaraunts.schemas.item import Item

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


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Items (
    id INTEGER PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    price REAL NOT NULL,
    name TEXT NOT NULL
)
''')


#Триггер для автоматического обновления updated_at
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS update_items_updated_at
AFTER UPDATE ON Items
FOR EACH ROW
BEGIN
    UPDATE Items SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
''')

connection.commit()
connection.close()


def add_item(name, price):
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Items (name, price) 
            VALUES (?, ?)
        ''', (name, price))
        print(f"Товар '{name}' добавлен. ID: {cursor.lastrowid}")
