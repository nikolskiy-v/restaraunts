from restaraunts.database import get_connection


connection = get_connection()
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Items (
    id INTEGER PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    price REAL NOT NULL,
    name TEXT NOT NULL,
    is_active INTEGER DEFAULT 1
)
''')


#Триггер для автоматического обновления updated_at
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS update_items_updated_at
AFTER UPDATE ON Items
FOR EACH ROW
BEGIN
    UPDATE Items SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
''')

connection.commit()
connection.close()


def add_item(name, price):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Items (name, price) 
            VALUES (?, ?)
        ''', (name, price))
        print(f"Товар '{name}' добавлен. ID: {cursor.lastrowid}")


def delete_item(item_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Items SET is_active = 0 WHERE id = ?",
            (item_id,)
        )
        conn.commit()
        print(f"Товар с ID {item_id} деактивирован.")


def get_all_items(show_archived=False):
    """
    Получает список всех товаров.
    :param show_archived: Если True, вернет в том числе и 'удаленные' товары.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        
        if show_archived:
            cursor.execute("SELECT * FROM item")
        else:
            cursor.execute("SELECT * FROM item WHERE is_active = 1")
            
        return [dict(row) for row in cursor.fetchall()]
    

def restore_item(item_id: int):
    """Восстанавливает ранее деактивированный товар."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE item SET is_active = 1 WHERE id = ?",
            (item_id,)
        )
        conn.commit()
        print(f"Товар с ID {item_id} снова активен.")
