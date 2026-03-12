import sqlite3

connection = sqlite3.connect('my_database.db')
connection.execute("PRAGMA foreign_keys = ON;")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS OrderedItems (
    id INTEGER PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    item_id INTEGER,
    "status" TEXT NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (item_id) REFERENCES item(id) ON DELETE CASCADE
)
''')


#Триггер для автоматического обновления updated_at
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS update_ordereditems_updated_at
AFTER UPDATE ON OrderedItems
FOR EACH ROW
BEGIN
    UPDATE OrderedItems SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
''')

connection.commit()
connection.close()


def add_ordered_item(item_id, status, price):
    with sqlite3.connect('my_database.db') as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO OrderedItems (item_id, "status", price)
            VALUES (?, ?, ?)
        ''', (item_id, status, price))
        conn.commit()
        return cursor.lastrowid

def update_item_status(ordereditem_id, new_status):
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE OrderedItems
            SET "status" = ?
            WHERE id = ?
        ''', (new_status, ordereditem_id))
        conn.commit()
