from src.restaraunts.database import get_cursor
#import asyncio


async def init_db():
    async with get_cursor() as cursor:
        await cursor.execute('''
        CREATE TABLE IF NOT EXISTS OrderedItems (
            id INTEGER PRIMARY KEY,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            item_id INTEGER,
            "status" TEXT NOT NULL DEFAULT 'Не готов',
            price REAL NOT NULL,
            order_id INTEGER,
            FOREIGN KEY (item_id) REFERENCES Items(id) ON DELETE SET NULL,
            FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE RESTRICT
        )
        ''')


        #Триггер для автоматического обновления updated_at
        await cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS update_ordereditems_updated_at
        AFTER UPDATE ON OrderedItems
        FOR EACH ROW
        BEGIN
            UPDATE OrderedItems SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END;
        ''')

#asyncio.run(init_db())


async def add_ordered_item(item_id, status, price, order_id):
    async with get_cursor() as cursor:
        await cursor.execute('''
            INSERT INTO OrderedItems (item_id, "status", price, order_id)
            VALUES (?, ?, ?, ?)
        ''', (item_id, status, price, order_id))
        return cursor.lastrowid
    

async def update_item_status(ordereditem_id, new_status):
    async with get_cursor() as cursor:
        await cursor.execute('''
            UPDATE OrderedItems
            SET "status" = ?
            WHERE id = ?
        ''', (new_status, ordereditem_id))
