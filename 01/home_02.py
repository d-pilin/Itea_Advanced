"""
    Создать словарь Страна:Столица. Создать список стран. Не все
    страны со списка должны сходиться с названиями стран со словаря.
    С помощою оператора in проверить на вхождение элемента страны в
    словарь, и если такой ключ действительно существует вывести
    столицу.
"""

countries_and_capitals_dict = dict(
    China='Beijing',
    Cuba='Havana',
    Egypt='Cairo',
    France='Paris'
)

countries_list = {'China', 'Ukraine', 'Russia', 'France'}

for k, v in countries_and_capitals_dict.items():

    if k in countries_list:
        print(f'Capital of {k} is {v}')
