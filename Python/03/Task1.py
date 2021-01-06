# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def div(a, b):
    """
    >>> div(5, 2)
    2.5
    >>> div(4, 2)
    2.0
    >>> div(5, 0)
    'Делить на 0 нельзя'
    """

    if b:
        return a / b
    else:
        return 'Делить на 0 нельзя'


print(div(9, 3))
print(div(9, 0))
print(div(5, 2))
print(div(6, 3))

if __name__ == "__main__":
    import doctest
    doctest.testmod()