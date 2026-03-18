from src.restaraunts.database import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS OrderedItems (
    id INTEGER PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    item_id INTEGER,
    "status" TEXT NOT NULL DEFAULT 'Не готов',
    price REAL NOT NULL,
    order_id INTEGER,
    FOREIGN KEY (item_id) REFERENCES Items(id) ON DELETE SET NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE RESTRICT
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


def add_ordered_item(item_id, status, price, order_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO OrderedItems (item_id, "status", price, order_id)
            VALUES (?, ?, ?, ?)
        ''', (item_id, status, price, order_id))
        conn.commit()
        return cursor.lastrowid

def update_item_status(ordereditem_id, new_status):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE OrderedItems
            SET "status" = ?
            WHERE id = ?
        ''', (new_status, ordereditem_id))
        conn.commit()

#Тест на "битую" ссылку
#def test_foreign_key_insert():
#    with get_connection() as conn:
#        try:
            # Пытаемся добавить заказ к несуществующему товару
#            conn.execute('INSERT INTO OrderedItems (item_id, "status", price, order_id) VALUES (99999, "test", 100, 11111)')
#            print("❌ Ошибка: Внешний ключ НЕ работает (запись добавлена)")
#        except sqlite3.IntegrityError as e:
#            print(f"✅ Успех: База запретила вставку ({e})")
#test_foreign_key_insert()
