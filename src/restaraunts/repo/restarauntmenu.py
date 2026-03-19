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


async def add_restarauntmenu(restaraunt_id, menu_id):
    async with get_cursor() as cursor:
        await cursor.execute('''
            INSERT INTO RestarauntMenus (restaraunt_id, menu_id) 
            VALUES (?, ?)
        ''', (restaraunt_id, menu_id))
        print(f"Меню с ID: '{menu_id}' добавлено к ресторану с ID: '{restaraunt_id}'")

#asyncio.run(add_restarauntmenu(2, 1))
