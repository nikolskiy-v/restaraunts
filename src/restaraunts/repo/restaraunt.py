from src.restaraunts.database import get_connection
from src.restaraunts.schemas.restaraunt import Restaraunt

connection = get_connection()
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


def get_all_restaraunts_from_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Restaraunts")
        rows = cursor.fetchall()
        # Превращаем каждую строку в объект Restaraunt
        return [Restaraunt(**dict(row)) for row in rows]


def add_restaraunt(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Restaraunts (name) 
            VALUES (?)
        ''', (name,))
        print(f"Ресторан '{name}' добавлен. ID: {cursor.lastrowid}")
add_restaraunt('Макколи')
