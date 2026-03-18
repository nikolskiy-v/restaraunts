from src.restaraunts.database import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "status" TEXT NOT NULL DEFAULT 'Новый',
    price REAL NOT NULL,
    restaraunt_id INTEGER,
    FOREIGN KEY (restaraunt_id) REFERENCES Restaraunts(id) ON DELETE RESTRICT
)
''')


#Триггер для автоматического обновления updated_at
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS update_Orders_updated_at
AFTER UPDATE ON Orders
FOR EACH ROW
BEGIN
    UPDATE Orders SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
''')

connection.commit()
connection.close()



def add_order(status, price, restaraunt_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Orders ("status", price, restaraunt_id)
            VALUES (?, ?, ?)
        ''', (status, price, restaraunt_id))
        conn.commit()
        return cursor.lastrowid

def update_order_status(order_id, new_status):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Orders
            SET "status" = ?
            WHERE id = ?
        ''', (new_status, order_id))
        conn.commit()
