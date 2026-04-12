import sqlite3
import aiosqlite
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy import text, event
from src.restaraunts.config import DB_PATH, DB_PATH_V2
from contextlib import asynccontextmanager


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


DATABASE_URL = f"sqlite+aiosqlite:///{DB_PATH_V2}"

engine = create_async_engine(DATABASE_URL, echo=True)


@event.listens_for(engine.sync_engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


async_session_factory = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db():
    async with async_session_factory() as session:
        yield session


async def test_conn():
    async with async_session_factory() as session:
        async with session.begin():
            result = await session.execute(text("SELECT 'session is working'"))
            print(result.scalar())
