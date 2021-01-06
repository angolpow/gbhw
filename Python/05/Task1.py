"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def write_data(filename):
    with open(filename, 'a') as f:
        string = input('Введите строку или Enter для завершения: ')
        while string:
            f.write(string + '\n')
            string = input('Введите строку или Enter для завершения: ')


write_data('t1')
