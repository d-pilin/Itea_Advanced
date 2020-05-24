"""
    Создать декоратор с аргументами. Который будет вызывать функцию,
    определенное кол-во раз, будет выводить кол-во времени
    затраченного на выполнение данной функции и её название.
"""
import time


def decorator(input_arg):
    time_start = time.time()

    def counter(func):
        def wrapper(*args):
            for _ in range(input_arg):
                result = func(*args)

            time_finish = time.time()
            run_time = time_finish - time_start
            print(f'{func.__name__} run: {run_time} sec')

            return result

        return wrapper

    return counter


@decorator(5000)
def math(a, b):
    exp = a ** b
    return exp


print(math(500, 200))


