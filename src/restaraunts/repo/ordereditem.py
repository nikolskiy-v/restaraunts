from src.restaraunts.database import get_cursor
from src.restaraunts.schemas.ordereditem import OrderedItem
from typing import List
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


async def add_ordered_item(item_id: int, order_id: int) -> OrderedItem | None:
    async with get_cursor() as cursor:
        await cursor.execute('''
            INSERT INTO OrderedItems (item_id, order_id, price)
            SELECT id, ?, price 
            FROM Items 
            WHERE id = ?
            RETURNING *
        ''', (order_id, item_id))
        row = await cursor.fetchone()
        if row is None:
            return None
        return OrderedItem(**dict(row))
    

async def get_all_ordered(order_id: int) -> List[OrderedItem]:
    async with get_cursor() as cursor:
        await cursor.execute('''
            SELECT * 
            FROM OrderedItems
            WHERE order_id = ?
        ''', (order_id,))
        rows = await cursor.fetchall()
        return [OrderedItem(**dict(row)) for row in rows]


async def get_ordereditem(order_id: int, ordereditem_id: int) -> OrderedItem | None:
    async with get_cursor() as cursor:
        await cursor.execute('''
            SELECT * 
            FROM OrderedItems
            WHERE order_id = ?
            AND id = ?
        ''', (order_id, ordereditem_id))
        row = await cursor.fetchone()
        if row is None:
            return None
        return OrderedItem(**dict(row))

    
async def update_status(ordereditem_id, new_status) -> OrderedItem:
    async with get_cursor() as cursor:
        await cursor.execute('''
            UPDATE OrderedItems
            SET "status" = ?
            WHERE id = ?
            RETURNING *
        ''', (new_status, ordereditem_id))
        row = await cursor.fetchone() 
        return OrderedItem(**dict(row))


async def remove_from_order(order_id: int, item_id: int) -> bool:
    async with get_cursor() as cursor:
        await cursor.execute('''
            DELETE FROM OrderedItems
            WHERE order_id = ? 
              AND id = ? 
              AND status = 'Не готов'
        ''', (order_id, item_id))
        
        return cursor.rowcount > 0
