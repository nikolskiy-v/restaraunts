"""Класс для представления заказа"""
from OrderStatus_cls import OrderStatus

class Order:
    """Модель заказа"""
    next_order_id = 0

    def __init__(self, visitor, restaraunt):
        self.id = Order.next_order_id
        Order.next_order_id += 1
        self.visitor = visitor
        self.restaraunt = restaraunt
        self.status = OrderStatus.NEW
        self.items = []
        self.total_price = 0

    def save_item_into_json(self, item_id):
        with open(f'order_id{self.id}_list.json', 'a') as w:
            print(f'{item_id}', file=w)

    def describe_order(self):
        print(self)

    def __str__(self):
        """Выводит информацию о заказе"""
        return f'Заказ для: {self.visitor.name}, в ресторане: {self.restaraunt.name}, ID: {self.id}, сумма заказа: {self.total_price} статус: {self.status}'