"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, date_string: str):
        self.date_string = date_string

    @classmethod
    def get_date_as_int(cls, date_string: str):
        day, month, year = map(int, date_string.split('-'))
        return day, month, year

    @staticmethod
    def check_date(day: int, month: int, year: int):
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        if not 1 <= month <= 12:
            return False
        if not 1 <= day <= 31:
            return False
        if not 1 <= year <= 2021:
            return False
        if month == 2 and day > 29:
            return False
        elif month not in months_31 and day == 31:
            return False
        else:
            return True


dates = ['44-12-2004',
         '23-04-2000',
         '30-02-2011',
         '31-04-2020',
         '31-01-2021',
         '15-12-2030']

for i in dates:
    test = Data(i)
    date_ints = Data.get_date_as_int(i)
    print(test.date_string, f'is {"valid" if Data.check_date(date_ints[0], date_ints[1], date_ints[2]) else "invalid"}')
