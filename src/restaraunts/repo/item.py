from src.restaraunts.database import get_cursor
from src.restaraunts.schemas.item import Item
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


async def add_item(name, price) -> int:
    async with get_cursor() as cursor:
        await cursor.execute('''
            INSERT INTO Items (name, price) 
            VALUES (?, ?)
        ''', (name, price))
        return cursor.lastrowid

#asyncio.run(add_item("Кофе", 250))


async def delete_item(item_id: int):
    async with get_cursor() as cursor:
        await cursor.execute(
            "UPDATE Items SET is_active = 0 WHERE id = ?",
            (item_id,)
        )


async def get_all(show_archived=False):
    """
    Получает список всех товаров.
    :param show_archived: Если True, вернет в том числе и 'удаленные' товары.
    """
    async with get_cursor() as cursor:
        if show_archived:
            await cursor.execute("SELECT * FROM Items")
        else:
            await cursor.execute("SELECT * FROM Items WHERE is_active = 1")
        rows = await cursor.fetchall()
        return [Item(**dict(row)) for row in rows]


async def get_all_for_menu(menu_id: int):
    async with get_cursor() as cursor:
        query = '''
            SELECT i.* 
            FROM Items i
            JOIN MenuItems mi ON i.id = mi.item_id
            WHERE mi.menu_id = ?
        '''
        await cursor.execute(query, (menu_id,))
        rows = await cursor.fetchall()
        return [Item(**dict(row)) for row in rows]
    

async def get_item_for_menu(menu_id: int, item_id: int):
    async with get_cursor() as cursor:
        query = '''
            SELECT i.* 
            FROM Items i
            JOIN MenuItems mi ON i.id = mi.item_id
            WHERE mi.menu_id = ?
            AND mi.item_id = ?
         '''
        await cursor.execute(query, (menu_id, item_id))
        row = await cursor.fetchone()
        if row is None:
            return None
        return Item(**dict(row))


async def restore_item(item_id: int):
    """Восстанавливает ранее деактивированный товар."""
    async with get_cursor() as cursor:
        await cursor.execute(
            "UPDATE Items SET is_active = 1 WHERE id = ?",
            (item_id,)
        )
