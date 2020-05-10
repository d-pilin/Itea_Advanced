"""
    Реализовать функцию bank, которая приннимает следующие
    аргументы: сумма депозита, кол-во лет, и процент. Результатом
    выполнения должна быть сумма по истечению депозита.
"""


def bank(deposit_value, percent_value, period_value):
    sum_of_percents = (deposit_value * percent_value * period_value) / (365 * 100)

    return sum_of_percents


# deposit =int(input('set deposit sum:'))
deposit = 50000.1

# percents = int(input('set percents:'))
percents = 10.5

# period = int(input ('input period in years'))
period = 10

period_days = period * 365

result = bank(deposit, period_days, percents)
print(f'Sum of percents after {period} year(s) is: {result}')
