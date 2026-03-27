from src.restaraunts.database import get_cursor
#import asyncio


async def init_db():
    async with get_cursor() as cursor:
        await cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER PRIMARY KEY,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            "status" TEXT NOT NULL DEFAULT 'Новый',
            price REAL NOT NULL,
            restaraunt_id INTEGER,
            FOREIGN KEY (restaraunt_id) REFERENCES Restaraunts(id) ON DELETE RESTRICT
        )
        ''')


        #Триггер для автоматического обновления updated_at
        await cursor.executecursor.execute('''
        CREATE TRIGGER IF NOT EXISTS update_Orders_updated_at
        AFTER UPDATE ON Orders
        FOR EACH ROW
        BEGIN
            UPDATE Orders SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END;
        ''')

#asyncio.run(init_db())


async def add_order(status, price, restaraunt_id):
    async with get_cursor() as cursor:
        await cursor.execute('''
            INSERT INTO Orders ("status", price, restaraunt_id)
            VALUES (?, ?, ?)
        ''', (status, price, restaraunt_id))
        return cursor.lastrowid


async def update_order_status(order_id, new_status):
    async with get_cursor() as cursor:
        await cursor.execute('''
            UPDATE Orders
            SET "status" = ?
            WHERE id = ?
        ''', (new_status, order_id))
