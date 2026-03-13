import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Restaraunts (
    id INTEGER PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL
)
''')


#Триггер для автоматического обновления updated_at
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS update_Restaraunts_updated_at
AFTER UPDATE ON Restaraunts
FOR EACH ROW
BEGIN
    UPDATE Restaraunts SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
''')

connection.commit()
connection.close()