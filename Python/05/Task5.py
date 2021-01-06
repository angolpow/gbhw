"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randrange
from functools import reduce


def write_random_nums_to_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(1, randrange(10, 20)):
            f.write(f'{randrange(1, 15)} ')


def calculate_sum_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        num_list = [int(i) for i in f.readline().split()]
        return reduce(lambda x, y: x+y, num_list)


write_random_nums_to_file('t5')
print(calculate_sum_from_file('t5'))
