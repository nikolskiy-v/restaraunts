from src.restaraunts.database import get_cursor
#import asyncio


async def init_db():
    async with get_cursor() as cursor:
        await cursor.execute('''
        CREATE TABLE IF NOT EXISTS Items (
            id INTEGER PRIMARY KEY,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            price REAL NOT NULL,
            name TEXT NOT NULL,
            is_active INTEGER DEFAULT 1
        )
        ''')


        #Триггер для автоматического обновления updated_at
        await cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS update_items_updated_at
        AFTER UPDATE ON Items
        FOR EACH ROW
        BEGIN
            UPDATE Items SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END;
        ''')

#asyncio.run(init_db())


async def add_item(name, price):
    async with get_cursor() as cursor:
        await cursor.execute('''
            INSERT INTO Items (name, price) 
            VALUES (?, ?)
        ''', (name, price))
        print(f"Товар '{name}' добавлен. ID: {cursor.lastrowid}")

#asyncio.run(add_item("Кофе", 250))


async def delete_item(item_id: int):
    async with get_cursor() as cursor:
        await cursor.execute(
            "UPDATE Items SET is_active = 0 WHERE id = ?",
            (item_id,)
        )


async def get_all_items(show_archived=False):
    """
    Получает список всех товаров.
    :param show_archived: Если True, вернет в том числе и 'удаленные' товары.
    """
    async with get_cursor() as cursor:
        if show_archived:
            await cursor.execute("SELECT * FROM item")
        else:
            await cursor.execute("SELECT * FROM item WHERE is_active = 1")
    return [dict(row) for row in cursor.fetchall()]
    

async def restore_item(item_id: int):
    """Восстанавливает ранее деактивированный товар."""
    async with get_cursor() as cursor:
        await cursor.execute(
            "UPDATE item SET is_active = 1 WHERE id = ?",
            (item_id,)
        )
