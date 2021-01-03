"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
"""


from itertools import count, cycle


# a)
def gen_int(start, limit):
    for i in count(start):
        if i == limit+1:
            break
        yield i


# start, limit = map(int, input('a) Введите начальное значение и верхнюю границу через пробел: ').split())
# print([i for i in gen_int(start, limit)])

for i in gen_int(3, 10):
    print(i)


# b)
def gen_list_cycle(_list, _max):
    _max = len(_list) * _max
    counter = 0
    for i in cycle(_list):
        if counter >= _max:
            break
        counter += 1
        yield i


user_list = [23, 1, 3, 10, 4, 11]

repeat = int(input("b) Сколько раз повторить список? "))

for i in gen_list_cycle(user_list, repeat):
    print(i)
