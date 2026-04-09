from src.restaraunts.database import get_cursor
from src.restaraunts.schemas.restaraunt import Restaraunt
import sqlite3
#import asyncio

async def init_db():
    async with get_cursor() as cursor:
        await cursor.execute('''
        CREATE TABLE IF NOT EXISTS Restaraunts (
            id INTEGER PRIMARY KEY,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            name TEXT NOT NULL
        )
        ''')


        #Триггер для автоматического обновления updated_at
        await cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS update_Restaraunts_updated_at
        AFTER UPDATE ON Restaraunts
        FOR EACH ROW
        BEGIN
            UPDATE Restaraunts SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END;
        ''')

#asyncio.run(init_db())


async def get_all():
    async with get_cursor() as cursor:
        await cursor.execute("SELECT * FROM Restaraunts")
        rows = await cursor.fetchall() 
        # Превращаем каждую строку в объект Restaraunt
        return [Restaraunt(**dict(row)) for row in rows]


async def get_restaraunt(restaraunt_id: int):
    async with get_cursor() as cursor:
        await cursor.execute(
            "SELECT * FROM Restaraunts WHERE id = ?",
            (restaraunt_id,)
        )
        row = await cursor.fetchone()
        if row is None:
            return None
        return Restaraunt(**dict(row))
        

async def add_restaraunt(name):
    async with get_cursor() as cursor:
        await cursor.execute('''
            INSERT INTO Restaraunts (name) 
            VALUES (?)
        ''', (name,))
        print(f"Ресторан '{name}' добавлен. ID: {cursor.lastrowid}")

#asyncio.run(add_restaraunt('Пхали'))


async def link_restaraunt_and_menu(restaraunt_id: int, menu_id: int):
    async with get_cursor() as cursor:
        try:
            await cursor.execute('''
                INSERT INTO RestarauntMenus (restaraunt_id, menu_id)
                VALUES (?, ?)
            ''', (restaraunt_id, menu_id))
        except sqlite3.IntegrityError as e:
            if "FOREIGN KEY constraint failed" in str(e):
                return "not_found"
            if "UNIQUE constraint failed" in str(e):
                return "already_exists"
            raise e
        return "success"
    