import argparse
import enum
from Restaraunt_cls import Restaraunt
from Visitor_cls import Visitor
from Order_cls import Order
from OrderStatus_cls import OrderStatus
from Item_cls import Item


#Посетители
visitor1 = Visitor('Иван')
visitor2 = Visitor('Антонина')
visitor3 = Visitor('Гоша')

#Рестораны и их описание
phali = Restaraunt('Пхали-хинкали','грузинский')
makkoli = Restaraunt('Макколи-микс', 'все подряд')
hach = Restaraunt('Хачапури и вино', 'грузинский')
Restaraunt.describe_all_restaraunts()
print('ТЕСТ ДОБАВЛЕНИЯ ТОВАРА В КОРЗИНУ:::::::::::')
visitor1.add_item(2)

###Товары
item0 = Item('Суп из 3 залуп', '100000000')

#Тест входа посетителя в ресторан
hach.enter_restaraunt(visitor1)
makkoli.enter_restaraunt(visitor2)
makkoli.enter_restaraunt(visitor3)

print('ТЕСТ ДОБАВЛЕНИЯ ТОВАРА В КОРЗИНУ222222:::::::::::')
visitor1.add_item(item0)
visitor1.finish_order()

#Тест входа посетителя одновременно в два ресторана
makkoli.enter_restaraunt(visitor1)

#Тест повторного входа посетителя в тот же самый ресторан
hach.enter_restaraunt(visitor1)

#Тест выхода посетителя из ресторана
hach.leave_restaraunt(visitor1)

#Тест повторного выхода посетителя из ресторана
hach.leave_restaraunt(visitor1)

#Тест заказа
visitor2.create_order()
visitor2.finish_order()
visitor2.describe_visitor()
visitor2.show_orders()
visitor3.show_orders()

#Описание посетителей
visitors = [visitor1, visitor2, visitor3]
for visitor in visitors:
    visitor.describe_visitor()

Visitor.get_visitor_with_max_total_orders_price()

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--orders", help="Get order's history", action='store_true' )
parser.add_argument("-v", "--visitors", help="Get visitor's history", action='store_true' )
parser.add_argument("-a", "--average", help="Get the arithm.mean of the total orders prices across restaurants", action='store_true' )
parser.add_argument("-i", "--info", help="Get the information on restaraunts", action='store_true' )
parser.add_argument("-m", "--max", help="Get the visitor with max total orders prices", action='store_true' )

args = parser.parse_args()
if args.orders:
    Restaraunt.get_orders_history()
if args.visitors:
    restaraunts = [phali, makkoli, hach]      ###лучше сделать реализацию этого же через classmethod
    for restaraunt in restaraunts:
        print(f'Число обслуженных посетителей: {restaraunt.name} - {restaraunt.number_served}')
if args.average:
    print('Средний чек по ресторанам:')
    Restaraunt.get_avg_order_total_price()
if args.info:
    print('Информация по состоянию всех ресторанов')
    Restaraunt.describe_all_restaraunts()
if args.max:
    Visitor.get_visitor_with_max_total_orders_price()
