"""
1) Создать класс автомобиля. Описать общие аттрибуты. Создать
классы легкового автомобиля и грузового. Описать в основном
классе базовые аттрибуты для автомобилей. Будет плюсом если в
классах наследниках переопределите методы базового класса.
"""


class Car:

    def __init__(self, beep, wheels, weight):
        self.beep = beep
        self.wheels = wheels
        self.weight = weight

    def move(self):
        return f'On {self.wheels} wheels the car rides more stably'

    def signal(self):
        return f'Car signal is: {self.beep}'

    def info(self):
        return f'Car info:\nWheels: {self.wheels}\n' \
               f'Signal: {self.beep}\n' \
               f'Weight: {self.weight}'


class Cargo(Car):

    def move(self, arg):
        return f'{self.weight} tons car can\'t move faster but can transport {arg}!'

    def signal(self):
        return f'Heavy {self.beep} signals shake the walls'


class Passenger(Car):

    def move(self):
        return f'Wroom wroom. Catch me if u can'


cargo = Cargo('BOOO', 8, 50)
print(cargo.info())
print(cargo.move('mountains'))
print(cargo.signal())

passenger = Passenger('beep', 4, 2)
print(passenger.info())
print(passenger.move())
print(passenger.signal())
