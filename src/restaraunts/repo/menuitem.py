from src.restaraunts.database import get_cursor
#import asyncio


async def init_db():
    async with get_cursor() as cursor:
        await cursor.execute('''
        CREATE TABLE IF NOT EXISTS MenuItems (
            menu_id INTEGER,
        item_id INTEGER,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (menu_id, item_id),
        FOREIGN KEY (menu_id) REFERENCES Menus(id) ON DELETE CASCADE
        FOREIGN KEY (item_id) REFERENCES Items(id) ON DELETE CASCADE
        )
        ''')


        #Триггер для автоматического обновления updated_at
        await cursor.executecursor.execute('''
        CREATE TRIGGER IF NOT EXISTS update_MenuItems_updated_at
        AFTER UPDATE ON MenuItems
        FOR EACH ROW
        BEGIN
            UPDATE MenuItems SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END;
        ''')

#asyncio.run(init_db())
