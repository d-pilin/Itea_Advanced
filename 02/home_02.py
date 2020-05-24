"""
2) Создать класс магазина. Конструктор должен инициализировать
значения: «Название магазина» и «Количество проданных
товаров». Реализовать методы объекта, которые будут увеличивать
кол-во проданных товаров, и реализовать вывод значения
переменной класса, которая будет хранить общее количество
товаров проданных всеми магазинами.
"""


class Shop:
    total_sold_items = 0

    def __init__(self, shop_name, sold_items):
        self.shop_name = shop_name
        self.sold_items = sold_items
        Shop.total_sold_items += sold_items

    def add_sold_items(self, sold_num):
        self.sold_items += sold_num
        Shop.total_sold_items += sold_num


"""
вариант 2: вызвывать функцию count_total вместо прямой записи в классовую переменную

def count_total(count):
    Shop.total_sold_items += count
"""

meds = Shop('Medicine', 500)
foods = Shop('Foodmarket', 100)
cars = Shop('Bentley', 10)

print(f'{meds.shop_name} Shop sold: {meds.sold_items} items')
print(f'Total sold: {Shop.total_sold_items}\n')

meds.add_sold_items(100)
foods.add_sold_items(200)
cars.add_sold_items(2)

print(f'meds:{meds.sold_items}')
print(f'foods:{foods.sold_items}')
print(f'cars:{cars.sold_items}')
print(f'Total sold: {Shop.total_sold_items}')
