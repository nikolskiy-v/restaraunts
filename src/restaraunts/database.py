import sqlite3
import aiosqlite
from src.restaraunts.config import DB_PATH
from contextlib import asynccontextmanager

# def get_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row  
#     conn.execute("PRAGMA foreign_keys = ON") 
#     return conn

@asynccontextmanager
async def get_cursor():
    conn = await aiosqlite.connect(DB_PATH)
    try:
        conn.row_factory = sqlite3.Row
        await conn.execute("PRAGMA foreign_keys = ON")
        async with conn.cursor() as cursor:
            yield cursor
        await conn.commit()
    except Exception as e:
        await conn.rollback()
        raise e
    finally:
        await conn.close()
