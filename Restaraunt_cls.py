"""Класс для представления ресторана"""
from OrderStatus_cls import OrderStatus
from pathlib import Path
import json

class Restaraunt:
    """Модель ресторона"""
    next_restaraunt_id = 0
    all_restaraunts = []

    def __init__(self, name, cuisine_type):
        """Инициализирует атрибуты ресторана"""
        self.id = Restaraunt.next_restaraunt_id
        Restaraunt.next_restaraunt_id += 1
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.visitors_entered = []
        self.orders = []
        Restaraunt.all_restaraunts.append(self)

    @classmethod
    def describe_all_restaraunts(cls):
        """Вызывает метод описания ресторана для всех ресторанов"""
        for r in cls.all_restaraunts:
            r.describe_restaraunt()
        print()

    @classmethod
    def get_orders_history(cls):
        """Выводит общую историю заказов"""
        for r in cls.all_restaraunts:
            try:
                h = open(f'orders_history_{r.name}.json', 'r')
            except FileNotFoundError:
                print(f'У ресторана {r.name} не было заказов!')
            else:
                with h:
                    for line in h:
                        print(json.loads(line))

    @classmethod
    def get_avg_order_total_price(cls):
        """Выводит средний чек по всем ресторанам"""
        for r in cls.all_restaraunts:
            orders_prices = []
            for o in r.orders:
                orders_prices.append(o.total_price)
            try:
                avg_order_price = sum(orders_prices) / len(orders_prices)
                print(f'Средний чек ресторана {r.name} - {avg_order_price}')
            except ZeroDivisionError:
                print(f'У ресторана {r.name} не было заказов ваще!')

    def open_restaraunt(self):
        """Выводит сообщение о том что ресторан открыт"""
        print(f'Ресторан {self.name} открыт!')

    def increment_number_served(self):
        """Увеличивает кол-во обслуженных посетителей на 1"""
        self.number_served += 1

    def enter_restaraunt(self, visitor):
        """Моделирует вход посетителя в ресторан"""
        print(f"Посетитель {visitor.name} пытается войти в {self.name}")
        if visitor in self.visitors_entered:
            print(f"Посетитель {visitor.name} уже в ресторане {self.name}! Пашол нахуй")
            print()
            return
        if visitor.location is not None:
            print(f"Посетитель {visitor.name} уже в другом ресторане {visitor.location.name}! Нихуя он наглый")
            print()
            return
        self.visitors_entered.append(visitor)
        visitor.location = self
        self.increment_number_served()
        print(f"Посетитель {visitor.name} вошел в ресторан {self.name}")
        self.describe_restaraunt()
        print()

    def leave_restaraunt(self, visitor):
        """Моделирует выход посетителя из ресторана"""
        print(f"Посетитель {visitor.name} пытается выйти из {self.name}")
        if visitor not in self.visitors_entered:
            print(f"Посетитель {visitor.name} пытается выйти из {self.name}, хотя не в ресторане! Не лохмать бабушку")
            print()
            return
        self.visitors_entered.remove(visitor)
        visitor.location = None
        print(f"Посетитель {visitor.name} вышел из ресторана {self.name}")
        self.describe_restaraunt()
        print()

    def cook_order(self, order):
        order.status = OrderStatus.PREPARING
        print(f'Начинаем готовить заказ: {order}')
        order.status = OrderStatus.READY
        print(f'Ебать наготовили заказ: {order}')
        order.describe_order()
        saving_order = json.dumps(order.__str__())
        with open(f'orders_history_{self.name}.json', 'a') as h:
            print(f'{saving_order}', file=h)
        print()

    def get_visitors_names(self):
        return [it.name for it in self.visitors_entered]

    def describe_restaraunt(self):
        print(self)

    def __str__(self):
        """Выводит  информацию о ресторане"""
        return f'ID: {self.id}, Название:{self.name}, Тип кухни:{self.cuisine_type} \nЧисло обслуженных посетителей:{self.number_served}, Посетители внутри заведения: {self.get_visitors_names()}'