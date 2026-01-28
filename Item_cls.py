class Item:
    """Модель элемента заказа"""
    next_item_id = 0

    def __init__(self, title, price):
        self.id = Item.next_item_id
        Item.next_item_id += 1
        self.title = title
        self.price = int(price)