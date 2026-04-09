from src.restaraunts.database import get_cursor
from src.restaraunts.schemas.order import Order
#import asyncio


async def init_db():
    async with get_cursor() as cursor:
        await cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER PRIMARY KEY,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            "status" TEXT DEFAULT 'Новый' NOT NULL,
            price REAL NOT NULL,
            restaraunt_id INTEGER,
            FOREIGN KEY (restaraunt_id) REFERENCES Restaraunts(id) ON DELETE RESTRICT
        )
        ''')


        #Триггер для автоматического обновления updated_at
        await cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS update_Orders_updated_at
        AFTER UPDATE ON Orders
        FOR EACH ROW
        BEGIN
            UPDATE Orders SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END;
        ''')

#asyncio.run(init_db())


async def add_order(price, restaraunt_id):
    async with get_cursor() as cursor:
        await cursor.execute('''
            INSERT INTO Orders (price, restaraunt_id)
            VALUES (?, ?)
        ''', (price, restaraunt_id))
        return cursor.lastrowid


async def update_status(order_id, new_status):
    async with get_cursor() as cursor:
        await cursor.execute('''
            UPDATE Orders
            SET "status" = ?
            WHERE id = ?
            RETURNING *
        ''', (new_status, order_id))
        row = await cursor.fetchone() 
        return Order(**dict(row))


async def get_all_for_restaraunt(restaraunt_id: int):
    async with get_cursor() as cursor:
        await cursor.execute('''
            SELECT * 
            FROM Orders
            WHERE restaraunt_id = ?
        ''', (restaraunt_id,))
        rows = await cursor.fetchall()
        return [Order(**dict(row)) for row in rows]
    

async def get_order_for_restaraunt(restaraunt_id: int, order_id: int):
    async with get_cursor() as cursor:
        await cursor.execute('''
            SELECT * 
            FROM Orders
            WHERE restaraunt_id = ?
            AND id = ?
        ''', (restaraunt_id, order_id))
        row = await cursor.fetchone()
        if row is None:
            return None
        return Order(**dict(row))
