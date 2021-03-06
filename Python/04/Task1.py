"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def salary(hours, hourly_rate, bonus):
    return hours * hourly_rate + bonus


try:
    print(salary(float(argv[1]), float(argv[2]), float(argv[3])))
except IndexError:
    print('Передайте значения выработки, ставки и премии')
except ValueError:
    print('Проверьте введенные значения. Для десятичных дробей используйте точку.')
