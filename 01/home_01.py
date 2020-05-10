"""
    Создать список из N элементов (от 0 до n с шагом 1). В этом списке
    вывести все четные значения.
"""

# value = int(input('enter value:'))
value = 10

elements_list = [*range(value)]

for i in elements_list:

    if not i % 2 and i != 0:
        print(i)
