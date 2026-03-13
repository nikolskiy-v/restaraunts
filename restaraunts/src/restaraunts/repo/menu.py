from restaraunts.schemas.menu import Menu
from datetime import datetime
import sqlite3

fake_db = {
    'test_menu_id' : {
        'id' : 'test_menu_id',
        'created_at' : datetime.now(),
        'updated_at' : datetime.now(),
        'items' : [],
        'resraraunt_id' : 'test_restaraunt_id',
        'version' : 1,
        'name' : 'test_menu_name'
    }
}



connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Menus (
    id INTEGER PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    version INTEGER NOT NULL DEFAULT 1
)
''')


#Триггер для автоматического обновления updated_at
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS update_Menus_updated_at
AFTER UPDATE ON Menus
FOR EACH ROW
BEGIN
    UPDATE Menus SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
''')

connection.commit()
connection.close()