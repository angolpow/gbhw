"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZeroDiv(Exception):
    def __init__(self, txt='Zero division error'):
        self.txt = txt


def main():
    while True:
        a = float(input('Введите делимое: '))
        b = float(input('Введите делитель: '))
        try:
            if b == 0:
                raise ZeroDiv
        except ZeroDiv:
            print('На ноль делить нельзя')
        else:
            print(a / b)


main()
