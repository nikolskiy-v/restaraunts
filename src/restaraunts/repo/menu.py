from src.restaraunts.database import get_cursor
from src.restaraunts.schemas.menu import Menu
#import asyncio


async def init_db():
    async with get_cursor() as cursor:
        await cursor.execute('''
        CREATE TABLE IF NOT EXISTS Menus (
            id INTEGER PRIMARY KEY,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            name TEXT NOT NULL,
            version INTEGER NOT NULL DEFAULT 1
        )
        ''')


        #Триггер для автоматического обновления updated_at
        await cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS update_Menus_updated_at
        AFTER UPDATE ON Menus
        FOR EACH ROW
        BEGIN
            UPDATE Menus SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END;
        ''')

#asyncio.run(init_db())


async def add_menu(name: str) -> int:
    async with get_cursor() as cursor:
        await cursor.execute('''
            INSERT INTO Menus (name) 
            VALUES (?)
        ''', (name,))
        return cursor.lastrowid

#asyncio.run(add_menu('Сезонное'))


async def get_all():
    async with get_cursor() as cursor:
        await cursor.execute("SELECT * FROM Menus")
        rows = await cursor.fetchall() 
        return [Menu(**dict(row)) for row in rows]


async def get_all_for_restaraunt(restaraunt_id: int):
    async with get_cursor() as cursor:
        query = '''
            SELECT m.* 
            FROM Menus m
            JOIN RestarauntMenus rm ON m.id = rm.menu_id
            WHERE rm.restaraunt_id = ?
        '''
        await cursor.execute(query, (restaraunt_id,))
        rows = await cursor.fetchall()
        return [Menu(**dict(row)) for row in rows]
    

async def get_menu_for_restaraunt(restaraunt_id: int, menu_id: int):
    async with get_cursor() as cursor:
        query = '''
            SELECT m.* 
            FROM Menus m
            JOIN RestarauntMenus rm ON m.id = rm.menu_id
            WHERE rm.restaraunt_id = ?
            AND rm.menu_id = ?
        '''
        await cursor.execute(query, (restaraunt_id, menu_id))
        row = await cursor.fetchone()
        if row is None:
            return None
        return Menu(**dict(row))
