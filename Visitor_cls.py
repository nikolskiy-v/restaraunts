"""Класс для представления посетителя"""
from Order_cls import Order
from Restaraunt_cls import Restaraunt
from Item_cls import Item

class Visitor:
    """Модель посетителя"""
    all_visitors = []

    def __init__(self, name):
        self.name = name
        self.location = None
        self.order = None
        self.orders = []
        self.total_orders_price = 0
        Visitor.all_visitors.append(self)


    @classmethod
    def get_visitor_with_max_total_orders_price(cls):
        top_buyer = max(cls.all_visitors, key=lambda visitor: visitor.total_orders_price)
        print(f"Больше всех тратил {top_buyer.name}, а именно: {top_buyer.total_orders_price}")


    def create_order(self):
        """Создает заказ, если посетитель находится в ресторане"""
        if self.location is None:
            print('Для создания заказа зайдите в ресторан!')
        else:
            print(f'{self.name} делает заказ.')
            self.order = Order(self, self.location)
            self.orders.append(self.order)
            self.location.orders.append(self.order)

    def add_item(self, item):
        if self.location is None:
            print('Для создания заказа зайдите в ресторан!')
            return
        elif self.order is None:
            self.create_order()
        elif self.order.status == 'READY':
            self.create_order()
        self.order.items.append(item)
        self.order.total_price += item.price
        self.order.save_item_into_json(item)
        print(f'Элемент {item} добавлен в заказ для {self.name}')

    def finish_order(self):
       if self.order is None:
           print('Для оформления заказа необходимо создать новый заказ!')
           return
       elif self.order.status == 'READY':
           print('Для оформления заказа необходимо создать новый заказ!')
           return
       elif len(self.order.items) < 1:
           print('Добавьте хотя бы одну позицию в заказ!')
           return
       else:
           self.location.cook_order(self.order)
           self.total_orders_price += self.order.total_price
             
    def show_orders(self):
        """Выводит все заказы посетителя"""
        if not self.orders:
            print(f'У посетителя {self.name} нет оформленных заказов.\n')
        else:
            for order in self.orders:
                order.describe_order()
            print()

    def describe_visitor(self):
        """Выводит информацию о посетителе"""
        location = self.location.name if self.location else None
        print(f'Имя: {self.name}, местоположение: {location}, количество заказов: {len(self.orders)}\n')