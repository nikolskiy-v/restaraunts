from src.restaraunts.database import get_cursor
#import asyncio


async def init_db():
    async with get_cursor() as cursor:
        await cursor.execute('''
        CREATE TABLE IF NOT EXISTS RestarauntMenus (
            restaraunt_id INTEGER,
            menu_id INTEGER,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (restaraunt_id, menu_id),
            FOREIGN KEY (restaraunt_id) REFERENCES Restaraunts(id) ON DELETE CASCADE
            FOREIGN KEY (menu_id) REFERENCES Menus(id) ON DELETE CASCADE
        )
        ''')


        #Триггер для автоматического обновления updated_at
        await cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS update_RestarauntMenus_updated_at
        AFTER UPDATE ON RestarauntMenus
        FOR EACH ROW
        BEGIN
            UPDATE RestarauntMenus SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END;
        ''')

#asyncio.run(init_db())
